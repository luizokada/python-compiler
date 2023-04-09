from components.codeGenerator import CodeGenerator
from Tree.Tree import Node

from llvmlite import ir
import uuid
class TreeWalker:
    def __init__(self, codeGen:CodeGenerator,initalNode: Node):
        self.codeGen = codeGen
        self.initialNode = initalNode
        self.variables = {}
        self.current_variable_type = None
        self.teste = 0
        
        
    def walk(self,currentNode:Node,lastScope:ir.IRBuilder=None):
        if(currentNode ==None):
            return
        else:
            if(currentNode.type == 'main'):
                args = [] # NAO TEM ARGUMENTO NA LINGUAGEM
                function_type = self.codeGen.ir.FunctionType(self.codeGen.ir.VoidType(), args)
                main_function = self.codeGen.ir.Function(self.codeGen.module, function_type, name="main")
                self.codeGen.main_function = main_function
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
                if(not currentNode.children[0].leaf or self.current_variable_type == 'int'):
                    return self.codeGen.ir.Constant(self.codeGen.getVariableType('int'),int(currentNode.leaf))
                else:    
                    return self.codeGen.ir.Constant(self.codeGen.getVariableType('float'),currentNode.leaf)
            elif(currentNode.type == 'term'):
                variableName = currentNode.leaf
                variableScope = currentNode.children[0].leaf
                variable=self.variables[(variableName,variableScope)][0]
                builder = lastScope
                return builder.load(variable)
            elif(currentNode.type == 'for'):
                return self.build_for(currentNode,lastScope)
            elif(currentNode.type == 'sequence'):
                return
            elif(currentNode.type == 'return'):
                builder = lastScope
                return builder.ret_void()
            elif(currentNode.type == 'assignment'):
                variableName = currentNode.children[0].leaf
                variableScope = currentNode.children[0].children[0].leaf
                variable=self.variables[(variableName,variableScope)][0]
                self.current_variable_type =self.variables[(variableName,variableScope)][1]
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
            elif (currentNode.type == 'scan'):
                return self.build_scan(currentNode,lastScope)
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
            
        return
    
    
    def build_scan(self,node:Node,lastScope:ir.IRBuilder):
        builder = lastScope
        value  = node.children[0].leaf.replace("'","")
        value = value + "\0"
        variableName = node.children[1].leaf
        format_str = ir.GlobalVariable(self.codeGen.module, ir.ArrayType(ir.IntType(8), len(value)), name=uuid.uuid4().hex)
        format_str.global_constant = True
        format_str.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len(value)), bytearray(value.encode("utf8")))
        
        function_pointer = builder.bitcast(format_str, self.codeGen.function_pointer_scan)
      
        args = [function_pointer]
        if(len(node.children)>1):
            child = node.children[1].children[0]      
            variableName = child.leaf
            variableScope = child.children[0].leaf
            # this val can come from anywhere
    
            variable =  self.variables[(variableName,variableScope)][0]


           
            variable_ptr_ptr =variable
                    
            args.append(variable_ptr_ptr)
        
        scanf = self.codeGen.scanf
        result = builder.call(scanf,args=args)
        return result
        
        
    
    def build_print(self,node:Node,lastScope:ir.IRBuilder):
            builder = lastScope
            value = node.children[0].leaf.replace("'","") + '\n\0'
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
            
                    variable =  self.variables[(variableName,variableScope)][0]
               
                    variableAddr =  builder.load(variable)
                    args.append(variableAddr)
            
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
                    self.walk(scope_if.children[0],builder)  
                    
                with otherwise:

                    self.walk(scope_else,builder)
        else:
            with builder.if_then(condition_function):
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
    
    def build_division(self,node:Node,lastScope:ir.IRBuilder):
        left = self.walk(node.children[0],lastScope)
        right = self.walk(node.children[1],lastScope)
        builder = lastScope
        if(self.current_variable_type == 'int'):
            return builder.sdiv(left,right)
        return builder.fdiv(left,right)
    
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
    
    
        
    def build_for(self,node:Node,lastScope:ir.IRBuilder):
        builder = lastScope
        
        for_init = node.children[0]
        condition = node.children[1]
        incrementation = node.children[2]
        scope_for = node.children[3].children[0]
        self.walk(for_init.children[0],builder)
        bb = builder.basic_block
        for_init = builder.append_basic_block(bb.name+'.for_init')
        builder.branch(for_init)
        for_loop = builder.append_basic_block(bb.name+ '.for_loop')
        for_end = builder.append_basic_block(bb.name+ '.for_end')
        builder.position_at_start(for_init)
        condition_function = self.build_condition(condition,builder)
        builder.cbranch(condition_function, for_loop, for_end)
        builder.position_at_start(for_loop)
        loopBuilder = self.codeGen.ir.IRBuilder(for_loop)
        self.walk(scope_for,loopBuilder)
        self.build_iteration(incrementation,loopBuilder)

        loopBuilder.branch(for_init)
        builder.position_at_end(for_end)



        
  
          