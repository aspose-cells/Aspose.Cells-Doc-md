---
title: Get Cells Index
type: docs
weight: 600
url: /python-net/get-cells-index/
description: Learn how to get a row or column by the name of the row through the Aspose.Cells for Python via .NET API, as well as a column or cell. Convert the name of a cell to its zero‑based row and column indexes using the Aspose.Cells for Python via .NET API.
keywords: Python Excel, Get Row index and Column index by the name of the cell using Python, Get Column index by the name of the column using Python, Get Row index by the name of the row using Python, Get the index of a cell by its name using Python
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
The default view of Excel is the A1‑style reference; each column is labeled A, B, C..., and cells are named A1, B2, C3..., and so on.  
You may want to know which row and column this cell is in.
{{% /alert %}}

## **Possible Usage Scenarios**
When you only need to manipulate specific data on the worksheet by row and column index, you need to know the row and column indexes of that specific cell.  
Aspose.Cells for Python via .NET offers this feature to get row and column indexes by the name of the row, column, or cell.  
Aspose.Cells for Python via .NET provides the following properties and methods to help you achieve your goals.

- [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)
- [**CellsHelper.column_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_index_to_name/#int)
- [**CellsHelper.column_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_name_to_index/#str)
- [**CellsHelper.row_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_index_to_name/#int)
- [**CellsHelper.row_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_name_to_index/#str)

**Note:** The indexing is zero‑based in Aspose.Cells for Python via .NET, but the row index is one‑based in Microsoft Excel.

## **Get Cell Indexes using Aspose.Cells for Python via .NET**
This example shows how to:

1. Create a workbook and add some data.  
2. Find a specific cell in the first worksheet.  
3. Get the row index and column index by the name of the cell.  
4. Get the column index by the name of the column.  
5. Get the row index by the name of the row.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-get-index.py" >}}
{{< app/cells/assistant language="python-net" >}}
