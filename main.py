from components.lexer import Lexer
from components.parser import Parser
from components.parser import variables
from components.codeGenerator import CodeGenerator
from components.treeWalker import TreeWalker
import sys
import subprocess

LANGUAGE_EXTENCION = "c"
def main(fille_name):
    try:
        #verifica de fille_name termina com .c
        extencion = fille_name.split(".")[-1]
        if(extencion != LANGUAGE_EXTENCION):
            print("Fille extencion is not .c")
            exit(1)
        fille = open(f"./tests/{fille_name}")
    except:
        print("Fille not found")
        exit(1)
        
    text = fille.read()
    lexer = Lexer()
    lexer.build()
    lexer.lexer.input(text)

    parser = Parser(lexer.tokens)
    test = parser.parse(text, lexer=lexer) 

    test.print_tree()

    codeGenrator = CodeGenerator() 
    walker = TreeWalker(codeGenrator,test)
    walker.walk(test)
    print(walker.codeGen.module)
    

    codeGenrator.compile(f'result/{fille_name.split(".")[0]}')
    codeGenrator.save_ir(f'result/{fille_name.split(".")[0]}.ll')
    comand = f' llc -filetype=obj -relocation-model=pic result/{fille_name.split(".")[0]}.ll -o result/{fille_name.split(".")[0]}.o'
    gcc_comand = f'gcc result/{fille_name.split(".")[0]}.o -o result/{fille_name.split(".")[0]}'

    subprocess.run(comand, shell=True, universal_newlines=True)
    subprocess.run(gcc_comand, shell=True, universal_newlines=True)



    

if __name__ == "__main__":
    fille_name = sys.argv[1]
    main(fille_name)