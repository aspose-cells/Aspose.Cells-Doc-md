---
title: 使用C++统计工作表中的单元格数量
linktitle: 计算工作表中单元格的数量
type: docs
weight: 110
url: /zh/cpp/count-number-of-cells-in-the-worksheet/
description: 在本文中，你将学习如何使用Aspose.Cells的C++ API编程统计Excel工作表中的单元格数目。
keywords: 统计Excel工作表中的单元格数 C++，Excel工作表单元格C++
---

您可以使用下面给出的代码示例中所示的[**Cells.GetCount()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcount/)或[**Cells.GetCountLarge()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcountlarge/)属性来计算工作表中的单元格数量。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    Workbook workbook(sourceDir + u"BookWithSomeData.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print number of cells in the Worksheet
    std::cout << "Number of Cells: " << worksheet.GetCells().GetCount() << std::endl;

    // In case the number of cells is greater than 2147483647, use CountLarge
    std::cout << "Number of Cells (CountLarge): " << worksheet.GetCells().GetCountLarge() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
