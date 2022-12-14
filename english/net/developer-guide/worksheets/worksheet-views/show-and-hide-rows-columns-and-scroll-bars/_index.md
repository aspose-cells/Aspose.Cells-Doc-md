---
title: Show and Hide Rows Columns and Scroll Bars
type: docs
weight: 20
url: /net/show-and-hide-rows-columns-and-scroll-bars/
---

{{% alert color="primary" %}}

Aspose.Cells provides ways to control the visibility of Rows, Column and Scroll Bars of a worksheet.

{{% /alert %}}

## **Show and Hide Rows and Columns**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection that represents all cells in the worksheet. The [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection provides several methods for managing rows or columns in a worksheet. A few of these are discussed below.

### **Show Rows and Columns**

Developers can show any hidden row or column by calling the [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) and [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) methods of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection respectively. Both methods take two parameters:

- **Row or column index** - the index of a row or column that is used to show the specific row or column.
- **Row height or column width** - the row height or column width assigned to the row or column after unhiding.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

While making a hidden column visible, if you need to restore it to previously assigned width or to its original width, please unhide the column with a negative width. For example: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Hide Rows and Columns**

Developers can hide a row or column by calling the [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) and [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) methods of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection respectively. Both methods take the row and column index as a parameter to hide the specific row or column.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

It is also possible to hide a row or column by setting the row height or column width to 0 respectively.

{{% /alert %}}

### **Hide Multiple Rows and Columns**

Developers can hide multiple rows or columns at once by calling the [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) and [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) methods of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection respectively. Both methods take the starting row or column index and the number of rows or columns that should be hidden as parameters.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **Show and Hide Scroll Bars**

Scroll bars are used to navigate the contents of any file. Normally, there are two kinds of scroll bars:

- Vertical scroll bars
- Horizontal scroll bars

Microsoft Excel also provides horizontal and vertical scroll bars so that users can scroll through worksheet contents. Using Aspose.Cells, developers can control the visibility of both types of scroll bars in Excel files.

### **Controlling the Visibility of Scroll Bars**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class provides a wide range of properties and methods for managing an Excel file. To control the visibility of scroll bars, use the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class' [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) and [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) properties. [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) and [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) are Boolean properties, which means that these properties can only store **true** or **false** values.

#### **Making Scroll Bars Visible**

Make scroll bars visible by setting the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class' [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) or [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) property to **true**.

#### **Hiding Scroll Bars**

Hide scroll bars by setting the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class' [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) or [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) property to **false**.

**Sample Code**

Below is a complete code that opens an Excel file, book1.xls, hides both scroll bars and then saves the modified file as output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
