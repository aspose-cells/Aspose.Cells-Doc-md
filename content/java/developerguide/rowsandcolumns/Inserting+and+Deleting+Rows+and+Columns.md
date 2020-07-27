+++
title = "Inserting and Deleting Rows and Columns" 
description = "" 
weight = 12157 
+++

Aspose.Cells for Java : Inserting and Deleting Rows and Columns  

# Aspose.Cells for Java : Inserting and Deleting Rows and Columns


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#InsertingandDeletingRowsandColumns-Introduction)
*   2 [Managing Rows/Columns](#InsertingandDeletingRowsandColumns-ManagingRows/Columns)
    *   2.1 [Inserting a Row](#InsertingandDeletingRowsandColumns-InsertingaRow)
    *   2.2 [Inserting Multiple Rows](#InsertingandDeletingRowsandColumns-InsertingMultipleRows)
    *   2.3 [Insert a Row with Formatting](#InsertingandDeletingRowsandColumns-InsertaRowwithFormatting)
    *   2.4 [Deleting a Row](#InsertingandDeletingRowsandColumns-DeletingaRow)
    *   2.5 [Deleting Multiple Rows](#InsertingandDeletingRowsandColumns-DeletingMultipleRows)
    *   2.6 [Inserting one or Multiple Columns](#InsertingandDeletingRowsandColumns-InsertingoneorMultipleColumns)
    *   2.7 [Deleting a Column](#InsertingandDeletingRowsandColumns-DeletingaColumn)
{{< /panel >}}
 

 

### Introduction

Whether creating a new worksheet from scratch or working on an existing worksheet, we may need to add extra rows or columns to accommodate more data. Inversely, we may also need to delete rows or columns from specified positions in the worksheet.

To fulfill these requirements, Aspose.Cells provides a very simplest set of classes and methods, discussed below.

### Managing Rows/Columns

Aspose.Cells provides a [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook) class that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook) class contains a [WorksheetCollection](https://apireference.aspose.com/java/cells/com.aspose.cells/WorksheetCollection) that allows access to each worksheet in an Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class. The [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class provides a [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection that represents all cells in the worksheet.

The [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection provides several methods for managing rows and columns in a worksheet. Some of these are discussed below.

When rows or columns are added, the content in the worksheet is shifted down or to the right, but if rows or columns are removed, the content is shifted up or the left.

#### Inserting a Row

Insert a row into at any location by calling the [insertRows](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#insertRows(int,%20int)) method of the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection. The [insertRows ](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#insertRows(int,%20int))method takes the index of the row where the new row will be inserted as the first argument, and the number of rows to be inserted as the second argument.


#### Inserting Multiple Rows

To insert multiple rows into the worksheet, call the [insertRows](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#insertRows(int,%20int)) method of the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection. The [insertRows](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#insertRows(int,%20int)) method takes two parameters:

*   Row index: the index of the row from where the new rows will be inserted.
*   Number of rows: the total number of rows that need to be inserted.  
      
    

#### Insert a Row with Formatting

To insert a row with formatting options, use the [insertRows](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#insertRows(int,%20int,%20com.aspose.cells.InsertOptions)) overload that takes [InsertOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/InsertOptions) as a parameter. Set the [CopyFormatType](https://apireference.aspose.com/java/cells/com.aspose.cells/insertoptions#CopyFormatType) property of [InsertOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/InsertOptions) class with [CopyFormatType](https://apireference.aspose.com/java/cells/com.aspose.cells/CopyFormatType) Enumeration. The [CopyFormatType](https://apireference.aspose.com/java/cells/com.aspose.cells/CopyFormatType) Enumeration has three members as listed below.

*   [SAME\_AS\_ABOVE](https://apireference.aspose.com/java/cells/com.aspose.cells/copyformattype#SAME_AS_ABOVE): Formats the row same as the above row.
*   [SAME\_AS\_BELOW](https://apireference.aspose.com/java/cells/com.aspose.cells/copyformattype#SAME_AS_BELOW):  Formats the row same as below row.
*   [CLEAR](https://apireference.aspose.com/java/cells/com.aspose.cells/copyformattype#CLEAR): Clears the formatting.  
      
    

#### Deleting a Row

To delete a row at any location, call the [deleteRows](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#deleteRows(int,%20int)) method of the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection. The [deleteRows](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#deleteRows(int,%20int)) method takes two parameters:

*   Row index: the index of the row from where the rows will be deleted.
*   Number of rows: the total number of rows that need to be deleted.  
      
    

#### Deleting Multiple Rows

To delete multiple rows from a worksheet, call the [deleteRows](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#deleteRows(int,%20int)) method of the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection. The [deleteRows](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#deleteRows(int,%20int)) method takes two parameters:

*   Row index: the index of the row from where the rows will be deleted.
*   Number of rows: the total number of rows that need to be deleted.  
      
    

#### Inserting one or Multiple Columns

Developers can also insert a column into the worksheet at any location by calling the [insertColumns](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#insertColumns(int,%20int)) method of the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection. The [insertColumns](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#insertColumns(int,%20int)) method takes two parameters:

*   Column index, the index of the column from where the column will be inserted
*   Number of columns, the total number of columns that need to be inserted  
      
    

#### Deleting a Column

To delete a column from the worksheet at any location, call the [deleteColumns](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#deleteColumns(int,%20int,%20boolean)) method of the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection. The [deleteColumns](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#deleteColumns(int,%20int,%20boolean)) method takes the following parameters:

*   Column index: the index of the column from where the column will be deleted.
*   Number of columns: the total number of columns that need to be deleted.
*   Update Reference: Boolean parameter to indicate whether to update references in other worksheets.  
      
    

