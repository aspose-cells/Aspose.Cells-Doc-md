---
title: Заставить панели Excel листа зафиксировать с помощью C++
linktitle: Замораживание областей
type: docs
weight: 190
url: /ru/cpp/how-to-freeze-panes-of-excel-worksheet
description: В этой статье вы узнаете, как программно зафиксировать панели Excel листов с помощью библиотеки C++ и API Aspose.Cells.
keywords: Зафиксировать панели, зафиксировать окно.
---

## **Введение**

 В этой статье мы расскажем, как зафиксировать панели. Когда у вас есть большой объем данных с общей заголовком, вы не сможете видеть заголовки при прокрутке листа. Каждый запис содержит много данных. Вы можете зафиксировать панели, чтобы видеть зафиксированную часть, даже когда остальная часть данных прокручивается. Вы легко сможете видеть заголовки в верхних строках или первых столбцах. Зафиксировать и разблокировать панели — это лишь изменение вида данных, без изменения самих данных.

## **В Excel**

**![Замораживание областей в Excel](Freeze-panes.png)**

1. Если хотите зафиксировать панели, закрепите строки и столбцы, сначала выберите ячейку (например, B2).
2. Нажмите Вид > Заморозка областей.
3. В выпадающем меню выберите Заморозить области.
4. При прокрутке вниз или вправо первая строка и первый столбец останутся зафиксированными.

**![Зафиксированные панели](Frozen-Panes.png)**

Как видно, первая строка и столбец A зафиксированы, вторая строка — 32, а вторая видимая колонка — D.

Зафиксированные панели позволяют просматривать большие данные, не запоминая номера строк или столбцов.

## **Фиксация панелей с помощью Aspose.Cells for C++**
Это просто зафиксировать панели с помощью Aspose.Cells for C++. Используйте метод [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) для закрепления панелей в выбранной ячейке.
1. Создайте рабочую книгу для открытия файла или создайте пустой файл.
2. Зафиксировать панели с помощью метода Worksheet.FreezePanes().
3. Сохранить файл.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Freeze.xlsx");
    Workbook workbook(inputFilePath);

    // Freeze panes at the cell B2
    WorksheetCollection sheets = workbook.GetWorksheets();
    sheets.Get(0).FreezePanes(u"B2", 1, 1);

    // Save the file
    U16String outputFilePath(u"frozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Прикреплен файл [образец исходного файла Excel](Freeze.xlsx).
