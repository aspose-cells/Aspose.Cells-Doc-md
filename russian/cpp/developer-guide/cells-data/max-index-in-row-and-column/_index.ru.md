---
title: Получить максимальный индекс столбца в строке и максимальный индекс строки в столбце с помощью C++
linktitle: Получить максимальный индекс столбца в строке и максимальный индекс строки в столбце
type: docs
weight: 600
url: /ru/cpp/get-max-index-in-row-and-column/
description: Узнайте, как получить максимальный индекс столбца в строке и максимальный индекс строки в столбце через API Aspose.Cells for C++.
keywords: Получите максимальный индекс столбца в строке, получите максимальный индекс строки в столбце, получите максимальный индекс данных столбца в строке, получите максимальный индекс строки данных в столбце
---

## **Возможные сценарии использования**
Когда вам нужно манипулировать только некоторыми данными в строках или столбцах, важно знать диапазон данных этих строк и столбцов. Aspose.Cells предоставляет эту функцию. Чтобы получить максимальный индекс столбца в строке, можно использовать свойства [Row.GetLastCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/) и [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/), а затем — свойство [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/), чтобы получить максимальный индекс столбца и максимальный индекс столбца с данными. Для получения максимального индекса строки и индекса строки с данными в столбце вам нужно создать диапазон по столбцу, пройтись по диапазону, чтобы найти последнюю ячейку, и, наконец, получить атрибут [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) этой ячейки.

Aspose.Cells предоставляет следующие свойства и методы, чтобы помочь вам достичь своих целей.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)

## **Получите максимальный индекс столбца в строке и максимальный индекс строки в столбце, используя Aspose.Cells**
Этот пример показывает, как:

1. Загрузите [образец файла](sample.xlsx).
1. Получите строку, которая нуждается в получении максимального индекса столбца и максимального индекса данных столбца.
1. Получите атрибут [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) на ячейке.
1. Создайте диапазон на основе столбца.
1. Получите итератор и пройдите по диапазону.
1. Получите атрибут [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) на ячейке.

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filePath = srcDir + u"sample.xlsx";

    Workbook workbook(filePath);
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    Row row = cells.CheckRow(1);
    if (row)
    {
        std::cout << "Max column index in row: " << row.GetLastCell().GetColumn() << std::endl;
        std::cout << "Max data column index in row: " << row.GetLastDataCell().GetColumn() << std::endl;
    }

    Range columnRange = cells.CreateRange(1, 1, true);
    auto colIter = columnRange.GetEnumerator();

    int maxRow = 0;
    int maxDataRow = 0;

    while (colIter.MoveNext())
    {
        Cell currCell = colIter.GetCurrent();
        if (!currCell.GetStringValue().IsEmpty())
        {
            maxDataRow = currCell.GetRow();
        }
        if (!currCell.GetStringValue().IsEmpty() || currCell.GetHasCustomStyle())
        {
            maxRow = currCell.GetRow();
        }
    }

    std::cout << "Max row index in Column: " << maxRow << std::endl;
    std::cout << "Max data row index in Column: " << maxDataRow << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
