---
title: Get Cells Index
type: docs
weight: 600
url: /python-net/get-cells-index/
description: Learn how to get row or column in by the name of row through the Aspose.Cells for Python via .NET API, column or cells. Convert the name of the cell to row and column index zero-based through the Aspose.Cells for Python via .NET API.
keywords: Python Excel, Get Row index and Column index by the name of the cell using Python, Get Column index by the name of the column using Python, Get Row index by the name of the row using Python, Get the index by the name of cell using Python. 
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
The default view of Excel is A1 style reference，each column is defined as A, B, C.... , and the cells are named as A1, B2, C3... and so on.
You may want to know which row and column is this cell in.

{{% /alert %}}


## **Possible Usage Scenarios**
When you only need to manipulate a specific data on the worksheet by row and column index, you need to know the column and column indexes of that specific cell. 
Aspose.Cells for Python via .NET offers this feature to get row and column index by the name of the row, column and cell. 
Aspose.Cells for Python via .NET provides the following properties and methods to help you achieve your goals.
- [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)
- [**CellsHelper.column_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_index_to_name/#int)
- [**CellsHelper.column_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_name_to_index/#str)
- [**CellsHelper.row_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_index_to_name/#int)
- [**CellsHelper.row_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_name_to_index/#str)

Note: The indexing is zero-based in Aspose.Cells for Python via .NET, but the id of Row is one-based in MS Excel.

## **Get Cells Indexes using Aspose.Cells for Python Excel Library**
This example shows how to:

1. Create a workbook and add some data.
1. Find the specific cell in the first worksheet.
1. Get Row index and Column index by the name of the cell.
1. Get Column index by the name of the column.
1. Get Row index by the name of the row.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-get-index.py" >}}
{{< app/cells/assistant language="python-net" >}}
