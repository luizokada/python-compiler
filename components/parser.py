import ply.yacc as yacc
class Node:
    def __init__(self,type,children=None,leaf=None):
         self.type = type
         if children:
              self.children = children
         else:
              self.children = [ ]
         self.leaf = leaf
	 
variabes = {}
current_variable_identifier = None
current_variable_type = None
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.parser = yacc.yacc(module=self)
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
        """
        p[0] = Node("binop", [p[1], p[3]], p[2])

    def p_expression_term(self, p):
        """
        expression : term
                    | factor
        """
        p[0] = Node("expression", leaf=p[1])

    def p_term(self, p):
        """
        term : IDENTIFIER

        """
        if(p[1] is not Node):
            current_variable_identifier = p[1]
        
        p[0] = Node('term', leaf=p[1])

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
        if p[1].leaf in variabes:
            if(variable not in variabes[p[1].leaf]):
                variabes[p[1].leaf].append(variable)
        else:
            variabes[p[1].leaf] = [variable]
            
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
        print(len(p))
        if(len(p)>3):
            p[0] = Node('param', [Node('PAREN',leaf=p[1]),p[2],Node('PAREN',leaf=p[3])])
        else:
            p[0] = Node('param', leaf=p[1]+p[2])
        pass
    def p_error(self, p):
        print("Syntax error in input on line: ", p.lineno)
        print(p)
        exit(1)

        

        