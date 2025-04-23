---
title: Cómo construir Aspose.Cells for Go via C++ desde el paquete de código fuente.
type: docs
linktitle: Construir desde código fuente
weight: 50
url: /es/go-cpp/how-to-build-aspose-cells-for-go-via-c++-from-the-source-code-package
---


## **Cómo construir Aspose.Cells for Go via C++ desde el paquete de código fuente**

### 1. Descargar paquete fuente Aspose.Cells for Go via C++

- **Puedes descargar el paquete de código fuente desde dos ubicaciones:**

1. Descarga el paquete de código fuente desde la [página de descarga Aspose.Cells for Go via C++](https://downloads.aspose.com/cells/go-cpp/).  
1. Descarga el paquete de código fuente desde el [repositorio de GitHub](https://github.com/aspose-cells/aspose-cells-go-cpp) o directamente vía [Archivo de paquete de GitHub](https://github.com/aspose-cells/aspose-cells-go-cpp/archive/refs/heads/main.zip).  

### 2. Cómo instalar el paquete Aspose.Cells for Go via C++ en tu proyecto

- **Crea un directorio para tu proyecto y un archivo main.go dentro. Agrega el siguiente código a tu main.go.**

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

- **Inicializa el proyecto go.mod**

```bash

go mod init main

```

- **Extrae el archivo ZIP a la carpeta cells-go-cpp en tu directorio de proyecto.**

 --cells-go-cpp-muestras
   -- cells-go-cpp (carpeta)
     -- start_up.go
     -- aspose_cells.go
     -- ......
     -- go.mod
     -- AsposeCellsCWrapper.h
   -- main.go
   -- go.mod

- **Modifica tu archivo `go` para especificar la ubicación del paquete:**

   ```go
    module main

    go 1.19

    require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0
    replace github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0  => ./cells-go-cpp
   ```

- **Configura tu PATH para apuntar a las librerías compartidas en Aspose.Cells for Go via C++ en tu consola de comandos actual. Reemplaza your_version con la versión de Aspose.Cells for Go via C++ que estás usando.**

```bash

set PATH=%PATH%;%YourProjectPath%/cells-go-cpp-samples/cells-go-cpp/lib/win_x86_64/

```

O en tu PowerShell

```powershell

$env:Path = $env:Path+ ";${YourProjectPath}\cells-go-cpp-samples\cells-go-cpp\lib\win_x86_64\"

```

También puedes copiar los archivos DLL de la ruta anterior a la misma ubicación que tu ejecutable del proyecto.

- **Ejecuta tu aplicación creada.**

```bash

go run main.go

```
