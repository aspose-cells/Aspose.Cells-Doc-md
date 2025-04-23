---
title: 用 C++ 测量单元格值的宽度和高度（以像素为单位）
linktitle: 测量大小。
type: docs
weight: 260
url: /zh/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: 学习如何通过Aspose.Cells for C++ API测量单元格值的宽度和高度（像素单位）。
keywords: 测量单元格值的宽度（像素单位），测量单元格值的高度（像素单位），获取单元格值的宽度（像素单位），获取单元格值的高度（像素单位）
---

{{% alert color="primary" %}}

有时候您需要计算单元格值的宽度和高度，以使单元格值适合单元格内。Aspose.Cells 为此目的提供了 [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) 和 [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) 方法。通过使用这些方法，您可以计算单元格值的宽度和高度，然后分别设置该单元格的列宽和行高，从而调整或使单元格值适合单元格内。

另外，你还可以使用Aspose.Cells API[自动调整行高和列宽](/cells/zh/cpp/autofit-rows-and-columns/)。

{{% /alert %}}

以下代码解释了 [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) 和 [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) 方法的使用。

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

## **高级主题**
- [获取单元值的文本宽度](/cells/zh/cpp/get-text-width-of-cell-value/)
