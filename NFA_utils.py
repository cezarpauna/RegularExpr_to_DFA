from NFA import NFA

# given two nfas returns the concatenation of those nfas
# construct a new nfa, that has initial state 0
# we suppose that both nfas have initial state = 0 (we construct them this way)
# copy first delta in new delta, extend alphabet, the new number of states
# will be n1.no_states + n2.no_states - 1 (chose to make n1.final_state = n2.initial_state)
# every state of the second nfa should be increased by the number of states
# of nfa1 - 1 (-1 because nfa1 final state will be nfa2 initial state,
# so given two nfas with 2 states we should return a nfa with 3 states not 4)
def concatenate(n1, n2):

	new_no_states = n1.no_states + n2.no_states - 1
	new_alphabet = n1.alphabet
	new_alphabet.extend(n2.alphabet)
	new_initial_state = 0
	new_final_state = n1.final_state + n2.no_states - 1
	new_delta = n1.delta

	for (i, k) in n2.delta:
		lst = []
		for j in n2.delta[(i, k)]:
			lst.append(j + n1.no_states - 1)
		new_delta[(i + n1.no_states - 1, k)] = lst

	nfa = NFA(new_no_states,
			  new_alphabet,
			  new_initial_state,
			  new_final_state,
			  new_delta)

	return nfa


# the same idea as previous, but different operation
# so we make 2 new states (initial and final)
#						nfa1
#					 /		  \
# new_initial_state  			 new_final_state	
#					 \		  /
#						nfa2
def or_op(n1, n2):

	new_no_states = n1.no_states + n2.no_states + 2
	new_alphabet = n1.alphabet
	new_alphabet.extend(n2.alphabet)
	new_initial_state = 0
	new_final_state = n1.final_state + n2.no_states + 2
	new_delta = {(new_initial_state, 'eps') : [n1.initial_state + 1, n2.initial_state + 1 + n1.no_states]}
	new_delta[(n1.final_state + 1, 'eps')] = [new_final_state]
	new_delta[(n2.final_state + 1 + n1.no_states, 'eps')] = [new_final_state]

	for (i, k) in n1.delta:
		lst = []
		for j in n1.delta[(i, k)]:
			lst.append(j + 1)
		new_delta[(i + 1, k)] = lst

	for (i, k) in n2.delta:
		lst = []
		for j in n2.delta[(i, k)]:
			lst.append(j + 1 + n1.no_states)
		new_delta[(i + 1 + n1.no_states, k)] = lst

	nfa = NFA(new_no_states,
			  new_alphabet,
			  new_initial_state,
			  new_final_state,
			  new_delta)

	return nfa


# read above
def kleene_star(n):

	new_initial_state = 0
	new_final_state = n.final_state + 2
	new_delta = {}
	new_no_states = n.no_states

	for (i, k) in n.delta:
		lst = []
		for j in n.delta[(i, k)]:
			lst.append(j + 1)

		new_delta[(i + 1, k)] = lst

	new_delta[(0, 'eps')] = [1, new_final_state];
	new_delta[(n.final_state + 1, 'eps')] = [new_final_state]
	new_delta[(new_final_state - 1, 'eps')] = [n.initial_state + 1, new_final_state]
	new_no_states = n.no_states + 2
	new_alphabet = n.alphabet

	nfa = NFA(new_no_states,
			  new_alphabet,
			  new_initial_state,
			  new_final_state,
			  new_delta)

	return nfa


# make a simple nfa with 2 state one initial state
# one final state and a single transition
# for the given lettter
def simple_nfa(letter):
	initial_state = 0
	final_state = initial_state + 1
	delta = {(initial_state, letter): [final_state]}
	no_states = 2
	alphabet = [letter]

	return NFA(no_states, alphabet, initial_state, final_state, delta)


