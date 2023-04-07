from components.codeGenerator import CodeGenerator
from Tree.Tree import Node
import uuid
class TreeWalker:
    def __init__(self, codeGen:CodeGenerator,initalNode: Node):
        self.codeGen = codeGen
        self.initialNode = initalNode
        self.variables = {}
        
        
    def walk(self,currentNode:Node,lastScope='',id_scope = ''):
        if(currentNode ==None):
            return
        else:
            if(currentNode.type == 'main'):
                args = [] # NAO TEM ARGUMENTO NA LINGUAGEM
                function_type = self.codeGen.ir.FunctionType(self.codeGen.ir.VoidType(), args)
                main_function = self.codeGen.ir.Function(self.codeGen.module, function_type, name="main")
                main_scope = main_function.append_basic_block('entry')           
                self.codeGen.create_builder(main_scope,main_function)
                self.codeGen.append_scope('main_scope',main_scope)  
                self.walk(currentNode.children[2],'main_scope') #vai para o scopo
            elif(currentNode.type == 'scope'):
                if(lastScope == 'main_scope'):
                    self.walk(currentNode.children[0],lastScope,uuid.uuid4().hex)
                else:
                    new_scope = self.codeGen.main_function.append_basic_block(lastScope)
                    self.codeGen.append_scope(new_scope,lastScope)
                return 
            elif(currentNode.type == 'statements'):
                for child in currentNode.children:
                    self.walk(child,lastScope)
                return
            elif(currentNode.type == 'statement'):
                for child in currentNode.children:
                    self.walk(child,lastScope)
                return
            elif(currentNode.type == 'CHARACTER'):
                return
            elif(currentNode.type == 'expression'):
                if(len(currentNode.children) == 1):
                    return self.walk(currentNode.children[0],lastScope)
                else:
                    return self.build_operation()
            elif(currentNode.type == 'NUMBER'):
                if(currentNode.children[0].type):
                    return self.codeGen.ir.Constant(self.codeGen.getVariableType('int'),currentNode.leaf)
                else:
                    
                    return self.codeGen.ir.Constant(self.codeGen.getVariableType('float'),float(currentNode.leaf))
            elif(currentNode.type == 'term'):
                variableName = currentNode.leaf
                variableScope = currentNode.children[0].leaf
                variable=self.variables[(variableName,variableScope)][0]
                scope = self.codeGen.scopes[lastScope]
                builder = self.codeGen.ir.IRBuilder(scope)
                return builder.load(variable)

            elif(currentNode.type == 'sequence'):
                return
            elif(currentNode.type == 'return'):
                return
            elif(currentNode.type == 'assignment'):
                variableName = currentNode.children[0].leaf
                variableScope = currentNode.children[0].children[0].leaf
                variable=self.variables[(variableName,variableScope)][0]
                type = self.variables[(variableName,variableScope)][0]
                expression = self.walk(currentNode.children[1],lastScope)
                scope = self.codeGen.scopes[lastScope]
                builder = self.codeGen.ir.IRBuilder(scope)
                builder.store(expression, variable)
                return
            elif(currentNode.type == 'binop'):
               return
            elif(currentNode.type == 'iteration_op'):
               return
            elif(currentNode.type == 'condition'):
               return 
            elif(currentNode.type == 'declaration'):
                type = currentNode.children[0].leaf
                variableName = currentNode.children[1].leaf
                variableScope = currentNode.children[1].children[0].leaf
                scope = self.codeGen.scopes[lastScope]
                builder = self.codeGen.ir.IRBuilder(scope)
                variable = builder.alloca(self.codeGen.getVariableType(type),name=variableName)  
                self.variables[(variableName,variableScope)] = (variable,type) 
                return
            elif(currentNode.type == 'array_index'):
                return
            elif(currentNode.type == 'assignment_array'):
                return
            elif(currentNode.type == 'array_declaration'):
                return
            elif(currentNode.type == 'if'):
                return
            elif(currentNode.type == 'IF'):
                return
            elif(currentNode.type == 'IF'):
                return
            elif(currentNode.type == 'ELSE'):
                return
            elif(currentNode.type == 'print'):
                return
            elif(currentNode.type == 'IF'):
                return
    
    def build_operation(self,node:Node):
        if(node.leaf and node.leaf =='+'):
            return
        elif(node.leaf and node.leaf =='-'):
            return
        elif(node.leaf and node.leaf =='/'):
            return
        elif(node.leaf and node.leaf == '*'):
            return
        elif(node.leaf and node.leaf == '='):
            return
        else:
            return
        