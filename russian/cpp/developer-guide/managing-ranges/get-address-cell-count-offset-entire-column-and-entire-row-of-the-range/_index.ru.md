---
title: Получить адрес, количество ячеек, смещение, весь столбец и всю строку диапазона с помощью C++
linktitle: Получить адрес, количество ячеек, смещение, весь столбец и всю строку диапазона
type: docs
weight: 330
url: /ru/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: Узнайте, как получать адрес, количество ячеек, смещение, весь столбец и всю строку диапазона с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**
Aspose.Cells предоставляет объект `Range`, который содержит различные утилитные методы для удобной работы с диапазонами Excel. В этой статье показано использование следующих методов или свойств объекта `Range`:

- **Адрес**

  Получает адрес диапазона.

- **Количество ячеек**

  Получает общее количество ячеек в диапазоне.

- **Смещение**

  Получает диапазон со смещением.

- **Весь столбец**

  Получает объект `Range`, который представляет весь столбец (или столбцы), содержащие указанный диапазон.

- **Вся строка**

  Получает объект `Range`, который представляет всю строку (или строки), содержащие указанный диапазон.

## **Получить адрес, количество ячеек, смещение, весь столбец и всю строку диапазона**
Следующий пример кода поясняет использование методов и свойств, изложенных выше. Пожалуйста, посмотрите вывод в консоли ниже для справки.

## **Образец кода**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Create range A1:B3
    cout << "Creating Range A1:B3" << endl;
    Range rng = ws.GetCells().CreateRange(u"A1:B3");

    // Print range address and cell count
    cout << "Range Address: " << rng.GetAddress().ToUtf8() << endl;
    cout << "Range row Count: " << rng.GetRowCount() << endl;
    cout << "Range column Count: " << rng.GetColumnCount() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    // Create range A1
    cout << "Creating Range A1" << endl;
    rng = ws.GetCells().CreateRange(u"A1");

    // Print range offset, entire column and entire row
    cout << "Offset: " << rng.GetOffset(2, 2).GetAddress().ToUtf8() << endl;
    cout << "Entire Column: " << rng.GetEntireColumn().GetAddress().ToUtf8() << endl;
    cout << "Entire Row: " << rng.GetEntireRow().GetAddress().ToUtf8() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Вывод в консоль**
{{< highlight java >}}

Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
