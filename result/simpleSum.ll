; ModuleID = '<string>'
source_filename = "<string>"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@"633fd268103d4fb5979a485a8ccc7d8e" = internal constant [21 x i8] c"Digite o valor de a\0A\00"
@f5c81f76016a49aaae4c70109214951f = constant [3 x i8] c"%d\00"
@"654818043c5a4b3bac9b326c7d570156" = internal constant [21 x i8] c"Digite o valor de b\0A\00"
@"8c7eaa295d7c4db3be87a2898614570a" = constant [3 x i8] c"%d\00"
@c4032d4b135249cb8e4c243cb24d4d3a = internal constant [12 x i8] c"a + b = %d\0A\00"
@"648f8ad066484be18b031bd74ed69a89" = internal constant [34 x i8] c"Soma maior que 10 AAAAAAAAAAAAAA\0A\00"
@"40f4a1f828b84f31b6323412c80acf6d" = internal constant [19 x i8] c"Soma menor que 10\0A\00"
@"887be7dd7b1e4419819416248a97ef2a" = internal constant [19 x i8] c"Soma maior que 10\0A\00"
@"0c5062c4ca284f898ddbc4827923ff11" = internal constant [8 x i8] c"i = %d\0A\00"

declare i32 @printf(i8*, ...)

declare i32 @scanf(i8*, ...)

define void @main() {
entry:
  %a = alloca i32, align 4
  %b = alloca i32, align 4
  %soma = alloca i32, align 4
  %.2 = bitcast [21 x i8]* @"633fd268103d4fb5979a485a8ccc7d8e" to i8*
  %.3 = call i32 (i8*, ...) @printf(i8* %.2)
  %.4 = bitcast [3 x i8]* @f5c81f76016a49aaae4c70109214951f to i8*
  %.5 = call i32 (i8*, ...) @scanf(i8* %.4, i32* %a)
  %.6 = bitcast [21 x i8]* @"654818043c5a4b3bac9b326c7d570156" to i8*
  %.7 = call i32 (i8*, ...) @printf(i8* %.6)
  %.8 = bitcast [3 x i8]* @"8c7eaa295d7c4db3be87a2898614570a" to i8*
  %.9 = call i32 (i8*, ...) @scanf(i8* %.8, i32* %b)
  %.10 = load i32, i32* %a, align 4
  %.11 = load i32, i32* %b, align 4
  %.12 = add i32 %.10, %.11
  store i32 %.12, i32* %soma, align 4
  %.14 = bitcast [12 x i8]* @c4032d4b135249cb8e4c243cb24d4d3a to i8*
  %.15 = load i32, i32* %soma, align 4
  %.16 = call i32 (i8*, ...) @printf(i8* %.14, i32 %.15)
  %.17 = load i32, i32* %soma, align 4
  %.18 = icmp sgt i32 %.17, 10
  %.19 = load i32, i32* %a, align 4
  %.20 = icmp ne i32 %.19, 10
  %.21 = and i1 %.18, %.20
  %.22 = xor i1 %.21, true
  br i1 %.22, label %entry.if, label %entry.else

entry.if:                                         ; preds = %entry
  %.24 = bitcast [34 x i8]* @"648f8ad066484be18b031bd74ed69a89" to i8*
  %.25 = call i32 (i8*, ...) @printf(i8* %.24)
  br label %entry.endif

entry.else:                                       ; preds = %entry
  %.27 = bitcast [19 x i8]* @"40f4a1f828b84f31b6323412c80acf6d" to i8*
  %.28 = call i32 (i8*, ...) @printf(i8* %.27)
  br label %entry.endif

entry.endif:                                      ; preds = %entry.else, %entry.if
  %.30 = load i32, i32* %soma, align 4
  %.31 = icmp sgt i32 %.30, 10
  br i1 %.31, label %entry.endif.if, label %entry.endif.endif

entry.endif.if:                                   ; preds = %entry.endif
  %.33 = bitcast [19 x i8]* @"887be7dd7b1e4419819416248a97ef2a" to i8*
  %.34 = call i32 (i8*, ...) @printf(i8* %.33)
  br label %entry.endif.endif

entry.endif.endif:                                ; preds = %entry.endif.if, %entry.endif
  %i = alloca i32, align 4
  store i32 0, i32* %i, align 4
  br label %entry.endif.endif.for_init

entry.endif.endif.for_init:                       ; preds = %entry.endif.endif.for_loop, %entry.endif.endif
  %.38 = load i32, i32* %i, align 4
  %.39 = icmp slt i32 %.38, 10
  br i1 %.39, label %entry.endif.endif.for_loop, label %entry.endif.endif.for_end

entry.endif.endif.for_loop:                       ; preds = %entry.endif.endif.for_init
  %.41 = bitcast [8 x i8]* @"0c5062c4ca284f898ddbc4827923ff11" to i8*
  %.42 = load i32, i32* %i, align 4
  %.43 = call i32 (i8*, ...) @printf(i8* %.41, i32 %.42)
  %.44 = load i32, i32* %i, align 4
  %.45 = add i32 %.44, 1
  store i32 %.45, i32* %i, align 4
  br label %entry.endif.endif.for_init

entry.endif.endif.for_end:                        ; preds = %entry.endif.endif.for_init
  ret void
}

; Function Attrs: nounwind
declare void @llvm.stackprotector(i8*, i8**) #0

attributes #0 = { nounwind }
