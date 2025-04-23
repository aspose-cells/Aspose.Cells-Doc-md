---
title: البدء
type: docs
weight: 10
url: /ar/go-cpp/getting-started/
description: كيفية تثبيت Aspose Cells للغة Go عبر C++ وإنشاء تطبيق Hello World.
---

{{% alert color="primary" %}}

ستُظهر لك هذه الصفحة كيفية تثبيت Aspose Cells لـ Go عبر C++ وإنشاء تطبيق Hello World.

{{% /alert %}}

## تكامل Aspose.Cells for Go via C++

مرحبًا بك في Aspose.Cells for Go via C++! يدعم هذا الحل متعدد المنصات كل من Windows و Linux. للبدء، نفذ ملف رمز يستخدم الحزمة.

### المتطلبات الأساسية

- [Go (>=1.13)](https://golang.org/doc/install/)
- [Git](https://git-scm.com/downloads)

### تشغيل Aspose.Cells for Go via C++ في مشروعك

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
 workbook.Save_String("HELLO.xlsx")

}

```

1. تهيئة مشروع go.mod

```bash

go mod init main

```

1. جلب الاعتمادات للمشروع.

```bash

go mod tidy

```

1. اضبط مسار PATH الخاص بك ليشير إلى المكتبات المشتركة في Aspose.Cells for Go via C++ في قشرة الأوامر الحالية. استبدل your_version بنسخة Aspose.Cells for Go via C++ التي تستخدمها.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.0/lib/linux_x86_64/

```

أو في PowerShell الخاص بك

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.0\lib\win_x86_64\"

```

يمكنك أيضًا نسخ ملفات DLL من المسار أعلاه إلى نفس مكان ملف التنفيذ الخاص بمشروعك.

1. قم بتشغيل التطبيق الذي أنشأته.

```bash

go run main.go

```
