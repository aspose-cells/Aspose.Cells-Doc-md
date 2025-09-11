---
title: Get Max Column Index in Row and Max Row Index in Column
type: docs
weight: 600
url: /nodejs-cpp/get-max-index-in-row-and-column/
description: Learn how to Get Max Column Index in Row and Max Row Index in Column through the Aspose.Cells for Node.js via C++ API.
keywords: Get Max Column Index in Row Node.js via C++, Get Max Row Index in Column Node.js via C++, Get Max Data Column Index in Row Node.js via C++, Get Max Data Row Index in Column Node.js via C++.
---

## **Possible Usage Scenarios**
When you only need to manipulate some data on the rows or columns, you need to know the data range of rows and columns. Aspose.Cells for Node.js via C++ offers this feature. To obtain the maximum column index on a row, you can obtain the [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--) and [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--) methods, and then use the [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) method to obtain the maximum column index and maximum data column index. But in order to obtain the maximum row index and maximum row data index on a column, you need to create a range on the column, then traverse the range to find the last cell, and finally call the [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) method on the cell.

Aspose.Cells for Node.js via C++ provides the following properties and methods to help you achieve your goals.
- [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--)
- [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--)
- [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)
- [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)

## **Get Max Column Index in Row and Max Row Index in Column**
This example shows how to:

1. Load the [sample file](sample.xlsx).
1. Get the row that needs to get the maximum column index and maximum data column index.
1. Call the [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) method on the cell.
1. Create a range based on column.
1. Get iterator and traverse range.
1. Call the [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) method on the cell.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-max-index-in-row-and-column.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}