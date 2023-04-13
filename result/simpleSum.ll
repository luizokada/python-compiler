; ModuleID = '<string>'
source_filename = "<string>"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@c235aea637334f188d7a4a5ee8dbe6dd = internal constant [21 x i8] c"Digite o valor de a\0A\00"
@"7a7eab3b71d74d49b05a202a29738d07" = constant [3 x i8] c"%d\00"
@"1deb1cf5759741df9e7221486e5640ca" = internal constant [21 x i8] c"Digite o valor de b\0A\00"
@c4270d6002bc4b619116f53639647ee2 = constant [3 x i8] c"%d\00"
@bbe3450b9bc24124a1025f44d9e8a15f = internal constant [12 x i8] c"a + b = %d\0A\00"
@"958c63be0ecd42709630c35133a99396" = internal constant [19 x i8] c"Soma maior que 10\0A\00"
@"987b608dd75b4405ae0f0ef6fcfe8e39" = internal constant [19 x i8] c"Soma menor que 10\0A\00"
@"1027ed4f73204bd582c0100657b5076f" = internal constant [19 x i8] c"Soma maior que 10\0A\00"
@"135bd78b859a4a5ca2071608949e009f" = internal constant [8 x i8] c"i = %d\0A\00"

declare i32 @printf(i8*, ...)

declare i32 @scanf(i8*, ...)

define void @main() {
entry:
  %a = alloca i32, align 4
  %b = alloca i32, align 4
  %soma = alloca i32, align 4
  %.2 = bitcast [21 x i8]* @c235aea637334f188d7a4a5ee8dbe6dd to i8*
  %.3 = call i32 (i8*, ...) @printf(i8* %.2)
  %.4 = bitcast [3 x i8]* @"7a7eab3b71d74d49b05a202a29738d07" to i8*
  %.5 = call i32 (i8*, ...) @scanf(i8* %.4, i32* %a)
  %.6 = bitcast [21 x i8]* @"1deb1cf5759741df9e7221486e5640ca" to i8*
  %.7 = call i32 (i8*, ...) @printf(i8* %.6)
  %.8 = bitcast [3 x i8]* @c4270d6002bc4b619116f53639647ee2 to i8*
  %.9 = call i32 (i8*, ...) @scanf(i8* %.8, i32* %b)
  %.10 = load i32, i32* %a, align 4
  %.11 = load i32, i32* %b, align 4
  %.12 = add i32 %.10, %.11
  store i32 %.12, i32* %soma, align 4
  %.14 = load i32, i32* %soma, align 4
  %.15 = load i32, i32* %b, align 4
  %.16 = add i32 %.14, %.15
  store i32 %.16, i32* %a, align 4
  %.18 = bitcast [12 x i8]* @bbe3450b9bc24124a1025f44d9e8a15f to i8*
  %.19 = load i32, i32* %soma, align 4
  %.20 = call i32 (i8*, ...) @printf(i8* %.18, i32 %.19)
  %.21 = load i32, i32* %soma, align 4
  %.22 = icmp sgt i32 %.21, 10
  br i1 %.22, label %entry.if, label %entry.else

entry.if:                                         ; preds = %entry
  %soma.1 = alloca i8, align 1
  %.24 = bitcast [19 x i8]* @"958c63be0ecd42709630c35133a99396" to i8*
  %.25 = call i32 (i8*, ...) @printf(i8* %.24)
  br label %entry.endif

entry.else:                                       ; preds = %entry
  %.27 = bitcast [19 x i8]* @"987b608dd75b4405ae0f0ef6fcfe8e39" to i8*
  %.28 = call i32 (i8*, ...) @printf(i8* %.27)
  br label %entry.endif

entry.endif:                                      ; preds = %entry.else, %entry.if
  %.30 = load i32, i32* %soma, align 4
  %.31 = icmp sgt i32 %.30, 10
  br i1 %.31, label %entry.endif.if, label %entry.endif.endif

entry.endif.if:                                   ; preds = %entry.endif
  %.33 = bitcast [19 x i8]* @"1027ed4f73204bd582c0100657b5076f" to i8*
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
  %.41 = bitcast [8 x i8]* @"135bd78b859a4a5ca2071608949e009f" to i8*
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
