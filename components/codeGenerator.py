from llvmlite import ir,binding

class CodeGenerator:
    def __init__(self):
        self.binding = binding
        self.binding.initialize()
        self.binding.initialize_native_target()
        self.binding.initialize_native_asmprinter()
        self._config_llvm()
        self._create_types()
        self._declare_print_function()
        self.scopes = {}
    
    
    def append_scope(self,new_scope,scope:ir.Function.entry_basic_block):
        self.scopes[new_scope] = scope

    def _config_llvm(self):
        # Config LLVM
        self.module = ir.Module(name='teste')
        self.module.triple = self.binding.get_default_triple()
        self.ir = ir
        
        
    def create_builder(self,block,main:ir.Function):
        self.main_function = main
        self.builder = self.ir.IRBuilder(block)


    def _declare_print_function(self):
        # Declare Printf function
        voidptr_ty = self.ir.IntType(8).as_pointer()
        printf_ty = self.ir.FunctionType(self.ir.IntType(32), [voidptr_ty], var_arg=True)
        printf = self.ir.Function(self.module, printf_ty, name="printf")
        self.printf = printf
    
    def _create_types(self):
        self.int = self.ir.IntType(32)
        self.float = self.ir.FloatType()
        self.char = self.ir.IntType(8)

        
    def getVariableType(self, type:str):
        if type == 'int':
            return self.int
        elif type == 'float':
            return self.float
        elif type == 'char':
            return self.char
