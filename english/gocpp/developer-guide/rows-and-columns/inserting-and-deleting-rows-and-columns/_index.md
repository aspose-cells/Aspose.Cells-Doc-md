---
title: Inserting and Deleting Rows and Columns of an Excel File with Golang via C++
linktitle: Inserting and Deleting Rows and Columns
type: docs
weight: 70
url: /go-cpp/inserting-and-deleting-rows-and-columns/
description: This article shows how to insert and delete rows and columns using the Aspose.Cells for Go via Go API.
keywords: Aspose.Cells Go manage rows and columns, insert rows and columns, delete rows and columns
---

## **Introduction**

Whether creating a new worksheet from scratch or working on an existing worksheet, we may need to add extra rows or columns to accommodate more data. Conversely, we may also need to delete rows or columns from specified positions in the worksheet.  
To fulfill these requirements, Aspose.Cells provides a very simple set of classes and methods, discussed below.

### **Manage Rows and Columns**

Aspose.Cells provides a class [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides a **GetCells()** collection that represents all cells in the worksheet.

The **GetCells()** collection provides several methods for managing rows and columns in a worksheet. Some of these are discussed below.

{{% alert color="primary" %}}

When rows or columns are added, the content in the worksheet is shifted down or to the right, and if rows or columns are removed, the content is shifted up or to the left.

{{% /alert %}}

## **Insert Rows and Columns**

### **How to Insert a Row**

Insert a row into the worksheet at any location by calling the **InsertRow** method of the **GetCells()** collection. The **InsertRow** method takes the index of the row where the new row will be inserted.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingAndDeletingRowsAndColumns.go" >}}

### **How to Insert Multiple Rows**

To insert multiple rows into a worksheet, call the **InsertRows** method of the **GetCells()** collection. The **InsertRows** method takes two parameters:

- **Row index** – the index of the row from where the new rows will be inserted.  
- **Number of rows** – the total number of rows that need to be inserted.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingAndDeletingRowsAndColumns-1.go" >}}

### **How to Insert a Row with Formatting**

To insert a row with formatting options, use the **InsertRows** overload that takes **InsertOptions** as a parameter. Set the **CopyFormatType** property of the **InsertOptions** class using the **CopyFormatType** enumeration. The **CopyFormatType** enumeration has three members as listed below.

- **SameAsAbove** – Formats the row the same as the row above.  
- **SameAsBelow** – Formats the row the same as the row below.  
- **Clear** – Clears the formatting.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingAndDeletingRowsAndColumns-2.go" >}}

### **How to Insert a Column**

You can also insert a column into the worksheet at any location by calling the **InsertColumn** method of the **GetCells()** collection. The **InsertColumn** method takes the index of the column where the new column will be inserted.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingAndDeletingRowsAndColumns-3.go" >}}

## **Delete Rows and Columns**

### **How to Delete Multiple Rows**

To delete multiple rows from a worksheet, call the **DeleteRows** method of the **GetCells()** collection. The **DeleteRows** method takes two parameters:

- **Row index** – the index of the row from where the rows will be deleted.  
- **Number of rows** – the total number of rows that need to be deleted.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingAndDeletingRowsAndColumns-4.go" >}}

### **How to Delete a Column**

To delete a column from the worksheet at any location, call the **DeleteColumn** method of the **GetCells()** collection. The **DeleteColumn** method takes the index of the column to delete.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingAndDeletingRowsAndColumns-5.go" >}}
{{< app/cells/assistant language="go" >}}
