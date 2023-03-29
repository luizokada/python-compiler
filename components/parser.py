import ply.yacc as yacc
from ply.yacc import format_stack_entry
class Node:
    def __init__(self,type,children=None,leaf=None):
         self.type = type
         if children:
              self.children = children
         else:
              self.children = [ ]
         self.leaf = leaf
	 
variables = {}
current_variable_identifier = None
current_variable_type = None
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.stack = []
        self.parser = yacc.yacc(module=self,debug=True)
        self.precedence = (
            ('left', 'OR'),
            ('left', 'AND'),
            ('left', 'NOT'),
            ('nonassoc', 'EQUALS', 'GREATER', 'LESSER', 'GREATER_OR_EQUALS', 'LESSER_OR_EQUALS'),
            ('left', 'SUM', 'SUB'),
            ('left', 'MUL', 'DIV'),
        )


    def p_start(self,p):
        """
        main : type MAIN param scope
        """
        p[0] = Node('main', [p[1], p[3], p[4]])
        pass
    
    
    def p_scope(self,p):
        """
        scope : OPEN_BRAKETS statements CLOSE_BRAKETS
              
        """
        
        p[0] = Node('scope', [p[2]])
    
        
        
        
    def p_statements(self, p):
        """
        statements : statement SEMI_COLON statements
                   | statement SEMI_COLON 
                   | if_statement statement
                   | if_statement
                   | for_statement
                   
        """
        statements = [p[1]]
        if len(p) > 3:
            statements += p[3].children
        p[0] = Node('statements', statements)
        

    def p_statement(self, p):
        """
        statement : expression
                  | assignment
                  | declaration
        """
        p[0] =  Node('statement', [p[1]])

    def p_assignment(self, p):
        """
        assignment : term ASSING expression
                    | term ASSING term
                    | term ASSING factor 
        """
        p[0] = Node('assignment', [p[1], p[3]],p[2])
        pass
    

        
    def p_expression_binop(self, p):
        """
        expression : expression SUM expression
                   | expression SUB expression
                   | expression MUL expression
                   | expression DIV expression
                   | expression OR expression
                   | expression NOT expression
                   | expression EQUALS expression
                   | expression GREATER expression
                   | expression LESSER expression
                   | expression GREATER_OR_EQUALS expression
                   | expression LESSER_OR_EQUALS expression
        """
        p[0] = Node("binop", [p[1], p[3]], p[2])

    def p_expression_term(self, p):
        """
        expression : term
                    | factor
        """
        p[0] = Node("expression", [p[1]])

    def p_term(self, p):
        """
        term : IDENTIFIER

        """
        
        p[0] = Node('term', leaf=p[1])

      
    def p_for_statement(self, p):
        """
        for_statement : T_FOR OPEN_PAREN for_initilizer SEMI_COLON expression SEMI_COLON expression CLOSE_PAREN scope
        """
        p[0] =  Node('for', [])
        
        
    def p_for_initializer(self,p):
        """
        for_initilizer : assignment
                        | declaration assignment
        
        """
        if(len(p)==2):
            p[0] = Node('for_initilizer', [p[1]])
        else:
            p[0] = Node('for_initilizer', [p[1],p[2]])
    def p_if_statement(self, p):
        """
        if_statement : IF OPEN_PAREN expression CLOSE_PAREN scope 
                            | IF OPEN_PAREN expression CLOSE_PAREN scope ELSE scope
        """
        if len(p) == 6:
            p[0] = Node('if', [Node('IF', leaf=p[1]), Node('PAREN', leaf=p[2]), p[3], Node('PAREN', leaf=p[4]), p[5]])
        else:
            p[0] = Node('if', [Node('IF', leaf=p[1]), Node('PAREN', leaf=p[2]), p[3], Node('PAREN', leaf=p[4]), p[5], Node('ELSE', leaf=p[6]), p[7]])
        pass
    
    
    def p_factor_num(self, p):
        """
        factor : NUMBER
        """
        p[0] =  Node('NUMBER', leaf=p[1])
        
    def p_type(self,p):
        """
        type : INT
             | FLOAT
             | CHAR
        """ 
        
        p[0] = Node('type', leaf=p[1]) 
        pass

    def p_declaration(self,p):
        """
        declaration : type term
                    | type assignment 
        """
        variable = None
        if(p[2].type != 'assignment'):
            variable = p[2].leaf
        else:
            variable = p[2].children[0].leaf
        if(variable in variables.keys()):
            print("Syntax error in declaration statement. Variable already declared.")
            
                
        variables[variable] = p[1].leaf
            
        p[0] = Node('declaration', [p[1], p[2]])
        pass

    def p_declarations(self,p):
        """
        declarations : declaration COMMA declarations
                     | declaration
        """
        if(len(p)>3):
            p[0] = Node('declarations', [p[1], p[3]])
        else:
            p[0] = Node('declarations', [p[1]])
        
    
    def p_param(self,p):
        """
        param : OPEN_PAREN declarations CLOSE_PAREN
              | OPEN_PAREN CLOSE_PAREN
        """
        if(len(p)>3):
            p[0] = Node('param', [Node('PAREN',leaf=p[1]),p[2],Node('PAREN',leaf=p[3])])
        else:
            p[0] = Node('param', leaf=p[1]+p[2])
        pass
  
        
    
   
    def p_error(self, p):
        print("Syntax error in input on line: ", p.lineno)
        print(p)

        

        