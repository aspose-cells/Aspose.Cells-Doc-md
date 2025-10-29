---
title: Получение строкового значения ячейки с форматированием и без него с помощью C++
linktitle: Получить строковое значение ячейки
type: docs
weight: 240
url: /ru/cpp/get-cell-string-value-with-and-without-formatting/
description: Узнайте, как получать строковое значение ячейки с форматированием и без него через API Aspose.Cells for C++.
keywords: Получение значения строки ячейки с и без форматирования, извлечение значения строки ячейки с и без форматирования, получение значения строки ячейки с и без форматирования
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет метод [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), который можно использовать для получения строкового значения ячейки с любым или без форматирования. Предположим, у вас есть ячейка со значением 0.012345, и вы отформатировали его так, чтобы отображать только два знака после запятой. В Excel оно будет отображаться как 0.01. Вы можете получить строковые значения как 0.01, так и 0.012345, используя метод [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/). Он принимает параметр типа [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/), который имеет следующие значения:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

Приведенный ниже образец кода объясняет использование метода [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Put value inside the cell
    cell.PutValue(0.012345);

    // Format the cell to display 0.01 instead of 0.012345
    Style style = cell.GetStyle();
    style.SetNumber(2);
    cell.SetStyle(style);

    // Get string value as Cell Style
    U16String value = cell.GetStringValue(CellValueFormatStrategy::CellStyle);
    std::cout << value.ToUtf8() << std::endl;

    // Get string value without any formatting
    value = cell.GetStringValue(CellValueFormatStrategy::None);
    std::cout << value.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
