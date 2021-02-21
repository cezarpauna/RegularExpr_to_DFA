grammar Regex;

KLEENE     : '*'+ ;
OR         : '|' ;
OPEN       : '(' ;
CLOSED     : ')' ;
WHITESPACE : [ \t\r\n]+ -> skip ;
VAR        : [a-z];

expr : conc_expr | conc_expr OR expr;
conc_expr : kleene_expr | conc_expr kleene_expr;
kleene_expr : atom | kleene;
kleene : atom KLEENE;

variable : VAR;
inner_expr : OPEN expr CLOSED;
atom : variable | inner_expr;



