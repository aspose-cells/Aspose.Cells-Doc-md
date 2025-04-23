---
title: 用C++冻结Excel工作表的第一列
linktitle: 冻结列
type: docs
weight: 190
url: /zh/cpp/how-to-freeze-columns-of-excel-worksheet
description: 在本文中，你将学习如何使用Aspose.Cells API通过C++编程冻结Excel工作表的左侧列。
keywords: 冻结左侧列，冻结首列，锁定列
---

## **介绍**

在本文中，我们将学习如何冻结左列。当您的行中有大量数据时，水平滚动时无法看到左边的列。您可以冻结并锁定第一列，以便在滚动其余数据时仍然可以看到冻结部分。您可以轻松查看左侧列中的标题。

## **Excel中的冻结列**

**![在Excel中冻结左侧列](freeze-columns.png)**

1. 如果您想冻结左列，则首先选择需要冻结的列下面的列。
2. 单击“查看”>“冻结窗格”
3. 在下拉菜单中，点击“冻结首列”。
4. 滚动时，第一列始终显示在左侧视图中。

**![冻结列](frozen-columns.png)**

如您所见，第1列已被冻结，水平滚动时第一列始终锁在视图顶部。

冻结列让您在查看长数据时无需追踪第一列。

## **使用Aspose.Cells for C++冻结列**
使用Aspose.Cells for C++轻松冻结第一列。 
请使用[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)方法在选定的列上冻结列。
1.构建工作簿以打开文件或创建一个空文件。
2. 使用Worksheet.FreezePanes()方法冻结第一列。
3.保存文件。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Freeze.xlsx");

    // Freezing panes at the second column
    workbook.GetWorksheets().Get(0).FreezePanes(u"B1", 0, 1);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

附上[示例源Excel文件](Freeze.xlsx)。
