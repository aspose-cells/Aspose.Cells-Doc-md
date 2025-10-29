---
title: Как управлять просмотром рабочей книги с помощью C++
linktitle: Как управлять видом книги
type: docs
weight: 600
url: /ru/cpp/how-to-control-workbook-view/
description: Научитесь управлять просмотром рабочей книги, используя API Aspose.Cells for C++.
keywords: Как управлять видом книги, установить вид Excel, управлять видом книги, установить вид книги, управлять видом Excel.
---

## **Возможные сценарии использования**
Когда нужно настроить отображение страниц Excel, необходимо знать, как управлять каждым модулем, например горизонтальной и вертикальной панелями прокрутки, скрывать ли открытые файлы Excel и так далее. Aspose.Cells предоставляет такую возможность. Aspose.Cells содержит следующие свойства и методы для достижения ваших целей.

- [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/)
- [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/)
- [**WorkbookSettings.IsHidden**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishidden/)
- [**WorkbookSettings.IsMinimized**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isminimized/)
- [**WorkbookSettings.GetWindowHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowheight/)
- [**WorkbookSettings.GetWindowWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowwidth/)
- [**WorkbookSettings.GetWindowLeft()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowleft/)
- [**WorkbookSettings.GetWindowTop()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowtop/)

## **Как управлять видом рабочей книги с помощью Aspose.Cells for C++**
Этот пример показывает, как:

1. Создать книгу.
1. Добавить данные в ячейки на первом листе.
1. Скрыть горизонтальные и вертикальные полосы прокрутки в Виде книги.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
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

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    // Apply style to cell E10
    cell = cells.Get(u"E10");
    Style temp = workbook.CreateStyle();
    temp.GetFont().SetColor(Color::Red());
    cell.SetStyle(temp);

    // Hide horizontal and vertical scrollbars
    workbook.GetSettings().SetIsHScrollBarVisible(false);
    workbook.GetSettings().SetIsVScrollBarVisible(false);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```

Предварительный просмотр результирующего файла:
<br>
<image src="result.png" width="70%" />
{{< app/cells/assistant language="cpp" >}}
