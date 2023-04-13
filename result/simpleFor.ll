; ModuleID = '<string>'
source_filename = "<string>"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@"68c18f3c1b1c446991da80261d1be611" = internal constant [22 x i8] c"i = %d j = %d k = %d\0A\00"

declare i32 @printf(i8*, ...)

declare i32 @scanf(i8*, ...)

define void @main() {
entry:
  %i = alloca i32, align 4
  %j = alloca i32, align 4
  %k = alloca i32, align 4
  store i32 0, i32* %i, align 4
  br label %entry.for_init

entry.for_init:                                   ; preds = %entry.for_loop.for_end, %entry
  %.4 = load i32, i32* %i, align 4
  %.5 = icmp slt i32 %.4, 10
  br i1 %.5, label %entry.for_loop, label %entry.for_end

entry.for_loop:                                   ; preds = %entry.for_init
  store i32 0, i32* %j, align 4
  br label %entry.for_loop.for_init

entry.for_end:                                    ; preds = %entry.for_init
  ret void

entry.for_loop.for_init:                          ; preds = %entry.for_loop.for_loop.for_end, %entry.for_loop
  %.9 = load i32, i32* %j, align 4
  %.10 = icmp slt i32 %.9, 10
  br i1 %.10, label %entry.for_loop.for_loop, label %entry.for_loop.for_end

entry.for_loop.for_loop:                          ; preds = %entry.for_loop.for_init
  store i32 0, i32* %k, align 4
  br label %entry.for_loop.for_loop.for_init

entry.for_loop.for_end:                           ; preds = %entry.for_loop.for_init
  %.30 = load i32, i32* %i, align 4
  %.31 = add i32 %.30, 1
  store i32 %.31, i32* %i, align 4
  br label %entry.for_init

entry.for_loop.for_loop.for_init:                 ; preds = %entry.for_loop.for_loop.for_loop, %entry.for_loop.for_loop
  %.14 = load i32, i32* %k, align 4
  %.15 = icmp slt i32 %.14, 10
  br i1 %.15, label %entry.for_loop.for_loop.for_loop, label %entry.for_loop.for_loop.for_end

entry.for_loop.for_loop.for_loop:                 ; preds = %entry.for_loop.for_loop.for_init
  %.17 = bitcast [22 x i8]* @"68c18f3c1b1c446991da80261d1be611" to i8*
  %.18 = load i32, i32* %i, align 4
  %.19 = load i32, i32* %j, align 4
  %.20 = load i32, i32* %k, align 4
  %.21 = call i32 (i8*, ...) @printf(i8* %.17, i32 %.18, i32 %.19, i32 %.20)
  %.22 = load i32, i32* %k, align 4
  %.23 = add i32 %.22, 1
  store i32 %.23, i32* %k, align 4
  br label %entry.for_loop.for_loop.for_init

entry.for_loop.for_loop.for_end:                  ; preds = %entry.for_loop.for_loop.for_init
  %.26 = load i32, i32* %j, align 4
  %.27 = add i32 %.26, 1
  store i32 %.27, i32* %j, align 4
  br label %entry.for_loop.for_init
}

; Function Attrs: nounwind
declare void @llvm.stackprotector(i8*, i8**) #0

attributes #0 = { nounwind }
