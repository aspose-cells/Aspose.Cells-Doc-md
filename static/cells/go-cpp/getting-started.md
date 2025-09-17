##Getting Started
How to install Aspose Cells for Go via C++ and create a Hello World application.
This page will show you how to install Aspose Cells for Go via C++ and create a Hello World application.
## Aspose.Cells for Go via C++ integration
Welcome to Aspose.Cells for Go via C++! This cross-platform solution supports both Windows and Linux. To get started, execute a code file that uses the package.
### Prerequisites
- [Go (>=1.13)](https://golang.org/doc/install/)
- [Git](https://git-scm.com/downloads)
### Running Aspose.Cells for Go via C++ in your project
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
workbook.Save_String("HELLO.xlsx")
}
```
1. Initialize project go.mod
```bash
go mod init main
```
1. Fetch the dependencies for project.
```bash
go mod tidy
```
1. Set your PATH to point to the shared libraries in Aspose.Cells for Go via C++ in your current command shell. Replace your_version with the version of Aspose.Cells for Go via C++ you are running.
```bash
set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.0/lib/linux_x86_64/
```
Or in your powershell
```powershell
$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.0\lib\win_x86_64\"
```
You may also copy the DLL files from the above path to the same place as your project executable.
1. Run your created application.
```bash
go run main.go
```
