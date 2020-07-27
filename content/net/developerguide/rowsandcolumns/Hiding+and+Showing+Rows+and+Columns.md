+++
title = "Hiding and Showing Rows and Columns" 
description = "" 
weight = 12186 
+++

Aspose.Cells for .NET : Hiding and Showing Rows and Columns  

# Aspose.Cells for .NET : Hiding and Showing Rows and Columns


Sometimes, it makes sense to hide certain rows or columns in a worksheet and display them later. Microsoft Excel provides this feature and so does Aspose.Cells.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Controlling the Visibility of Rows and Columns](#HidingandShowingRowsandColumns-ControllingtheVisibilityofRowsandColumns)
    *   1.1 [Hiding Rows and Columns](#HidingandShowingRowsandColumns-HidingRowsandColumns)
    *   1.2 [Showing Rows and Columns](#HidingandShowingRowsandColumns-ShowingRowsandColumns)
    *   1.3 [Hiding Multiple Rows and Columns](#HidingandShowingRowsandColumns-HidingMultipleRowsandColumns)
{{< /panel >}}
 

 

## Controlling the Visibility of Rows and Columns

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [WorksheetCollection](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection) that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection that represents all cells in the worksheet. The [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection provides several methods for managing rows or columns in a worksheet. A few of these are discussed below.

### Hiding Rows and Columns

Developers can hide a row or column by calling the [HideRow](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/hiderow) and [HideColumn](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/hidecolumn) methods of the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection respectively. Both methods take the row and column index as a parameter to hide the specific row or column.

It is also possible to hide a row or column by setting the row height or column width to 0 respectively.

### Showing Rows and Columns

Developers can show any hidden row or column by calling the [UnhideRow](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/unhiderow) and [UnhideColumn](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/unhidecolumn) methods of the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection respectively. Both methods take two parameters:

*   **Row or column index** - the index of a row or column that is used to show the specific row or column.
*   **Row height or column width** - the row height or column width assigned to the row or column after unhiding.

While making a hidden column visible, if you need to restore it to previously assigned width or to its original width, please unhide the column with a negative width. For example: `worksheet.Cells.UnhideColumn(5, -1)`

### Hiding Multiple Rows and Columns

Developers can hide multiple rows or columns at once by calling the [HideRows](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/hiderows) and [HideColumns](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/hidecolumns) methods of the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection respectively. Both methods take the starting row or column index and the number of rows or columns that should be hidden as parameters.

It is also possible to use the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) class' [UnhideRows](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/unhiderows) and [UnhideColumns](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/unhidecolumns) methods to make multiple rows and columns visible.

