; ModuleID = '<string>'
source_filename = "<string>"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@"9abf5386a1ee43e883e09aaec7b8d728" = internal constant [21 x i8] c"Digite o valor de a\0A\00"
@da76e41c5b8d470b93f06542e1ff45dd = constant [3 x i8] c"%d\00"
@e131ac60114f48768c8e87f18f24ec67 = internal constant [21 x i8] c"Digite o valor de b\0A\00"
@"696d02bc3cf4410ba442b7ab66cafb20" = constant [3 x i8] c"%d\00"
@"4eb19da353e74a8cbcf3026b3967b2fc" = internal constant [12 x i8] c"a + b = %d\0A\00"
@e71f7a4c112a4a72a1a5da3ca6c771be = internal constant [19 x i8] c"Soma maior que 10\0A\00"
@"412bce5818c84942af299ca0a9bd9bac" = internal constant [19 x i8] c"Soma menor que 10\0A\00"
@a07c5e2d18ab400896fed3de0e50e95a = internal constant [8 x i8] c"i = %d\0A\00"

declare i32 @printf(i8*, ...)

declare i32 @scanf(i8*, ...)

define void @main() {
entry:
  %a = alloca i32, align 4
  %b = alloca i32, align 4
  %soma = alloca i32, align 4
  %.2 = bitcast [21 x i8]* @"9abf5386a1ee43e883e09aaec7b8d728" to i8*
  %.3 = call i32 (i8*, ...) @printf(i8* %.2)
  %.4 = bitcast [3 x i8]* @da76e41c5b8d470b93f06542e1ff45dd to i8*
  %.5 = call i32 (i8*, ...) @scanf(i8* %.4, i32* %a)
  %.6 = bitcast [21 x i8]* @e131ac60114f48768c8e87f18f24ec67 to i8*
  %.7 = call i32 (i8*, ...) @printf(i8* %.6)
  %.8 = bitcast [3 x i8]* @"696d02bc3cf4410ba442b7ab66cafb20" to i8*
  %.9 = call i32 (i8*, ...) @scanf(i8* %.8, i32* %b)
  %.10 = load i32, i32* %a, align 4
  %.11 = load i32, i32* %b, align 4
  %.12 = add i32 %.10, %.11
  store i32 %.12, i32* %soma, align 4
  %.14 = bitcast [12 x i8]* @"4eb19da353e74a8cbcf3026b3967b2fc" to i8*
  %.15 = load i32, i32* %soma, align 4
  %.16 = call i32 (i8*, ...) @printf(i8* %.14, i32 %.15)
  %.17 = load i32, i32* %soma, align 4
  %.18 = icmp sgt i32 %.17, 10
  br i1 %.18, label %entry.if, label %entry.else

entry.if:                                         ; preds = %entry
  %.20 = bitcast [19 x i8]* @e71f7a4c112a4a72a1a5da3ca6c771be to i8*
  %.21 = call i32 (i8*, ...) @printf(i8* %.20)
  br label %entry.endif

entry.else:                                       ; preds = %entry
  %.23 = bitcast [19 x i8]* @"412bce5818c84942af299ca0a9bd9bac" to i8*
  %.24 = call i32 (i8*, ...) @printf(i8* %.23)
  br label %entry.endif

entry.endif:                                      ; preds = %entry.else, %entry.if
  %i = alloca i32, align 4
  store i32 0, i32* %i, align 4
  br label %entry.endif.for_init

entry.endif.for_init:                             ; preds = %entry.endif.for_loop, %entry.endif
  %.28 = load i32, i32* %i, align 4
  %.29 = icmp slt i32 %.28, 10
  br i1 %.29, label %entry.endif.for_loop, label %entry.endif.for_end

entry.endif.for_loop:                             ; preds = %entry.endif.for_init
  %.31 = bitcast [8 x i8]* @a07c5e2d18ab400896fed3de0e50e95a to i8*
  %.32 = load i32, i32* %i, align 4
  %.33 = call i32 (i8*, ...) @printf(i8* %.31, i32 %.32)
  %.34 = load i32, i32* %i, align 4
  %.35 = add i32 %.34, 1
  store i32 %.35, i32* %i, align 4
  br label %entry.endif.for_init

entry.endif.for_end:                              ; preds = %entry.endif.for_init
  ret void
}

; Function Attrs: nounwind
declare void @llvm.stackprotector(i8*, i8**) #0

attributes #0 = { nounwind }
