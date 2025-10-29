---
title: 用 C++ 取消冻结 Excel 工作表的行或列
linktitle: 取消冻结窗格
type: docs
weight: 190
url: /zh/cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: 在本文中，您将学习如何使用 Aspose.Cells for C++ API 以编程方式取消冻结 Excel 工作表的行、列或窗格。
keywords: 取消冻结窗格、取消冻结行、取消冻结列、取消冻结窗口。
---

## **介绍**

在本文中，我们将学习如何在 Excel 工作表中取消冻结行、列和窗格。如果工作表被冻结，有时我们希望取消冻结或调整冻结的行、列或窗格。

## **在Excel中**

1. 点击 **视图** 标签 > **冻结窗格** > **取消冻结窗格**。

**![在Excel中取消冻结窗格](Unfreeze-Panes.png)**

## **使用 Aspose.Cells for C++ 取消冻结行、列或窗格**
使用 Aspose.Cells for C++ 非常简单。调用 [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unfreezepanes/) 方法取消冻结窗格。

1. 构建一个 `Workbook` 对象以打开冻结的文件。
2. 使用 `Worksheet.UnFreezePanes()` 方法取消冻结窗格。
3.保存文件。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Frozen.xlsx");
    Workbook workbook(inputFilePath);

    // Unfreeze panes in the first worksheet
    workbook.GetWorksheets().Get(0).UnFreezePanes();

    // Save the modified workbook
    U16String outputFilePath(u"Unfrozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes unfrozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

附有【示例源Excel文件】(Frozen.xlsx)。
{{< app/cells/assistant language="cpp" >}}
