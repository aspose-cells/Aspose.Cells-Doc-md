---
title: كيفية تثبيت Aspose.Cells for Go via C++ باستخدام أمر Go.
type: docs
linktitle: التثبيت عبر أمر Go
weight: 40
url: /ar/go-cpp/how-to-install-aspose-cells-for-go-via-c++-using-the-go-command
---


## **كيفية تثبيت Aspose.Cells for Go via C++ باستخدام أمر Go**

   من إصدار Go 1.16، يمكنك استخدام الأمر `go install` مباشرة لتثبيت حزمة Aspose.Cells for Go via C++. يتيح الأمر تثبيت أدوات سطر الأوامر عالمياً دون القلق بشأن التأثير على اعتماديات المشروع الحالية.

```go

go install github.com/aspose-cells/aspose-cells-go-cpp/v25@latest

```

   عند استخدامك لأمر `go get` لتثبيت حزمة Aspose.Cells for Go via C++، يجب أن يكون ملف go.mod موجوداً في الدليل الحالي أو في أي دليل أعلى منه. راجع [تثبيت حزمة Aspose.Cells for Go via C++ وتشغيل الشيفرة في مشروعك](#Installation-in-your-project)

```go

go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1

```

### تثبيت حزمة Aspose.Cells for Go via C++ وتشغيل الكود الخاص بك في مشروعك {#Installation-in-your-project}

1. أنشئ دليلًا لمشروعك وملف main.go داخله. أضف الكود التالي إلى main.go.

```Go

package main

import (
 . "github.com/aspose-cells/aspose-cells-go-cpp/v25"
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

1. تهيئة مشروع go.mod

```bash

go mod init main

```

1. استرجاع الاعتمادات لمشروعك.

```bash

go mod tidy

```

إذا لم يتم تثبيت Aspose.Cells for Go via C++ في بيئة التطوير، فسيقوم Go تلقائيًا بتثبيت الحزمة في مجلد `$GOPATH` الفرعي.

1. اضبط مسار PATH الخاص بك ليشير إلى المكتبات المشتركة في Aspose.Cells for Go via C++ في قشرة الأوامر الحالية. استبدل your_version بنسخة Aspose.Cells for Go via C++ التي تستخدمها.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1/lib/linux_x86_64/

```

أو في PowerShell الخاص بك

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.1\lib\win_x86_64\"

```

يمكنك أيضًا نسخ ملفات DLL من المسار أعلاه إلى نفس مكان ملف التنفيذ الخاص بمشروعك.

1. قم بتشغيل التطبيق الذي أنشأته.

```bash

go run main.go

```
