
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSING BREAK CHAR CHARACTER CLOSE_BRAKETS CLOSE_INTER CLOSE_PAREN COMMA DECREMENT DIFERENT DIV DO DOUBLE ELSE EQUALS FLOAT FOR GREATER GREATER_OR_EQUALS IDENTIFIER IF INCREMENT INT LESSER LESSER_OR_EQUALS MAIN MUL NOT NUMBER OPEN_BRAKETS OPEN_INTER OPEN_PAREN OR PRINT RETURN SCAN SEMI_COLON STRING_LITERAL SUB SUM WHILE\n        main : type MAIN param scope\n        \n        scope : OPEN_BRAKETS new_scope statements CLOSE_BRAKETS\n              | OPEN_BRAKETS new_scope statements return_statement CLOSE_BRAKETS\n              \n        \n        new_scope :\n        \n        statements : statement statements\n                   | statement  \n                   \n        \n        statement : expression SEMI_COLON\n                  | assignment SEMI_COLON\n                  | declaration SEMI_COLON\n                  | array_declaration SEMI_COLON\n                  | if_statement\n                  | for_statement\n                  | do_while_statement\n                  | while_statement\n                  | call_function\n \n        \n        factor_char : CHARACTER\n        \n        expression : term\n                    | factor\n                   \n        \n        term : IDENTIFIER\n\n        \n        type : INT\n             | FLOAT\n             | CHAR\n        \n        factor : NUMBER\n                | SUB NUMBER\n        \n        sequence : NUMBER COMMA sequence\n                 | NUMBER\n                 | CHARACTER COMMA sequence\n                 | CHARACTER\n        \n        return_statement : RETURN expression SEMI_COLON\n                         | RETURN SEMI_COLON\n        \n        assignment : term ASSING expression\n                    | term ASSING term\n                    | term ASSING factor \n                    | term ASSING factor_char\n                    | term array_index ASSING factor\n                    | term array_index ASSING term\n                    | term array_index ASSING factor_char\n        \n        expression : expression SUM expression\n                   | expression SUB expression\n                   | expression MUL expression\n                   | expression DIV expression\n                   | expression DECREMENT\n                   | expression INCREMENT  \n                   | OPEN_PAREN expression CLOSE_PAREN  \n        \n        condition : expression OR expression\n                   | expression AND expression\n                   | expression EQUALS expression\n                   | condition OR condition\n                   | condition AND condition\n                   | expression DIFERENT expression\n                   | expression GREATER expression\n                   | expression LESSER expression\n                   | expression GREATER_OR_EQUALS expression\n                   | expression LESSER_OR_EQUALS expression\n                   | expression DIFERENT factor_char\n                   | expression EQUALS factor_char\n                   | OPEN_PAREN condition CLOSE_PAREN\n                   | NOT condition\n\n                   \n        \n        declaration : type term\n    \n        \n        array_index : OPEN_INTER factor CLOSE_INTER\n        \n        assignment_array : ASSING OPEN_INTER sequence CLOSE_INTER\n        \n        array_declaration : type term OPEN_INTER NUMBER CLOSE_INTER\n                          | type term OPEN_INTER NUMBER CLOSE_INTER assignment_array\n        \n        declarations : declaration COMMA declarations\n                     | declaration\n        \n        if_statement : IF OPEN_PAREN condition CLOSE_PAREN scope \n                     | IF OPEN_PAREN condition CLOSE_PAREN scope ELSE scope\n        \n        param : OPEN_PAREN declarations CLOSE_PAREN\n              | OPEN_PAREN CLOSE_PAREN\n        \n        passing_param : term COMMA passing_param\n                      | term\n                      | factor COMMA passing_param\n                      | factor\n        \n        print_statement : PRINT OPEN_PAREN STRING_LITERAL CLOSE_PAREN SEMI_COLON\n                        | PRINT OPEN_PAREN STRING_LITERAL COMMA passing_param CLOSE_PAREN SEMI_COLON\n        \n        scan_statement : SCAN OPEN_PAREN STRING_LITERAL COMMA passing_param CLOSE_PAREN SEMI_COLON\n        \n        call_function : IDENTIFIER OPEN_PAREN passing_param CLOSE_PAREN SEMI_COLON\n                      | IDENTIFIER OPEN_PAREN CLOSE_PAREN SEMI_COLON\n                      | print_statement\n                      | scan_statement\n                      \n        \n        for_statement : FOR OPEN_PAREN for_initilizer SEMI_COLON condition SEMI_COLON expression CLOSE_PAREN scope\n        \n        for_initilizer : assignment\n        \n        \n        do_while_statement : DO scope WHILE OPEN_PAREN condition CLOSE_PAREN SEMI_COLON\n      \n        \n        while_statement : WHILE OPEN_PAREN condition CLOSE_PAREN scope\n        \n        '
    
