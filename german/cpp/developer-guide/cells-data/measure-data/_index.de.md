---
title: Bestimmen der Breite und Höhe des Zellwerts in Pixeln mit C++
linktitle: Messung der Größe
type: docs
weight: 260
url: /de/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Lernen Sie, wie man die Breite und Höhe des Zellwerts in Pixeln mit der API Aspose.Cells for C++ misst.
keywords: Messung der Breite des Zellwerts in Pixel, Messung der Höhe des Zellwerts in Pixel, Holen Sie sich die Breite des Zellwerts in Pixel, Holen Sie sich die Höhe des Zellwerts in Pixel.
---

{{% alert color="primary" %}}

Manchmal müssen Sie die Breite und Höhe des Zellwerts berechnen, um den Zellwert in die Zelle zu passen. Aspose.Cells bietet [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) und [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) Methoden für diesen Zweck. Durch die Verwendung dieser Methoden können Sie die Breite und Höhe des Zellwerts berechnen und dann die Breite der Spalte und die Höhe der Zeile dieser Zelle entsprechend setzen. Dadurch wird der Zellwert dann in die Zelle passt.

Alternativ können Sie auch [AutoAnpassen der Zeilen und Spalten Ihrer Zelle(n) oder Bereichs](/cells/de/cpp/autofit-rows-and-columns/) mit Aspose.Cells APIs verwenden.

{{% /alert %}}

Der folgende Code erläutert die Verwendung der Methoden [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) und [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/).

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

## **Erweiterte Themen**
- [Breite des Zellenwerts abrufen](/cells/de/cpp/get-text-width-of-cell-value/)
