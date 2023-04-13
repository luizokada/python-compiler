; ModuleID = '<string>'
source_filename = "<string>"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@e15143ddd22b481299fac3d4070535c5 = internal constant [21 x i8] c"Digite o valor de a\0A\00"
@a0b389927ad34d4db8debe673d2fd5fb = constant [3 x i8] c"%d\00"
@"83c8ee81ab074e569e8768c321d5dcde" = internal constant [21 x i8] c"Digite o valor de b\0A\00"
@"49b6e689f4b840ae8309e39c4bedd5b2" = constant [3 x i8] c"%d\00"
@d7f5c11d10144cdfa74e55eb8e30af90 = internal constant [14 x i8] c"%d + %d = %d\0A\00"

declare i32 @printf(i8*, ...)

declare i32 @scanf(i8*, ...)

define void @main() {
entry:
  %a = alloca i32, align 4
  %b = alloca i32, align 4
  %soma = alloca i32, align 4
  %c = alloca i32, align 4
  %.2 = bitcast [21 x i8]* @e15143ddd22b481299fac3d4070535c5 to i8*
  %.3 = call i32 (i8*, ...) @printf(i8* %.2)
  %.4 = bitcast [3 x i8]* @a0b389927ad34d4db8debe673d2fd5fb to i8*
  %.5 = call i32 (i8*, ...) @scanf(i8* %.4, i32* %a)
  %.6 = bitcast [21 x i8]* @"83c8ee81ab074e569e8768c321d5dcde" to i8*
  %.7 = call i32 (i8*, ...) @printf(i8* %.6)
  %.8 = bitcast [3 x i8]* @"49b6e689f4b840ae8309e39c4bedd5b2" to i8*
  %.9 = call i32 (i8*, ...) @scanf(i8* %.8, i32* %b)
  %.10 = load i32, i32* %a, align 4
  %.11 = load i32, i32* %b, align 4
  %.12 = add i32 %.10, %.11
  store i32 %.12, i32* %soma, align 4
  %.14 = bitcast [14 x i8]* @d7f5c11d10144cdfa74e55eb8e30af90 to i8*
  %.15 = load i32, i32* %a, align 4
  %.16 = load i32, i32* %b, align 4
  %.17 = load i32, i32* %soma, align 4
  %.18 = call i32 (i8*, ...) @printf(i8* %.14, i32 %.15, i32 %.16, i32 %.17)
  ret void
}

; Function Attrs: nounwind
declare void @llvm.stackprotector(i8*, i8**) #0

attributes #0 = { nounwind }
