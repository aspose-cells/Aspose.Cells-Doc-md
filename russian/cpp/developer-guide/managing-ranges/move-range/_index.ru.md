---
title: Перемещение диапазона ячеек в листе с C++
linktitle: Перемещение диапазона ячеек на листе
type: docs
weight: 370
url: /ru/cpp/move-range-of-cells-in-a-worksheet/
description: Узнайте, как переместить диапазон ячеек в листе, используя Aspose.Cells и C++.
---

{{% alert color="primary" %}}

В этой статье показано, как перемещать диапазон ячеек на листе.

{{% /alert %}}

## **Перемещение диапазона ячеек на листе**
В примере кода используется файл-шаблон для демонстрации задачи.

**Входной файл**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)

Пожалуйста, ознакомьтесь с созданным файлом с перемещением диапазона A1:B5 в C1:D5.

**Выходной файл**

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
