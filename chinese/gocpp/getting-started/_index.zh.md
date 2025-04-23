---
title: 入门
type: docs
weight: 10
url: /zh/go-cpp/getting-started/
description: 如何安装 Aspose Cells for Go via C++ 并创建“Hello World”应用程序。
---

{{% alert color="primary" %}}

此页面将向您展示如何安装 Aspose Cells for Go via C++ 并创建“Hello World”应用程序。

{{% /alert %}}

## Aspose.Cells for Go via C++ 集成

欢迎使用Aspose.Cells for Go via C++！这个跨平台解决方案支持Windows和Linux。开始使用前，执行一个使用该包的代码文件。

### 前提条件

- [Go (>=1.13)](https://golang.org/doc/install/)
- [Git](https://git-scm.com/downloads)

### 在你的项目中运行Aspose.Cells for Go via C++

1. 创建您的项目目录和一个main.go文件。在main.go中添加以下代码。

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

1. 初始化项目 go.mod

```bash

go mod init main

```

1. 获取项目依赖。

```bash

go mod tidy

```

1. 在当前命令终端中，将你的PATH设置为指向Aspose.Cells for Go via C++的共享库。用你的版本替换your_version。

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.0/lib/linux_x86_64/

```

或者在您的PowerShell中

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.0\lib\win_x86_64\"

```

您也可以将上述路径中的DLL文件复制到与您的项目可执行文件相同的地方。

1. 运行您创建的应用程序。

```bash

go run main.go

```
