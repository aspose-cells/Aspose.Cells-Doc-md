---
title: Получить ширину текста значения ячейки с помощью C++
linktitle: Получить ширину текста значения ячейки
type: docs
weight: 50
url: /ru/cpp/get-text-width-of-cell-value/
description: Узнайте, как получать ширину текста значения ячейки через API Aspose.Cells for C++.
keywords: Получить ширину текста значения ячейки, Получить ширину текста значения ячейки
---

## **Получить ширину текста значения ячейки**

Иногда разработчикам понадобится вычислить ширину значения ячейки для размещения данных в определенной раскладке. Aspose.Cells предоставляет метод [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/), который позволяет разработчикам получать ширину текста значения ячейки. Следующий пример кода иллюстрирует, как использовать [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/), чтобы получить ширину текста ячейки.

Исходный файл, использованный в следующем фрагменте кода, прикреплен для вашего ознакомления.

[Исходный файл](96928090.xlsx)

## Образец кода

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory path for source files
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook from the specified Excel file
    Workbook workbook(sourceDir + u"GetTextWidthSample.xlsx");

    // Calculate the text width for the string value of cell A1
    double textWidth = CellsHelper::GetTextWidth(workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue(), workbook.GetDefaultStyle().GetFont(), 1);

    // Output the text width
    std::wcout << u"Text width: " << textWidth << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
