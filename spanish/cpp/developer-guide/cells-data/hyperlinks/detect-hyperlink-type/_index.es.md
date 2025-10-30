---
title: Detectar Tipo de Hiperenlace con C++
linktitle: Detectar tipo de hipervínculo
type: docs
weight: 160
url: /es/cpp/detect-hyperlink-type/
description: Aprende cómo detectar el tipo de hiper enlace a través de la API Aspose.Cells for C++.
keywords: Detectar el tipo de hipervínculo, Obtener el tipo de hipervínculo
---

## **Detectar tipo de hipervínculo**

Un archivo de Excel puede tener diferentes tipos de hipervínculos como externos, referencias de celda, rutas de archivo, etc. Aspose.Cells admite la función para detectar el tipo de hipervínculo. Los tipos de hipervínculos están representados por la enumeración [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/). La enumeración [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) tiene los siguientes miembros.

- Externo: Enlace externo
- RutaArchivo: Ruta local y completa a archivos/carpetas.
- CorreoElectrónico: Correo electrónico
- ReferenciaCelda: Enlace a celda o rango nombrado.

Para verificar el tipo de hipervínculo, la clase [**Hyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/) proporciona una propiedad [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/) con un tipo de retorno de [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/). El siguiente fragmento de código demuestra el uso de la propiedad [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/) utilizando este [archivo de Excel fuente](94896195.xlsx).

### Código Fuente

```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"LinkTypes.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    if (!worksheet)
    {
        std::cerr << "Worksheet not found!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Range range = worksheet.GetCells().CreateRange(u"A1", u"A7");
    if (!range)
    {
        std::cerr << "Range creation failed!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();


    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink link = hyperlinks[i];
        if (link)
        {
            std::cout << link.GetTextToDisplay().ToUtf8() << ": "
                << static_cast<int>(link.GetLinkType()) << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

El siguiente es el resultado generado por el fragmento de código dado anteriormente.

### Salida en Consola
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
{{< app/cells/assistant language="cpp" >}}
