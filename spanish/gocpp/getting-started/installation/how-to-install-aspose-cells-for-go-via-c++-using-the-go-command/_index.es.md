---
title: Cómo instalar Aspose.Cells for Go via C++ usando el comando Go.
type: docs
linktitle: Instalar vía comando Go
weight: 40
url: /es/go-cpp/how-to-install-aspose-cells-for-go-via-c++-using-the-go-command
---


## **Cómo instalar Aspose.Cells for Go via C++ usando el comando Go**

   Desde Go 1.16, puedes usar el comando `go install` directamente para instalar el paquete Aspose.Cells for Go via C++. El comando permite la instalación global de herramientas de línea de comandos sin preocuparse por afectar las dependencias existentes del proyecto.

```go

go install github.com/aspose-cells/aspose-cells-go-cpp/v25@latest

```

   Cuando usas `go get` para instalar el paquete Aspose.Cells for Go via C++, debe existir el archivo go.mod en el directorio actual o en cualquier directorio superior. Consulta [instalación del paquete Aspose.Cells for Go via C++ y ejecución de tu código en tu proyecto](#Installation-in-your-project)

```go

go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1

```

### Instalación del paquete Aspose.Cells for Go via C++ y ejecución de tu código en tu proyecto {#Installation-in-your-project}

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
 workbook.Save_String("HELLO.pdf")

}

```

1. Inicializa el proyecto go.mod

```bash

go mod init main

```

1. Obtén las dependencias de tu proyecto.

```bash

go mod tidy

```

Si Aspose.Cells for Go via C++ no está instalado en el entorno de desarrollo, Go instalará automáticamente el paquete en el subdirectorio `$GOPATH`.

1. Configura tu PATH para apuntar a las librerías compartidas en Aspose.Cells for Go via C++ en tu consola de comandos actual. Reemplaza your_version con la versión de Aspose.Cells for Go via C++ que estás usando.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1/lib/linux_x86_64/

```

O en tu PowerShell

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.1\lib\win_x86_64\"

```

También puedes copiar los archivos DLL de la ruta anterior a la misma ubicación que tu ejecutable del proyecto.

1. Ejecuta tu aplicación creada.

```bash

go run main.go

```
