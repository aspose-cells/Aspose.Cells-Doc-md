---
title: Show and Hide Rows Columns and Scroll Bars
type: docs
weight: 20
url: /python-net/show-and-hide-rows-columns-and-scroll-bars/
description: This article demonstrates how to programmatically display and hide Excel worksheet rows and columns using the Aspose.Cells for Python via .NET API. The visibility of scroll bars can be adjusted, and several rows and columns can be hidden.
keywords: Python Excel Library, Python show rows and columns, Python Hide rows and columns, Python show vertical scroll bar, Python show horizontal scroll bar, Python hide vertical scroll bar, Python hide horizontal scroll bar, Python Show and Hide Rows Columns and Scroll Bars.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET provides ways to control the visibility of Rows, Column and Scroll Bars of a worksheet.

{{% /alert %}}

## **Show and Hide Rows and Columns**

Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection that represents all cells in the worksheet. The [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection provides several methods for managing rows or columns in a worksheet. A few of these are discussed below.

### **Show Rows and Columns**

Developers can show any hidden row or column by calling the [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) and [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) methods of the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) collection respectively. Both methods take two parameters:

- **Row or column index** - the index of a row or column that is used to show the specific row or column.
- **Row height or column width** - the row height or column width assigned to the row or column after unhiding.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

While making a hidden column visible, if you need to restore it to previously assigned width or to its original width, please unhide the column with a negative width. For example: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Hide Rows and Columns**

Developers can hide a row or column by calling the [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) and [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) methods of the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection respectively. Both methods take the row and column index as a parameter to hide the specific row or column.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

It is also possible to hide a row or column by setting the row height or column width to 0 respectively.

{{% /alert %}}

### **Hide Multiple Rows and Columns**

Developers can hide multiple rows or columns at once by calling the [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) and [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns) methods of the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) collection respectively. Both methods take the starting row or column index and the number of rows or columns that should be hidden as parameters.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

## **Show and Hide Scroll Bars**

Scroll bars are used to navigate the contents of any file. Normally, there are two kinds of scroll bars:

- Vertical scroll bars
- Horizontal scroll bars

Microsoft Excel also provides horizontal and vertical scroll bars so that users can scroll through worksheet contents. Using Aspose.Cells for Python via .NET, developers can control the visibility of both types of scroll bars in Excel files.

### **Controlling the Visibility of Scroll Bars**

Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class provides a wide range of properties and methods for managing an Excel file. To control the visibility of scroll bars, use the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class' [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) and [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) properties. [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) and [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) are Boolean properties, which means that these properties can only store **true** or **false** values.

#### **Making Scroll Bars Visible**

Make scroll bars visible by setting the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class' [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) or [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) property to **true**.

#### **Hiding Scroll Bars**

Hide scroll bars by setting the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class' [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) or [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) property to **false**.

**Sample Code**

Below is a complete code that opens an Excel file, book1.xls, hides both scroll bars and then saves the modified file as output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Worksheets-Display-DisplayHideScrollBars-1.py" >}}
