---
title: Обнаружение пустых листов с помощью C++
linktitle: Обнаружение пустых рабочих листов
type: docs
weight: 410
url: /ru/cpp/detecting-empty-worksheets/
description: В этой статье показан код, объясняющий, как программно обнаружить пустые листы Excel с помощью API C++ и библиотеки Aspose.Cells.
keywords: обнаружение пустого листа C++, поиск пустого листа Excel C++
---

## **Проверка заполненных ячеек**

Листы могут иметь одно или несколько заполненных ячеек, где значение может быть простым (текст, число, дата/время) или формулой или значением на основе формулы. В таком случае легко определить, является ли данный лист пустым или нет. Всё, что нужно проверить — это свойства [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) или [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/). Если указанные свойства возвращают ноль или положительные значения, это означает, что одна или несколько ячеек заполнены. Однако, если любое из этих свойств возвращает -1, это указывает на то, что ячейки в листе не заполнены.

{{% alert color="primary" %}}

Коллекции строк и столбцов имеют нумерацию с нуля, поэтому ячейка в строке 0 и столбце 0 означает первую ячейку листа, то есть A1.

{{% /alert %}}

## **Проверка пустых инициализированных ячеек**

Все ячейки, содержащие значения, автоматически инициализируются. Однако возможно, что на листе есть ячейки только с форматированием. В таком случае свойства [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) или [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) вернут -1, что указывает на отсутствие заполненных значений. Но инициализированные ячейки из-за форматирования не могут быть обнаружены этим методом. Для проверки наличия пустых инициализированных ячеек рекомендуется использовать метод `MoveNext` у перечислителя, полученного из коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Если метод `MoveNext` возвращает **true**, значит в листе есть одна или более инициализированных ячеек.

## **Проверка фигур**

Возможна ситуация, что в листе нет заполненных ячеек, однако он может содержать формы и объекты, такие как управляемые элементы, диаграммы, изображения и т.д. Чтобы проверить наличие каких-либо фигур, достаточно проверить свойство [**ShapeCollection.Count**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/getcount/). Положительное значение означает наличие фигур в листе.

## **Пример программирования**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load an existing spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Loop over all worksheets in the workbook
    WorksheetCollection sheets = book.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);

        // Check if worksheet has populated cells
        if (sheet.GetCells().GetMaxDataRow() != -1)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are populated" << endl;
        }
        // Check if worksheet has shapes
        else if (sheet.GetShapes().GetCount() > 0)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because there are one or more shapes" << endl;
        }
        // Check if worksheet has empty initialized cells
        else
        {
            Range range = sheet.GetCells().GetMaxDisplayRange();
            auto rangeIterator = range.GetEnumerator();
            if (rangeIterator.MoveNext())
            {
                cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are initialized" << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
