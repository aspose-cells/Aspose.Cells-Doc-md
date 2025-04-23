---
title: Medir el ancho y la altura del valor de la celda en unidades de píxeles con C++
linktitle: Medir el tamaño
type: docs
weight: 260
url: /es/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Aprende cómo medir el ancho y la altura del valor de la celda en unidades de píxeles mediante la API Aspose.Cells for C++.
keywords: Medir el ancho del valor de la celda en unidades de píxeles, medir la altura del valor de la celda en unidades de píxeles, obtener el ancho del valor de la celda en unidades de píxeles, obtener la altura del valor de la celda en unidades de píxeles
---

{{% alert color="primary" %}}

A veces necesitas calcular el ancho y la altura del valor de la celda para que encaje dentro de la celda. Aspose.Cells proporciona métodos [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) y [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) para este propósito. Usando estos métodos puedes calcular el ancho y la altura del valor de la celda y luego establecer el ancho de la columna y la altura de la fila de esa celda respectivamente y así ajustar o encajar el valor de la celda dentro de la celda

Alternativamente, también puedes [ajustar automáticamente filas y columnas de tu celda o rango de celdas](/cells/es/cpp/autofit-rows-and-columns/) usando las APIs de Aspose.Cells.

{{% /alert %}}

El siguiente código explica el uso de los métodos [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) y [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell B2 and add some value inside it
    Cell cell = worksheet.GetCells().Get(u"B2");
    cell.PutValue(u"Welcome to Aspose!");

    // Enlarge its font to size 16
    Style style = cell.GetStyle();
    style.GetFont().SetSize(16);
    cell.SetStyle(style);

    // Calculate the width and height of the cell value in unit of pixels
    int32_t widthOfValue = cell.GetWidthOfValue();
    int32_t heightOfValue = cell.GetHeightOfValue();

    // Print both values
    std::wcout << u"Width of Cell Value: " << widthOfValue << std::endl;
    std::wcout << u"Height of Cell Value: " << heightOfValue << std::endl;

    // Set the row height and column width to adjust/fit the cell value inside cell
    worksheet.GetCells().SetColumnWidthPixel(1, widthOfValue);
    worksheet.GetCells().SetRowHeightPixel(1, heightOfValue);

    // Save the output excel file
    U16String outFilePath = u"output_out.xlsx";
    workbook.Save(outFilePath);

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Obtener Ancho de Texto del Valor de la Celda](/cells/es/cpp/get-text-width-of-cell-value/)
