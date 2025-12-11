---
title: How to Build Aspose.Cells for Go via C++ from the Source Code Package.
type: docs
linktitle: Build from Source Code
weight: 50
url: /go-cpp/how-to-build-aspose-cells-for-go-via-c++-from-the-source-code-package
---

## **How to build Aspose.Cells for Go via C++ from the Source Code Package**

### 1. Download Aspose.Cells for Go via C++ source package

- **You can download the source code package from two locations:**

1. Download the source code package from the [Aspose.Cells for Go via C++ download page](https://downloads.aspose.com/cells/go-cpp/).  
2. Download the source code package from the [GitHub repository](https://github.com/aspose-cells/aspose-cells-go-cpp) or directly via [GitHub Archive Package](https://github.com/aspose-cells/aspose-cells-go-cpp/archive/refs/heads/main.zip).  

### 2. How to install Aspose.Cells for Go via C++ package into your project

- **Create a directory for your project and a `main.go` file within. Add the following code to your `main.go`.**

```go
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

- **Initialize the project `go.mod` file**

```bash
go mod init main
```

- **Extract the ZIP file to the `cells-go-cpp` folder in your project directory.**

```
cells-go-cpp-samples
  cells-go-cpp (folder)
    start_up.go
    aspose_cells.go
    ...
    go.mod
    AsposeCellsCWrapper.h
  main.go
  go.mod
```

- **Modify your Go `go.mod` file to specify the package's location:**

```go
module main

go 1.19

require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0
replace github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0 => ./cells-go-cpp
```

- **Set your PATH to point to the shared libraries in Aspose.Cells for Go via C++ in your current command shell. Replace `your_version` with the version of Aspose.Cells for Go via C++ you are running.**

```bash
set PATH=%PATH%;%YourProjectPath%/cells-go-cpp-samples/cells-go-cpp/lib/win_x86_64/
```

Or in PowerShell:

```powershell
$env:Path = $env:Path + ";${YourProjectPath}\cells-go-cpp-samples\cells-go-cpp\lib\win_x86_64\"
```

You may also copy the DLL files from the above path to the same location as your project executable.

- **Run your created application.**

```bash
go run main.go
```