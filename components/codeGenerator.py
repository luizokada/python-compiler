from llvmlite import ir,binding
from llvmlite import binding as llvm
class CodeGenerator:
    def __init__(self):
        self.binding = binding
        
        self._config_llvm()
        self._create_types()
        self.declare_print()
        self.declare_scanf()
    
   
    def _config_llvm(self):
        # Config LLVM
        self.module = ir.Module(name=__file__)
        self.module.triple = self.binding.get_default_triple()
        self.ir = ir
  
        
    def create_builder(self,block,main:ir.Function):
        self.main_function = main
        self.builder = self.ir.IRBuilder(block)


        
    
    def _create_types(self):
        self.int = self.ir.IntType(32)
        self.float = self.ir.FloatType()
        self.char = self.ir.IntType(8)

        
    def compile(self, filename):
        self.binding.initialize()
        self.binding.initialize_native_target()
        self.binding.initialize_native_asmprinter()
        target = self.binding.Target.from_default_triple()
        target_machine = target.create_target_machine()
        backing_mod = binding.parse_assembly("")
        engine = binding.create_mcjit_compiler(backing_mod, target_machine)
        self.engine = engine
        llvm_ir = str(self.module)
        mod = self.binding.parse_assembly(llvm_ir)
        mod.verify()
        self.engine.add_module(mod)
        self.engine.finalize_object()
        self.engine.run_static_constructors()
        self.module=mod
            
    def declare_print(self):
        self.function_pointer = self.ir.PointerType(ir.IntType(8), 0)
        self.print_pointer = self.ir.FunctionType(self.ir.IntType(32), [self.function_pointer], var_arg=True)
        self.printf = self.ir.Function(self.module, self.print_pointer, name="printf")
    
    def declare_scanf(self):
        self.function_pointer_scan = self.ir.PointerType(ir.IntType(8), 0)
        self.scanf_pointer = self.ir.FunctionType(self.ir.IntType(32), [self.function_pointer_scan], var_arg=True)
        self.scanf = self.ir.Function(self.module, self.scanf_pointer, name="scanf")
        
    def save_ir(self, filename):
        with open(filename, 'w') as output_file:
            output_file.write(str(self.module))
            
    def getVariableType(self, type:str):
        if type == 'int':
            return self.int
        elif type == 'float':
            return self.float
        elif type == 'char':
            return self.char
