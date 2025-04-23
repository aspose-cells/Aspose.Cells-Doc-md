---
title: Copiar alturas de filas del rango fuente al rango destino con C++
linktitle: Copiar alturas de fila del rango de origen al rango de destino
type: docs
weight: 590
url: /es/cpp/copy-row-heights-of-source-range-to-destination-range/
description: Aprende cómo copiar alturas de fila de un rango fuente a un rango destino usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A veces, los usuarios necesitan copiar alturas de filas de un rango fuente a un rango destino. Aspose.Cells proporciona el enumerado [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) para este propósito. Cuando configures la propiedad [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) con el enumerado [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/), las alturas de todas las filas dentro del rango fuente serán copiadas al rango destino.

{{% /alert %}}

El siguiente código de ejemplo explica cómo usar el enumerado [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) para copiar alturas de filas de un rango fuente a un rango destino. Una vez que abras el archivo Excel generado en Microsoft Excel, verás que las alturas de fila del rango destino son exactamente iguales a las del rango fuente.

```cpp
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

    // Create workbook object
    Workbook workbook;

    // Source worksheet
    Worksheet srcSheet = workbook.GetWorksheets().Get(0);

    // Add destination worksheet
    Worksheet dstSheet = workbook.GetWorksheets().Add(u"Destination Sheet");

    // Set the row height of the 4th row. This row height will be copied to destination range
    srcSheet.GetCells().SetRowHeight(3, 50);

    // Create source range to be copied
    Range srcRange = srcSheet.GetCells().CreateRange(u"A1:D10");

    // Create destination range in destination worksheet
    Range dstRange = dstSheet.GetCells().CreateRange(u"A1:D10");

    // PasteOptions, we want to copy row heights of source range to destination range
    PasteOptions opts;
    opts.SetPasteType(PasteType::RowHeights);

    // Copy source range to destination range with paste options
    dstRange.Copy(srcRange, opts);

    // Write informative message in cell D4 of destination worksheet
    dstSheet.GetCells().Get(u"D4").PutValue(u"Row heights of source range copied to destination range");

    // Save the workbook in xlsx format
    workbook.Save(outDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Row heights copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
