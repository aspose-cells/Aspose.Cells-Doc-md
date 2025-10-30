---
title: Renderizar caracteres suplementarios Unicode en PDF de salida con C++ por Aspose.Cells
linktitle: Renderizar caracteres suplementarios Unicode
type: docs
weight: 350
url: /es/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Aprende cómo renderizar caracteres suplementarios Unicode en PDF de salida usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Los caracteres Unicode normales tienen una longitud de 2 bytes, mientra que los caracteres Unicode suplementarios tienen una longitud de 4 bytes. Ahora, Aspose.Cells admite la renderización de estos caracteres Unicode de 4 bytes.

En el Estándar de Caracteres Unicode, los Caracteres Suplementarios son los caracteres asignados a puntos de código desde U+10000 hasta U+10FFFF. En otras palabras, estos son los caracteres Unicode mayores que U+FFFF.

- En UTF-8 estos caracteres tienen cada uno una longitud de 4 bytes.
- En UTF-16 estos caracteres requieren 2 sustitutos (unidades de 16 bits).

{{% /alert %}}

## Renderizar caracteres suplementarios Unicode en el PDF de salida por Aspose.Cells

La siguiente captura de pantalla muestra cómo Aspose.Cells renderizó el [archivo de Excel fuente](5115563.xlsx) en el [PDF de salida](5115564.pdf). Como puede ver, se han renderizado exactamente los tres caracteres Unicode suplementarios como lo hizo Microsoft Excel.

![todo:image_alt_text](output.png)

## Código de Muestra

Puede usar este código de ejemplo para convertir [archivo de Excel fuente](5115563.xlsx) en [PDF de salida](5115564.pdf).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"unicode-supplementary-characters.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"RenderUnicodeInOutput_out.pdf";

    // Load the source excel file containing Unicode Supplementary characters
    Workbook wb(inputFilePath);

    // Save the workbook as PDF
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully with Unicode Supplementary characters!" << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
