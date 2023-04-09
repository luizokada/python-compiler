; ModuleID = '<string>'
source_filename = "<string>"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@"1740ffb9dbb14f61b0d8472e9e51be74" = internal constant [18 x i8] c"'Hello World %d'\0A\00"
@"24880c4c4d6740cfba9d722f8a420a1b" = internal constant [18 x i8] c"'Hello World %d'\0A\00"
@bce50f0ab92e473d8f73abfccc8624a4 = internal constant [17 x i8] c"'Hello ERRO %d'\0A\00"
@"3198ecc5b8b7408b8a5577f742cb7717" = internal constant [17 x i8] c"'Hello ERRO %d'\0A\00"
@"27596ec1dc06427bb4c1e546b052c4a5" = internal constant [18 x i8] c"'Hello World %d'\0A\00"

declare i32 @printf(i8*, ...)

define void @main() {
entry:
  %a = alloca i32, align 4
  %b = alloca i32, align 4
  store i32 10, i32* %a, align 4
  %.3 = load i32, i32* %a, align 4
  %.4 = icmp eq i32 %.3, 10
  br i1 %.4, label %entry.if, label %entry.else

entry.if:                                         ; preds = %entry
  %.6 = bitcast [18 x i8]* @"1740ffb9dbb14f61b0d8472e9e51be74" to i8*
  %.7 = load i32, i32* %a, align 4
  %.8 = call i32 (i8*, ...) @printf(i8* %.6, i32 %.7)
  %.9 = load i32, i32* %a, align 4
  %.10 = icmp eq i32 %.9, 10
  br i1 %.10, label %entry.if.if, label %entry.if.else

entry.else:                                       ; preds = %entry
  %.21 = bitcast [17 x i8]* @"3198ecc5b8b7408b8a5577f742cb7717" to i8*
  %.22 = load i32, i32* %a, align 4
  %.23 = call i32 (i8*, ...) @printf(i8* %.21, i32 %.22)
  br label %entry.endif

entry.endif:                                      ; preds = %entry.if.if, %entry.if.else, %entry.else
  store i32 20, i32* %a, align 4
  %.26 = bitcast [18 x i8]* @"27596ec1dc06427bb4c1e546b052c4a5" to i8*
  %.27 = load i32, i32* %a, align 4
  %.28 = call i32 (i8*, ...) @printf(i8* %.26, i32 %.27)
  ret void

entry.if.if:                                      ; preds = %entry.if
  %.12 = bitcast [18 x i8]* @"24880c4c4d6740cfba9d722f8a420a1b" to i8*
  %.13 = load i32, i32* %a, align 4
  %.14 = call i32 (i8*, ...) @printf(i8* %.12, i32 %.13)
  br label %entry.endif

entry.if.else:                                    ; preds = %entry.if
  %.16 = bitcast [17 x i8]* @bce50f0ab92e473d8f73abfccc8624a4 to i8*
  %.17 = load i32, i32* %a, align 4
  %.18 = call i32 (i8*, ...) @printf(i8* %.16, i32 %.17)
  br label %entry.endif
}

; Function Attrs: nounwind
declare void @llvm.stackprotector(i8*, i8**) #0

attributes #0 = { nounwind }
