---
title: Inserting, Deleting Rows and Columns
type: docs
weight: 40
url: /go-cpp/inserting-deleting-rows-and-columns/
---

## **Introduction**

Whether creating a new worksheet from scratch or working on an existing worksheet, we may need to add extra rows or columns to accommodate more data. Inversely, we may also need to delete rows or columns from specified positions in the worksheet. To fulfill these requirements, Aspose.Cells provides a very simplest set of classes and methods, discussed below.

### **Managing Rows and Columns**

Aspose.Cells provides a class, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) class contains an [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class. The [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides an [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection that represents all cells in the worksheet.

The [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection provides several methods managing rows and columns in a worksheet. Some of these are discussed below.

{{% alert color="primary" %}}

When rows or columns are added, the content in the worksheet is shifted down or to the right, and if rows or columns are removed, the content is shifted up or the left.

{{% /alert %}}

Insert a row into the worksheet at any location by calling the [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) method of the [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection. The [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) method takes the index of the row where the new row will be inserted.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertRow.go" >}}

#### **Inserting Multiple Rows**

To insert multiple rows into a worksheet, call the [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrows_int_int/) method of the [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection. The [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrowinsertrows_int_ints/) method takes two parameters:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingMultipleRows.go" >}}

#### **Deleting Multiple Rows**

To delete multiple rows from a worksheet, call the [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) method of the [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection. The [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) method takes two parameters:

- Row index, the index of the row from where the rows will be deleted.
- Number of rows, the total number of rows that need to be deleted.

#### **Insert a Column**

Developers can also insert a column into the worksheet at any location by calling the [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) method of the [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection. [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) method takes the index of the column where the new column will be inserted.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertColumn.go" >}}

To delete a column from the worksheet at any location, call the [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) method of the [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection. The [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) method takes the index of the column to delete.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteColumn.go" >}}
