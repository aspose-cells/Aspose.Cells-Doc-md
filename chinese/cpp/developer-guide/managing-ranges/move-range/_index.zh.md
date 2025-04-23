---
title: 用C++在工作表中移动单元格范围
linktitle: 移动工作表中的单元格范围
type: docs
weight: 370
url: /zh/cpp/move-range-of-cells-in-a-worksheet/
description: 学习如何使用Aspose.Cells和C++在工作表中移动单元格范围。
---

{{% alert color="primary" %}}

本文介绍了如何移动工作表中的单元格范围。

{{% /alert %}}

## **在工作表中移动单元格范围**
示例代码使用模板文件演示了该任务。

**输入文件**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)

请参阅以下生成的文件，范围 A1:B5 移动到 C1:D5。

**输出文件**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the workbook object. Open the Excel file
    U16String inputFilePath = u"book1.xlsx";
    Workbook workbook(inputFilePath);

    // Access the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create a range from A1 to B5
    Range range = cells.CreateRange(u"A1", u"B5");

    // Move the range to the right by 2 columns
    range.MoveTo(0, 2);

    Aspose::Cells::Cleanup();
}
```
