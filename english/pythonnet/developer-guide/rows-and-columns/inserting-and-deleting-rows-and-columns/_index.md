---
title: Inserting and Deleting Rows and Columns of Excel file
linktitle: Inserting and Deleting Rows and Columns
type: docs
weight: 70
url: /python-net/inserting-and-deleting-rows-and-columns/
description: This article shows how to insert and delete rows and columns by the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Aspose.Cells Python manage rows and columns, Python insert rows and columns, Python delete rows and columns, Python Remove rows and columns.
---

## **Introduction**

Whether creating a new worksheet from scratch or working on an existing worksheet, we may need to add extra rows or columns to accommodate more data. Inversely, we may also need to delete rows or columns from specified positions in the worksheet.
To fulfill these requirements, Aspose.Cells for Python via .NET provides a very simplest set of classes and methods, discussed below.

### **Manage Rows and Columns**

Aspose.Cells for Python via .NET provides a class [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection that represents all cells in the worksheet.

The [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection provides several methods managing rows and columns in a worksheet. Some of these are discussed below.

{{% alert color="primary" %}}

When rows or columns are added, the content in the worksheet is shifted down or to the right, and if rows or columns are removed, the content is shifted up or the left.

{{% /alert %}}


## **Insert Rows and Columns**

### **How to Insert a Row**

Insert a row into the worksheet at any location by calling the [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) method of the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection. The [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) method takes the index of the row where the new row will be inserted.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARow-1.py" >}}

### **How to Insert Multiple Rows**

To insert multiple rows into a worksheet, call the [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) method of the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection. The [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) method takes two parameters:

- Row index, the index of the row from where the new rows will be inserted.
- Number of rows, the total number of rows that need to be inserted.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.py" >}}

### **How to Insert a Row with Formatting**

To insert a row with formatting options, use the [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int-aspose.cells.InsertOptions) overload that takes [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) as a parameter. Set the [**copy_format_type**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions/copy_format_type/) property of [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) class with [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/) Enumeration. The [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/) Enumeration has three members as listed below.

- SAME_AS_ABOVE: Formats the row same as the above row.
- SAME_AS_BELOW:  Formats the row same as below row.
- CLEAR: Clears the formatting.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.py" >}}

### **How to Insert a Column**

Developers can also insert a column into the worksheet at any location by calling the [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) method of the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection. The [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) method takes the index of the column where the new column will be inserted.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingAColumn-1.py" >}}

## **Delete Rows and Columns**

### **How to Delete Multiple Rows**

To delete multiple rows from a worksheet, call the [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) method of the [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection. The [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) method takes two parameters:

- Row index, the index of the row from where the rows will be deleted.
- Number of rows, the total number of rows that need to be deleted.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.py" >}}


### **How to Delete a Column**

To delete a column from the worksheet at any location, call the [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) method of the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection. The [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) method takes the index of the column to delete.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingAColumn-1.py" >}}
{{< app/cells/assistant language="python-net" >}}