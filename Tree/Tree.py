class Node:
    def __init__(self,type,children=None,leaf=None):
         self.type = type
         if children:
              self.children = children
         else:
              self.children = [ ]
         self.leaf = leaf
    
    def __str__(self):
         return self.type
    
    def print_tree(self,level=0):
         indent = ' ' * level
         if self.leaf is not None:
              print(f'{indent}{self.type}: {self.leaf}')
         else:
              print(f'{indent}{self.type}')
         for child in self.children:
              child.print_tree(level + 1)
    
    def find_expression_with_binop(self,node):
        if node.type == "expression":
            for child in node.children:
                if child.type == "binop":
                    return child
        for child in node.children:
            result = self.find_expression_with_binop(child)
            if result is not None:
                return result
        return None
    
    def resolve_binop_as_child(self):
        for child in self.children:
            return
            
            
    def reorganize_tree(self,node,father):
        if node.type == "expression":
            binops = [child for child in node.children if child.type == "binop"]
            for binop in binops:
                # remove binop from expression children
                node.children.remove(binop)
                # make binop the parent of expression
                binop.children.append(node)
                binop.type="expression"
                father.children.remove(node)
                father.children.append(binop)
                node = binop
                for child in node.children:
                    self.reorganize_tree(child,node)
        else:
            for child in node.children:
                self.reorganize_tree(child,node)
    
    def validate_all_leafs(self,type):
        if (self.leaf is not None) and (self.type != type) and self.type != "expression" and self.type!="binop":
            return False
        else:
            for child in self.children:
                if not child.validate_all_leafs(type):
                    return False       
        return True
        
