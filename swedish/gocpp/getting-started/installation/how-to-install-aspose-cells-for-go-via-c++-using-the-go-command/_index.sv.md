---
title: Hur man installerar Aspose.Cells for Go via C++ med Go kommandot.
type: docs
linktitle: Installera via Go kommandot
weight: 40
url: /sv/go-cpp/how-to-install-aspose-cells-for-go-via-c++-using-the-go-command
---


## **Hur man installerar Aspose.Cells for Go via C++ med Go-kommandot**

   Från Go 1.16 använder du `go install`-kommandot direkt för att installera paketet Aspose.Cells for Go via C++. Kommandot tillåter global installation av kommandoradsverktyg utan att påverka befintliga projektberoenden.

```go

go install github.com/aspose-cells/aspose-cells-go-cpp/v25@latest

```

   När du använder `go get`-kommandot för att installera paketet Aspose.Cells for Go via C++, måste filen go.mod finnas i den aktuella katalogen eller någon överordnad katalog. Se till att [installera Aspose.Cells for Go via C++-paketet och köra din kod i ditt projekt](#Installation-in-your-project)

```go

go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1

```

### Installera Aspose.Cells for Go via C++ paketet och kör din kod i ditt projekt {#Installation-in-your-project}

1. Skapa en katalog för ditt projekt och en main.go-fil däri. Lägg till följande kod i din main.go.

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

1. Initiera projektet go.mod

```bash

go mod init main

```

1. Hämta beroenden till ditt projekt.

```bash

go mod tidy

```

Om Aspose.Cells for Go via C++ inte är installerat i utvecklingsmiljön, kommer Go automatiskt att installera paketet i `$GOPATH` underkatalogen.

1. Ange din PATH så att den pekar till de delade biblioteken i Aspose.Cells for Go via C++ i din aktuella kommandoskal. Ersätt your_version med den version av Aspose.Cells for Go via C++ du kör.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1/lib/linux_x86_64/

```

Eller i din powershell

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.1\lib\win_x86_64\"

```

Du kan också kopiera DLL-filerna från ovanstående sökväg till samma plats som ditt projekts körbara fil.

1. Kör din skapade applikation.

```bash

go run main.go

```
