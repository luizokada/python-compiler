from Tree.Tree import Node
from Errors.SemanticError import SemanticError

class SemanticValidator:
    def __init__(self) -> None:
        pass
    
    #validate if variable is declared. DOES NOT VALIDATE SCOPE
    def validate_variable(self, node,variables):
        print(node.leaf)
        variable = node.leaf
        
        for key in variables.keys():
            if variable in key[0]:
                return
        raise SemanticError(f"Variavel {variable} nao declarada",node)
        
    def validate_number(self, node:Node, vairable):
        if( not node.validate_all_leafs("NUMBER")):
            raise SemanticError(f"Atribuiçao invalida na variavel {vairable}",node)
        return
        
    def validate_string(self, node):
        if node.type == "string":
            return True
        return False
    
        