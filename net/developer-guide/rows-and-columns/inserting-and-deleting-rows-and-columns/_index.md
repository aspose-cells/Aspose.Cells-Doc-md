---
title: Inserting and Deleting Rows and Columns
type: docs
weight: 70
url: /net/inserting-and-deleting-rows-and-columns/
---

## **Introduction**

Whether creating a new worksheet from scratch or working on an existing worksheet, we may need to add extra rows or columns to accommodate more data. Inversely, we may also need to delete rows or columns from specified positions in the worksheet.
To fulfill these requirements, Aspose.Cells provides a very simplest set of classes and methods, discussed below.

### **Manage Rows and Columns**

Aspose.Cells provides a class [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection that represents all cells in the worksheet.

The [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection provides several methods managing rows and columns in a worksheet. Some of these are discussed below.

{{% alert color="primary" %}}

When rows or columns are added, the content in the worksheet is shifted down or to the right, and if rows or columns are removed, the content is shifted up or the left.

{{% /alert %}}


## **Insert Rows and Columns **

### **Insert a Row**

Insert a row into the worksheet at any location by calling the [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) method of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection. The [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) method takes the index of the row where the new row will be inserted.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **Insert Multiple Rows**

To insert multiple rows into a worksheet, call the [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) method of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection. The [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) method takes two parameters:

- Row index, the index of the row from where the new rows will be inserted.
- Number of rows, the total number of rows that need to be inserted.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **Insert a Row with Formatting**

To insert a row with formatting options, use the [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) overload that takes [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) as a parameter. Set the [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) property of [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) class with [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Enumeration. The [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Enumeration has three members as listed below.

- SameAsAbove: Formats the row same as the above row.
- SameAsBelow:  Formats the row same as below row.
- Clear: Clears the formatting.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **Insert a Column**

Developers can also insert a column into the worksheet at any location by calling the [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) method of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection. The [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) method takes the index of the column where the new column will be inserted.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **Delete Rows and Columns **

### **Delete Multiple Rows**

To delete multiple rows from a worksheet, call the [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) method of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection. The [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) method takes two parameters:

- Row index, the index of the row from where the rows will be deleted.
- Number of rows, the total number of rows that need to be deleted.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **Delete a Column**

To delete a column from the worksheet at any location, call the [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) method of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection. The [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) method takes the index of the column to delete.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
