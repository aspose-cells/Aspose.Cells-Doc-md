---
title: Форматировать диапазоны с помощью C++
linktitle: Форматирование диапазонов
type: docs
weight: 105
url: /ru/cpp/how-to-format-a-range/
description: Узнайте, как форматировать диапазоны в Excel с помощью Aspose.Cells и C++. Програмmatically применяйте стили, шрифты и цвета к диапазонам ячеек.
---

## **Возможные сценарии использования**
Когда вам необходимо применить стиль к диапазону, вы можете использовать форматирование диапазона.

## **Как форматировать диапазон в Excel**

Для форматирования диапазона ячеек в Excel вы можете использовать встроенные варианты форматирования, предоставленные Excel. Вот как можно форматировать диапазон ячеек непосредственно в Excel:

1. Откройте Excel и книгу, которая содержит диапазон, который вы хотите отформатировать.

2. Выберите диапазон ячеек, который вы хотите отформатировать. Вы можете щелкнуть и перетащить, чтобы выбрать диапазон, или вы можете использовать комбинации клавиш, такие как Shift + стрелки, чтобы расширить выбор.

3. После выбора диапазона щелкните правой кнопкой мыши по выбранному диапазону и выберите "Формат ячеек" в контекстном меню. В качестве альтернативы, вы можете перейти на вкладку "Домой" на ленте Excel, щелкнуть на выпадающем списке "Формат" в группе "Ячейки" и выбрать "Формат ячеек".

4. Появится диалоговое окно "Формат ячеек". Здесь вы можете выбрать различные варианты форматирования для применения к выбранному диапазону. Например, вы можете изменить стиль шрифта, размер шрифта, цвет шрифта, формат чисел, границы, цвет фона и т. д. Исследуйте различные вкладки в диалоговом окне, чтобы получить доступ к различным вариантам форматирования.

5. После внесения желаемых изменений форматирования нажмите кнопку "OK", чтобы применить форматирование к выбранному диапазону.

## **Как форматировать диапазон с помощью C++**

Для форматирования диапазона с помощью Aspose.Cells используйте следующие методы:
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/cpp/aspose.cells/range/setstyle/)

## **Образец кода**
В этом примере мы создаем рабочую книгу Excel, добавляем образец данных, получаем доступ к первому листу и определяем два диапазона («A1:C3» и «A4:C5»). Затем создаем новые стили, задаем различные параметры форматирования (например, цвет шрифта, жирность) и применяем стиль к диапазону. В конце сохраняем книгу в новый файл.
<br>
![todo:image_alt_text](format-range.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
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

    Range range = worksheet.GetCells().CreateRange(u"A1:C3");
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Red());
    style.GetFont().SetIsBold(true);

    StyleFlag flag;
    flag.SetFont(true);
    range.ApplyStyle(style, flag);

    Range range2 = worksheet.GetCells().CreateRange(u"A4:C5");
    Style style2 = workbook.CreateStyle();
    style2.GetFont().SetColor(Color::Blue());
    style2.GetFont().SetIsItalic(true);
    range2.SetStyle(style2);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
