---
title: Hur man bygger Aspose.Cells for Go via C++ från källkodspaketet.
type: docs
linktitle: Bygg från källkod
weight: 50
url: /sv/go-cpp/how-to-build-aspose-cells-for-go-via-c++-from-the-source-code-package
---


## **Hur man bygger Aspose.Cells for Go via C++ från källkodspaketet**

### 1. Ladda ner källpaketet Aspose.Cells for Go via C++

- **Du kan ladda ner källkodspaketet från två platser:**

1. Ladda ner källkodspaketet från [Aspose.Cells for Go via C++ nedladdningssida](https://downloads.aspose.com/cells/go-cpp/).  
1. Ladda ner källkodspaketet från [GitHub-repositoryt](https://github.com/aspose-cells/aspose-cells-go-cpp) eller direkt via [GitHub Archive Package](https://github.com/aspose-cells/aspose-cells-go-cpp/archive/refs/heads/main.zip).  

### 2. Hur man installerar paketet Aspose.Cells for Go via C++ i ditt projekt

- **Skapa en katalog för ditt projekt och en main.go-fil däri. Lägg till följande kod i din main.go.**

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

- **Initiera projektet go.mod**

```bash

go mod init main

```

- **Extrahera ZIP-filen till mappen cells-go-cpp i din projektkatalog.**

 --cells-go-cpp-prover
   -- cells-go-cpp (mapp) 
     -- start_up.go
     -- aspose_cells.go
     -- ......
     -- go.mod
     -- AsposeCellsCWrapper.h
   -- main.go
   -- go.mod

- **Ändra din Go `mod`-fil för att specificera paketets plats:**

   ```go
    module main

    go 1.19

    require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0
    replace github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0  => ./cells-go-cpp
   ```

- **Ange din PATH så att den pekar till de delade biblioteken i Aspose.Cells for Go via C++ i din aktuella kommandoskal. Ersätt your_version med den version av Aspose.Cells for Go via C++ du kör.**

```bash

set PATH=%PATH%;%YourProjectPath%/cells-go-cpp-samples/cells-go-cpp/lib/win_x86_64/

```

Eller i din powershell

```powershell

$env:Path = $env:Path+ ";${YourProjectPath}\cells-go-cpp-samples\cells-go-cpp\lib\win_x86_64\"

```

Du kan också kopiera DLL-filerna från ovanstående sökväg till samma plats som ditt projekts körbara fil.

- **Kör din skapade applikation.**

```bash

go run main.go

```
