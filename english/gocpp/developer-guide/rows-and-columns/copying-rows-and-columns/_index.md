---
title: Copying Rows and Columns
type: docs
weight: 20
url: /go-cpp/copying-rows-and-columns/
---

## **Introduction**

Sometimes you need to copy rows and columns in a worksheet without copying the entire worksheet. With Aspose.Cells, it is possible to copy rows and columns within or between workbooks.  
When a row (or column) is copied, the data contained in it, including formulas - with updated references - and values, comments, formatting, hidden cells, images and other drawing objects **are** copied too.

## **Copying Rows and Columns with Microsoft Excel**

1. Select the row or column that you want to copy.  
2. To copy rows or columns, click **Copy** on the **Standard** toolbar, or press **CTRL**+**C**.  
3. Select a row or column below or to the right of where you want to copy your selection.  
4. When you are copying rows or columns, click **Copied Cells** on the **Insert** menu.  

{{% alert color="primary" %}}

If you click **Paste** on the **Standard** toolbar or press **CTRL**+**V** instead of clicking a command on the **Insert** menu, any contents of the destination cells **are** replaced.

{{% /alert %}}

## **Using Aspose.Cells**

### **Copying Rows**

Aspose.Cells provides the `CopyRow` method of the `Aspose::Cells::ICells` class. This method copies all types of data including formulas, values, comments, cell formats, hidden cells, images and other drawing objects from the source row to the destination row.

The `CopyRow` method takes the following parameters:

- the source `Cells` object,
- the source row index, and
- the destination row index.

Use this method to copy a row within a sheet, or to another sheet. The `CopyRow` method works in a similar way to Microsoft Excel. So, for example, you don't need to set the height of the destination row explicitly; that value is copied too.

The following example shows how to copy a row in a worksheet. It uses a template Microsoft Excel file and copies the second row (complete with data, formatting, comments, images and so on) and **pasts** it to the 12th row in the same worksheet.

You can skip the step that gets the source row height using the **GetRowHeight** method and then sets the destination row height using the **SetRowHeight** method**,** as the **CopyRow** method automatically takes care of the row height.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyingRows.go" >}}

{{% alert color="primary" %}}

When copying rows, it is important to note related images, charts or other drawing objects **as this is the same as** Microsoft Excel:

1. If the source row index is 5, the image, chart, etc., is copied if it is contained in the three rows (the starting row index is 4 and the ending row index is 6).  
2. The existing images, charts, etc., in the destination row will not be removed.

{{% /alert %}}

### **Copying Columns**

Aspose.Cells provides the `CopyColumn` method of the `ICells` class; this method copies all types of data, including formulas - with updated references - and values, comments, cell formats, hidden cells, images and other drawing objects from the source column to the destination column.

The `CopyColumn` method takes the following parameters:

- the source `Cells` object,
- source column index, and
- the destination column index.

Use the `CopyColumn` method to copy a column within a sheet or to another sheet.

This example copies a column from a worksheet and pastes it into a worksheet in another workbook.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyingColumns.go" >}}