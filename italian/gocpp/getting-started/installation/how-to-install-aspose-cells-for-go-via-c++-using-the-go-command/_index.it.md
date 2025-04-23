---
title: Come installare Aspose.Cells for Go via C++ usando il comando Go.
type: docs
linktitle: Installazione tramite comando Go
weight: 40
url: /it/go-cpp/how-to-install-aspose-cells-for-go-via-c++-using-the-go-command
---


## **Come installare Aspose.Cells for Go via C++ usando il comando Go**

   Da Go 1.16, puoi usare il comando `go install` direttamente per installare il pacchetto Aspose.Cells for Go via C++. Il comando permette di installare globalmente gli strumenti da riga di comando senza preoccuparti di influire sulle dipendenze dei progetti esistenti.

```go

go install github.com/aspose-cells/aspose-cells-go-cpp/v25@latest

```

   Quando usi il comando `go get` per installare il pacchetto Aspose.Cells for Go via C++, il file go.mod deve esistere nella directory corrente o in qualsiasi directory superiore. vedi [installazione del pacchetto Aspose.Cells for Go via C++ e esecuzione del tuo codice nel tuo progetto](#Installation-in-your-project)

```go

go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1

```

### Installazione del pacchetto Aspose.Cells for Go via C++ ed esecuzione del tuo codice nel progetto {#Installation-in-your-project}

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
 workbook.Save_String("HELLO.pdf")

}

```

1. Inizializza go.mod del progetto

```bash

go mod init main

```

1. Scarica le dipendenze per il tuo progetto.

```bash

go mod tidy

```

Se Aspose.Cells for Go via C++ non è installato nell'ambiente di sviluppo, Go installerà automaticamente il pacchetto nella sottocartella `$GOPATH`.

1. Imposta il tuo PATH per puntare alle librerie condivise di Aspose.Cells for Go via C++ nel tuo attuale shell di comando. Sostituisci your_version con la versione di Aspose.Cells for Go via C++ che stai eseguendo.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1/lib/linux_x86_64/

```

Oppure in Powershell

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.1\lib\win_x86_64\"

```

Puoi anche copiare i file DLL dal percorso sopra nel stesso luogo esecutivo del tuo progetto.

1. Esegui la tua applicazione creata.

```bash

go run main.go

```
