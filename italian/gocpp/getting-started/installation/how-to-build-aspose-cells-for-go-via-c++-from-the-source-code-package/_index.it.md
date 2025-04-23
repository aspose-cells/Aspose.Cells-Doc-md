---
title: Come creare Aspose.Cells for Go via C++ dal pacchetto di codice sorgente.
type: docs
linktitle: Compila dal codice sorgente
weight: 50
url: /it/go-cpp/how-to-build-aspose-cells-for-go-via-c++-from-the-source-code-package
---


## **Come compilare Aspose.Cells for Go via C++ dal pacchetto di codice sorgente**

### 1. Scarica il pacchetto sorgente Aspose.Cells for Go via C++

- **Puoi scaricare il pacchetto del codice sorgente da due posizioni:**

1. Scarica il pacchetto del codice sorgente dalla [pagina di download Aspose.Cells for Go via C++](https://downloads.aspose.com/cells/go-cpp/).  
1. Scarica il pacchetto del codice sorgente dal [ repository GitHub](https://github.com/aspose-cells/aspose-cells-go-cpp) o direttamente tramite [Pacchetto archivio GitHub](https://github.com/aspose-cells/aspose-cells-go-cpp/archive/refs/heads/main.zip).  

### 2. Come installare il pacchetto Aspose.Cells for Go via C++ nel tuo progetto

- **Crea una directory per il tuo progetto e un file main.go al suo interno. Aggiungi il seguente codice a main.go.**

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

- **Inizializza il progetto go.mod**

```bash

go mod init main

```

- **Estrai il file ZIP nella cartella cells-go-cpp nella directory del tuo progetto.**

 --cells-go-cpp-samples
   -- cells-go-cpp ( cartella)
     -- start_up.go
     -- aspose_cells.go
     -- ......
     -- go.mod
     -- AsposeCellsCWrapper.h
   -- main.go
   -- go.mod

- **Modifica il file `go` del tuo progetto per specificare la posizione del pacchetto:**

   ```go
    module main

    go 1.19

    require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0
    replace github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0  => ./cells-go-cpp
   ```

- **Imposta il tuo PATH per puntare alle librerie condivise in Aspose.Cells for Go via C++ nel tuo attuale shell dei comandi. Sostituisci your_version con la versione di Aspose.Cells for Go via C++ in esecuzione.**

```bash

set PATH=%PATH%;%YourProjectPath%/cells-go-cpp-samples/cells-go-cpp/lib/win_x86_64/

```

Oppure in Powershell

```powershell

$env:Path = $env:Path+ ";${YourProjectPath}\cells-go-cpp-samples\cells-go-cpp\lib\win_x86_64\"

```

Puoi anche copiare i file DLL dal percorso sopra nel stesso luogo esecutivo del tuo progetto.

- **Esegui l'applicazione creata.**

```bash

go run main.go

```
