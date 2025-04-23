---
title: 使用C++对Excel文件的自动填充范围
linktitle: 自动填充范围
type: docs
weight: 105
url: /zh/cpp/autofill-ranges/
description: 学习如何使用Aspose.Cells与C++对Excel文件中的指定范围执行自动填充操作。
---

## **在Excel中对指定范围执行自动填充**

在Excel中，选择范围，将鼠标移动到右下角，然后拖动“+”以自动填充数据。

## **使用Aspose.Cells自动填充范围**

以下示例展示了如何在范围内执行AutoFill操作。这里提供了测试这个功能的示例文件：

[range_autofill.xlsx](range_autofill.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"range_autofill.xlsx");

    // Get Cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create Range
    Range src = cells.CreateRange(u"C3:C4");
    Range dest = cells.CreateRange(u"C5:C10");

    // AutoFill
    src.AutoFill(dest, AutoFillType::Series);

    // Save the Workbook
    workbook.Save(u"range_autofill_result.xlsx");

    std::cout << "Range auto-filled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
