---
title: Comment installer Aspose.Cells for Go via C++ en utilisant la commande Go.
type: docs
linktitle: Installer via la commande Go
weight: 40
url: /fr/go-cpp/how-to-install-aspose-cells-for-go-via-c++-using-the-go-command
---


## **Comment installer Aspose.Cells for Go via C++ en utilisant la commande Go**

   À partir de Go 1.16, utilisez la commande `go install` directement pour installer le package Aspose.Cells for Go via C++. La commande permet l'installation globale des outils en ligne de commande sans affecter les dépendances existantes du projet.

```go

go install github.com/aspose-cells/aspose-cells-go-cpp/v25@latest

```

   Lorsque vous utilisez la commande `go get` pour installer le package Aspose.Cells for Go via C++, un fichier go.mod doit exister dans le répertoire actuel ou dans un répertoire parent. Voir [l'installation du package Aspose.Cells for Go via C++ et l'exécution de votre code dans votre projet](#Installation-in-your-project)

```go

go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1

```

### Installation du package Aspose.Cells for Go via C++ et exécution de votre code dans votre projet {#Installation-in-your-project}

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
 workbook.Save_String("HELLO.pdf")

}

```

1. Initialisez le projet go.mod

```bash

go mod init main

```

1. Récupérez les dépendances pour votre projet.

```bash

go mod tidy

```

Si Aspose.Cells for Go via C++ n'est pas installé dans l'environnement de développement, Go installera automatiquement le package dans le sous-répertoire `$GOPATH`.

1. Configurez votre PATH pour pointer vers les bibliothèques partagées de Aspose.Cells for Go via C++ dans votre shell de commande actuel. Remplacez your_version par la version de Aspose.Cells for Go via C++ que vous utilisez.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1/lib/linux_x86_64/

```

Ou dans votre powershell

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.1\lib\win_x86_64\"

```

Vous pouvez également copier les fichiers DLL du chemin ci-dessus à l'endroit où se trouve votre exécutable de projet.

1. Exécutez votre application créée.

```bash

go run main.go

```
