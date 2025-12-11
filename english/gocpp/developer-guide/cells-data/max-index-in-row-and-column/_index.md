---
title: Get Max Column Index in Row and Max Row Index in Column with Golang via C++
linktitle: Get Max Column Index in Row and Max Row Index in Column
type: docs
weight: 600
url: /go-cpp/get-max-index-in-row-and-column/
description: Learn how to get the max column index in a row and the max row index in a column through the Aspose.Cells for C++ API.
keywords: Get Max Column Index in Row, Get Max Row Index in Column, Get Max Data Column Index in Row, Get Max Data Row Index in Column.
---

## **Possible Usage Scenarios**
When you only need to manipulate some data on the rows or columns, you need to know the data range of rows and columns. Aspose.Cells offers this feature. To obtain the maximum column index on a row, you can obtain the [Row.GetLastCell()](https://reference.aspose.com/cells/go-cpp/row/getlastcell/) and [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/) properties, and then use the [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) property to obtain the maximum column index and maximum data column index. But in order to obtain the maximum row index and maximum data row index on a column, you need to create a range on the column, then traverse the range to find the last cell, and finally obtain the [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) attribute of the cell.

Aspose.Cells provides the following properties and methods to help you achieve your goals.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/go-cpp/cell/getrow/)

## **Get Max Column Index in Row and Max Row Index in Column using Aspose.Cells**
This example shows how to:

1. Load the [sample file](sample.xlsx).  
2. Get the row whose maximum column index and maximum data column index you need.  
3. Retrieve the [Cell.GetColumn()](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/) attribute of the cell.  
4. Create a range based on the column.  
5. Obtain an iterator and traverse the range.  
6. Retrieve the [Cell.GetRow()](https://reference.aspose.com/cells/go-cpp/cell/getrow/) attribute of the cell.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MaxIndexInRowAndColumn.go" >}}