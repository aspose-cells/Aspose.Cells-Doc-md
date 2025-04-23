---
title: Iniziare
type: docs
weight: 10
url: /it/go-cpp/getting-started/
description: Come installare Aspose Cells per Go tramite C++ e creare un applicazione Hello World.
---

{{% alert color="primary" %}}

Questa pagina ti mostrerà come installare Aspose Cells per Go tramite C++ e creare un'app Hello World.

{{% /alert %}}

## Integrazione Aspose.Cells for Go via C++

Benvenuto in Aspose.Cells for Go via C++! Questa soluzione multipiattaforma supporta sia Windows che Linux. Per iniziare, esegui un file di codice che utilizza il pacchetto.

### Prerequisiti

- [Go (>=1.13)](https://golang.org/doc/install/)
- [Git](https://git-scm.com/downloads)

### Eseguire Aspose.Cells for Go via C++ nel tuo progetto

1. Crea una directory per il tuo progetto e un file main.go al suo interno. Aggiungi il seguente codice al tuo main.go.

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

1. Inizializza go.mod del progetto

```bash

go mod init main

```

1. Ottieni le dipendenze del progetto.

```bash

go mod tidy

```

1. Imposta il tuo PATH per puntare alle librerie condivise di Aspose.Cells for Go via C++ nel tuo attuale shell di comando. Sostituisci your_version con la versione di Aspose.Cells for Go via C++ che stai eseguendo.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.0/lib/linux_x86_64/

```

Oppure in Powershell

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.0\lib\win_x86_64\"

```

Puoi anche copiare i file DLL dal percorso sopra nel stesso luogo esecutivo del tuo progetto.

1. Esegui la tua applicazione creata.

```bash

go run main.go

```
