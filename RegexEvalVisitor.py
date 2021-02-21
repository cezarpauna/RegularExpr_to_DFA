import sys
from antlr4 import *
from RegexVisitor import RegexVisitor
from RegexParser import RegexParser
from NFA_utils import *

class RegexEvalVisitor(RegexVisitor):


	# check if we have conc_expr or conc_expr OR expr
	# visit expression and return evaluation of conc_expr
	# or make the OR operation and return resulting nfa
	def visitExpr(self, ctx:RegexParser.ExprContext):
		or_e = ctx.conc_expr()
		e = ctx.expr()

		if e:
			nfa1 = self.visit(or_e)
			nfa2 = self.visit(e)
			return or_op(nfa1, nfa2)

		if or_e:
			return self.visit(or_e)


	# visit the given expresison and returns the concatenation of
	# returned nfas or visits the next expression with kleene star
	def visitConc_expr(self, ctx:RegexParser.Conc_exprContext):
		conc_e = ctx.conc_expr()
		kleene_e = ctx.kleene_expr()

		if conc_e:
			nfa1 = self.visit(kleene_e)
			nfa2 = self.visit(conc_e)
			nfa = concatenate(nfa2, nfa1)
			return nfa

		if kleene_e:
			return self.visit(kleene_e)


	# same ideea, visiting the given expressions and returning nfas
	def visitKleene_expr(self, ctx:RegexParser.Kleene_exprContext):
		atom_e = ctx.atom()
		kleene_e = ctx.kleene()

		if kleene_e:
			nfa1 = self.visit(kleene_e)
			nfa = kleene_star(nfa1)
			return nfa

		if atom_e:
			return self.visit(atom_e)


	# visit atom
	def visitKleene(self, ctx:RegexParser.KleeneContext):
		atom_e = ctx.atom()
		return self.visit(atom_e)


	# visit letter or inner
	def visitAtom(self, ctx:RegexParser.AtomContext):
		letter = ctx.variable()
		inner = ctx.inner_expr()

		if letter:
			return self.visit(letter)

		if inner:
			return self.visit(inner)


	# make simple nfa (for a letter make a 2 states nfa)
	def visitVariable(self, ctx:RegexParser.VariableContext):
		letter = ctx.VAR()
		nfa = simple_nfa(letter)
		return nfa


	# evaluate inner expression
	def visitInner_expr(self, ctx:RegexParser.Inner_exprContext):
		return self.visit(ctx.expr())
		