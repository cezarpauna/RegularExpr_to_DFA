import sys
from antlr4 import *
from RegexVisitor import RegexVisitor
from RegexParser import RegexParser

class RegexShowVisitor(RegexVisitor):
	
	def visitVariable(self, ctx:RegexParser.VariableContext):
		print(ctx.VAR())
		return self.visitChildren(ctx)