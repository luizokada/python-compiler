from Tree.Tree import Node
from Errors.SemanticError import SemanticError

class SemanticValidator:
    def __init__(self) -> None:
        pass
    
    def isScopeParent(self, node:Node, uuid:str):
        if(node ==None):
            return False
        elif(node.leaf == uuid):
            return False
        else:
            for child in node.children:
                if(child.leaf == uuid):
                    return True
                elif(self.isScopeParent(child,uuid)):
                    return True
            return False
            
    def findNodeInTree(self,node:Node,uuid:str):
        if(node ==None):
            return None
        elif(node.leaf == uuid):
            return node
        else:
            for child in node.children:
                if(child.leaf == uuid):
                    return child
                else:
                    parent =  self.findNodeInTree(child,uuid)
                    if(parent):
                        return parent
            return None 
        
    
    #validate if variable is declared. DOES NOT VALIDATE SCOPE
    def validate_variable(self, node,variables,current_node_scope,scopes):
        variable = node.leaf
        try:
            return variables[(variable,current_node_scope.leaf)],current_node_scope.leaf
        except:
            type= None
            scopeVar =None
            for key in variables.keys():
                if variable in key[0]:
                    node = self.findNodeInTree(scopes,key[1])
                    if(self.isScopeParent(node,current_node_scope.leaf)):
                        type = variables[key]
                        scopeVar =  key[1]
        if(type!=None):
            return type,scopeVar
        raise SemanticError(f"Variavel {variable} nao declarada",node)
        
    def validate_number(self, node:Node, vairable,variables):
        if( not node.validate_all_leafs("NUMBER",variables)):
            raise SemanticError(f"Atribuiçao invalida na variavel {vairable}",node)
        return
    
    def validate_char(self, node:Node, vairable,variables):
        if( not node.validate_all_leafs("CHARACTER",variables)):
            raise SemanticError(f"Atribuiçao invalida na variavel {vairable}",node)
        return
        
    def validate_scan(self, node:Node,params:list,variables):
        string_scan = node.children[0].leaf
        string_scan=string_scan.replace("'","")
        if(string_scan != "%d"):
            raise SemanticError(f"Tipo de variavel invalido para leitura",node)
        if(len(params.children)!=1):
            raise SemanticError(f"Numero de parametros invalido para leitura",node)
        else:
            variable_name = params.children[0].leaf
            variable_scope = params.children[0].children[0].leaf
            if(variables[(variable_name,variable_scope)] != "int"):
                raise SemanticError(f"Tipo de variavel invalido para leitura",node)
        return
    def validate_string(self, node):
        if node.type == "string":
            return True
        return False
    
        