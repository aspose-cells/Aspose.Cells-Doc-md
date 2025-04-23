---
title: Pour commencer
type: docs
weight: 10
url: /fr/go-cpp/getting-started/
description: Comment installer Aspose Cells pour Go via C++ et créer une application Hello World.
---

{{% alert color="primary" %}}

Cette page vous montrera comment installer Aspose Cells pour Go via C++ et créer une application Hello World.

{{% /alert %}}

## Intégration Aspose.Cells for Go via C++

Bienvenue à Aspose.Cells for Go via C++ ! Cette solution multiplateforme prend en charge Windows et Linux. Pour commencer, exécutez un fichier code utilisant le package.

### Prérequis

- [Go (>=1.13)](https://golang.org/doc/install/)
- [Git](https://git-scm.com/downloads)

### Exécution de Aspose.Cells for Go via C++ dans votre projet

1. Créez un répertoire pour votre projet et un fichier main.go. Ajoutez le code suivant à votre main.go.

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

1. Initialisez le projet go.mod

```bash

go mod init main

```

1. Récupérez les dépendances du projet.

```bash

go mod tidy

```

1. Configurez votre PATH pour pointer vers les bibliothèques partagées de Aspose.Cells for Go via C++ dans votre shell de commande actuel. Remplacez your_version par la version de Aspose.Cells for Go via C++ que vous utilisez.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.0/lib/linux_x86_64/

```

Ou dans votre powershell

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.0\lib\win_x86_64\"

```

Vous pouvez également copier les fichiers DLL du chemin ci-dessus à l'endroit où se trouve votre exécutable de projet.

1. Exécutez votre application créée.

```bash

go run main.go

```
