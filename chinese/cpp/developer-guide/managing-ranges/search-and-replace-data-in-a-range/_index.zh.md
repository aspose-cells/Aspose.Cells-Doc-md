---
title: 用C++在范围内搜索和替换数据
linktitle: 在 Excel 中使用 C# 代码搜索和替换范围内的数据
type: docs
weight: 170
url: /zh/cpp/search-and-replace-data-in-a-range/
description: 本文演示如何用C++代码在Excel中搜索和替换范围内的数据。
keywords: 用C++在Excel中搜索和替换数据，搜索Excel中的数据，用C++在范围内搜索和替换数据，搜索范围中的数据，用C++搜索范围内的数据，用C++搜索范围中的数据，搜索Excel中的数据，用C++在范围内搜索数据，用C++与C++在范围内搜索和替换数据
---

{{% alert color="primary" %}}

有时你需要在范围内搜索并替换特定数据，而忽略范围外的任何单元格值。Aspose.Cells允许你将搜索限制在特定范围内。本文将对此进行说明。

{{% /alert %}}

Aspose.Cells提供了[**FindOptions::SetRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/setrange/)方法，用于在搜索数据时指定范围。下面的示例演示了如何在范围内搜索和替换数据。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"input.xlsx";

    // Create workbook
    Workbook workbook(filePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Specify the range where you want to search
    // Here the range is E9:H15
    CellArea area = CellArea::CreateCellArea(u"E9", u"H15");

    // Specify Find options
    FindOptions opts;
    opts.SetLookInType(LookInType::Values);
    opts.SetLookAtType(LookAtType::EntireContent);
    opts.SetRange(area);

    Cell cell;
    do
    {
        // Search the cell with value search within range
        cell = worksheet.GetCells().Find(u"search", cell, opts);

        // If no such cell found, then break the loop
        if (!cell)
            break;

        // Replace the cell with value replace
        cell.PutValue(u"replace");

    } while (true);

    // Save the workbook
    U16String outputPath = srcDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
