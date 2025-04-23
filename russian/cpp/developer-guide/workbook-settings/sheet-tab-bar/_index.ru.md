---
title: Как управлять панелью вкладок листа с помощью C++
linktitle: Как управлять панелью вкладок листа
type: docs
weight: 600
url: /ru/cpp/how-to-control-sheet-tab-bar/
description: Научитесь управлять панелью вкладок листа через API Aspose.Cells for C++.
keywords: Как управлять панелью вкладок листа, управлять панелью вкладок листа, установить панель вкладок листа, управлять панелью вкладок листа. 
---

## **Возможные сценарии использования**
Когда нужно настроить отображение панели листов Excel, необходимо знать, как управлять вкладками листов, например скрывать или показывать панель вкладок, менять ширину панели вкладок, задавать первый видимый вкладка и так далее. Aspose.Cells поддерживает эти функции. Aspose.Cells предоставляет следующие свойства и методы для достижения ваших целей.

- [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)
- [**WorkbookSettings.GetSheetTabBarWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getsheettabbarwidth/)
- [**WorkbookSettings.GetFirstVisibleTab()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getfirstvisibletab/)

## **Как управлять панелью вкладок листа с помощью Aspose.Cells for C++**
Этот пример показывает, как:

1. Создать книгу.
1. Добавить данные в ячейки на первом листе.
1. Отобразите панель вкладок и установите ширину панели вкладок.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Obtain the reference to the newly added worksheet
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

    // Display the sheet tab and set the width of the tab bar
    workbook.GetSettings().SetShowTabs(true);
    workbook.GetSettings().SetSheetTabBarWidth(150);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Предварительный просмотр результирующего файла:
<br>
<image src="result.png" width="70%" />

