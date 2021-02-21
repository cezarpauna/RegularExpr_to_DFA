
class NFA:


    def __init__(self, no_states, alphabet, initial_state, final_state, delta):
        self.no_states = no_states
        self.states = set(range(initial_state, final_state))
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_state = final_state
        self.delta = delta


    def to_string(self):
        s = ''
        s += str(self.no_states)
        s += '\n'
        s += str(self.final_state)
        s += '\n'
        for (i, k) in self.delta:
            s += str(i) + ' ' + str(k)
            for j in self.delta[(i, k)]:
                s += ' ' + str(j)
            s += '\n'
        return s