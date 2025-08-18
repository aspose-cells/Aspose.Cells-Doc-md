---
title: Get Cells Index with Golang via C++
linktitle: Get Cells Index
type: docs
weight: 600
url: /go-cpp/get-cells-index/
description: Learn how to get row or column index by the name of row, column, or cells. Convert the name of the cell to row and column index zero-based using Aspose.Cells with Golang via C++.
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

- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/rownametoindex/)

Note: The indexing is zero-based in Aspose.Cells for C++, but the id of Row is one-based in MS Excel.

## **Get Cells Indexes using Aspose.Cells**

This example shows how to:

1. Create a workbook and add some data.
1. Find the specific cell in the first worksheet.
1. Get Row index and Column index by the name of the cell.
1. Get Column index by the name of the column.
1. Get Row index by the name of the row.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-CellsIndex.go" >}}
