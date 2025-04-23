---
title: Comment construire Aspose.Cells for Go via C++ à partir du package de code source.
type: docs
linktitle: Construire à partir du code source
weight: 50
url: /fr/go-cpp/how-to-build-aspose-cells-for-go-via-c++-from-the-source-code-package
---


## **Comment construire Aspose.Cells for Go via C++ à partir du package de code source**

### 1. Télécharger le package source Aspose.Cells for Go via C++

- **Vous pouvez télécharger le package de code source depuis deux emplacements :**

1. Télécharger le package de code source depuis la [page de téléchargement Aspose.Cells for Go via C++](https://downloads.aspose.com/cells/go-cpp/).  
1. Télécharger le package de code source depuis le [dépôt GitHub](https://github.com/aspose-cells/aspose-cells-go-cpp) ou directement via [GitHub Archive Package](https://github.com/aspose-cells/aspose-cells-go-cpp/archive/refs/heads/main.zip).  

### 2. Comment installer le package Aspose.Cells for Go via C++ dans votre projet

- **Créez un répertoire pour votre projet et un fichier main.go à l'intérieur. Ajoutez le code suivant dans votre main.go.**

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

- **Initialisez le fichier go.mod de votre projet**

```bash

go mod init main

```

- **Extrayez le fichier ZIP dans le dossier cells-go-cpp dans votre répertoire de projet.**

 --cells-go-cpp-exemples
   -- dossier cells-go-cpp
     -- start_up.go
     -- aspose_cells.go
     -- ......
     -- go.mod
     -- AsposeCellsCWrapper.h
   -- main.go
   -- go.mod

- **Modifiez votre fichier Go `mod` pour indiquer l'emplacement du package :**

   ```go
    module main

    go 1.19

    require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0
    replace github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0  => ./cells-go-cpp
   ```

- **Configurez votre PATH pour pointer vers les bibliothèques partagées dans Aspose.Cells for Go via C++ dans votre session de commande actuelle. Remplacez your_version par la version de Aspose.Cells for Go via C++ que vous utilisez.**

```bash

set PATH=%PATH%;%YourProjectPath%/cells-go-cpp-samples/cells-go-cpp/lib/win_x86_64/

```

Ou dans votre powershell

```powershell

$env:Path = $env:Path+ ";${YourProjectPath}\cells-go-cpp-samples\cells-go-cpp\lib\win_x86_64\"

```

Vous pouvez également copier les fichiers DLL du chemin ci-dessus à l'endroit où se trouve votre exécutable de projet.

- **Exécutez votre application créée.**

```bash

go run main.go

```
