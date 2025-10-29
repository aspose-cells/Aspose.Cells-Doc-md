---
title: Получить индекс ячейки с помощью C++
linktitle: Для получения индексов ячеек
type: docs
weight: 600
url: /ru/cpp/get-cells-index/
description: Узнайте, как получить индекс строки или столбца по имени строки, столбца или ячейки. Преобразуйте имя ячейки в индексы строки и столбца, начиная с нуля, с помощью Aspose.Cells и C++.
keywords: Получить индекс строки и столбца по имени ячейки, Получить индекс столбца по имени столбца, Получить индекс строки по имени строки, Получить индекс по имени ячейки.
---

{{% alert color="primary" %}}
По умолчанию представление Excel использует ссылку в стиле A1, где каждый столбец обозначается как A, B, C..., а ячейки обозначаются как A1, B2, C3... и так далее.
Вам может понадобиться знать, в какой строке и столбце находится эта ячейка.

{{% /alert %}}

## **Возможные сценарии использования**
Когда вам нужно манипулировать только определенными данными на листе, по индексу строки и столбца, необходимо знать эти индексы. 
Aspose.Cells предоставляет эту возможность получать индекс строки и столбца по имени строки, столбца и ячейки. 
Aspose.Cells предоставляет следующие свойства и методы для достижения ваших целей:
- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rownametoindex/)

Примечание: Индексация в Aspose.Cells for C++ нулевая, но ID строки в MS Excel — единичная.

## **Получить индексы ячеек с использованием Aspose.Cells**
Этот пример показывает, как:

1. Создать книгу и добавить некоторые данные.
1. Найдите конкретную ячейку на первом рабочем листе.
1. Получите индекс строки и столбца по имени ячейки.
1. Получите индекс столбца по имени столбца.
1. Получите индекс строки по имени строки.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Obtaining the reference of the newly added worksheet
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

    Cell curr = cells.Find(u"Blackberry", nullptr);
    int currRow, currCol;

    // Get row and column index of current cell
    CellsHelper::CellNameToIndex(curr.GetName(), currRow, currCol);
    std::cout << "Row Index: " << currRow << "  Column Index: " << currCol << std::endl;

    // Get column name by column index
    U16String columnName = CellsHelper::ColumnIndexToName(currCol);

    // Get row name by row index
    U16String rowName = CellsHelper::RowIndexToName(currRow);

    std::cout << "Column Name: " << columnName.ToUtf8() << " Row Name: " << rowName.ToUtf8() << std::endl;

    // Get column index by column name
    int columnIndex = CellsHelper::ColumnNameToIndex(columnName);

    // Get row index by row name
    int rowIndex = CellsHelper::RowNameToIndex(rowName);

    std::cout << "Column Index: " << columnIndex << " Row Index: " << rowIndex << std::endl;

    // Assertions
    if (columnIndex != currCol || rowIndex != currRow) {
        std::cerr << "Assertion failed!" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
