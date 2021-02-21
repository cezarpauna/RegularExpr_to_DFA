# Generated from Regex.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RegexParser import RegexParser
else:
    from RegexParser import RegexParser

# This class defines a complete generic visitor for a parse tree produced by RegexParser.

class RegexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RegexParser#expr.
    def visitExpr(self, ctx:RegexParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#conc_expr.
    def visitConc_expr(self, ctx:RegexParser.Conc_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#kleene_expr.
    def visitKleene_expr(self, ctx:RegexParser.Kleene_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#kleene.
    def visitKleene(self, ctx:RegexParser.KleeneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#variable.
    def visitVariable(self, ctx:RegexParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#inner_expr.
    def visitInner_expr(self, ctx:RegexParser.Inner_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#atom.
    def visitAtom(self, ctx:RegexParser.AtomContext):
        return self.visitChildren(ctx)



del RegexParser