---
title: Wie man Aspose.Cells for Go via C++ mit dem Go Befehl installiert.
type: docs
linktitle: Installation über den Go Befehl
weight: 40
url: /de/go-cpp/how-to-install-aspose-cells-for-go-via-c++-using-the-go-command
---


## **Wie man Aspose.Cells for Go via C++ mit dem Go-Befehl installiert**

   Ab Go 1.16 verwendest du den Befehl `go install` direkt, um das Paket Aspose.Cells for Go via C++ zu installieren. Der Befehl ermöglicht die globale Installation von Kommandozeilentools, ohne sich Sorgen machen zu müssen, bestehende Projektabhängigkeiten zu beeinträchtigen.

```go

go install github.com/aspose-cells/aspose-cells-go-cpp/v25@latest

```

   Wenn du den Befehl `go get` verwendest, um das Paket Aspose.Cells for Go via C++ zu installieren, muss die Datei go.mod im aktuellen Verzeichnis oder in einem der übergeordneten Verzeichnisse vorhanden sein. siehe [Installation des Aspose.Cells for Go via C++-Pakets und Ausführung deines Codes in deinem Projekt](#Installation-in deinem Projekt)

```go

go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1

```

### Installation des Aspose.Cells for Go via C++-Pakets und Ausführung deines Codes in deinem Projekt {#Installation-in-deinem-Projekt}

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
 workbook.Save_String("HELLO.pdf")

}

```

1. Initialisieren Sie project go.mod

```bash

go mod init main

```

1. Hole die Abhängigkeiten für dein Projekt.

```bash

go mod tidy

```

Wenn Aspose.Cells for Go via C++ nicht in der Entwicklungsumgebung installiert ist, installiert Go das Paket automatisch im Unterverzeichnis `$GOPATH`.

1. Setzen Sie Ihren PATH so, dass er auf die gemeinsam genutzten Bibliotheken in Aspose.Cells for Go via C++ in Ihrer aktuellen Befehls-Shell verweist. Ersetzen Sie your_version durch die Version von Aspose.Cells for Go via C++, die Sie verwenden.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1/lib/linux_x86_64/

```

Oder in Ihrer PowerShell

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.1\lib\win_x86_64\"

```

Sie können die DLL-Dateien auch vom oben genannten Pfad in den gleichen Ordner wie Ihre Projekt-Executable kopieren.

1. Führen Sie Ihre erstellte Anwendung aus.

```bash

go run main.go

```
