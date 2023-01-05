---
title: Inserting, Deleting Rows and Columns
type: docs
weight: 40
url: /cpp/inserting-deleting-rows-and-columns/
---

## **Introduction**
Whether creating a new worksheet from scratch or working on an existing worksheet, we may need to add extra rows or columns to accommodate more data. Inversely, we may also need to delete rows or columns from specified positions in the worksheet. To fulfill these requirements, Aspose.Cells provides a very simplest set of classes and methods, discussed below.
### **Managing Rows and Columns**
Aspose.Cells provides a class, [IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook), that represents a Microsoft Excel file. The [IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) class contains an [IWorksheets](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class. The [IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) class provides an [ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collection that represents all cells in the worksheet.

The [ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collection provides several methods managing rows and columns in a worksheet. Some of these are discussed below.

{{% alert color="primary" %}} 

When rows or columns are added, the content in the worksheet is shifted down or to the right, and if rows or columns are removed, the content is shifted up or the left.

{{% /alert %}} 
#### **Insert a Row**
Insert a row into the worksheet at any location by calling the [InsertRow](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7) method of the [ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collection. The [InsertRow](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7) method takes the index of the row where the new row will be inserted.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow.cpp" >}}


#### **Inserting Multiple Rows**
To insert multiple rows into a worksheet, call the [InsertRows](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0) method of the [ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collection. The [InsertRows](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0) method takes two parameters:

- Row index, the index of the row from where the new rows will be inserted.
- Number of rows, the total number of rows that need to be inserted.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows.cpp" >}}


#### **Deleting Multiple Rows**
To delete multiple rows from a worksheet, call the [DeleteRows](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1) method of the [ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collection. The [DeleteRows](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1) method takes two parameters:

- Row index, the index of the row from where the rows will be deleted.
- Number of rows, the total number of rows that need to be deleted.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows.cpp" >}}


#### **Insert a Column**
Developers can also insert a column into the worksheet at any location by calling the [InsertColumn](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55) method of the [ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collection. [InsertColumn](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55) method takes the index of the column where the new column will be inserted.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn.cpp" >}}


#### **Delete a Column**
To delete a column from the worksheet at any location, call the [DeleteColumn](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b) method of the [ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collection. The [DeleteColumn](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b) method takes the index of the column to delete.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn.cpp" >}}
