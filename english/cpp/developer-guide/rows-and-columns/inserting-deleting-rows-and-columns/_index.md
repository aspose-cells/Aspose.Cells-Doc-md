---
title: Inserting, Deleting Rows and Columns
type: docs
weight: 40
url: /cpp/inserting-deleting-rows-and-columns/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**
Whether creating a new worksheet from scratch or working on an existing worksheet, we may need to add extra rows or columns to accommodate more data. Inversely, we may also need to delete rows or columns from specified positions in the worksheet. To fulfill these requirements, Aspose.Cells provides a very simplest set of classes and methods, discussed below.
### **Managing Rows and Columns**
Aspose.Cells provides a class, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains an [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides an [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection that represents all cells in the worksheet.

The [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection provides several methods managing rows and columns in a worksheet. Some of these are discussed below.

{{% alert color="primary" %}} 

When rows or columns are added, the content in the worksheet is shifted down or to the right, and if rows or columns are removed, the content is shifted up or the left.

{{% /alert %}} 
#### **Insert a Row**
Insert a row into the worksheet at any location by calling the [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) method of the [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. The [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) method takes the index of the row where the new row will be inserted.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


#### **Inserting Multiple Rows**
To insert multiple rows into a worksheet, call the [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) method of the [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. The [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) method takes two parameters:

- Row index, the index of the row from where the new rows will be inserted.
- Number of rows, the total number of rows that need to be inserted.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


#### **Deleting Multiple Rows**
To delete multiple rows from a worksheet, call the [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) method of the [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. The [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) method takes two parameters:

- Row index, the index of the row from where the rows will be deleted.
- Number of rows, the total number of rows that need to be deleted.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


#### **Insert a Column**
Developers can also insert a column into the worksheet at any location by calling the [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) method of the [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) method takes the index of the column where the new column will be inserted.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


#### **Delete a Column**
To delete a column from the worksheet at any location, call the [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) method of the [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. The [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) method takes the index of the column to delete.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
