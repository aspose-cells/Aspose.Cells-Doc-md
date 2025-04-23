---
title: Komma igång
type: docs
weight: 10
url: /sv/go-cpp/getting-started/
description: Hur man installerar Aspose Cells for Go via C++ och skapar ett Hello World program.
---

{{% alert color="primary" %}}

Den här sidan visar hur du installerar Aspose Cells för Go via C++ och skapar en Hello World-applikation.

{{% /alert %}}

## Aspose.Cells for Go via C++ integration

Välkommen till Aspose.Cells for Go via C++! Denna plattformsoberoende lösning stöder både Windows och Linux. För att komma igång, kör en kodfil som använder paketet.

### Förutsättningar

- [Go (>=1.13)](https://golang.org/doc/install/)
- [Git](https://git-scm.com/downloads)

### Kör Aspose.Cells for Go via C++ i ditt projekt

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
 workbook.Save_String("HELLO.xlsx")

}

```

1. Initiera projektet go.mod

```bash

go mod init main

```

1. Hämta beroenden för projektet.

```bash

go mod tidy

```

1. Ange din PATH så att den pekar till de delade biblioteken i Aspose.Cells for Go via C++ i din aktuella kommandoskal. Ersätt your_version med den version av Aspose.Cells for Go via C++ du kör.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.0/lib/linux_x86_64/

```

Eller i din powershell

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.0\lib\win_x86_64\"

```

Du kan också kopiera DLL-filerna från ovanstående sökväg till samma plats som ditt projekts körbara fil.

1. Kör din skapade applikation.

```bash

go run main.go

```
