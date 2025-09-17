##Get Cells Index
Learn how to get row or column in by the name of row , column or cells. Convert the name of the cell to row and column index zero-based.
The default view of Excel is A1 style reference，each column is defined as A, B, C.... , and the cells are named as A1, B2, C3... and so on.
You may want to know which row and column is this cell in.
## **Possible Usage Scenarios**
When you only need to manipulate a specific data on the worksheet by row and column index, you need to know the column and column indexes of that specific cell.
Aspose.Cells offers this feature to get row and column index by the name of the row, column and cell.
Aspose.Cells provides the following properties and methods to help you achieve your goals.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)
Note: The indexing is zero-based in Aspose.Cells for .Net, but the id of Row is one-based in MS Excel.
## **Get Cells Indexes using Aspose.Cells**
This example shows how to:
1. Create a workbook and add some data.
1. Find the specific cell in the first worksheet.
1. Get Row index and Column index by the name of the cell.
1. Get Column index by the name of the column.
1. Get Row index by the name of the row.