_lr_action_items = {'INT':([0,8,10,15,17,21,26,27,28,29,30,42,43,47,51,58,59,60,75,130,138,153,154,157,168,170,171,172,180,],[3,3,-4,3,3,3,-11,-12,-13,-14,-15,-79,-80,-2,-7,-8,-9,-10,-3,-78,-66,-84,-77,-74,-67,-83,-75,-76,-81,]),'FLOAT':([0,8,10,15,17,21,26,27,28,29,30,42,43,47,51,58,59,60,75,130,138,153,154,157,168,170,171,172,180,],[4,4,-4,4,4,4,-11,-12,-13,-14,-15,-79,-80,-2,-7,-8,-9,-10,-3,-78,-66,-84,-77,-74,-67,-83,-75,-76,-81,]),'CHAR':([0,8,10,15,17,21,26,27,28,29,30,42,43,47,51,58,59,60,75,130,138,153,154,157,168,170,171,172,180,],[5,5,-4,5,5,5,-11,-12,-13,-14,-15,-79,-80,-2,-7,-8,-9,-10,-3,-78,-66,-84,-77,-74,-67,-83,-75,-76,-81,]),'$end':([1,9,47,75,],[0,-1,-2,-3,]),'MAIN':([2,3,4,5,],[6,-20,-21,-22,]),'IDENTIFIER':([3,4,5,10,14,15,21,26,27,28,29,30,34,35,42,43,47,49,51,52,53,54,55,58,59,60,61,68,69,71,72,75,87,91,94,115,116,117,118,119,120,121,122,123,124,126,127,130,131,132,134,135,138,153,154,157,163,168,170,171,172,180,],[-20,-21,-22,-4,19,41,41,-11,-12,-13,-14,-15,19,19,-79,-80,-2,19,-7,19,19,19,19,-8,-9,-10,19,19,19,19,19,-3,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-78,19,19,19,19,-66,-84,-77,-74,19,-67,-83,-75,-76,-81,]),'OPEN_PAREN':([6,10,15,21,26,27,28,29,30,34,37,38,40,41,42,43,44,45,47,49,51,52,53,54,55,58,59,60,61,68,71,75,91,94,98,115,116,117,118,119,120,121,122,123,124,126,127,130,138,153,154,157,163,168,170,171,172,180,],[8,-4,34,34,-11,-12,-13,-14,-15,34,68,69,71,72,-79,-80,73,74,-2,34,-7,34,34,34,34,-8,-9,-10,34,91,91,-3,91,91,127,91,91,34,34,34,34,34,34,34,34,91,91,-78,-66,-84,-77,-74,34,-67,-83,-75,-76,-81,]),'OPEN_BRAKETS':([7,12,16,39,114,128,162,176,],[10,-69,-68,10,10,10,10,10,]),'CLOSE_PAREN':([8,11,13,18,19,32,36,46,56,57,64,65,66,72,78,79,80,81,86,89,92,99,100,102,103,104,112,113,125,137,139,140,141,142,143,144,145,146,147,148,149,150,152,155,156,158,159,169,],[12,16,-65,-59,-19,-18,-23,-64,-42,-43,-24,89,-17,101,-38,-39,-40,-41,-16,-44,114,128,129,-71,-73,133,137,89,-58,-57,-48,-49,-45,-46,-47,-56,-50,-55,-51,-52,-53,-54,164,-70,-72,165,166,176,]),'IF':([10,15,21,26,27,28,29,30,42,43,47,51,58,59,60,75,130,138,153,154,157,168,170,171,172,180,],[-4,37,37,-11,-12,-13,-14,-15,-79,-80,-2,-7,-8,-9,-10,-3,-78,-66,-84,-77,-74,-67,-83,-75,-76,-81,]),'FOR':([10,15,21,26,27,28,29,30,42,43,47,51,58,59,60,75,130,138,153,154,157,168,170,171,172,180,],[-4,38,38,-11,-12,-13,-14,-15,-79,-80,-2,-7,-8,-9,-10,-3,-78,-66,-84,-77,-74,-67,-83,-75,-76,-81,]),'DO':([10,15,21,26,27,28,29,30,42,43,47,51,58,59,60,75,130,138,153,154,157,168,170,171,172,180,],[-4,39,39,-11,-12,-13,-14,-15,-79,-80,-2,-7,-8,-9,-10,-3,-78,-66,-84,-77,-74,-67,-83,-75,-76,-81,]),'WHILE':([10,15,21,26,27,28,29,30,42,43,47,51,58,59,60,70,75,130,138,153,154,157,168,170,171,172,180,],[-4,40,40,-11,-12,-13,-14,-15,-79,-80,-2,-7,-8,-9,-10,98,-3,-78,-66,-84,-77,-74,-67,-83,-75,-76,-81,]),'NUMBER':([10,15,21,26,27,28,29,30,33,34,42,43,47,49,51,52,53,54,55,58,59,60,61,63,68,71,72,75,87,90,91,94,115,116,117,118,119,120,121,122,123,124,126,127,130,131,132,134,135,138,153,154,157,163,167,168,170,171,172,178,179,180,],[-4,36,36,-11,-12,-13,-14,-15,64,36,-79,-80,-2,36,-7,36,36,36,36,-8,-9,-10,36,36,36,36,36,-3,36,111,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-78,36,36,36,36,-66,-84,-77,-74,36,174,-67,-83,-75,-76,174,174,-81,]),'SUB':([10,15,19,21,22,26,27,28,29,30,31,32,34,36,41,42,43,47,49,51,52,53,54,55,56,57,58,59,60,61,63,64,65,66,68,71,72,75,76,78,79,80,81,82,83,84,87,89,91,93,94,113,115,116,117,118,119,120,121,122,123,124,126,127,130,131,132,134,135,138,141,142,143,145,147,148,149,150,153,154,157,163,168,169,170,171,172,180,],[-4,33,-19,33,53,-11,-12,-13,-14,-15,-17,-18,33,-23,-19,-79,-80,-2,33,-7,33,33,33,33,-42,-43,-8,-9,-10,33,33,-24,53,-17,33,33,33,-3,53,53,53,53,53,-17,53,-18,33,-44,33,53,33,53,33,33,33,33,33,33,33,33,33,33,33,33,-78,33,33,33,33,-66,53,53,53,53,53,53,53,53,-84,-77,-74,33,-67,53,-83,-75,-76,-81,]),'PRINT':([10,15,21,26,27,28,29,30,42,43,47,51,58,59,60,75,130,138,153,154,157,168,170,171,172,180,],[-4,44,44,-11,-12,-13,-14,-15,-79,-80,-2,-7,-8,-9,-10,-3,-78,-66,-84,-77,-74,-67,-83,-75,-76,-81,]),'SCAN':([10,15,21,26,27,28,29,30,42,43,47,51,58,59,60,75,130,138,153,154,157,168,170,171,172,180,],[-4,45,45,-11,-12,-13,-14,-15,-79,-80,-2,-7,-8,-9,-10,-3,-78,-66,-84,-77,-74,-67,-83,-75,-76,-81,]),'COMMA':([13,18,19,36,64,102,103,104,105,174,175,],[17,-59,-19,-23,-24,131,132,134,135,178,179,]),'SUM':([19,22,31,32,36,41,56,57,64,65,66,76,78,79,80,81,82,83,84,89,93,113,141,142,143,145,147,148,149,150,169,],[-19,52,-17,-18,-23,-19,-42,-43,-24,52,-17,52,52,52,52,52,-17,52,-18,-44,52,52,52,52,52,52,52,52,52,52,52,]),'MUL':([19,22,31,32,36,41,56,57,64,65,66,76,78,79,80,81,82,83,84,89,93,113,141,142,143,145,147,148,149,150,169,],[-19,54,-17,-18,-23,-19,-42,-43,-24,54,-17,54,54,54,54,54,-17,54,-18,-44,54,54,54,54,54,54,54,54,54,54,54,]),'DIV':([19,22,31,32,36,41,56,57,64,65,66,76,78,79,80,81,82,83,84,89,93,113,141,142,143,145,147,148,149,150,169,],[-19,55,-17,-18,-23,-19,-42,-43,-24,55,-17,55,55,55,55,55,-17,55,-18,-44,55,55,55,55,55,55,55,55,55,55,55,]),'DECREMENT':([19,22,31,32,36,41,56,57,64,65,66,76,78,79,80,81,82,83,84,89,93,113,141,142,143,145,147,148,149,150,169,],[-19,56,-17,-18,-23,-19,-42,-43,-24,56,-17,56,56,56,56,56,-17,56,-18,-44,56,56,56,56,56,56,56,56,56,56,56,]),'INCREMENT':([19,22,31,32,36,41,56,57,64,65,66,76,78,79,80,81,82,83,84,89,93,113,141,142,143,145,147,148,149,150,169,],[-19,57,-17,-18,-23,-19,-42,-43,-24,57,-17,57,57,57,57,57,-17,57,-18,-44,57,57,57,57,57,57,57,57,57,57,57,]),'OPEN_INTER':([19,31,41,67,97,161,],[-19,63,-19,90,63,167,]),'SEMI_COLON':([19,22,23,24,25,31,32,36,41,49,56,57,64,66,67,76,78,79,80,81,82,83,84,85,86,89,95,96,101,107,108,109,125,129,133,136,137,139,140,141,142,143,144,145,146,147,148,149,150,151,160,164,165,166,177,],[-19,51,58,59,60,-17,-18,-23,-19,77,-42,-43,-24,-17,-59,106,-38,-39,-40,-41,-17,-31,-18,-34,-16,-44,126,-82,130,-36,-35,-37,-58,154,157,-62,-57,-48,-49,-45,-46,-47,-56,-50,-55,-51,-52,-53,-54,163,-63,170,171,172,-61,]),'OR':([19,32,36,56,57,64,66,78,79,80,81,86,89,92,93,99,112,113,125,137,139,140,141,142,143,144,145,146,147,148,149,150,151,152,],[-19,-18,-23,-42,-43,-24,-17,-38,-39,-40,-41,-16,-44,115,117,115,115,117,115,-57,115,115,-45,-46,-47,-56,-50,-55,-51,-52,-53,-54,115,115,]),'AND':([19,32,36,56,57,64,66,78,79,80,81,86,89,92,93,99,112,113,125,137,139,140,141,142,143,144,145,146,147,148,149,150,151,152,],[-19,-18,-23,-42,-43,-24,-17,-38,-39,-40,-41,-16,-44,116,118,116,116,118,116,-57,116,116,-45,-46,-47,-56,-50,-55,-51,-52,-53,-54,116,116,]),'EQUALS':([19,32,36,56,57,64,66,78,79,80,81,89,93,113,],[-19,-18,-23,-42,-43,-24,-17,-38,-39,-40,-41,-44,119,119,]),'DIFERENT':([19,32,36,56,57,64,66,78,79,80,81,89,93,113,],[-19,-18,-23,-42,-43,-24,-17,-38,-39,-40,-41,-44,120,120,]),'GREATER':([19,32,36,56,57,64,66,78,79,80,81,89,93,113,],[-19,-18,-23,-42,-43,-24,-17,-38,-39,-40,-41,-44,121,121,]),'LESSER':([19,32,36,56,57,64,66,78,79,80,81,89,93,113,],[-19,-18,-23,-42,-43,-24,-17,-38,-39,-40,-41,-44,122,122,]),'GREATER_OR_EQUALS':([19,32,36,56,57,64,66,78,79,80,81,89,93,113,],[-19,-18,-23,-42,-43,-24,-17,-38,-39,-40,-41,-44,123,123,]),'LESSER_OR_EQUALS':([19,32,36,56,57,64,66,78,79,80,81,89,93,113,],[-19,-18,-23,-42,-43,-24,-17,-38,-39,-40,-41,-44,124,124,]),'ASSING':([19,31,41,62,97,110,136,],[-19,61,-19,87,61,-60,161,]),'CLOSE_BRAKETS':([20,21,26,27,28,29,30,42,43,47,48,50,51,58,59,60,75,77,106,130,138,153,154,157,168,170,171,172,180,],[47,-6,-11,-12,-13,-14,-15,-79,-80,-2,75,-5,-7,-8,-9,-10,-3,-30,-29,-78,-66,-84,-77,-74,-67,-83,-75,-76,-81,]),'RETURN':([20,21,26,27,28,29,30,42,43,47,50,51,58,59,60,75,130,138,153,154,157,168,170,171,172,180,],[49,-6,-11,-12,-13,-14,-15,-79,-80,-2,-5,-7,-8,-9,-10,-3,-78,-66,-84,-77,-74,-67,-83,-75,-76,-81,]),'CLOSE_INTER':([36,64,88,111,173,174,175,181,182,],[-23,-24,110,136,177,-26,-28,-25,-27,]),'ELSE':([47,75,138,],[-2,-3,162,]),'CHARACTER':([61,87,119,120,167,178,179,],[86,86,86,86,175,175,175,]),'NOT':([68,71,91,94,115,116,126,127,],[94,94,94,94,94,94,94,94,]),'STRING_LITERAL':([73,74,],[104,105,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'main':([0,],[1,]),'type':([0,8,15,17,21,],[2,14,35,14,35,]),'param':([6,],[7,]),'scope':([7,39,114,128,162,176,],[9,70,138,153,168,180,]),'declarations':([8,17,],[11,46,]),'declaration':([8,15,17,21,],[13,24,13,24,]),'new_scope':([10,],[15,]),'term':([14,15,21,34,35,49,52,53,54,55,61,68,69,71,72,87,91,94,115,116,117,118,119,120,121,122,123,124,126,127,131,132,134,135,163,],[18,31,31,66,67,66,66,66,66,66,82,66,97,66,102,107,66,66,66,66,66,66,66,66,66,66,66,66,66,66,102,102,102,102,66,]),'statements':([15,21,],[20,50,]),'statement':([15,21,],[21,21,]),'expression':([15,21,34,49,52,53,54,55,61,68,71,91,94,115,116,117,118,119,120,121,122,123,124,126,127,163,],[22,22,65,76,78,79,80,81,83,93,93,113,93,93,93,141,142,143,145,147,148,149,150,93,93,169,]),'assignment':([15,21,69,],[23,23,96,]),'array_declaration':([15,21,],[25,25,]),'if_statement':([15,21,],[26,26,]),'for_statement':([15,21,],[27,27,]),'do_while_statement':([15,21,],[28,28,]),'while_statement':([15,21,],[29,29,]),'call_function':([15,21,],[30,30,]),'factor':([15,21,34,49,52,53,54,55,61,63,68,71,72,87,91,94,115,116,117,118,119,120,121,122,123,124,126,127,131,132,134,135,163,],[32,32,32,32,32,32,32,32,84,88,32,32,103,108,32,32,32,32,32,32,32,32,32,32,32,32,32,32,103,103,103,103,32,]),'print_statement':([15,21,],[42,42,]),'scan_statement':([15,21,],[43,43,]),'return_statement':([20,],[48,]),'array_index':([31,97,],[62,62,]),'factor_char':([61,87,119,120,],[85,109,144,146,]),'condition':([68,71,91,94,115,116,126,127,],[92,99,112,125,139,140,151,152,]),'for_initilizer':([69,],[95,]),'passing_param':([72,131,132,134,135,],[100,155,156,158,159,]),'assignment_array':([136,],[160,]),'sequence':([167,178,179,],[173,181,182,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main","S'",1,None,None,None),
  ('main -> type MAIN param scope','main',4,'p_start','parser.py',60),
  ('scope -> OPEN_BRAKETS new_scope statements CLOSE_BRAKETS','scope',4,'p_scope','parser.py',70),
  ('scope -> OPEN_BRAKETS new_scope statements return_statement CLOSE_BRAKETS','scope',5,'p_scope','parser.py',71),
  ('new_scope -> <empty>','new_scope',0,'p_new_scope','parser.py',89),
  ('statements -> statement statements','statements',2,'p_statements','parser.py',104),
  ('statements -> statement','statements',1,'p_statements','parser.py',105),
  ('statement -> expression SEMI_COLON','statement',2,'p_statement','parser.py',116),
  ('statement -> assignment SEMI_COLON','statement',2,'p_statement','parser.py',117),
  ('statement -> declaration SEMI_COLON','statement',2,'p_statement','parser.py',118),
  ('statement -> array_declaration SEMI_COLON','statement',2,'p_statement','parser.py',119),
  ('statement -> if_statement','statement',1,'p_statement','parser.py',120),
  ('statement -> for_statement','statement',1,'p_statement','parser.py',121),
  ('statement -> do_while_statement','statement',1,'p_statement','parser.py',122),
  ('statement -> while_statement','statement',1,'p_statement','parser.py',123),
  ('statement -> call_function','statement',1,'p_statement','parser.py',124),
  ('factor_char -> CHARACTER','factor_char',1,'p_factor_char','parser.py',134),
  ('expression -> term','expression',1,'p_expression_term','parser.py',142),
  ('expression -> factor','expression',1,'p_expression_term','parser.py',143),
  ('term -> IDENTIFIER','term',1,'p_term','parser.py',161),
  ('type -> INT','type',1,'p_type','parser.py',170),
  ('type -> FLOAT','type',1,'p_type','parser.py',171),
  ('type -> CHAR','type',1,'p_type','parser.py',172),
  ('factor -> NUMBER','factor',1,'p_factor_num','parser.py',180),
  ('factor -> SUB NUMBER','factor',2,'p_factor_num','parser.py',181),
  ('sequence -> NUMBER COMMA sequence','sequence',3,'p_sequence','parser.py',193),
  ('sequence -> NUMBER','sequence',1,'p_sequence','parser.py',194),
  ('sequence -> CHARACTER COMMA sequence','sequence',3,'p_sequence','parser.py',195),
  ('sequence -> CHARACTER','sequence',1,'p_sequence','parser.py',196),
  ('return_statement -> RETURN expression SEMI_COLON','return_statement',3,'p_return_statement','parser.py',206),
  ('return_statement -> RETURN SEMI_COLON','return_statement',2,'p_return_statement','parser.py',207),
  ('assignment -> term ASSING expression','assignment',3,'p_assignment','parser.py',219),
  ('assignment -> term ASSING term','assignment',3,'p_assignment','parser.py',220),
  ('assignment -> term ASSING factor','assignment',3,'p_assignment','parser.py',221),
  ('assignment -> term ASSING factor_char','assignment',3,'p_assignment','parser.py',222),
  ('assignment -> term array_index ASSING factor','assignment',4,'p_assignment','parser.py',223),
  ('assignment -> term array_index ASSING term','assignment',4,'p_assignment','parser.py',224),
  ('assignment -> term array_index ASSING factor_char','assignment',4,'p_assignment','parser.py',225),
  ('expression -> expression SUM expression','expression',3,'p_expression_binop','parser.py',243),
  ('expression -> expression SUB expression','expression',3,'p_expression_binop','parser.py',244),
  ('expression -> expression MUL expression','expression',3,'p_expression_binop','parser.py',245),
  ('expression -> expression DIV expression','expression',3,'p_expression_binop','parser.py',246),
  ('expression -> expression DECREMENT','expression',2,'p_expression_binop','parser.py',247),
  ('expression -> expression INCREMENT','expression',2,'p_expression_binop','parser.py',248),
  ('expression -> OPEN_PAREN expression CLOSE_PAREN','expression',3,'p_expression_binop','parser.py',249),
  ('condition -> expression OR expression','condition',3,'p_condition','parser.py',262),
  ('condition -> expression AND expression','condition',3,'p_condition','parser.py',263),
  ('condition -> expression EQUALS expression','condition',3,'p_condition','parser.py',264),
  ('condition -> condition OR condition','condition',3,'p_condition','parser.py',265),
  ('condition -> condition AND condition','condition',3,'p_condition','parser.py',266),
  ('condition -> expression DIFERENT expression','condition',3,'p_condition','parser.py',267),
  ('condition -> expression GREATER expression','condition',3,'p_condition','parser.py',268),
  ('condition -> expression LESSER expression','condition',3,'p_condition','parser.py',269),
  ('condition -> expression GREATER_OR_EQUALS expression','condition',3,'p_condition','parser.py',270),
  ('condition -> expression LESSER_OR_EQUALS expression','condition',3,'p_condition','parser.py',271),
  ('condition -> expression DIFERENT factor_char','condition',3,'p_condition','parser.py',272),
  ('condition -> expression EQUALS factor_char','condition',3,'p_condition','parser.py',273),
  ('condition -> OPEN_PAREN condition CLOSE_PAREN','condition',3,'p_condition','parser.py',274),
  ('condition -> NOT condition','condition',2,'p_condition','parser.py',275),
  ('declaration -> type term','declaration',2,'p_declaration','parser.py',305),
  ('array_index -> OPEN_INTER factor CLOSE_INTER','array_index',3,'p_array_index','parser.py',319),
  ('assignment_array -> ASSING OPEN_INTER sequence CLOSE_INTER','assignment_array',4,'p_assignment_array','parser.py',325),
  ('array_declaration -> type term OPEN_INTER NUMBER CLOSE_INTER','array_declaration',5,'p_array_declaration','parser.py',332),
  ('array_declaration -> type term OPEN_INTER NUMBER CLOSE_INTER assignment_array','array_declaration',6,'p_array_declaration','parser.py',333),
  ('declarations -> declaration COMMA declarations','declarations',3,'p_declarations','parser.py',346),
  ('declarations -> declaration','declarations',1,'p_declarations','parser.py',347),
  ('if_statement -> IF OPEN_PAREN condition CLOSE_PAREN scope','if_statement',5,'p_if_statement','parser.py',357),
  ('if_statement -> IF OPEN_PAREN condition CLOSE_PAREN scope ELSE scope','if_statement',7,'p_if_statement','parser.py',358),
  ('param -> OPEN_PAREN declarations CLOSE_PAREN','param',3,'p_param','parser.py',369),
  ('param -> OPEN_PAREN CLOSE_PAREN','param',2,'p_param','parser.py',370),
  ('passing_param -> term COMMA passing_param','passing_param',3,'p_passing_param','parser.py',380),
  ('passing_param -> term','passing_param',1,'p_passing_param','parser.py',381),
  ('passing_param -> factor COMMA passing_param','passing_param',3,'p_passing_param','parser.py',382),
  ('passing_param -> factor','passing_param',1,'p_passing_param','parser.py',383),
  ('print_statement -> PRINT OPEN_PAREN STRING_LITERAL CLOSE_PAREN SEMI_COLON','print_statement',5,'p_print_statement','parser.py',403),
  ('print_statement -> PRINT OPEN_PAREN STRING_LITERAL COMMA passing_param CLOSE_PAREN SEMI_COLON','print_statement',7,'p_print_statement','parser.py',404),
  ('scan_statement -> SCAN OPEN_PAREN STRING_LITERAL COMMA passing_param CLOSE_PAREN SEMI_COLON','scan_statement',7,'p_scan_statement','parser.py',414),
  ('call_function -> IDENTIFIER OPEN_PAREN passing_param CLOSE_PAREN SEMI_COLON','call_function',5,'p_call_function','parser.py',423),
  ('call_function -> IDENTIFIER OPEN_PAREN CLOSE_PAREN SEMI_COLON','call_function',4,'p_call_function','parser.py',424),
  ('call_function -> print_statement','call_function',1,'p_call_function','parser.py',425),
  ('call_function -> scan_statement','call_function',1,'p_call_function','parser.py',426),
  ('for_statement -> FOR OPEN_PAREN for_initilizer SEMI_COLON condition SEMI_COLON expression CLOSE_PAREN scope','for_statement',9,'p_for_statement','parser.py',440),
  ('for_initilizer -> assignment','for_initilizer',1,'p_for_initializer','parser.py',448),
  ('do_while_statement -> DO scope WHILE OPEN_PAREN condition CLOSE_PAREN SEMI_COLON','do_while_statement',7,'p_do_while_statement','parser.py',460),
  ('while_statement -> WHILE OPEN_PAREN condition CLOSE_PAREN scope','while_statement',5,'p_while_statement','parser.py',468),
]
