---
title: Format Rows and Columns
linktitle: Rows and Columns
type: docs
weight: 100
url: /net/adjusting-row-height-and-column-width/
---


{{% alert color="primary" %}}

When working with spreadsheets and adding data to rows or columns, you might need to change the height of rows or width of columns. Sometimes, applying formatting on rows or columns means that the current height or width needs to change to show the data. Normally, users adjust row heights and column widths in a WYSIWYG environment using Microsoft Excel. But, with Aspose.Cells developers can perform these operations at runtime.

{{% /alert %}}

## **Working with Rows**

### **Adjusting Row Height**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection that represents all cells in the worksheet.

The [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection provides several methods to manage rows or columns in a worksheet. Some of these are discussed below in more detail.

### **Setting the Height of a Row**

It is possible to set the height of a single row by calling the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection's [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) method. The [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) method takes the following parameters as follows:

- **Row index**, the index of the row that you're changing the height of.
- **Row height**, the row height to apply on the row.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **Setting the Height of All Rows in a Worksheet**

If developers need to set the same row height for all rows in the worksheet, they can do it by using the [**StandardHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) property of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection.

**Example:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **Working with Columns**

### **Setting the Width of a Column**

Set the width of a column by calling the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection's [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) method. The [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) method takes the following parameters:

- **Column index**, the index of the column that you're changing the width of.
- **Column width**, the desired column width.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **Setting Column Width in Pixels**

Set the width of a column by calling the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection's [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) method. The [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) method takes the following parameters:

- **Column index**, the index of the column that you're changing the width of.
- **Column width**, the desired column width in pixels.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **Setting the Width of All Columns in a Worksheet**

To set the same column width for all columns in the worksheet, use the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection's [**StandardWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **Advance topics**
- [AutoFit Rows and Columns](/cells/net/autofit-rows-and-columns/)
- [Convert Text to Columns using Aspose.Cells](/cells/net/convert-text-to-columns-using-aspose-cells/)
- [Copying Rows and Columns](/cells/net/copying-rows-and-columns/)
- [Delete Blank Rows and Columns in a Worksheet](/cells/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Grouping and Ungrouping Rows and Columns](/cells/net/grouping-and-ungrouping-rows-and-columns/)
- [Hiding and Showing Rows and Columns](/cells/net/hiding-and-showing-rows-and-columns/)
- [Insert or Delete Rows in an Excel Worksheet](/cells/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Inserting and Deleting Rows and Columns of Excel file](/cells/net/inserting-and-deleting-rows-and-columns/)
- [Remove duplicate rows in a Worksheet](/cells/net/remove-duplicate-rows-in-a-worksheet/)
- [Update references in other worksheets while deleting blank columns and rows in a worksheet](/cells/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
