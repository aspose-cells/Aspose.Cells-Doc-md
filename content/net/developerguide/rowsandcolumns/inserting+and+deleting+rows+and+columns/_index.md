---
title : "Inserting and Deleting Rows and Columns" 
description : "" 
weight : 12187 
toc : false
type: docs
url: /net/developerguide/rowsandcolumns/inserting+and+deleting+rows+and+columns/
---

# Aspose.Cells for .NET : Inserting and Deleting Rows and Columns


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#introduction)
*   2 [Managing Rows and Columns](#managing-rows-and-columns)
    *   2.1 [Insert a Row](#insert-a-row)
    *   2.2 [Inserting Multiple Rows](#inserting-multiple-rows)
    *   2.3 [Insert a Row with Formatting](#insert-a-row-with-formatting)
    *   2.4 [Deleting Multiple Rows](#deleting-multiple-rows)
    *   2.5 [Insert a Column](#insert-a-column)
    *   2.6 [Delete a Column](#delete-a-column)
{{< /panel >}}
 

## Introduction

Whether creating a new worksheet from scratch or working on an existing worksheet, we may need to add extra rows or columns to accommodate more data. Inversely, we may also need to delete rows or columns from specified positions in the worksheet.  
To fulfill these requirements, Aspose.Cells provides a very simplest set of classes and methods, discussed below.

## Managing Rows and Columns

Aspose.Cells provides a class [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection that represents all cells in the worksheet.

The [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection provides several methods managing rows and columns in a worksheet. Some of these are discussed below.

When rows or columns are added, the content in the worksheet is shifted down or to the right, and if rows or columns are removed, the content is shifted up or the left.

#### Insert a Row

Insert a row into the worksheet at any location by calling the [InsertRow](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/insertrow) method of the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. The [InsertRow](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/insertrow) method takes the index of the row where the new row will be inserted.

#### Inserting Multiple Rows

To insert multiple rows into a worksheet, call the [InsertRows](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/insertrows) method of the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. The [InsertRows](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/insertrows) method takes two parameters:

*   Row index, the index of the row from where the new rows will be inserted.
*   Number of rows, the total number of rows that need to be inserted.

#### Insert a Row with Formatting

To insert a row with formatting options, use the [InsertRows](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/insertrows) overload that takes [InsertOptions](https://apireference.aspose.com/net/cells/aspose.cells/insertoptions) as a parameter. Set the [CopyFormatType](https://apireference.aspose.com/net/cells/aspose.cells/insertoptions/properties/copyformattype) property of [InsertOptions](https://apireference.aspose.com/net/cells/aspose.cells/insertoptions) class with [CopyFormatType](https://apireference.aspose.com/net/cells/aspose.cells/copyformattype) Enumeration. The [CopyFormatType](https://apireference.aspose.com/net/cells/aspose.cells/copyformattype) Enumeration has three members as listed below.

*   SameAsAbove: Formats the row same as the above row.
*   SameAsBelow: Formats the row same as below row.
*   Clear: Clears the formatting.

#### Deleting Multiple Rows

To delete multiple rows from a worksheet, call the [DeleteRows](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/deleterows) method of the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. The [DeleteRows](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/deleterows) method takes two parameters:

*   Row index, the index of the row from where the rows will be deleted.
*   Number of rows, the total number of rows that need to be deleted.

#### Insert a Column

Developers can also insert a column into the worksheet at any location by calling the [InsertColumn](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/insertcolumn) method of the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. The [InsertColumn](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/insertcolumn) method takes the index of the column where the new column will be inserted.

#### Delete a Column

To delete a column from the worksheet at any location, call the [DeleteColumn](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/deletecolumn) method of the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. The [DeleteColumn](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/deletecolumn) method takes the index of the column to delete.

