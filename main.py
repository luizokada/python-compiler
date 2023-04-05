from components.lexer import Lexer
from components.parser import Parser
from components.parser import variables


fille = open("./tests/simpleSum.c")
text = fille.read()
lexer = Lexer()
lexer.build()
tokens = lexer.lexer.input(text)

"""for token in lexer.lexer:
    print (token)"""

#input_str = [f"{tok[0]}:{tok[1]}" for tok in tokens]
parser = Parser(lexer.tokens)
test = parser.parse(text, lexer=lexer) 
#test.print_tree()
test.print_tree()

print(variables)



"""print(test.find_expression_with_binop(test))
print(f'variables: {variables}')

testeEXP = test.children[2].children[0].children[0].children[0].children[0]

#print(testeEXP.find_expression_with_binop(testeEXP))

nodeAtual = testeEXP.find_expression_with_binop(testeEXP)
#print(nodeAtual.print_tree())
lastNode = nodeAtual
while nodeAtual:
    nodeAtual = testeEXP.find_expression_with_binop(nodeAtual)
    if(nodeAtual):
        lastNode = nodeAtual
        
#print(lastNode.print_tree())
test.resolve_binop_as_child(test)
print"""