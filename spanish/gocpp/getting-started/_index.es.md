---
title: Empezando
type: docs
weight: 10
url: /es/go-cpp/getting-started/
description: Cómo instalar Aspose Cells para Go mediante C++ y crear una aplicación Hello World.
---

{{% alert color="primary" %}}

Esta página te mostrará cómo instalar Aspose Cells para Go vía C++ y crear una aplicación Hola Mundo.

{{% /alert %}}

## Integración Aspose.Cells for Go via C++

¡Bienvenido a Aspose.Cells for Go via C++! Esta solución multiplataforma soporta Windows y Linux. Para comenzar, ejecuta un archivo de código que utilice el paquete.

### Requisitos previos

- [Go (>=1.13)](https://golang.org/doc/install/)
- [Git](https://git-scm.com/downloads)

### Ejecutando Aspose.Cells for Go via C++ en tu proyecto

1. Crea un directorio para tu proyecto y un archivo main.go dentro. Agrega el siguiente código a tu main.go.

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

1. Inicializa el proyecto go.mod

```bash

go mod init main

```

1. Obtén las dependencias del proyecto.

```bash

go mod tidy

```

1. Configura tu PATH para apuntar a las librerías compartidas en Aspose.Cells for Go via C++ en tu consola de comandos actual. Reemplaza your_version con la versión de Aspose.Cells for Go via C++ que estás usando.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.0/lib/linux_x86_64/

```

O en tu PowerShell

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.0\lib\win_x86_64\"

```

También puedes copiar los archivos DLL de la ruta anterior a la misma ubicación que tu ejecutable del proyecto.

1. Ejecuta tu aplicación creada.

```bash

go run main.go

```
