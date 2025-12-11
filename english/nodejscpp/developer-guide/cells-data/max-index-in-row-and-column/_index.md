---
title: Get Max Column Index in Row and Max Row Index in Column
type: docs
weight: 600
url: /nodejs-cpp/get-max-index-in-row-and-column/
description: Learn how to get the max column index in a row and the max row index in a column using the Aspose.Cells for Node.js via C++ API.
keywords: Get Max Column Index in Row Node.js via C++, Get Max Row Index in Column Node.js via C++, Get Max Data Column Index in Row Node.js via C++, Get Max Data Row Index in Column Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
When you only need to manipulate some data on the rows or columns, you need to know the data range of those rows and columns. Aspose.Cells for Node.js via C++ offers this feature. To obtain the maximum column index on a row, you can call the [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--) and [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--) methods, and then use the [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) method to obtain the maximum column index and the maximum data column index. However, to obtain the maximum row index and the maximum data row index on a column, you need to create a range for the column, traverse the range to find the last cell, and finally call the [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) method on that cell.

Aspose.Cells for Node.js via C++ provides the following properties and methods to help you achieve your goals.

- [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--)
- [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--)
- [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)
- [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)

## **Get Max Column Index in Row and Max Row Index in Column**
This example shows how to:

1. Load the [sample file](sample.xlsx).  
2. Get the row for which you need to obtain the maximum column index and the maximum data column index.  
3. Call the [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) method on the cell.  
4. Create a range based on the column.  
5. Obtain an iterator and traverse the range.  
6. Call the [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) method on the cell.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-max-index-in-row-and-column.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
