---
title: Encontrar celdas con estilo específico con C++
linktitle: Encontrar Celdas con Estilo Específico
type: docs
weight: 190
url: /es/cpp/find-cells-with-specific-style/
description: Aprende cómo encontrar o buscar celdas con un estilo particular aplicado mediante la API Aspose.Cells for C++.
keywords: Encontrar celdas con un estilo particular aplicado, Buscar celdas con un estilo particular aplicado
---

{{% alert color="primary" %}}

A veces, necesitas encontrar celdas con un estilo particular aplicado. Puedes usar Aspose.Cells para encontrar todas las celdas con un estilo común. Aspose.Cells proporciona la propiedad [**FindOptions.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/getstyle/) que puedes usar para especificar el estilo por el que buscar celdas.

{{% /alert %}}

El código de este ejemplo encuentra todas las celdas que tienen el mismo estilo que la celda A1. Después de que se haya ejecutado el código, todas las celdas que tienen el mismo estilo que A1 contienen el texto "Encontrado".

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"TestBook.xlsx";

    Workbook workbook(filePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    FindOptions options;
    options.SetStyle(style);

    Cell nextCell;

    do
    {
        nextCell = worksheet.GetCells().Find(U16String(), nextCell, options);
        if (nextCell.GetRow() == -1)
            break;
        nextCell.PutValue(u"Found");
    } while (true);

    U16String outputPath = outDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
