---
title: Mät cellvärdets bredd och höjd i pixelenhet med C++
linktitle: Mäta storleken
type: docs
weight: 260
url: /sv/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Lär dig hur du mäter cellvärdets bredd och höjd i pixelenhet via API et Aspose.Cells for C++.
keywords: Mät bredden på cellvärdet i pixlars enhet, Mät höjden på cellvärdet i pixlars enhet, Hämta bredden på cellvärdet i pixlars enhet, Hämta höjden på cellvärdet i pixlars enhet
---

{{% alert color="primary" %}}

Ibland behöver du beräkna bredden och höjden på cellvärdet för att passa cellvärdet inuti cellen. Aspose.Cells tillhandahåller [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) och [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) metoder för detta ändamål. Genom att använda dessa metoder kan du beräkna bredden och höjden på cellvärdet och sedan ställa in bredden på kolumnen och höjden på raden för den cellen respektive och detta kommer sedan att justera eller passa cellvärdet inuti cellen.

Alternativt kan du också [autofit rader och kolumner för din cell eller cellområde](/cells/sv/cpp/autofit-rows-and-columns/) med Aspose.Cells API:er.

{{% /alert %}}

Följande kod förklarar användningen av [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) och [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) metoder.

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

## **Fortsatta ämnen**
- [Få textens bredd av cellvärdet](/cells/sv/cpp/get-text-width-of-cell-value/)
