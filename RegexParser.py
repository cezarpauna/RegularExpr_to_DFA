# Generated from Regex.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\3\2\3\2\3\2\3\2\3\2\5\2\26\n\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\7\3\35\n\3\f\3\16\3 \13\3\3\4\3\4\5\4$\n\4\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\5\b\61\n\b\3\b")
        buf.write("\2\3\4\t\2\4\6\b\n\f\16\2\2\2/\2\25\3\2\2\2\4\27\3\2\2")
        buf.write("\2\6#\3\2\2\2\b%\3\2\2\2\n(\3\2\2\2\f*\3\2\2\2\16\60\3")
        buf.write("\2\2\2\20\26\5\4\3\2\21\22\5\4\3\2\22\23\7\4\2\2\23\24")
        buf.write("\5\2\2\2\24\26\3\2\2\2\25\20\3\2\2\2\25\21\3\2\2\2\26")
        buf.write("\3\3\2\2\2\27\30\b\3\1\2\30\31\5\6\4\2\31\36\3\2\2\2\32")
        buf.write("\33\f\3\2\2\33\35\5\6\4\2\34\32\3\2\2\2\35 \3\2\2\2\36")
        buf.write("\34\3\2\2\2\36\37\3\2\2\2\37\5\3\2\2\2 \36\3\2\2\2!$\5")
        buf.write("\16\b\2\"$\5\b\5\2#!\3\2\2\2#\"\3\2\2\2$\7\3\2\2\2%&\5")
        buf.write("\16\b\2&\'\7\3\2\2\'\t\3\2\2\2()\7\b\2\2)\13\3\2\2\2*")
        buf.write("+\7\5\2\2+,\5\2\2\2,-\7\6\2\2-\r\3\2\2\2.\61\5\n\6\2/")
        buf.write("\61\5\f\7\2\60.\3\2\2\2\60/\3\2\2\2\61\17\3\2\2\2\6\25")
        buf.write("\36#\60")
        return buf.getvalue()


class RegexParser ( Parser ):

    grammarFileName = "Regex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'|'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "KLEENE", "OR", "OPEN", "CLOSED", "WHITESPACE", 
                      "VAR" ]

    RULE_expr = 0
    RULE_conc_expr = 1
    RULE_kleene_expr = 2
    RULE_kleene = 3
    RULE_variable = 4
    RULE_inner_expr = 5
    RULE_atom = 6

    ruleNames =  [ "expr", "conc_expr", "kleene_expr", "kleene", "variable", 
                   "inner_expr", "atom" ]

    EOF = Token.EOF
    KLEENE=1
    OR=2
    OPEN=3
    CLOSED=4
    WHITESPACE=5
    VAR=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conc_expr(self):
            return self.getTypedRuleContext(RegexParser.Conc_exprContext,0)


        def OR(self):
            return self.getToken(RegexParser.OR, 0)

        def expr(self):
            return self.getTypedRuleContext(RegexParser.ExprContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = RegexParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.conc_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.conc_expr(0)
                self.state = 16
                self.match(RegexParser.OR)
                self.state = 17
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Conc_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kleene_expr(self):
            return self.getTypedRuleContext(RegexParser.Kleene_exprContext,0)


        def conc_expr(self):
            return self.getTypedRuleContext(RegexParser.Conc_exprContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_conc_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConc_expr" ):
                return visitor.visitConc_expr(self)
            else:
                return visitor.visitChildren(self)



    def conc_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegexParser.Conc_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_conc_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.kleene_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 28
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RegexParser.Conc_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_conc_expr)
                    self.state = 24
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 25
                    self.kleene_expr() 
                self.state = 30
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Kleene_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(RegexParser.AtomContext,0)


        def kleene(self):
            return self.getTypedRuleContext(RegexParser.KleeneContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_kleene_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKleene_expr" ):
                return visitor.visitKleene_expr(self)
            else:
                return visitor.visitChildren(self)




    def kleene_expr(self):

        localctx = RegexParser.Kleene_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_kleene_expr)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.kleene()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KleeneContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(RegexParser.AtomContext,0)


        def KLEENE(self):
            return self.getToken(RegexParser.KLEENE, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_kleene

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKleene" ):
                return visitor.visitKleene(self)
            else:
                return visitor.visitChildren(self)




    def kleene(self):

        localctx = RegexParser.KleeneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_kleene)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.atom()
            self.state = 36
            self.match(RegexParser.KLEENE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(RegexParser.VAR, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = RegexParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(RegexParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inner_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(RegexParser.OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(RegexParser.ExprContext,0)


        def CLOSED(self):
            return self.getToken(RegexParser.CLOSED, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_inner_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInner_expr" ):
                return visitor.visitInner_expr(self)
            else:
                return visitor.visitChildren(self)




    def inner_expr(self):

        localctx = RegexParser.Inner_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_inner_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(RegexParser.OPEN)
            self.state = 41
            self.expr()
            self.state = 42
            self.match(RegexParser.CLOSED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(RegexParser.VariableContext,0)


        def inner_expr(self):
            return self.getTypedRuleContext(RegexParser.Inner_exprContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = RegexParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atom)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegexParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.variable()
                pass
            elif token in [RegexParser.OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.inner_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.conc_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def conc_expr_sempred(self, localctx:Conc_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




