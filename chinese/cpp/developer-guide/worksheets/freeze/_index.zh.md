---
title: 用C++冻结Excel工作表的窗格
linktitle: 冻结窗格
type: docs
weight: 190
url: /zh/cpp/how-to-freeze-panes-of-excel-worksheet
description: 在本文中，你将学习如何使用Aspose.Cells的C++库程序化冻结Excel工作表的窗格。
keywords: 冻结窗格，冻结窗口。
---

## **介绍**

 本文介绍如何冻结窗格。当你有大量数据在共同标题下时，滚动后无法看到标题行，且每条记录包含许多数据。通过冻结窗格，可以在滚动时仍然看到冻结的部分。你可以方便地看到顶部行或首列的标题。冻结和取消冻结窗格只会改变数据的视图，不会改变数据本身。

## **在Excel中**

**![Excel中的冻结窗格](Freeze-panes.png)**

 1. 若要冻结窗格、冻结行列，先选中一个单元格（如B2）。
2. 单击“查看”>“冻结窗格”
3. 在下拉菜单上，单击“冻结窗格”
 4. 向下或向右滚动时，第一行和第一列会被冻结。

**![冻结窗格](Frozen-Panes.png)**

 如图所示，第一行和A列已冻结，第二行是32，第二个可见列是D。

冻结窗格允许你浏览大量数据而无需跟踪行或列标签。

## ** 使用Aspose.Cells for C++冻结窗格**
 使用Aspose.Cells for C++冻结窗格非常简单。请使用[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)方法在所选单元格处冻结窗格。
 1. 构建一个Workbook以打开文件或创建一个空文件。
 2. 使用Worksheet.FreezePanes()方法冻结窗格。
3.保存文件。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Freeze.xlsx");
    Workbook workbook(inputFilePath);

    // Freeze panes at the cell B2
    WorksheetCollection sheets = workbook.GetWorksheets();
    sheets.Get(0).FreezePanes(u"B2", 1, 1);

    // Save the file
    U16String outputFilePath(u"frozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

附上[示例源Excel文件](Freeze.xlsx)。
{{< app/cells/assistant language="cpp" >}}
