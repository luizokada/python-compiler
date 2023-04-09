from components.codeGenerator import CodeGenerator
from Tree.Tree import Node

from llvmlite import ir
import uuid
class TreeWalker:
    def __init__(self, codeGen:CodeGenerator,initalNode: Node):
        self.codeGen = codeGen
        self.initialNode = initalNode
        self.variables = {}
        self.teste = 0
        
        
    def walk(self,currentNode:Node,lastScope:ir.IRBuilder=None):
        if(currentNode ==None):
            return
        else:
            if(currentNode.type == 'main'):
                args = [] # NAO TEM ARGUMENTO NA LINGUAGEM
                function_type = self.codeGen.ir.FunctionType(self.codeGen.ir.VoidType(), args)
                main_function = self.codeGen.ir.Function(self.codeGen.module, function_type, name="main")
                main_scope = main_function.append_basic_block('entry')           
                mains_builder = self.codeGen.ir.IRBuilder(main_scope) 
                
                self.walk(currentNode.children[2].children[0],mains_builder)
            elif(currentNode.type == 'statements'):
                for child in currentNode.children:
                    self.walk(child,lastScope)
                
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
                    return self.build_operation(currentNode, lastScope)
            elif(currentNode.type == 'NUMBER'):
                if(currentNode.children[0].type):
                    return self.codeGen.ir.Constant(self.codeGen.getVariableType('int'),currentNode.leaf)
                else:
                    
                    return self.codeGen.ir.Constant(self.codeGen.getVariableType('float'),float(currentNode.leaf))
            elif(currentNode.type == 'term'):
                variableName = currentNode.leaf
                variableScope = currentNode.children[0].leaf
                variable=self.variables[(variableName,variableScope)][0]
                builder = lastScope
                return builder.load(variable)

            elif(currentNode.type == 'sequence'):
                return
            elif(currentNode.type == 'return'):
                builder = lastScope
                return builder.ret_void()
            elif(currentNode.type == 'assignment'):
                variableName = currentNode.children[0].leaf
                variableScope = currentNode.children[0].children[0].leaf
                variable=self.variables[(variableName,variableScope)][0]
                type = self.variables[(variableName,variableScope)][0]
                expression = self.walk(currentNode.children[1],lastScope)
                builder = lastScope
                return builder.store(expression, variable)
                
            elif(currentNode.type == 'iteration_op'):
                return self.build_iteration(currentNode,lastScope)
            
            elif(currentNode.type == 'declaration'):
                type = currentNode.children[0].leaf
                variableName = currentNode.children[1].leaf
                variableScope = currentNode.children[1].children[0].leaf
                builder = lastScope
                variable = builder.alloca(self.codeGen.getVariableType(type),name=variableName)
             
                self.variables[(variableName,variableScope)] = (variable,type) 
                return variable
            elif(currentNode.type == 'array_index'):
                return
            elif(currentNode.type == 'assignment_array'):
                return
            elif(currentNode.type == 'array_declaration'):
                return
            elif(currentNode.type == 'if'):
                return self.build_if(currentNode,lastScope)

            elif(currentNode.type == 'print'):   
                return self.build_print(currentNode,lastScope)
    def build_print(self,node:Node,lastScope:ir.IRBuilder):
            builder = lastScope

            value = node.children[0].leaf + '\n\0'
            str_pointer = self.codeGen.ir.Constant(self.codeGen.ir.ArrayType(self.codeGen.ir.IntType(8), len(value)),
                                bytearray(value.encode("utf8")))
            global_fmt = self.codeGen.ir.GlobalVariable(self.codeGen.module, str_pointer.type, name=uuid.uuid4().hex)
            global_fmt.linkage = 'internal'
            global_fmt.global_constant = True
            global_fmt.initializer = str_pointer

            

            function_pointer = self.codeGen.function_pointer

            printf = self.codeGen.printf

            
            fmt_arg = builder.bitcast(global_fmt, function_pointer)
            args = [fmt_arg]
            if(len(node.children)>1):
                for child in node.children[1].children:
                    variableName = child.leaf
                    variableScope = child.children[0].leaf
                    # this val can come from anywhere
            
                    int_val =  self.variables[(variableName,variableScope)][0]
                    
                    #print(int_val)
                    variableAddr =  builder.load(int_val)
                    args.append(variableAddr)
            print(variableAddr)
            builder.call(printf, args = args)
        
    
    def build_if(self,node:Node,lastScope:ir.IRBuilder):
        condition = node.children[0]
        self.teste +=1
        condition_function = self.build_condition(condition,lastScope)
        scope_if = node.children[1]
        if(len(node.children)>2):
            else_block = node.children[2].children[0]
            scope_else = else_block.children[0]      
        builder = lastScope
        if(len(node.children)>2):
            
            with builder.if_else(condition_function) as (then, otherwise):
                with then:
                    # Insere a primeira instrução do bloco then
                    
                    self.walk(scope_if.children[0],builder)  
                    
                with otherwise:

                    self.walk(scope_else,builder)
        else:
            with builder.if_then(condition_function):

                    # Insere a primeira instrução do bloco then
                self.walk(scope_if.children[0],builder)  
                    
        return

            
    def build_operation(self,node:Node,lastScope:str):
        
        if(node.leaf and node.leaf =='+'):
            return self.build_add(node,lastScope)
        elif(node.leaf and node.leaf =='-'):
            return self.build_sub(node,lastScope)
        elif(node.leaf and node.leaf =='/'):
            return self.build_division(node,lastScope)
        elif(node.leaf and node.leaf == '*'):
            return self.builg_times(node,lastScope)
        else:
            return
        
    def build_condition(self,node:Node,lastScope:str):
        if(node.leaf and node.leaf !='!'):
            left  = self.walk(node.children[0],lastScope)
            right = self.walk(node.children[1],lastScope)
            builder = lastScope
            if(node.leaf and node.leaf =='>'):
                return builder.icmp_signed('>',left,right)
            elif(node.leaf and node.leaf =='<'):
                return builder.icmp_signed('<',left,right)
            elif(node.leaf and node.leaf =='=='):
                return builder.icmp_signed('==',left,right)
            elif(node.leaf and node.leaf == '>='):
                return builder.icmp_signed('>=',left,right)
            elif(node.leaf and node.leaf == '<='):
                return builder.icmp_signed('<=',left,right)
            elif(node.leaf and node.leaf == '!='):
                return builder.icmp_signed('!=',left,right)
            elif(node.leaf and node.leaf == '&&'):
                return builder.and_(left,right)
            elif(node.leaf and node.leaf == '||'):
                return builder.or_(left,right)
        else:
            condition = self.build_condition(node.children[0],lastScope)
            builder = lastScope
            return builder.not_(condition)
        
        
    def build_add(self,node:Node,lastScope:str):
        left = self.walk(node.children[0],lastScope)     
        right = self.walk(node.children[1],lastScope)
        builder = lastScope
        return builder.add(left,right)
    
    def builg_times(self,node:Node,lastScope:str):
        left = self.walk(node.children[0],lastScope)
        right = self.walk(node.children[1],lastScope)
        builder = lastScope
        return builder.mul(left,right)
    
    def build_division(self,node:Node,lastScope:str):
        left = self.walk(node.children[0],lastScope)
        right = self.walk(node.children[1],lastScope)
        builder = lastScope
        return builder.div(left,right)
    
    def build_sub(self,node:Node,lastScope:str):
        left = self.walk(node.children[0],lastScope)
        right = self.walk(node.children[1],lastScope)
        builder = lastScope
        return builder.sub(left,right)
      
    def build_iteration(self,node:Node,lastScope:str):
        variableName = node.children[0].children[0].leaf
        variableScope = node.children[0].children[0].children[0].leaf
        builder = lastScope
        variable=self.variables[(variableName,variableScope)][0]
        op = node.leaf
        if(op == '++'):
            result =  builder.add(builder.load(variable) ,self.codeGen.ir.Constant(self.codeGen.getVariableType('int'),1))
        else:
            result =  builder.sub(builder.load(variable) ,self.codeGen.ir.Constant(self.codeGen.getVariableType('int'),1))
        return builder.store(result,variable)
        