##Get Max Column Index in Row and Max Row Index in Column
Learn how to Get Max Column Index in Row and Max Row Index in Column through the Aspose.Cells for Python via .NET API.
## **Possible Usage Scenarios**
When you only need to manipulate some data on the rows or columns, you need to know the data range of  rows and columns. Aspose.Cells for Python via .NET offers this feature. To obtain the maximum column index on a row, you can obtain the [Row.last_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/) and [Row.last_data_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/) properties, and then use the [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) property to obtain the maximum column index and maximum data column index. But in order to obtain the maximum row index and maximum row data index on a column, you need to create a range on the column, then traverse the range to find the last cell, and finally obtain the [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) attribute on the cell.
Aspose.Cells for Python via .NET provides the following properties and methods to help you achieve your goals.
- [**Row.last_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/)
- [**Row.last_data_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/)
- [**Cell.column**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/)
- [**Cell.row**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/)
## **Get Max Column Index in Row and Max Row Index in Column using Aspose.Cells for Python Excel Library**
This example shows how to:
1. Load the [sample file](sample.xlsx).
1. Get the row that needs to get the maximum column index and maximum data column index.
1. Get [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) attribute on the cell.
1. Create a range based on column.
1. Get iterator and traverse range.
1. Get [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) attribute on the cell.
