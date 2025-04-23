---
title: 如何使用 Go 命令安装 Aspose.Cells for Go via C++。
type: docs
linktitle: 使用 Go 命令安装
weight: 40
url: /zh/go-cpp/how-to-install-aspose-cells-for-go-via-c++-using-the-go-command
---


## **如何使用 Go 命令安装 Aspose.Cells for Go via C++**

   从 Go 1.16 开始，您可以直接使用 `go install` 命令安装 Aspose.Cells for Go via C++ 包。该命令允许全局安装命令行工具，无需担心影响现有项目依赖。

```go

go install github.com/aspose-cells/aspose-cells-go-cpp/v25@latest

```

   当您使用 `go get` 命令安装 Aspose.Cells for Go via C++ 包时，需要当前目录或任意父目录中存在 go.mod 文件。详情请参阅 [项目中安装 Aspose.Cells for Go via C++ 包并运行您的代码](#Installation-in-your-project)

```go

go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1

```

### 在您的项目中安装 Aspose.Cells for Go via C++ 包并运行代码 {#Installation-in-your-project}

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
 workbook.Save_String("HELLO.pdf")

}

```

1. 初始化项目 go.mod

```bash

go mod init main

```

1. 获取项目的依赖项。

```bash

go mod tidy

```

如果开发环境中未安装 Aspose.Cells for Go via C++，Go 会自动将包安装到 `$GOPATH` 子目录中。

1. 在当前命令终端中，将你的PATH设置为指向Aspose.Cells for Go via C++的共享库。用你的版本替换your_version。

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1/lib/linux_x86_64/

```

或者在您的PowerShell中

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.1\lib\win_x86_64\"

```

您也可以将上述路径中的DLL文件复制到与您的项目可执行文件相同的地方。

1. 运行您创建的应用程序。

```bash

go run main.go

```
