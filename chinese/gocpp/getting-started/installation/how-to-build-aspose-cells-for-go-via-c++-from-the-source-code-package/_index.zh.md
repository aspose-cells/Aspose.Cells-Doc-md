---
title: 如何从源代码包构建 Aspose.Cells for Go via C++。
type: docs
linktitle: 从源代码构建
weight: 50
url: /zh/go-cpp/how-to-build-aspose-cells-for-go-via-c++-from-the-source-code-package
---


## **如何从源代码包构建 Aspose.Cells for Go via C++**

### 1. 下载 Aspose.Cells for Go via C++ 源码包

- **你可以从两个位置下载源码包：**

1. 从 [Aspose.Cells for Go via C++ 下载页面](https://downloads.aspose.com/cells/go-cpp/) 下载源码包。  
1. 从 [GitHub 仓库](https://github.com/aspose-cells/aspose-cells-go-cpp) 或直接通过 [GitHub Archive Package](https://github.com/aspose-cells/aspose-cells-go-cpp/archive/refs/heads/main.zip) 下载源代码包。  

### 2. 如何将 Aspose.Cells for Go via C++ 包安装到您的项目中

- **为您的项目创建一个目录，并在其中添加一个 main.go 文件。在您的 main.go 中添加以下代码。**

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

- **初始化项目的 go.mod**

```bash

go mod init main

```

- **将 ZIP 文件解压到您的项目目录中的 cells-go-cpp 文件夹。**

 --cells-go-cpp 示例
   -- cells-go-cpp（文件夹）
     -- start_up.go
     -- aspose_cells.go
     -- ......
     -- go.mod
     -- AsposeCellsCWrapper.h
   -- main.go
   -- go.mod

- **修改您的 Go `mod` 文件以指定包的位置：**

   ```go
    module main

    go 1.19

    require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0
    replace github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0  => ./cells-go-cpp
   ```

- **在当前命令行中将您的 PATH 指向 Aspose.Cells for Go via C++ 的共享库。将 your_version 替换为您使用的 Aspose.Cells for Go via C++ 版本。**

```bash

set PATH=%PATH%;%YourProjectPath%/cells-go-cpp-samples/cells-go-cpp/lib/win_x86_64/

```

或者在您的PowerShell中

```powershell

$env:Path = $env:Path+ ";${YourProjectPath}\cells-go-cpp-samples\cells-go-cpp\lib\win_x86_64\"

```

您也可以将上述路径中的DLL文件复制到与您的项目可执行文件相同的地方。

- **运行您创建的应用程序。**

```bash

go run main.go

```
