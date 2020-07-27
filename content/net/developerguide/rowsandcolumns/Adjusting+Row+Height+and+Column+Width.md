+++
title = "Adjusting Row Height and Column Width" 
description = "" 
weight = 12181 
+++

Aspose.Cells for .NET : Adjusting Row Height and Column Width  

# Aspose.Cells for .NET : Adjusting Row Height and Column Width


When working with spreadsheets and adding data to rows or columns, you might need to change the height of rows or width of columns. Sometimes, applying formatting on rows or columns means that the current height or width needs to change to show the data. Normally, users adjust row heights and column widths in a WYSIWYG environment using Microsoft Excel. But, with Aspose.Cells developers can perform these operations at runtime.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Working with Rows](#AdjustingRowHeightandColumnWidth-WorkingwithRows)
    *   1.1 [Adjusting Row Height](#AdjustingRowHeightandColumnWidth-AdjustingRowHeight)
        *   1.1.1 [Setting the Height of a Row](#AdjustingRowHeightandColumnWidth-SettingtheHeightofaRow)
        *   1.1.2 [Setting the Height of All Rows in a Worksheet](#AdjustingRowHeightandColumnWidth-SettingtheHeightofAllRowsinaWorksheet)
*   2 [Working with Columns](#AdjustingRowHeightandColumnWidth-WorkingwithColumns)
    *   2.1 [Setting the Width of a Column](#AdjustingRowHeightandColumnWidth-SettingtheWidthofaColumn)
    *   2.2 [Setting Column Width in Pixels](#AdjustingRowHeightandColumnWidth-SettingColumnWidthinPixels)
    *   2.3 [Setting the Width of All Columns in a Worksheet](#AdjustingRowHeightandColumnWidth-SettingtheWidthofAllColumnsinaWorksheet)
{{< /panel >}}
 

 

## Working with Rows

### Adjusting Row Height

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [WorksheetCollection](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection that represents all cells in the worksheet.

The [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection provides several methods to manage rows or columns in a worksheet. Some of these are discussed below in more detail.

#### Setting the Height of a Row

It is possible to set the height of a single row by calling the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection's [SetRowHeight](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/setrowheight) method. The [SetRowHeight](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/setrowheight) method takes the following parameters as follows:

*   **Row index**, the index of the row that you're changing the height of.
*   **Row height**, the row height to apply on the row.

#### Setting the Height of All Rows in a Worksheet

If developers need to set the same row height for all rows in the worksheet, they can do it by using the [StandardHeight](https://apireference.aspose.com/net/cells/aspose.cells/cells/properties/standardheight) property of the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection.

**Example:**

## Working with Columns

### Setting the Width of a Column

Set the width of a column by calling the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection's [SetColumnWidth](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/setcolumnwidth) method. The [SetColumnWidth](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/setcolumnwidth) method takes the following parameters:

*   **Column index**, the index of the column that you're changing the width of.
*   **Column width**, the desired column width.

### Setting Column Width in Pixels

Set the width of a column by calling the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection's [SetColumnWidthPixel](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/setcolumnwidthpixel) method. The [SetColumnWidthPixel](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/setcolumnwidthpixel) method takes the following parameters:

*   **Column index**, the index of the column that you're changing the width of.
*   **Column width**, the desired column width in pixels.

### Setting the Width of All Columns in a Worksheet

To set the same column width for all columns in the worksheet, use the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection's [StandardWidth](https://apireference.aspose.com/net/cells/aspose.cells/cells/properties/standardwidth) property.

