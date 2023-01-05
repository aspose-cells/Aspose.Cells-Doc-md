---
title: Hiding and Showing Rows and Columns
type: docs
weight: 60
url: /net/hiding-and-showing-rows-and-columns/
---

{{% alert color="primary" %}}

Sometimes, it makes sense to hide certain rows or columns in a worksheet and display them later. Microsoft Excel provides this feature and so does Aspose.Cells.

{{% /alert %}}

## **Controlling the Visibility of Rows and Columns**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection that represents all cells in the worksheet. The [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection provides several methods for managing rows or columns in a worksheet. A few of these are discussed below.

### **Hiding Rows and Columns**

Developers can hide a row or column by calling the [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) and [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) methods of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection respectively. Both methods take the row and column index as a parameter to hide the specific row or column.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

It is also possible to hide a row or column by setting the row height or column width to 0 respectively.

{{% /alert %}}

### **Showing Rows and Columns**

Developers can show any hidden row or column by calling the [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) and [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) methods of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection respectively. Both methods take two parameters:

- **Row or column index** - the index of a row or column that is used to show the specific row or column.
- **Row height or column width** - the row height or column width assigned to the row or column after unhiding.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

While making a hidden column visible, if you need to restore it to previously assigned width or to its original width, please unhide the column with a negative width. For example: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Hiding Multiple Rows and Columns**

Developers can hide multiple rows or columns at once by calling the [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) and [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) methods of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection respectively. Both methods take the starting row or column index and the number of rows or columns that should be hidden as parameters.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

It is also possible to use the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) class' [**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) and [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) methods to make multiple rows and columns visible.

{{% /alert %}}
