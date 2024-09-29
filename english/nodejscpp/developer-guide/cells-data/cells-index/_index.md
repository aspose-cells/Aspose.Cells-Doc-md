---
title: Get Cells Index
type: docs
weight: 600
url: /nodejs-cpp/get-cells-index/
description: Learn how to get row or column in by the name of row , column or cells. Convert the name of the cell to row and column index zero-based.
keywords: Get Row index and Column index by the name of the cell, Get Column index by the name of the column, Get Row index by the name of the row, Get the index by the name of cell. 
---

{{% alert color="primary" %}}
The default view of Excel is A1 style reference，each column is defined as A, B, C.... , and the cells are named as A1, B2, C3... and so on.
You may want to know which row and column is this cell in.

{{% /alert %}}


## **Possible Usage Scenarios**
When you only need to manipulate a specific data on the worksheet by row and column index, you need to know the column and column indexes of that specific cell. 
Aspose.Cells for Node.js via C++ offers this feature to get row and column index by the name of the row, column and cell. 
Aspose.Cells for Node.js via C++ provides the following properties and methods to help you achieve your goals.
- [**CellsHelper.cellNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#cellNameToIndex-string-number-number-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowNameToIndex-string-)

Note: The indexing is zero-based in Aspose.Cells for Node.js via C++, but the id of Row is one-based in MS Excel.

## **Get Cells Indexes using Aspose.Cells for Node.js via C++**
This example shows how to:

1. Create a workbook and add some data.
1. Find the specific cell in the first worksheet.
1. Get Row index and Column index by the name of the cell.
1. Get Column index by the name of the column.
1. Get Row index by the name of the row.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-get-index.js" >}}