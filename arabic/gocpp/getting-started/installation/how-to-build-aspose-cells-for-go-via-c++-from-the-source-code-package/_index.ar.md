---
title: كيفية بناء Aspose.Cells for Go via C++ من حزمة الشيفرة المصدرية.
type: docs
linktitle: بناء من الشيفرة المصدرية
weight: 50
url: /ar/go-cpp/how-to-build-aspose-cells-for-go-via-c++-from-the-source-code-package
---


## **كيفية بناء Aspose.Cells for Go via C++ من حزمة الشيفرة المصدرية**

### 1. تحميل حزمة مصدر Aspose.Cells for Go via C++

- **يمكنك تحميل حزمة الشيفرة المصدرية من موقعين:**

1. حمّل حزمة الشيفرة المصدرية من [صفحة تحميل Aspose.Cells for Go via C++](https://downloads.aspose.com/cells/go-cpp/).  
1. حمّل حزمة الشيفرة المصدرية من [مستودع GitHub](https://github.com/aspose-cells/aspose-cells-go-cpp) أو مباشرة عبر [حزمة أرشيف GitHub](https://github.com/aspose-cells/aspose-cells-go-cpp/archive/refs/heads/main.zip).  

### 2. كيفية تثبيت حزمة Aspose.Cells for Go via C++ في مشروعك

- **قم بإنشاء دليل لمشروعك وملف main.go بداخله. أضف الكود التالي إلى ملف main.go الخاص بك.**

```Go

package main

import (
 . "asposecells"
 "fmt"
)

func main() {
 lic, _ := NewLicense()
 lic.SetLicense_String("YOUR_LICENSE_File_PATH")
 workbook, _ := NewWorkbook()
 worksheets, _ := workbook.GetWorksheets()
 worksheet, _ := worksheets.Get_Int(0)
 cells, _ := worksheet.GetCells()
 cell, _ := cells.Get_String("A1")
 cell.PutValue_String_Bool("Hello World!", true)
 style, _ := cell.GetStyle()
 style.SetPattern(BackgroundType_Solid)
 color, _ := NewColor()
 color.Set_Color_R(uint8(255))
 color.Set_Color_G(uint8(128))
 style.SetForegroundColor(color)
 cell.SetStyle_Style(style)
 workbook.Save_String("HELLO.pdf")

}

```

- **تهيئة مشروع go.mod**

```bash

go mod init main

```

- **استخراج ملف ZIP إلى مجلد cells-go-cpp في دليل مشروعك.**

 --cells-go-cpp-samples
   -- مجلد cells-go-cpp
     -- start_up.go
     -- aspose_cells.go
     -- ......
     -- go.mod
     -- AsposeCellsCWrapper.h
   -- main.go
   -- go.mod

- **قم بتعديل ملف go `mod` الخاص بك لتحديد موقع الحزمة:**

   ```go
    module main

    go 1.19

    require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0
    replace github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0  => ./cells-go-cpp
   ```

- **قم بتعيين المسار الخاص بك ليشير إلى المكتبات المشتركة في Aspose.Cells for Go via C++ في جلسة الأوامر الحالية الخاصة بك. استبدل your_version بالإصدار المستخدم من Aspose.Cells for Go via C++.**

```bash

set PATH=%PATH%;%YourProjectPath%/cells-go-cpp-samples/cells-go-cpp/lib/win_x86_64/

```

أو في PowerShell الخاص بك

```powershell

$env:Path = $env:Path+ ";${YourProjectPath}\cells-go-cpp-samples\cells-go-cpp\lib\win_x86_64\"

```

يمكنك أيضًا نسخ ملفات DLL من المسار أعلاه إلى نفس مكان ملف التنفيذ الخاص بمشروعك.

- **قم بتشغيل التطبيق الذي أنشاته.**

```bash

go run main.go

```
