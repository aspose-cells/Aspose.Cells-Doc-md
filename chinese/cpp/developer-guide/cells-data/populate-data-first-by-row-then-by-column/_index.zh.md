---
title: 先按行后按列填充数据，使用C++
linktitle: 首先按行然后按列填充数据
type: docs
weight: 1000
url: /zh/cpp/populate-data-first-by-row-then-by-column/
description: 学习如何先按行后按列填充数据，通过Aspose.Cells for C++ API。
keywords: 通过行而不是列首先填充数据，然后插入数据按行而不是列，添加数据先按行然后按列，高性能数据插入，高性能数据添加
---

{{% alert color="primary" %}} 

通过首先按行然后按列填充电子表格来提高整体性能。

{{% /alert %}} 

将数据放入顺序A1，B1，A2，B2比A1，A2，B1，B2更快。如果工作表中有许多单元格，并且按行填充数据，这个提示可以使程序运行速度更快。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook workbook;

    // Populate Data into Cells
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();
    cells.Get(u"A1").PutValue(U"data1");
    cells.Get(u"B1").PutValue(U"data2");
    cells.Get(u"A2").PutValue(U"data3");
    cells.Get(u"B2").PutValue(U"data4");

    // Save workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
