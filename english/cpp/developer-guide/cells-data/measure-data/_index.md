---
title: Measure the Width and Height of the Cell Value in Unit of Pixels with C++
linktitle: Measure the Size
type: docs
weight: 260
url: /cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Learn how to measure the width and height of the cell value in units of pixels through the Aspose.Cells for C++ API.
keywords: Measure the Width of the Cell Value in Unit of Pixels, Measure the Height of the Cell Value in Unit of Pixels, Get the Width of the Cell Value in Unit of Pixels, Get the Height of the Cell Value in Unit of Pixels
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes you need to calculate the width and height of a cell's value to fit it inside the cell. Aspose.Cells provides [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) and [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) methods for this purpose. By using these methods you can calculate the width and height of the cell value and then set the width of the column and the height of the row of that cell, respectively, and this will adjust the cell value to fit inside the cell.

Alternatively, you can also [autofit rows and columns of your cell or range of cells](/cells/cpp/autofit-rows-and-columns/) using Aspose.Cells APIs.

{{% /alert %}}

The following code explains the use of [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) and [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) methods.

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

    // Access cell B2 and add a value inside it
    Cell cell = worksheet.GetCells().Get(u"B2");
    cell.PutValue(u"Welcome to Aspose!");

    // Enlarge its font to size 16
    Style style = cell.GetStyle();
    style.GetFont().SetSize(16);
    cell.SetStyle(style);

    // Calculate the width and height of the cell value in units of pixels
    int32_t widthOfValue = cell.GetWidthOfValue();
    int32_t heightOfValue = cell.GetHeightOfValue();

    // Print both values
    std::wcout << u"Width of Cell Value: " << widthOfValue << std::endl;
    std::wcout << u"Height of Cell Value: " << heightOfValue << std::endl;

    // Set the row height and column width to adjust/fit the cell value inside the cell
    worksheet.GetCells().SetColumnWidthPixel(1, widthOfValue);
    worksheet.GetCells().SetRowHeightPixel(1, heightOfValue);

    // Save the output Excel file
    U16String outFilePath = u"output_out.xlsx";
    workbook.Save(outFilePath);

    Aspose::Cells::Cleanup();
}
```

## **Advanced topics**
- [Get Text Width of Cell Value](/cells/cpp/get-text-width-of-cell-value/)
{{< app/cells/assistant language="cpp" >}}
