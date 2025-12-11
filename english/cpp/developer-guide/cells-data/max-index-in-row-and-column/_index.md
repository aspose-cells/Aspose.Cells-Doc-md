---
title: Get Max Column Index in Row and Max Row Index in Column with C++
linktitle: Get Max Column Index in Row and Max Row Index in Column
type: docs
weight: 600
url: /cpp/get-max-index-in-row-and-column/
description: Learn how to get the max column index in a row and the max row index in a column using the Aspose.Cells for C++ API.
keywords: Get Max Column Index in Row, Get Max Row Index in Column, Get Max Data Column Index in Row, Get Max Data Row Index in Column
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
When you only need to manipulate some data on the rows or columns, you need to know the data range of rows and columns. Aspose.Cells offers this feature. To obtain the maximum column index on a row, you can obtain the [Row.GetLastCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/) and [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/) properties, and then use the [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) property to obtain the maximum column index and maximum data column index. To obtain the maximum row index and maximum data row index on a column, you need to create a range on the column, traverse the range to find the last cell, and finally obtain the [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) property on the cell.

Aspose.Cells provides the following properties and methods to help you achieve your goals.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)

## **Get Max Column Index in Row and Max Row Index in Column using Aspose.Cells**
This example shows how to:

1. Load the [sample file](sample.xlsx).  
2. Get the row that needs to retrieve the maximum column index and maximum data column index.  
3. Get the [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) property on the cell.  
4. Create a range based on the column.  
5. Get an iterator and traverse the range.  
6. Get the [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) property on the cell.

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
{{< app/cells/assistant language="cpp" >}}
