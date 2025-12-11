---
title: Get Cells Index
type: docs
weight: 600
url: /net/get-cells-index/
description: Learn how to get a row or column by the name of the row, column, or cell. Convert the name of a cell to zero‑based row and column indexes.
keywords: Get row index and column index by the name of the cell, Get column index by the name of the column, Get row index by the name of the row, Get the index by the name of a cell
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
The default view of Excel is the A1 style reference; each column is defined as A, B, C..., and the cells are named A1, B2, C3..., and so on. You may want to know which row and column this cell is in.
{{% /alert %}}

## **Possible Usage Scenarios**
When you only need to manipulate specific data on the worksheet by row and column indexes, you need to know the row and column indexes of that specific cell.  
Aspose.Cells offers this feature to get row and column indexes by the name of the row, column, and cell.  
Aspose.Cells provides the following properties and methods to help you achieve your goals.

- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

**Note:** The indexing is zero‑based in Aspose.Cells for .NET, but the row index in MS Excel is one‑based.

## **Get Cells Indexes using Aspose.Cells**
This example shows how to:

1. Create a workbook and add some data.  
2. Find the specific cell in the first worksheet.  
3. Get row index and column index by the name of the cell.  
4. Get column index by the name of the column.  
5. Get row index by the name of the row.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}
{{< app/cells/assistant language="csharp" >}}
