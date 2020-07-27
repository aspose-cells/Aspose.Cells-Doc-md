+++
title = "Inserting Deleting Rows and Columns" 
description = "" 
weight = 12024 
+++

Aspose.Cells for C++ : Inserting, Deleting Rows and Columns  

# Aspose.Cells for C++ : Inserting, Deleting Rows and Columns


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#Inserting,DeletingRowsandColumns-Introduction)
    *   1.1 [Managing Rows and Columns](#Inserting,DeletingRowsandColumns-ManagingRowsandColumns)
        *   1.1.1 [Insert a Row](#Inserting,DeletingRowsandColumns-InsertaRow)
        *   1.1.2 [Inserting Multiple Rows](#Inserting,DeletingRowsandColumns-InsertingMultipleRows)
        *   1.1.3 [Deleting Multiple Rows](#Inserting,DeletingRowsandColumns-DeletingMultipleRows)
        *   1.1.4 [Insert a Column](#Inserting,DeletingRowsandColumns-InsertaColumn)
        *   1.1.5 [Delete a Column](#Inserting,DeletingRowsandColumns-DeleteaColumn)
{{< /panel >}}
 

## Introduction

Whether creating a new worksheet from scratch or working on an existing worksheet, we may need to add extra rows or columns to accommodate more data. Inversely, we may also need to delete rows or columns from specified positions in the worksheet. To fulfill these requirements, Aspose.Cells provides a very simplest set of classes and methods, discussed below.

### Managing Rows and Columns

Aspose.Cells provides a class, [IWorkbook](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/), that represents a Microsoft Excel file. The [IWorkbook](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/) class contains an [IWorksheets](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet_collection/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [IWorksheet](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet/) class. The [IWorksheet](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet/) class provides an [ICells](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/) collection that represents all cells in the worksheet.

The [ICells](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/) collection provides several methods managing rows and columns in a worksheet. Some of these are discussed below.

When rows or columns are added, the content in the worksheet is shifted down or to the right, and if rows or columns are removed, the content is shifted up or the left.

#### Insert a Row

Insert a row into the worksheet at any location by calling the [InsertRow](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/#ad9c067ccb5f34a7740f5d1cc3dbefbe7) method of the [ICells](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/) collection. The [InsertRow](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/#ad9c067ccb5f34a7740f5d1cc3dbefbe7) method takes the index of the row where the new row will be inserted.

#### Inserting Multiple Rows

To insert multiple rows into a worksheet, call the [InsertRows](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/#a61e4cd6dcaeeb0d11afd54616df75ee0) method of the [ICells](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/) collection. The [InsertRows](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/#a61e4cd6dcaeeb0d11afd54616df75ee0) method takes two parameters:

*   Row index, the index of the row from where the new rows will be inserted.
*   Number of rows, the total number of rows that need to be inserted.

#### Deleting Multiple Rows

To delete multiple rows from a worksheet, call the [DeleteRows](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/#a251261027b564ebdf27c2c6d5149c0e1) method of the [ICells](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/) collection. The [DeleteRows](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/#a251261027b564ebdf27c2c6d5149c0e1) method takes two parameters:

*   Row index, the index of the row from where the rows will be deleted.
*   Number of rows, the total number of rows that need to be deleted.

#### Insert a Column

Developers can also insert a column into the worksheet at any location by calling the [InsertColumn](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/#a8e8cb6d0812129669258378649b3fd55) method of the [ICells](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/) collection. [InsertColumn](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/#a8e8cb6d0812129669258378649b3fd55) method takes the index of the column where the new column will be inserted.

#### Delete a Column

To delete a column from the worksheet at any location, call the [DeleteColumn](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/#ae00721fd2be220e7b73b2cab6a70e89b) method of the [ICells](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/) collection. The [DeleteColumn](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/#ae00721fd2be220e7b73b2cab6a70e89b) method takes the index of the column to delete.

