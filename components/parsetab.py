
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSING BREAK CHAR CLOSE_BRAKETS CLOSE_PAREN DIV DO DOUBLE ELSE EQUALS FLOAT FOR GREATER GREATER_OR_EQUALS IDENTIFIER IF INT LESSER LESSER_OR_EQUALS MUL NOT NUMBER OPEN_BRAKETS OPEN_PAREN OR PRINT RETURN SEMI_COLON SUB SUM WHILE\n        statements : statement SEMI_COLON statements\n                   | statement SEMI_COLON \n        \n        statement : expression\n                  | assignment\n        \n        assignment : IDENTIFIER ASSING expression\n        \n        expression : expression SUM expression\n                   | expression SUB expression\n                   | expression MUL expression\n                   | expression DIV expression\n        \n        expression : term\n        \n        term : IDENTIFIER\n            | NUMBER\n\n        \n        factor : NUMBER\n        '
    
_lr_action_items = {'IDENTIFIER':([0,8,9,10,11,12,13,],[6,6,16,16,16,16,16,]),'NUMBER':([0,8,9,10,11,12,13,],[7,7,7,7,7,7,7,]),'$end':([1,8,14,],[0,-2,-1,]),'SEMI_COLON':([2,3,4,5,6,7,15,16,17,18,19,20,],[8,-3,-4,-10,-11,-12,-6,-11,-7,-8,-9,-5,]),'SUM':([3,5,6,7,15,16,17,18,19,20,],[9,-10,-11,-12,9,-11,9,9,9,9,]),'SUB':([3,5,6,7,15,16,17,18,19,20,],[10,-10,-11,-12,10,-11,10,10,10,10,]),'MUL':([3,5,6,7,15,16,17,18,19,20,],[11,-10,-11,-12,11,-11,11,11,11,11,]),'DIV':([3,5,6,7,15,16,17,18,19,20,],[12,-10,-11,-12,12,-11,12,12,12,12,]),'ASSING':([6,],[13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,8,],[1,14,]),'statement':([0,8,],[2,2,]),'expression':([0,8,9,10,11,12,13,],[3,3,15,17,18,19,20,]),'assignment':([0,8,],[4,4,]),'term':([0,8,9,10,11,12,13,],[5,5,5,5,5,5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statement SEMI_COLON statements','statements',3,'p_statements','parser.py',28),
  ('statements -> statement SEMI_COLON','statements',2,'p_statements','parser.py',29),
  ('statement -> expression','statement',1,'p_statement','parser.py',35),
  ('statement -> assignment','statement',1,'p_statement','parser.py',36),
  ('assignment -> IDENTIFIER ASSING expression','assignment',3,'p_assignment','parser.py',42),
  ('expression -> expression SUM expression','expression',3,'p_expression_binop','parser.py',48),
  ('expression -> expression SUB expression','expression',3,'p_expression_binop','parser.py',49),
  ('expression -> expression MUL expression','expression',3,'p_expression_binop','parser.py',50),
  ('expression -> expression DIV expression','expression',3,'p_expression_binop','parser.py',51),
  ('expression -> term','expression',1,'p_expression_term','parser.py',57),
  ('term -> IDENTIFIER','term',1,'p_term','parser.py',63),
  ('term -> NUMBER','term',1,'p_term','parser.py',64),
  ('factor -> NUMBER','factor',1,'p_factor_num','parser.py',74),
]
