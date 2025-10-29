---
title: Заморозить верхний ряд(ы) листа Excel с помощью C++
linktitle: Заморозить строки
type: docs
weight: 190
url: /ru/cpp/how-to-freeze-rows-of-excel-worksheet
description: В этой статье вы узнаете, как программно заморозить верхние строки листов Excel с помощью библиотеки C++ и API Aspose.Cells.
keywords: Заморозить верхние строки, Заморозить верхнюю строку.
---

## **Введение**

В этой статье мы узнаем, как заморозить верхнюю(ие) строку(и). Когда у вас большое количество данных под общей записью, вы не можете видеть заголовок при прокрутке листа вниз. Вы можете заморозить верхнюю(ие) строку(и), чтобы видеть зафиксированную часть даже при прокрутке остальной части данных. Вы легко увидите заголовки в верхних строках.

## **Заморозить строки в Excel**

**![Заморозить верхнюю строку(и) в Excel](Freeze-Rows.png)**

1. Если хотите заморозить верхнюю(ие) строку(и), сначала выберите строку под строкой, которую нужно зафиксировать.
2. Нажмите Вид > Заморозка областей.
3. В выпадающем меню нажмите "Заморозить верхнюю строку".
4. Если вы прокрутите вниз, первая строка всегда останется сверху.

**![Замороженная строка](Frozen-Row.png)**

Как видно, первая строка зафиксирована, и она всегда остается вверху при прокрутке вниз.

Заморозка строк позволяет просматривать большие данные, не теряя из виду метки строк.

## **Заморозить строки с помощью Aspose.Cells for C++**
Очень просто заморозить строку(и) с помощью Aspose.Cells for C++. 
Пожалуйста, используйте метод [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) для заморозки строки(и) в выбранной строке.
1. Создайте рабочую книгу для открытия файла или создайте пустой файл.
2. Заморозьте первую строку с помощью метода Worksheet.FreezePanes().
3. Сохранить файл.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Freeze.xlsx");

    // Freezing panes at the cell B2
    workbook.GetWorksheets().Get(0).FreezePanes(u"A2", 1, 0);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Приложен [образец исходного файла Excel](../Freeze.xlsx).
{{< app/cells/assistant language="cpp" >}}
