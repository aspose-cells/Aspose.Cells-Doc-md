---
title: Get Cells Index
type: docs
weight: 600
url: /nodejs-cpp/get-cells-index/
description: Learn how to get a row or column by the name of a row, column, or cell. Convert the name of a cell to zero‑based row and column indices.
keywords: Get Row index and Column index by the name of the cell, Get Column index by the name of the column, Get Row index by the name of the row, Get the index by the name of cell.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
The default view of Excel is A1‑style reference, where each column is defined as A, B, C…, and cells are named A1, B2, C3, and so on.  
You may want to know which row and column this cell is in.
{{% /alert %}}

## **Possible Usage Scenarios**
When you only need to manipulate specific data on the worksheet by row and column index, you need to know the row and column indexes of that specific cell.  
Aspose.Cells for Node.js via C++ offers this feature to get row and column indexes by the name of the row, column, or cell.  
Aspose.Cells for Node.js via C++ provides the following properties and methods to help you achieve your goals.

- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowNameToIndex-string-)

**Note:** The indexing is zero‑based in Aspose.Cells for Node.js via C++, but the row index is one‑based in Microsoft Excel.

## **Get Cell Indexes using Aspose.Cells for Node.js via C++**
This example shows how to:

1. Create a workbook and add some data.  
2. Find the specific cell in the first worksheet.  
3. Get row index and column index by the name of the cell.  
4. Get column index by the name of the column.  
5. Get row index by the name of the row.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-get-index.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
