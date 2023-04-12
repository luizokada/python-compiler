; ModuleID = '<string>'
source_filename = "<string>"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@"548cc8a8f27c42e1bb7cbe81c02a4564" = internal constant [21 x i8] c"Digite o valor de a\0A\00"
@"30525e19a08a4e31b280af404108d03c" = constant [3 x i8] c"%d\00"
@"8c209293ea3c4ccea5beb937496aac13" = internal constant [21 x i8] c"Digite o valor de b\0A\00"
@"33f0f0308ad143b98e74e88e1cc17a37" = constant [3 x i8] c"%d\00"
@"6400df54f1c24c2cb2a7270d1da66972" = internal constant [12 x i8] c"a + b = %d\0A\00"
@"6eaa3579ee824bc6b3468504abf5fe0f" = internal constant [19 x i8] c"Soma maior que 10\0A\00"
@c87ff480873c4d2e8aae13bb0acf21e8 = internal constant [19 x i8] c"Soma menor que 10\0A\00"
@"77b69753b5c24e3c99e499c30f360252" = internal constant [8 x i8] c"i = %d\0A\00"

declare i32 @printf(i8*, ...)

declare i32 @scanf(i8*, ...)

define void @main() {
entry:
  %a = alloca i32, align 4
  %b = alloca i32, align 4
  %soma = alloca i32, align 4
  %.2 = bitcast [21 x i8]* @"548cc8a8f27c42e1bb7cbe81c02a4564" to i8*
  %.3 = call i32 (i8*, ...) @printf(i8* %.2)
  %.4 = bitcast [3 x i8]* @"30525e19a08a4e31b280af404108d03c" to i8*
  %.5 = call i32 (i8*, ...) @scanf(i8* %.4, i32* %a)
  %.6 = bitcast [21 x i8]* @"8c209293ea3c4ccea5beb937496aac13" to i8*
  %.7 = call i32 (i8*, ...) @printf(i8* %.6)
  %.8 = bitcast [3 x i8]* @"33f0f0308ad143b98e74e88e1cc17a37" to i8*
  %.9 = call i32 (i8*, ...) @scanf(i8* %.8, i32* %b)
  %.10 = load i32, i32* %a, align 4
  %.11 = load i32, i32* %b, align 4
  %.12 = add i32 %.10, %.11
  store i32 %.12, i32* %soma, align 4
  %.14 = bitcast [12 x i8]* @"6400df54f1c24c2cb2a7270d1da66972" to i8*
  %.15 = load i32, i32* %soma, align 4
  %.16 = call i32 (i8*, ...) @printf(i8* %.14, i32 %.15)
  %.17 = load i32, i32* %soma, align 4
  %.18 = icmp sgt i32 %.17, 10
  br i1 %.18, label %entry.if, label %entry.else

entry.if:                                         ; preds = %entry
  %.20 = bitcast [19 x i8]* @"6eaa3579ee824bc6b3468504abf5fe0f" to i8*
  %.21 = call i32 (i8*, ...) @printf(i8* %.20)
  br label %entry.endif

entry.else:                                       ; preds = %entry
  %.23 = bitcast [19 x i8]* @c87ff480873c4d2e8aae13bb0acf21e8 to i8*
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
  %.31 = bitcast [8 x i8]* @"77b69753b5c24e3c99e499c30f360252" to i8*
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
