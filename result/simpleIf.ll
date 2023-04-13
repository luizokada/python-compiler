; ModuleID = '<string>'
source_filename = "<string>"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@"54650a3e0fc34e3ebf692e45bbd07390" = internal constant [21 x i8] c"Digite o valor de a\0A\00"
@"82037273927249beb18575577e6c14b0" = constant [3 x i8] c"%d\00"
@e8256a62742a44218d89ab3b3a652d63 = internal constant [21 x i8] c"Digite o valor de b\0A\00"
@"4ca39f5a84ff4c63babfdf11eb16e095" = constant [3 x i8] c"%d\00"
@"28b800348cbb4075bee529452b581710" = internal constant [14 x i8] c"%d + %d = %d\0A\00"
@e59e39b505f4444ba8fd632b348bba1b = internal constant [19 x i8] c"Valores invalidos\0A\00"

declare i32 @printf(i8*, ...)

declare i32 @scanf(i8*, ...)

define void @main() {
entry:
  %a = alloca i32, align 4
  %b = alloca i32, align 4
  %soma = alloca i32, align 4
  %.2 = bitcast [21 x i8]* @"54650a3e0fc34e3ebf692e45bbd07390" to i8*
  %.3 = call i32 (i8*, ...) @printf(i8* %.2)
  %.4 = bitcast [3 x i8]* @"82037273927249beb18575577e6c14b0" to i8*
  %.5 = call i32 (i8*, ...) @scanf(i8* %.4, i32* %a)
  %.6 = bitcast [21 x i8]* @e8256a62742a44218d89ab3b3a652d63 to i8*
  %.7 = call i32 (i8*, ...) @printf(i8* %.6)
  %.8 = bitcast [3 x i8]* @"4ca39f5a84ff4c63babfdf11eb16e095" to i8*
  %.9 = call i32 (i8*, ...) @scanf(i8* %.8, i32* %b)
  %.10 = load i32, i32* %a, align 4
  %.11 = icmp sgt i32 %.10, 0
  %.12 = load i32, i32* %b, align 4
  %.13 = icmp sgt i32 %.12, 0
  %.14 = and i1 %.11, %.13
  br i1 %.14, label %entry.if, label %entry.else

entry.if:                                         ; preds = %entry
  %.16 = load i32, i32* %a, align 4
  %.17 = load i32, i32* %b, align 4
  %.18 = add i32 %.16, %.17
  store i32 %.18, i32* %soma, align 4
  %.20 = bitcast [14 x i8]* @"28b800348cbb4075bee529452b581710" to i8*
  %.21 = load i32, i32* %a, align 4
  %.22 = load i32, i32* %b, align 4
  %.23 = load i32, i32* %soma, align 4
  %.24 = call i32 (i8*, ...) @printf(i8* %.20, i32 %.21, i32 %.22, i32 %.23)
  br label %entry.endif

entry.else:                                       ; preds = %entry
  %.26 = bitcast [19 x i8]* @e59e39b505f4444ba8fd632b348bba1b to i8*
  %.27 = call i32 (i8*, ...) @printf(i8* %.26)
  br label %entry.endif

entry.endif:                                      ; preds = %entry.else, %entry.if
  ret void
}

; Function Attrs: nounwind
declare void @llvm.stackprotector(i8*, i8**) #0

attributes #0 = { nounwind }
