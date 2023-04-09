; ModuleID = '<string>'
source_filename = "<string>"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@a3c118ba92f34eacbd7f94a5596abad3 = internal constant [20 x i8] c"'a is less than 5'\0A\00"
@"5513d642cb954e8d8720bcf8aa00e698" = internal constant [23 x i8] c"'a is greater than 5'\0A\00"

declare i32 @printf(i8*, ...)

define void @main() {
entry:
  %a = alloca i32, align 4
  %b = alloca i32, align 4
  %i = alloca i32, align 4
  store i32 0, i32* %a, align 4
  store i32 0, i32* %i, align 4
  br label %entry.for_init

entry.for_init:                                   ; preds = %entry.for_loop.endif, %entry
  %.5 = load i32, i32* %i, align 4
  %.6 = icmp slt i32 %.5, 10
  br i1 %.6, label %entry.for_loop, label %entry.for_end

entry.for_loop:                                   ; preds = %entry.for_init
  %.8 = load i32, i32* %a, align 4
  %.9 = add i32 %.8, 1
  store i32 %.9, i32* %a, align 4
  %.11 = load i32, i32* %a, align 4
  %.12 = icmp slt i32 %.11, 5
  br i1 %.12, label %entry.for_loop.if, label %entry.for_loop.else

entry.for_end:                                    ; preds = %entry.for_init
  %c = alloca i32, align 4
  ret void

entry.for_loop.if:                                ; preds = %entry.for_loop
  %.14 = bitcast [20 x i8]* @a3c118ba92f34eacbd7f94a5596abad3 to i8*
  %.15 = call i32 (i8*, ...) @printf(i8* %.14)
  br label %entry.for_loop.endif

entry.for_loop.else:                              ; preds = %entry.for_loop
  %.17 = bitcast [23 x i8]* @"5513d642cb954e8d8720bcf8aa00e698" to i8*
  %.18 = call i32 (i8*, ...) @printf(i8* %.17)
  br label %entry.for_loop.endif

entry.for_loop.endif:                             ; preds = %entry.for_loop.else, %entry.for_loop.if
  %.20 = load i32, i32* %i, align 4
  %.21 = add i32 %.20, 1
  store i32 %.21, i32* %i, align 4
  br label %entry.for_init
}

; Function Attrs: nounwind
declare void @llvm.stackprotector(i8*, i8**) #0

attributes #0 = { nounwind }
