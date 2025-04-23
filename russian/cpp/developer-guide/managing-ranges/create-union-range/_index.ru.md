---
title: Создать объединённый диапазон с помощью C++
linktitle: Создать объединенный диапазон
type: docs
weight: 360
url: /ru/cpp/create-union-range/
description: Создать объединённый диапазон в файлах Excel с помощью Aspose.Cells и C++.
---

## **Создать объединенный диапазон**
Aspose.Cells предоставляет возможность создавать объединённые диапазоны с помощью метода [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/). Метод [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/) принимает два параметра: адрес для создания объединённого диапазона и индекс листа. Метод возвращает объект [UnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/unionrange/).

Следующий пример кода демонстрирует создание объединённого диапазона с помощью метода [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/). Образец файла, сгенерированный этим кодом, прилагается для справки.

- [Выходной файл](106364952.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Create union range
    UnionRange unionRange = workbook.GetWorksheets().CreateUnionRange(u"sheet1!A1:A10,sheet1!C1:C10", 0);

    // Put value "ABCD" in the range
    unionRange.SetValue(u"ABCD");

    // Save the output workbook
    workbook.Save(u"CreateUnionRange_out.xlsx");

    std::cout << "Union range created and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
