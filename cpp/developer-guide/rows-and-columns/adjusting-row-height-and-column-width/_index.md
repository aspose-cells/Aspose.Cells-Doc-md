---
title: Adjusting Row Height and Column Width
type: docs
weight: 10
url: /cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

When working with spreadsheets and adding data to rows or columns, you might need to change the height of rows or the width of columns. Sometimes, applying formatting on rows or columns means that the current height or width needs to change to show the data. Normally, users adjust row heights and column widths in a WYSIWYG environment using Microsoft Excel. But, with Aspose.Cells developers can perform these operations at runtime.

{{% /alert %}} 
## **Working with Rows**
### **Adjusting Row Height**
Aspose.Cells provides a class, [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook/) that represents a Microsoft Excel file. The [IWorkbook](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_workbook/) class contains a [IWorksheetCollection](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection/) that allows access to each worksheet in the Excel file. A worksheet is represented by the [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet/) class. The [IWorksheet](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet/) class provides a [ICells](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/) collection that represents all cells in the worksheet. The [ICells](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/) collection provides several methods to manage rows or columns in a worksheet. Some of these are discussed below in more detail.
#### **Setting the Height of a Row**
It is possible to set the height of a single row by calling the [ICells](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/) collection's [SetRowHeight](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/#a7aa441877e03639232299627261a7d1f) method. The [SetRowHeight](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/#a7aa441877e03639232299627261a7d1f) method takes the following parameters as follows:

- **Row index**, the index of the row that you're changing the height of.
- **Row height**, the row height to apply on the row.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow.cpp" >}}


#### **Setting the Height of All Rows in a Worksheet**
If developers need to set the same row height for all rows in the worksheet, they can do it by using the [SetStandardHeight](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/#a0b79a3163e2b601aa1b6a6a1e3f1467f) method of the [ICells](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/) collection.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet.cpp" >}}
## **Working with Columns**
### **Setting the Width of a Column**
Set the width of a column by calling the [ICells](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/) collection's [SetColumnWidth](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/#ab1c6a4e89760d2a022d5bfba8bc40987) method. The [SetColumnWidth](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/#ab1c6a4e89760d2a022d5bfba8bc40987) method takes the following parameters:

- **Column index**, the index of the column that you're changing the width of.
- **Column width**, the desired column width.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn.cpp" >}}
### **Setting the Width of All Columns in a Worksheet**
To set the same column width for all columns in the worksheet, use the [ICells](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/) collection's [SetStandardWidth](https://apireference.aspose.com/cells/cpp/class/aspose.cells.i_cells/#a48f5dbccc3bf4bb9e6e882094b500bd7) method.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet.cpp" >}}
