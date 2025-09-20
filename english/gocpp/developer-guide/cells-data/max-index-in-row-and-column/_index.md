---
title: Get Max Column Index in Row and Max Row Index in Column with Golang via C++
linktitle: Get Max Column Index in Row and Max Row Index in Column
type: docs
weight: 600
url: /go-cpp/get-max-index-in-row-and-column/
description: Learn how to Get Max Column Index in Row and Max Row Index in Column through the Aspose.Cells for C++ API.
keywords: Get Max Column Index in Row, Get Max Row Index in Column, Get Max Data Column Index in Row, Get Max Data Row Index in Column.
---

## **Possible Usage Scenarios**
When you only need to manipulate some data on the rows or columns, you need to know the data range of rows and columns. Aspose.Cells offers this feature. To obtain the maximum column index on a row, you can obtain the [Row.GetLastCell()](https://reference.aspose.com/cells/go-cpp/row/getlastcell/) and [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/) properties, and then use the [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) property to obtain the maximum column index and maximum data column index. But in order to obtain the maximum row index and maximum row data index on a column, you need to create a range on the column, then traverse the range to find the last cell, and finally obtain the [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) attribute on the cell.

Aspose.Cells provides the following properties and methods to help you achieve your goals.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/go-cpp/cell/getrow/)

## **Get Max Column Index in Row and Max Row Index in Column using Aspose.Cells**
This example shows how to:

1. Load the [sample file](sample.xlsx).
1. Get the row that needs to get the maximum column index and maximum data column index.
1. Get [Cell.GetColumn()](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/) attribute on the cell.
1. Create a range based on column.
1. Get iterator and traverse range.
1. Get [Cell.GetRow()](https://reference.aspose.com/cells/go-cpp/cell/getrow/) attribute on the cell.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MaxIndexInRowAndColumn.go" >}}