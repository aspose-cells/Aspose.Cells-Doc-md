---
title: Автозаполнение диапазона Excel с помощью C++
linktitle: Автозаполнение диапазона
type: docs
weight: 105
url: /ru/cpp/autofill-ranges/
description: Узнайте, как выполнить операцию автозаполнения для указанного диапазона файла Excel с помощью Aspose.Cells и C++.
---

## **Выполнить автозаполнение в указанном диапазоне в Excel**

В Excel выберите диапазон, переместите мышь в правый нижний угол и перетащите "+" для автозаполнения данных.

## **Автозаполнение диапазонов с помощью Aspose.Cells**

Следующий пример демонстрирует, как выполнять операцию AutoFill на диапазоне. Вот пример файла, который можно скачать для тестирования этой функции:

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
{{< app/cells/assistant language="cpp" >}}
