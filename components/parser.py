import ply.yacc as yacc
class Node:
    def __init__(self,type,children=None,leaf=None):
         self.type = type
         if children:
              self.children = children
         else:
              self.children = [ ]
         self.leaf = leaf
	 


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
        """
        p[0] =  Node('statement', [p[1]])

    def p_assignment(self, p):
        """
        assignment : IDENTIFIER ASSING expression
        """
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
        """
        p[0] = Node("expression", leaf=p[1])

    def p_term(self, p):
        """
        term : IDENTIFIER
            | NUMBER

        """
        
        p[0] = p[1]

    def p_factor_num(self, p):
        """
        factor : NUMBER
        """
        p[0] =  Node('NUMBER', leaf=p[1])
        

        