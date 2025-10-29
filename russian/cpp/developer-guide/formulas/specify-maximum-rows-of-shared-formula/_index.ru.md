---
title: Указать максимальное количество строк общей формулы с помощью C++
linktitle: Укажите максимальное количество строк общей формулы
type: docs
weight: 40
url: /ru/cpp/specify-maximum-rows-of-shared-formula/
description: Узнайте, как задавать максимальное количество строк общей формулы в Excel файлах с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Максимальное количество строк общей формулы по умолчанию равно 64. Может быть любое число, например, 1000. Производительность общей формулы меняется при разном количестве строк. Поэтому Aspose.Cells предоставляет свойство [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/), которое можно использовать для задания максимального количества строк общей формулы. Общая формула будет разбита на несколько, если общее количество строк превышает указанное, как показано на следующем скриншоте.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Укажите максимальное количество строк общей формулы**

Следующий пример кода объясняет использование свойства [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/). Он устанавливает максимум строк общей формулы равным 5 и добавляет ее в ячейку D1 для 100 строк, сохраняя результат в [выходной Excel файл](61767856.xlsx). Если распаковать содержимое выходного файла Excel и проверить *sheet1.xml*, вы увидите, что общая формула разбивается после каждых 5 строк, как выделено на вышеуказанном скриншоте.

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Set the max rows of shared formula to 5
    wb.GetSettings().SetMaxRowsOfSharedFormula(5);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell D1
    Cell cell = ws.GetCells().Get(u"D1");

    // Set the shared formula in 100 rows
    cell.SetSharedFormula(u"=Sum(A1:A2)", 100, 1);

    // Save the output Excel file
    wb.Save(u"outputSpecifyMaximumRowsOfSharedFormula.xlsx");

    std::cout << "Shared formula set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
