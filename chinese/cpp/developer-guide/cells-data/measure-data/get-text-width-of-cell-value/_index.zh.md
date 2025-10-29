---
title: 使用C++获取单元格值的文本宽度
linktitle: 获取单元值的文本宽度
type: docs
weight: 50
url: /zh/cpp/get-text-width-of-cell-value/
description: 通过Aspose.Cells for C++ API学习如何获取单元格值的文本宽度。
keywords: 获取单元格值的文本宽度，获得单元格值的文本宽度
---

## **获取单元值的文本宽度**

 有时，开发者可能需要计算单元格值的宽度以进行布局安排。Aspose.Cells提供了[**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/)方法，允许开发者获取单元格值的文本宽度。下列示例展示如何使用[**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/)访问单元格值的文本宽度。

以下代码片段中使用的源文件，请参考附件。

[源文件](96928090.xlsx)

## 示例代码

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory path for source files
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook from the specified Excel file
    Workbook workbook(sourceDir + u"GetTextWidthSample.xlsx");

    // Calculate the text width for the string value of cell A1
    double textWidth = CellsHelper::GetTextWidth(workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue(), workbook.GetDefaultStyle().GetFont(), 1);

    // Output the text width
    std::wcout << u"Text width: " << textWidth << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
