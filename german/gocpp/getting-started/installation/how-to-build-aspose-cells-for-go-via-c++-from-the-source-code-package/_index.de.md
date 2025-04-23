---
title: Wie man Aspose.Cells for Go via C++ aus dem Quellcode Paket baut.
type: docs
linktitle: Vom Quellcode bauen
weight: 50
url: /de/go-cpp/how-to-build-aspose-cells-for-go-via-c++-from-the-source-code-package
---


## **Wie man Aspose.Cells for Go via C++ aus dem Quellcode-Paket erstellt**

### 1. Download des Quellcode-Pakets Aspose.Cells for Go via C++

- **Sie können das Quellcode-Paket von zwei Standorten herunterladen:**

1. Laden Sie das Quellcode-Paket von der [Aspose.Cells for Go via C++ Download-Seite](https://downloads.aspose.com/cells/go-cpp/) herunter.  
1. Laden Sie das Quellcode-Paket vom [GitHub-Repository](https://github.com/aspose-cells/aspose-cells-go-cpp) oder direkt über das [GitHub-Archivpaket](https://github.com/aspose-cells/aspose-cells-go-cpp/archive/refs/heads/main.zip) herunter.  

### 2. Wie das Paket Aspose.Cells for Go via C++ in Ihr Projekt installiert wird

- **Erstellen Sie ein Verzeichnis für Ihr Projekt und eine main.go Datei darin. Fügen Sie den folgenden Code in Ihre main.go ein.**

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

- **Initialisieren Sie die Projektdatei go.mod**

```bash

go mod init main

```

- **Entpacken Sie die ZIP-Datei in den Ordner cells-go-cpp in Ihrem Projektverzeichnis.**

 --cells-go-cpp-samples
   -- cells-go-cpp (Ordner)
     -- start_up.go
     -- aspose_cells.go
     -- ......
     -- go.mod
     -- AsposeCellsCWrapper.h
   -- main.go
   -- go.mod

- **Passen Sie Ihre Go `mod` Datei an, um den Ort des Pakets anzugeben:**

   ```go
    module main

    go 1.19

    require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0
    replace github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0  => ./cells-go-cpp
   ```

- **Setzen Sie Ihren PATH, um die gemeinsam genutzten Bibliotheken von Aspose.Cells for Go via C++ in Ihrer aktuellen Befehlszeile zu zeigen. Ersetzen Sie your_version durch die Version von Aspose.Cells for Go via C++, die Sie verwenden.**

```bash

set PATH=%PATH%;%YourProjectPath%/cells-go-cpp-samples/cells-go-cpp/lib/win_x86_64/

```

Oder in Ihrer PowerShell

```powershell

$env:Path = $env:Path+ ";${YourProjectPath}\cells-go-cpp-samples\cells-go-cpp\lib\win_x86_64\"

```

Sie können die DLL-Dateien auch vom oben genannten Pfad in den gleichen Ordner wie Ihre Projekt-Executable kopieren.

- **Führen Sie Ihre erstellte Anwendung aus.**

```bash

go run main.go

```
