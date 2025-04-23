---
title: Установка границ диапазона с C++
type: docs
weight: 600
url: /ru/cpp/set-range-border/
description: Узнайте, как устанавливать границы диапазона с помощью Aspose.Cells и C++.
---

## **Возможные сценарии использования**
Когда нужно установить границу для диапазона, не обязательно делать это для каждой ячейки отдельно. Можно установить границу для диапазона целиком. Aspose.Cells предоставляет такую возможность. В этой статье представлен пример кода, использующего Aspose.Cells для установки границы диапазона.

## **Установить границу диапазона в Excel**
Чтобы установить границу диапазона в Excel, выполните следующие шаги:
1. Выберите диапазон ячеек, к которым вы хотите применить границу.
2. На вкладке "Домой" ленты найдите группу "Шрифт".
3. Внутри группы "Шрифт" нажмите на кнопку "Границы".
<br>
<img src="border.png" />
4. Выберите тип границы, который вы хотите применить из вариантов в выпадающем меню. Вы можете выбрать из предустановленных стилей границы или настроить свою собственную границу.
5. Как только вы выбрали желаемый стиль границы, она будет применена к выбранному диапазону ячеек.

## **Установить границу диапазона с помощью Aspose.Cells**
Этот пример показывает, как:

1. Создать книгу.
2. Добавьте данные в ячейки на первом листе.
3. Создайте [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range).
4. Установка внутренней границы диапазона.
5. Установка внешней границы диапазона.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get("B1");
    cell.PutValue(u"Count");
    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");
    cell = cells.Get("A3");
    cell.PutValue(u"Mango");
    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);
    cell = cells.Get("B3");
    cell.PutValue(3);
    cell = cells.Get("B4");
    cell.PutValue(6);
    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);
    cell = cells.Get("C3");
    cell.PutValue(20);
    cell = cells.Get("C4");
    cell.PutValue(30);
    cell = cells.Get("C5");
    cell.PutValue(60);

    // Create a range (A1:C5)
    Range range = cells.CreateRange(u"A1", u"C5");

    // Set inner border of range
    CellsColor innerColor = workbook.CreateCellsColor();
    innerColor.SetColor(Color::Red());
    range.SetInsideBorders(BorderType::Vertical, CellBorderType::Thin, innerColor);
    innerColor.SetColor(Color::Green());
    range.SetInsideBorders(BorderType::Horizontal, CellBorderType::Thin, innerColor);

    // Set outer border of range
    CellsColor outerColor = workbook.CreateCellsColor();
    outerColor.SetColor(Color::Blue());
    range.SetOutlineBorders(CellBorderType::Thin, outerColor);

    // Save the Workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
