---
title: Управление строкой HTML ячеек с помощью C++
linktitle: Управление строкой HTML для ячеек
type: docs
weight: 600
url: /ru/cpp/manage-cells-html-string/
description: Узнайте, как управлять строкой HTML ячеек через API Aspose.Cells for C++.
keywords: Добавить HTML строку в ячейку, установить HTML строку в ячейке, добавить HTML строку, получить HTML строку ячейки, управлять HTML строкой ячейки
---

## **Возможные сценарии использования**
Когда нужно задать стилизованные данные для конкретной ячейки, можно присвоить ячейке строку HTML. Конечно, также можно получить строку HTML ячейки. Aspose.Cells предоставляет эту функцию. Aspose.Cells имеет следующие свойства и методы, чтобы помочь вам достичь вашей цели.
- [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)
- [**Cell::SetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/sethtmlstring/)

## **Получить и установить строку HTML с помощью Aspose.Cells**
Этот пример показывает, как:

1. Создать книгу и добавить некоторые данные.
1. Получить конкретную ячейку на первом листе.
1. Установить HTML-строку в ячейку.
1. Получить HTML-строку из ячейки.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");

    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");

    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");

    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");

    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    Cell c3 = cells.Get(u"C3");
    // Set HTML string for C3 cell
    c3.SetHtmlString(u"<b>test bold</b>");

    Cell c4 = cells.Get(u"C4");
    // Set HTML string for C4 cell
    c4.SetHtmlString(u"<i>test italic</i>");

    // Get the HTML string of specific cell
    std::cout << c3.GetHtmlString().ToUtf8() << std::endl;
    std::cout << c4.GetHtmlString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Вывод, созданный образцовым кодом

На следующем скриншоте показан вывод вышеприведенного образца кода.

![todo:image_alt_text](htmlstring.png)