# bad implementation do not read
def get_e_closure(no_states, final_states, alphabet, delta):

    new_states = []
    new_fstates = []
    for i in range(0, no_states):
        visited = set([i])
        queue = [str(i)]
        while queue:
            s = queue.pop(0)
            tr = (str(s), 'eps')
            if tr in delta:
                for i in delta[tr]:
                    if i not in visited:
                        visited.add(i)
                        queue.append(i)
        ls = ''.join(map(str, list(visited)))
        new_states.append(ls)
        for j in ls:
            if int(j) in final_states:
                new_fstates.append(ls)
    
    new_fstates = list(set(new_fstates))
    alphabet.remove('eps')
    dfa_delta = {}
    dfa_states = []
    dfa_fstates = []
    dfa_states.append(new_states[0])
    dfa_no_states = 1
    i = 0
    d = {new_states[0]:0}
    id_state = 1
    for state in dfa_states:
        for letter in alphabet:
            tr = (state, letter)
            l_state = []
            for i in state:
                if (i, letter) in delta:
                    l_state.extend(delta[(i, letter)])
            dfa_no_states += 1
            make_state = ''.join(set(l_state))
            if make_state not in d:
                d[make_state] = id_state
                id_state += 1
            if make_state not in dfa_states:
                dfa_states.append(make_state)
            if state != '':
                dfa_delta[(d[state], letter)] = d[make_state]

    for st in dfa_states:
        for i in st:
            if int(i) in final_states and st not in dfa_fstates:
                dfa_fstates.append(st)

    # transform string states to int
    for i in range(0, len(dfa_states)):
        dfa_states[i] = d[dfa_states[i]]

    for i in range(0, len(dfa_states)):
        if (i,alphabet[0]) not in dfa_delta:
            for j in alphabet:
                dfa_delta[(i, j)] = i

    if (len(dfa_states)- 1, alphabet[0]) not in dfa_delta:
        for letter in alphabet:
            dfa_delta[(str(len(dfa_states) - 1), letter)] = str(len(dfa_states) - 1)
    
    for i in dfa_delta:
        if dfa_delta[i] == '':
            dfa_delta[i] = str(len(dfa_states) - 1)

    for i in range(0, len(dfa_fstates)):
        dfa_fstates[i] = d[dfa_fstates[i]]

    return (dfa_states, dfa_delta, dfa_fstates)


# same algorithm as second part of e_closure
# insert first state of nfa into dfa and
# start finding new states
# the next function does this:
# -   A   B      -   A   B      -   A   B
# 0  1,2  0      0   12  0      0   1   0
# 1   2  0,1  => 12  12  01  => 1   1   2
# 2   1   2      01  12  01     2   1   2
def convert_nfa_dfa(no_states, final_states, alphabet, delta):
    # insert initial state of NFA into list of DFA states
    dfa_delta = {}
    dfa_states = []
    dfa_fstates = []
    dfa_states.append('0')
    dfa_no_states = 1
    i = 0
    d = {'0':0}
    id_state = 1
    
    if 'eps' in alphabet:
        (dfa_states, dfa_delta, dfa_fstates) = get_e_closure(no_states, final_states, alphabet, delta)
        return (dfa_states, dfa_delta, dfa_fstates)

    for state in dfa_states:
        for letter in alphabet:
            l_state = []
            for i in state:
                if (i, letter) in delta:
                    l_state.extend(delta[(i, letter)])
            dfa_no_states += 1
            make_state = ''.join(set(l_state))
            if make_state not in d:
                d[make_state] = id_state
                id_state += 1
            if make_state not in dfa_states:
                dfa_states.append(make_state)
            if state != '':
                dfa_delta[(d[state], letter)] = d[make_state]

    for st in dfa_states:
        for i in st:
            if i == 's':
                pass
            else:
                if int(i) == final_states and st not in dfa_fstates:
                    dfa_fstates.append(st)

    for i in range(0, len(dfa_states)):
        dfa_states[i] = d[dfa_states[i]]

    for i in range(0, len(dfa_states)):
        if (i,alphabet[0]) not in dfa_delta:
            for j in alphabet:
                dfa_delta[(i, j)] = i

    if (len(dfa_states)- 1, alphabet[0]) not in dfa_delta:
        for letter in alphabet:
            dfa_delta[(str(len(dfa_states) - 1), letter)] = str(len(dfa_states) - 1)
    
    for i in dfa_delta:
        if dfa_delta[i] == '':
            dfa_delta[i] = str(len(dfa_states) - 1)

    for i in range(0, len(dfa_fstates)):
        dfa_fstates[i] = d[dfa_fstates[i]]

    return (dfa_states, dfa_delta, set(dfa_fstates))
