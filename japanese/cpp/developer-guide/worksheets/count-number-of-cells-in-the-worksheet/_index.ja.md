---
title: C++ でワークシート内のセル数をカウント
linktitle: ワークシート内のセル数を数える
type: docs
weight: 110
url: /ja/cpp/count-number-of-cells-in-the-worksheet/
description: この記事では、Aspose.Cells の C++ API を使用してプログラム的にExcelワークシートのセル数をカウントする方法を学びます。
keywords: Excelワークシートのセル数をカウント（C++、ExcelセルカウントC++）
---

以下のコード例に示すように、[**Cells.GetCount()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcount/)または[**Cells.GetCountLarge()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getcountlarge/)プロパティを使用してワークシート内のセル数をカウントすることができます。

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
