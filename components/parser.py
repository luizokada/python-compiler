import ply.yacc as yacc
from ply.yacc import format_stack_entry
import uuid
from Errors.SemanticError import SemanticError
from Tree.Tree import Node
from components.semanticValidator import SemanticValidator


def search_parent_scope(scope:Node,uuid:str):
    if scope == None:
        return None
    else:
        for child in scope.children:
            if(child.leaf == uuid):
                return scope
        
        for child in scope.children:
            parent =  search_parent_scope(child,uuid)
            if(parent != None):
                return parent
        return None
    
    
variables = {}
current_variable_identifier = None
current_variable_type = None
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_scope = []
        self.scopes = None
        self.current_node_scope = None
        self.parent_node_scope = None
        self.parser = yacc.yacc(module=self,debug=True)
        self.precedence = (
            ('left', 'OR'),
            ('left', 'AND'),
            ('left', 'NOT'),
            ('nonassoc', 'EQUALS', 'GREATER', 'LESSER', 'GREATER_OR_EQUALS', 'LESSER_OR_EQUALS'),
            ('left', 'SUM', 'SUB'),
            ('left', 'MUL', 'DIV'),
        )
        self.semanticValidator = SemanticValidator()

    def parse(self, text,lexer)->Node:
        return self.parser.parse(text, lexer=lexer.lexer)
    
    
    def p_start(self,p):
        """
        main : type MAIN param scope
        """
        p[0] = Node('main', [p[1], p[3], p[4]])
        pass
    
    
    def p_scope(self,p):
        """
        scope : OPEN_BRAKETS new_scope statements CLOSE_BRAKETS
              
        """
        p[0] = Node('scope', [p[3]])
        self.current_scope.pop()
        if(self.parent_node_scope == None):
            self.parent_node_scope = self.scopes
        else:
            self.current_node_scope = self.parent_node_scope 
            self.parent_node_scope = search_parent_scope(self.scopes,self.current_node_scope.leaf)

        
    def p_new_scope(self,p):
        """
        new_scope :
        """
        self.current_scope.append(uuid.uuid4())
        new_scope = Node('Scope',[],self.current_scope[-1])
        if(self.scopes == None):
            self.scopes = new_scope
            self.current_node_scope = new_scope
        else:
            self.current_node_scope.children.append(new_scope)
            self.parent_node_scope = self.current_node_scope
            self.current_node_scope = new_scope

    def p_statements(self, p):
        """
        statements : statement statements
                   | statement  
                   
        """
        statements = [p[1]]
        if len(p) > 2:
            statements += p[2].children
        p[0] = Node('statements', statements)
            
    def p_statement(self, p):
        """
        statement : expression SEMI_COLON
                  | assignment SEMI_COLON
                  | declaration SEMI_COLON
                  | array_declaration SEMI_COLON
                  | if_statement
                  | for_statement
                  | do_while_statement
                  | while_statement
                  | call_function
                  | return_statement
                 
        """
        p[0] =  Node('statement', [p[1]])
    
        
        
        
        
    #PRIMITIVOS
    
    
    def p_factor_char(self, p):
        """
        factor_char : CHARACTER
        """
        p[0] = Node('CHARACTER', leaf=p[1])

            
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
        
    def p_type(self,p):
        """
        type : INT
             | FLOAT
             | CHAR
        """ 
        
        p[0] = Node('type', leaf=p[1]) 
        pass
    
    def p_factor_num(self, p):
        """
        factor : NUMBER
                | SUB NUMBER
        """
        if(p[1] == '-'):
            p[0] = Node('NUMBER', leaf=-p[2])
        else:
            
            p[0] =  Node('NUMBER', leaf=p[1])
            
    def p_sequence(self, p):
        """
        sequence : NUMBER COMMA sequence
                 | NUMBER
                 | CHARACTER COMMA sequence
                 | CHARACTER
        """
        if(len(p)<=2):
            p[0] = Node('sequence', [Node('SEQUENCE_DATA', leaf=p[1])])
        else:
            p[0] = Node('sequence', [Node('SEQUENCE_DATA', leaf=p[1]),Node('SEQUENCE_DATA',leaf=p[2]),p[3]])
            
    def p_return_statement(self,p):
        """
        return_statement : RETURN expression SEMI_COLON
                         | RETURN SEMI_COLON
        """
     
        if(len(p)>3):
            p[0]= Node('return',[p[2]])
        else:
            p[0] = Node('return',leaf=p[1])
        
    #STATEMENT TYPES -----------------------
    def p_assignment(self, p):
        """
        assignment : term ASSING expression
                    | term ASSING term
                    | term ASSING factor 
                    | term ASSING factor_char
                    | term array_index ASSING factor
                    | term array_index ASSING term
                    | term array_index ASSING factor_char
        """
        if(p[2]!='='):
            p[0] = Node('assignment', [p[1],Node('assing',leaf = p[2]), p[3]])
        else:
            p[0] = Node('assignment', [p[1], p[3]],p[2])   
        variable=self.semanticValidator.validate_variable(p[1],variables,self.current_node_scope,self.scopes)
        if(p[2]=='='):
            if variable == 'int' or variable == 'float':
                self.semanticValidator.validate_number(p[3],p[1].leaf)
            elif variable == 'char':
                self.semanticValidator.validate_char(p[3],p[1].leaf)
            
        
    def p_expression_binop(self, p):
        """
        expression : expression SUM expression
                   | expression SUB expression
                   | expression MUL expression
                   | expression DIV expression
                   | expression DECREMENT
                   | expression INCREMENT  
                   | OPEN_PAREN expression CLOSE_PAREN  
        """
        if(p[1]=='('):
            p[0] = Node("binop", [p[2]])
        else:
            if(len(p)==4):       
                p[0] = Node("expression", [p[1], p[3]],p[2])
            else:
                p[0] = p[0] = Node("iteration_op", [p[1] ,Node('operation',leaf= p[2])])
            
    def p_condition(self,p):
        """
        condition : expression OR expression
                   | expression NOT expression
                   | expression EQUALS expression
                   | expression DIFERENT expression
                   | expression GREATER expression
                   | expression LESSER expression
                   | expression GREATER_OR_EQUALS expression
                   | expression LESSER_OR_EQUALS expression
                   | expression DIFERENT factor_char
                   | expression EQUALS factor_char

                   
        """
        if(p[3].type == 'CHARACTER'):
            try:
                node = p[1].children[0]
                if(node.type!='term'):
                    raise Exception
                variable=self.semanticValidator.validate_variable(node,variables,self.current_node_scope,self.scopes)    
            except:
                raise SemanticError("Error: Incompatible types in condition",p[1].leaf)
            if(variable != 'char'):
                raise SemanticError("Error: Incompatible types in condition",p[1].leaf)
        p[0] = Node("condition", [p[1],Node('operation',leaf= p[2]), p[3]])
        pass

        
    def p_declaration(self,p):
        """
        declaration : type term
    
        """
        
    
        variable = None
        variable = (p[2].leaf,self.current_scope[-1])
        variables[variable] = (p[1].leaf)
            
                
            
        p[0] = Node('declaration', [p[1], p[2]])
        pass
    
    def p_array_index(self,p):
        """
        array_index : OPEN_INTER factor CLOSE_INTER
        """
        p[0] = Node('array_index', [p[2]])
        pass
    def p_assignment_array(self,p):
        """
        assignment_array : ASSING OPEN_INTER sequence CLOSE_INTER
        """
        p[0] = Node('assignment_array', [p[3]])
        pass

    def p_array_declaration(self,p):
        """
        array_declaration : type term OPEN_INTER NUMBER CLOSE_INTER
                          | type term OPEN_INTER NUMBER CLOSE_INTER assignment_array
        """
        variable = (p[2].leaf,self.current_scope[-1])
        variables[variable] = 'array ' +p[1].leaf
        if(len(p)==6):
            p[0] = Node('array_declaration', [p[2], Node('NUMBER',leaf = p[4])])
        else:
            p[0] = Node('array_declaration', [p[2], Node('NUMBER',leaf = p[4]),p[6]])
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
            
    def p_if_statement(self, p):
        """
        if_statement : IF OPEN_PAREN condition CLOSE_PAREN scope 
                     | IF OPEN_PAREN condition CLOSE_PAREN scope ELSE scope
        """
        if len(p) == 6:
            p[0] = Node('if', [Node('IF', leaf=p[1]), Node('PAREN', leaf=p[2]), p[3], Node('PAREN', leaf=p[4]), p[5]])
        else:
            p[0] = Node('if', [Node('IF', leaf=p[1]), Node('PAREN', leaf=p[2]), p[3], Node('PAREN', leaf=p[4]), p[5], Node('ELSE',[p[7]])])
            
 
    def p_param(self,p):
        """
        param : OPEN_PAREN declarations CLOSE_PAREN
              | OPEN_PAREN CLOSE_PAREN
        """
        if(len(p)>3):
            p[0] = Node('param', [p[2]])
        else:
            p[0] = Node('param', leaf=p[1]+p[2])
        pass
    
    def p_passing_param(self,p):
        """
        passing_param : term COMMA passing_param
                      | term
                      | factor COMMA passing_param
                      | factor
        """
        if(len(p)>3):
            p[0] = Node('PASSIN_PARAM', [p[1],p[3]])
        else:
            p[0] = Node('PASSIN_PARAM', [p[1]])
    
    def p_print_statement(self,p):
        """
        print_statement : PRINT OPEN_PAREN STRING_LITERAL CLOSE_PAREN SEMI_COLON
                        | PRINT OPEN_PAREN STRING_LITERAL COMMA passing_param CLOSE_PAREN SEMI_COLON
        """ 
        if(len(p)<7):
            p[0] = Node('PRINT',[Node("STRING",leaf=p[3])])
        else:
            p[0] = Node('PRINT',[Node("STRING",leaf=p[3]),p[5]])
            
        
    def p_call_function(self,p):
        """
        call_function : IDENTIFIER OPEN_PAREN passing_param CLOSE_PAREN SEMI_COLON
                      | IDENTIFIER OPEN_PAREN CLOSE_PAREN SEMI_COLON
                      | print_statement
                      
        """
        if(len(p)>5):
            p[0] = Node('call_function',[Node('IDENTIFIER',leaf=p[1]),p[3]])
        elif (len(p)>2):
            p[0] = Node('call_function',[Node('IDENTIFIER',leaf=p[1])])
        else:
             p[0] = p[1]
        pass
    
    
        #LAÇOS DE REPRETICÃO---------------------------------------------
    def p_for_statement(self, p):
        """
        for_statement : FOR OPEN_PAREN for_initilizer SEMI_COLON condition SEMI_COLON expression CLOSE_PAREN scope
        """
        p[0] =  Node('for', [p[3],p[5],p[7],p[9]])
         
        
    def p_for_initializer(self,p):
        """
        for_initilizer : assignment
        
        """
        if(len(p)==2):
            p[0] = Node('for_initilizer', [p[1]])
        else:
            p[0] = Node('for_initilizer', [p[1],p[2]])
            
        
    def p_do_while_statement(self,p):
        """
        do_while_statement : DO scope WHILE OPEN_PAREN condition CLOSE_PAREN SEMI_COLON
      
        """
        p[0] = Node('DO',[p[2],Node('WHILE',[p[5]])])
        
    def p_while_statement(self,p):
        """
        while_statement : WHILE OPEN_PAREN condition CLOSE_PAREN scope
        
        """
        p[0] = Node('WHILE',[p[3],p[5]])
    

    
    
   
            
   
      
            
    def p_error(self, p):
        print("Syntax error in input at line: ", p.lineno)
        print(p)
        exit(1)

        

        