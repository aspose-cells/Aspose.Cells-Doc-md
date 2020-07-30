---
title : "Adjusting Row Height and Column Width" 
description : "" 
weight : 12152 
toc : false
type: docs
url: /java/developerguide/rowsandcolumns/adjusting+row+height+and+column+width/
---

# Aspose.Cells for Java : Adjusting Row Height and Column Width


When working with spreadsheets and adding data to rows or columns, you might need to change the height of rows or width of columns. Sometimes, applying formatting to rows or columns means that the current height or width needs to change to show the data. Normally, users adjust row heights and column widths in a WYSIWYG environment using Microsoft Excel. But, with Aspose.Cells developers can perform these operations at runtime. Indexes of rows and columns will start from 0.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Working with Rows](#working-with-rows)
    *   1.1 [Adjusting Row Height](#adjusting-row-height)
    *   1.2 [Setting the Row Height](#setting-the-row-height)
    *   1.3 [Setting the Height of All Rows](#setting-the-height-of-all-rows)
*   2 [Working with Columns](#working-with-columns)
    *   2.1 [Setting the Width of a Column](#setting-the-width-of-a-column)
    *   2.2 [Setting the Width of All Columns](#setting-the-width-of-all-columns)
{{< /panel >}}
 

 

## Working with Rows

### Adjusting Row Height

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook) class contains a [WorksheetCollection](https://apireference.aspose.com/java/cells/com.aspose.cells/WorksheetCollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class. The [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class provides a [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection that represents all cells in the worksheet.

The [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection provides several methods to manage rows or columns in a worksheet. Some of these are discussed below in more detail.

### Setting the Row Height

It is possible to set the height of a single row by calling the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection's [setRowHeight](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#setRowHeight(int,%20double)) method. The [setRowHeight](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#setRowHeight(int,%20double)) method takes the following parameters:

*   **Row index**, the index of the row that you're changing the height of.
*   **Row height**, the row height to apply on the row.


### Setting the Height of All Rows

To set the same row height for all rows in a worksheet, use the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection's [setStandardHeight](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#StandardHeight) method.

## Working with Columns

### Setting the Width of a Column

Set the width of a column by calling the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection's [setColumnWidth](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#setColumnWidth(int,%20double)) method. The [setColumnWidth](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#setColumnWidth(int,%20double)) method takes the following parameters:

*   **Column index**, the index of the column that you're changing the width of.
*   **Column width**, the desired column width.

### Setting the Width of All Columns

To set the same column width for all columns in a worksheet, use the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) collection's [setStandardWidth](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#StandardWidth) method.

