---
title: How to Install Aspose.Cells for Go via C++ Using the Go Command.
type: docs
linktitle: Install via Go Command
weight: 40
url: /go-cpp/how-to-install-aspose-cells-for-go-via-c++-using-the-go-command
---


## **How to Install Aspose.Cells for Go via C++ Using the Go Command**

   From Go 1.16, you use `go install` command directly to install the Aspose.Cells for Go via C++ package. The command allows for the global installation of command-line tools without worrying about affecting existing project dependencies.

```go

go install github.com/aspose-cells/aspose-cells-go-cpp/v25@latest

```

   When you use `go get` command to install the Aspose.Cells for Go via C++ package, need exist the go.mod file in the current directory or any parent directory. see to [installation Aspose.Cells for Go via C++ package and running your code in your project](#Installation-in-your-project)

```go

go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1

```

### Installation Aspose.Cells for Go via C++ package and running your code in your project {#Installation-in-your-project}

1. Create a directory for your project and a main.go file within. Add the following code to your main.go.

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

1. Initialize project go.mod

```bash

go mod init main

```

1. Fetch the dependencies for your project.

```bash

go mod tidy

```

If Aspose.Cells for Go via C++ is not installed in the development environment, Go will automatically install the package in the `$GOPATH` subdirectory.

1. Set your PATH to point to the shared libraries in Aspose.Cells for Go via C++ in your current command shell. Replace your_version with the version of Aspose.Cells for Go via C++ you are running.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1/lib/linux_x86_64/

```

Or in your powershell

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.1\lib\win_x86_64\"

```

You may also copy the DLL files from the above path to the same place as your project executable.

1. Run your created application.

```bash

go run main.go

```
