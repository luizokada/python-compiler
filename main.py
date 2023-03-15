from components.lexer import Lexer

fille = open("./tests/simpleSum.c")
text = fille.read()
lexer = Lexer().get_lexer()
tokens = lexer.input(text)

for token in lexer:
    print(token)