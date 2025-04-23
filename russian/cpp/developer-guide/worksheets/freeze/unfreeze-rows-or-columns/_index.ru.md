---
title: Разморозить строки или столбцы листа Excel с помощью C++
linktitle: Снять замораживание панелей
type: docs
weight: 190
url: /ru/cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: В этой статье вы узнаете, как программно разморозить строки, столбцы или панели листов Excel, используя API Aspose.Cells for C++.
keywords: Разморозить панели, строки, столбцы, окно.
---

## **Введение**

В этой статье мы узнаем, как разморозить строки, столбцы и панели в листах Excel. Если листы Excel заморожены, иногда мы хотим их разморозить или отрегулировать замороженные строки, столбцы или панели.

## **В Excel**

1. Нажмите вкладку **Вид** > **Разморозить панели** > **Разморозить панели**.

**![снять замораживание панелей в Excel](Unfreeze-Panes.png)**

## **Разморозить строки, столбцы или панели с помощью Aspose.Cells for C++**
Простое разморозка панелей с помощью Aspose.Cells for C++. Используйте метод [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unfreezepanes/) для разморозки панелей.

1. Создайте объект `Workbook`, чтобы открыть замороженный файл.
2. Разморозить панели с помощью метода `Worksheet.UnFreezePanes()`.
3. Сохранить файл.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Frozen.xlsx");
    Workbook workbook(inputFilePath);

    // Unfreeze panes in the first worksheet
    workbook.GetWorksheets().Get(0).UnFreezePanes();

    // Save the modified workbook
    U16String outputFilePath(u"Unfrozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes unfrozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Прикреплен [образец исходного файла Excel](Frozen.xlsx).
