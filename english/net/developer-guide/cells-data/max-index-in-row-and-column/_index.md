---
title: Get Max Column Index in Row and Max Row Index in Column
type: docs
weight: 600
url: /net/get-max-index-in-row-and-column/
description: Learn how to Get Max Column Index in Row and Max Row Index in Column through the Aspose.Cells for .NET API.
keywords: Get Max Column Index in Row, Get Max Row Index in Column, Get Max Data Column Index in Row, Get Max Data Row Index in Column. 
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
When you only need to manipulate some data on the rows or columns, you need to know the data range of rows and columns. Aspose.Cells offers this feature. To obtain the maximum column index on a row, you can obtain the [Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) and [Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/) properties, and then use the [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) property to obtain the maximum column index and maximum data column index. But in order to obtain the maximum row index and maximum row data index on a column, you need to create a range on the column, then traverse the range to find the last cell, and finally obtain the [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) attribute on the cell.

Aspose.Cells provides the following properties and methods to help you achieve your goals.
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

## **Get Max Column Index in Row and Max Row Index in Column using Aspose.Cells**
This example shows how to:

1. Load the [sample file](sample.xlsx).
2. Get the row for which you need the maximum column index and maximum data column index.
3. Retrieve the [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) attribute on the cell.
4. Create a range based on the column.
5. Obtain an iterator and traverse the range.
6. Retrieve the [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) attribute on the cell.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}
{{< app/cells/assistant language="csharp" >}}
