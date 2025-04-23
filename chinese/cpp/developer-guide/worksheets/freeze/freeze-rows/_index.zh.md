---
title: 使用C++冻结Excel工作表顶部行
linktitle: 冻结行
type: docs
weight: 190
url: /zh/cpp/how-to-freeze-rows-of-excel-worksheet
description: 在本文中，您将学习如何使用Aspose.Cells API的C++库以编程方式冻结Excel工作表的顶部行。
keywords: 冻结顶部行，冻结顶部行。
---

## **介绍**

在本文中，我们将学习如何冻结顶部行。当您的数据在共同标题下时，滚动时无法看到标题。您可以冻结顶部行，以便在滚动其他数据时仍然可以看到冻结部分。您可以轻松在顶部行中查看标题。

## **在Excel中冻结行**

**![在Excel中冻结顶部行](Freeze-Rows.png)**

1. 如果您想冻结顶部行，则首先选择需要冻结的行以下的行。
2. 单击“查看”>“冻结窗格”
3. 在下拉菜单中，单击“冻结顶部行”。
4. 滚动时，第一行始终显示在顶部视图中。

**![冻结行](Frozen-Row.png)**

如您所见，第1行已被冻结，滚动时第一行始终位于顶部。

冻结行让您在查看大量数据时不丢失行标签。

## **使用Aspose.Cells for C++冻结行**
使用Aspose.Cells for C++轻松冻结行。 
请使用[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)方法在选定的行上冻结行。
 1. 构建一个Workbook以打开文件或创建一个空文件。
2. 使用Worksheet.FreezePanes()方法冻结第一行。
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

    // Freezing panes at the cell B2
    workbook.GetWorksheets().Get(0).FreezePanes(u"A2", 1, 0);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

附有[示例源Excel文件](../Freeze.xlsx)。
