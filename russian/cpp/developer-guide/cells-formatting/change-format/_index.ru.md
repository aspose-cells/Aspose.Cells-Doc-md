---
title: Изменение формата ячейки с помощью C++
linktitle: Изменение формата ячейки
description: Как использовать библиотеку Aspose.Cells в C++ для изменения форматирования ячеек, включая шрифт, цвет, границу и т.д. Регулируя эти свойства, вы получаете больший контроль над внешним видом ячеек.
keywords: Aspose.Cells, форматирование ячейки, C++, шрифт, цвет, граница
type: docs
weight: 20
url: /ru/cpp/how-to-change-format-of-cell/
---

## **Возможные сценарии использования**
Когда вы хотите выделить определенные данные, вы можете изменить стиль ячеек.

## **Как изменить формат ячейки в Excel**

Чтобы изменить формат одной ячейки в Excel, выполните следующие шаги:

1. Откройте Excel и книгу, содержащую ячейку, которую вы хотите отформатировать.

2. Найдите ячейку, которую вы хотите отформатировать.

3. Нажмите правой кнопкой мыши на ячейке и выберите "Формат ячеек" в контекстном меню. Кроме того, вы можете выбрать ячейку, перейти на вкладку "Главная" на ленте Excel, щелкнуть на выпадающем меню "Формат" в группе "Ячейки" и выбрать "Формат ячеек".

4. Появится диалоговое окно "Формат ячеек". Здесь вы можете выбрать различные параметры форматирования для применения к выбранной ячейке. Например, вы можете изменить стиль шрифта, размер шрифта, цвет шрифта, числовой формат, границы, цвет фона и т. д. Исследуйте различные вкладки в диалоговом окне для доступа к различным параметрам форматирования.

5. После внесения необходимых изменений в форматирование нажмите кнопку "OK", чтобы применить форматирование к выбранной ячейке.

## **Как изменить формат ячейки с помощью C++**

Чтобы изменить формат ячейки с помощью Aspose.Cells, вы можете использовать следующие методы:
1. [Cell.SetStyle(Style style)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)
2. [Cell.SetStyle(Стиль стиль, bool явныйФлаг)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)
3. [Cell.SetStyle(Стиль стиль, СтильФлаг флаг)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)

## **Образец кода**
В этом примере мы создаем книгу Excel, добавляем некоторые образцовые данные, получаем доступ к первому листу и получаем две ячейки ("A2" и "B3"). Затем мы получаем стиль ячейки, устанавливаем различные варианты форматирования (например, цвет шрифта, полужирный), и изменяем формат ячейки. Наконец, мы сохраняем книгу в новый файл.
![todo:image_alt_text](change-format.png)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

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

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell a2 = worksheet.GetCells().Get(u"A2");
    Style style = a2.GetStyle();
    style.GetFont().SetColor(Color::Red());
    style.GetFont().SetIsBold(true);

    StyleFlag flag;
    flag.SetFontColor(true);
    a2.SetStyle(style, flag);

    Cell b3 = worksheet.GetCells().Get(u"B3");
    Style style2 = b3.GetStyle();
    style2.GetFont().SetColor(Color::Blue());
    style2.GetFont().SetIsItalic(true);
    b3.SetStyle(style2);

    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
}
```
