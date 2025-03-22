---
title: Get Cells Index with C++
linktitle: Get Cells Index
type: docs
weight: 600
url: /cpp/get-cells-index/
description: Learn how to get row or column index by the name of row, column, or cells. Convert the name of the cell to row and column index zero-based using Aspose.Cells with C++.
keywords: Get Row index and Column index by the name of the cell, Get Column index by the name of the column, Get Row index by the name of the row, Get the index by the name of cell.
---

{{% alert color="primary" %}}
The default view of Excel is A1 style reference, where each column is defined as A, B, C...., and the cells are named as A1, B2, C3... and so on.
You may want to know which row and column this cell is in.

{{% /alert %}}

## **Possible Usage Scenarios**
When you only need to manipulate specific data on the worksheet by row and column index, you need to know the row and column indexes of that specific cell. 
Aspose.Cells offers this feature to get row and column index by the name of the row, column, and cell. 
Aspose.Cells provides the following properties and methods to help you achieve your goals:
- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rownametoindex/)

Note: The indexing is zero-based in Aspose.Cells for C++, but the id of Row is one-based in MS Excel.

## **Get Cells Indexes using Aspose.Cells**
This example shows how to:

1. Create a workbook and add some data.
1. Find the specific cell in the first worksheet.
1. Get Row index and Column index by the name of the cell.
1. Get Column index by the name of the column.
1. Get Row index by the name of the row.

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