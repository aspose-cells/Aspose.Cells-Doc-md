---
title: Разделение экрана листа Excel с помощью C++
linktitle: Разделенный экран
type: docs
weight: 190
url: /ru/cpp/how-to-split-screen-of-excel-worksheet
description: В этой статье вы узнаете, как вывести определенные строки и/или столбцы в отдельные панели, разделив лист на две или четыре части программно, используя C++.
keywords: Заморозить верхние строки, Заморозить верхнюю строку.
---

## **Введение**

В этой статье мы узнаем, как отображать определенные строки и/или столбцы в отдельных панелях с помощью разделения листа на две или четыре части. При работе с большими наборами данных нам нужно видеть несколько областей одного листа одновременно, чтобы сравнить разные подмножества данных. Функция разделения экрана поможет вам в этом.

## **Как разделить экран в Excel**
Чтобы разделить таблицу на две или четыре части, выполните следующее:

1. Выберите строку/столбец/ячейку до которой вы хотите разместить разбиение.
2. На вкладке Вид в группе Окна нажмите кнопку Разделить.

**![Разделить экран](Split-Screen.png)**

## **Разделить лист вертикально по столбцам**

Для разделения двух областей электронной таблицы вертикально выберите столбец справа от столбца, где вы хотите появление разделения, и нажмите кнопку Разделить в Excel.

Легко разделить лист вертикально по столбцам программно с помощью Aspose.Cells for C++, достаточно выбрать одну ячейку в верхней строке как активную, затем
разделить с методом [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Sets C1 cell in the top row as the active cell.
    sheet.SetActiveCell(u"C1");

    // Split worksheet vertically on columns.
    sheet.Split();

    std::cout << "Worksheet processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Разделить лист горизонтально по строкам**
Чтобы разделить ваше окно Excel горизонтально, выберите строку ниже строки, где вы хотите, чтобы произошло разделение в Excel.

Легко разделить лист горизонтально по строкам программно с помощью Aspose.Cells for C++, достаточно выбрать одну ячейку в левом столбце как активную, затем
разделить с методом [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and load an existing Excel file.
    Workbook workbook(u"Book1.xlsx");

    // Access the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set the A6 cell in the left column as the active cell.
    sheet.SetActiveCell(u"A6");

    // Split the worksheet horizontally on rows.
    sheet.Split();

    // Save the modified workbook to a new file.
    workbook.Save(u"dest.xlsx");

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Разделение листа на четыре части**
Чтобы просматривать одновременно четыре различных раздела одного листа, разделите экран как вертикально, так и горизонтально в Excel.

Легко разделить лист вертикально по столбцам программно с помощью Aspose.Cells for C++, достаточно выбрать одну ячейку, не находящуюся в первой строке и столбце, как активную, затем
разделить с методом [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set E6 cell as the active cell.
    sheet.SetActiveCell(u"E6");

    // Split worksheet into four parts.
    sheet.Split();

    Aspose::Cells::Cleanup();
}
```

## **Как удалить разделение**
Чтобы удалить разделение листа, просто повторно нажмите кнопку Разделить.

Aspose.Cells for C++ предоставляет метод [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) для удаления настроек разделения.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Remove split
    sheet.RemoveSplit();

    // Split worksheet into four parts
    sheet.Split();

    std::cout << "Worksheet split successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
