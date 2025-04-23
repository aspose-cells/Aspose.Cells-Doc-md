---
title: Erste Schritte
type: docs
weight: 10
url: /de/go-cpp/getting-started/
description: So installieren Sie Aspose Cells for Go über C++ und erstellen eine Hello World Anwendung.
---

{{% alert color="primary" %}}

Diese Seite zeigt Ihnen, wie Sie Aspose Cells für Go über C++ installieren und eine Hello World-Anwendung erstellen.

{{% /alert %}}

## Aspose.Cells for Go via C++ Integration

Willkommen bei Aspose.Cells for Go via C++! Diese plattformübergreifende Lösung unterstützt sowohl Windows als auch Linux. Um zu beginnen, führen Sie eine Code-Datei aus, die das Paket verwendet.

### Voraussetzungen

- [Go (>=1.13)](https://golang.org/doc/install/)
- [Git](https://git-scm.com/downloads)

### Ausführung von Aspose.Cells for Go via C++ in Ihrem Projekt

1. Erstellen Sie ein Verzeichnis für Ihr Projekt und eine main.go-Datei darin. Fügen Sie den folgenden Code zu Ihrer main.go hinzu.

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

1. Initialisieren Sie project go.mod

```bash

go mod init main

```

1. Holen Sie die Abhängigkeiten für das Projekt.

```bash

go mod tidy

```

1. Setzen Sie Ihren PATH so, dass er auf die gemeinsam genutzten Bibliotheken in Aspose.Cells for Go via C++ in Ihrer aktuellen Befehls-Shell verweist. Ersetzen Sie your_version durch die Version von Aspose.Cells for Go via C++, die Sie verwenden.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.0/lib/linux_x86_64/

```

Oder in Ihrer PowerShell

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.0\lib\win_x86_64\"

```

Sie können die DLL-Dateien auch vom oben genannten Pfad in den gleichen Ordner wie Ihre Projekt-Executable kopieren.

1. Führen Sie Ihre erstellte Anwendung aus.

```bash

go run main.go

```
