from components.lexer import Lexer
from components.parser import Parser
from components.parser import variabes


fille = open("./tests/simpleSum.c")
text = fille.read()
lexer = Lexer()
lexer.build()
tokens = lexer.lexer.input(text)

#input_str = [f"{tok[0]}:{tok[1]}" for tok in tokens]
parser = Parser(lexer.tokens)
test = parser.parser.parse(text, lexer=lexer.lexer)

def print_tree(node, level=0):
    if node is None:
        return
    indent = ' ' * level
    if node.leaf is not None:
        print(f'{indent}{node.type}: {node.leaf}')
    else:
        print(f'{indent}{node.type}')
    for child in node.children:
        print_tree(child, level + 1)
print_tree(test)
print(variabes)