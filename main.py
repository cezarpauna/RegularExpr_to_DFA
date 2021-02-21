import sys
from antlr4 import *
from RegexLexer import RegexLexer
from RegexParser import RegexParser
from RegexShowVisitor import RegexShowVisitor
from RegexEvalVisitor import RegexEvalVisitor
from NFA import NFA
from NFA_utils import *

input = FileStream(sys.argv[1])
output1 = open(sys.argv[2], 'w')
output2 = open(sys.argv[3], 'w')

lexer = RegexLexer(input)
stream = CommonTokenStream(lexer)
parser = RegexParser(stream)

tree = parser.expr()

evalVisitor = RegexEvalVisitor()

# get eval nfa
nfa = evalVisitor.visit(tree)

# write to file
output1.write(nfa.to_string())

# convert crt nfa to dfa --> todo (it doesn't work)
(dfa_states, dfa_delta, dfa_fstates) = convert_nfa_dfa(nfa.no_states, nfa.final_state, nfa.alphabet, nfa.delta)

# write dfa to file
output = str(len(dfa_states)) + '\n' + ' '.join(map(str,dfa_fstates)) + '\n'
for (a,b) in dfa_delta:
    output += str(a) + ' ' + str(b) + ' ' + str(dfa_delta[(a, b)]) + '\n'
    
output2.write(output)

