
import ply.lex as lex

class Lexer():
    def __init__(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        self.current_line = 1

    
    #ALL TOKENS 
    tokens = (
        'PRINT',
        'OPEN_PAREN',
        'CLOSE_PAREN',
        'OPEN_BRAKETS',
        'CLOSE_BRAKETS',
        'SEMI_COLON',
        'COMMA',
        'SUM',
        'SUB',
        'MUL',
        'DIV',
        'GREATER',
        'EQUALS',
        'GREATER_OR_EQUALS',
        'LESSER',
        'LESSER_OR_EQUALS',
        'ASSING',
        'AND',
        'OR',
        'NOT',
        'NUMBER',
        'INT',
        'FLOAT',
        'CHAR',
        'DOUBLE',
        'FOR',
        'WHILE',
        'IF',
        'ELSE',
        'DO',
        'BREAK',
        'RETURN',
        'IDENTIFIER',
        'MAIN',
    )
    # Print
    def t_PRINT(self, t):
        r'printf'
        return t

    # Parenthesis
    t_OPEN_PAREN = r'\('
    t_CLOSE_PAREN = r'\)'

    # Brackets
    t_OPEN_BRAKETS = r'\{'
    t_CLOSE_BRAKETS = r'\}'

    # Semi Colon
    t_SEMI_COLON = r'\;'

    #COMMA
    
    t_COMMA = r'\,'    
    # Operators
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_GREATER = r'\>'
    t_EQUALS = r'\=='
    t_GREATER_OR_EQUALS = r'\>='
    t_LESSER = r'\<'
    t_LESSER_OR_EQUALS = r'\<='
    t_ASSING = r'\='
    t_AND = r'\&&'
    t_OR = r'\|\|'
    t_NOT = r'\!'

    # MAIN
    def t_MAIN(self, t):
        r'main'
        t.value = t.value
        return t
    # Number
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Ignore spaces
    t_ignore=' \t\r\f\v'

    # Ignore comments
    def t_comment(self, t):
        r'\/\*([\s\S]*?)\*\/'
        pass

    # TYPES
    def t_INT(self, t):
        r'int'
        return t

    def t_FLOAT(self, t):
        r'float'
        return t

    def t_CHAR(self, t):
        r'char'
        return t

    def t_DOUBLE(self, t):
        r'double'
        return t

    # KEYWORDS
    def t_FOR(self, t):
        r'for'
        return t

    def t_WHILE(self, t):
        r'while'
        return t

    def t_IF(self, t):
        r'if'
        return t

    def t_ELSE(self, t):
        r'else'
        return t

    def t_DO(self, t):
        r'do'
        return t

    def t_BREAK(self, t):
        r'break'
        return t

    def t_RETURN(self, t):
        r'return'
        return t

    # IDENTIFIERS
    def t_IDENTIFIER(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        return t

    def t_error(self, t):
        print(f"Illegal character {t.value[0]}")
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        
        
    def t_newline(self,t):
        r'\n\s*'
        self.current_line += t.value.count('\n')
        self.lexer.lineno = self.current_line
        


    def tokenize(self, data):
        return self.lexer.input(data)
        return list(iter(self.lexer.token, None))