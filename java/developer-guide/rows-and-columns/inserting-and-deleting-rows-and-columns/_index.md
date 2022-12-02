---
title: Inserting and Deleting Rows and Columns
type: docs
weight: 60
url: /java/inserting-and-deleting-rows-and-columns/
---

## **Introduction**
Whether creating a new worksheet from scratch or working on an existing worksheet, we may need to add extra rows or columns to accommodate more data. Inversely, we may also need to delete rows or columns from specified positions in the worksheet.

To fulfill these requirements, Aspose.Cells provides a very simplest set of classes and methods, discussed below.
## **Managing Rows/Columns**
Aspose.Cells provides a [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class contains a [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) that allows access to each worksheet in an Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class. The [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class provides a [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) collection that represents all cells in the worksheet.

The [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) collection provides several methods for managing rows and columns in a worksheet. Some of these are discussed below.

{{% alert color="primary" %}} 

When rows or columns are added, the content in the worksheet is shifted down or to the right, but if rows or columns are removed, the content is shifted up or the left.

{{% /alert %}} 
## **Inserting a Row**
Insert a row into at any location by calling the [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) method of the [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection. The [insertRows ](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))method takes the index of the row where the new row will be inserted as the first argument, and the number of rows to be inserted as the second argument.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **Inserting Multiple Rows**
To insert multiple rows into the worksheet, call the [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) method of the [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection. The [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) method takes two parameters:

- Row index: the index of the row from where the new rows will be inserted.
- Number of rows: the total number of rows that need to be inserted.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **Insert a Row with Formatting**
To insert a row with formatting options, use the [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)) overload that takes [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) as a parameter. Set the [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType) property of [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) class with [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) Enumeration. The [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) Enumeration has three members as listed below.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE): Formats the row same as the above row.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW):  Formats the row same as below row.
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): Clears the formatting.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **Deleting a Row**
To delete a row at any location, call the [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) method of the [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection. The [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) method takes two parameters:

- Row index: the index of the row from where the rows will be deleted.
- Number of rows: the total number of rows that need to be deleted.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **Deleting Multiple Rows**
To delete multiple rows from a worksheet, call the [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) method of the [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection. The [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) method takes two parameters:

- Row index: the index of the row from where the rows will be deleted.
- Number of rows: the total number of rows that need to be deleted.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **Inserting one or Multiple Columns**
Developers can also insert a column into the worksheet at any location by calling the [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) method of the [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection. The [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) method takes two parameters:

- Column index, the index of the column from where the column will be inserted
- Number of columns, the total number of columns that need to be inserted

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **Deleting a Column**
To delete a column from the worksheet at any location, call the [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) method of the [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection. The [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) method takes the following parameters:

- Column index: the index of the column from where the column will be deleted.
- Number of columns: the total number of columns that need to be deleted.
- Update Reference: Boolean parameter to indicate whether to update references in other worksheets.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

