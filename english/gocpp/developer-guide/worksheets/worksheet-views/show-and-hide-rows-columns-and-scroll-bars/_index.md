---
title: Show and Hide Rows, Columns, and Scroll Bars with Golang via C++
linktitle: Show and Hide Rows, Columns, and Scroll Bars
type: docs
weight: 20
url: /go-cpp/show-and-hide-rows-columns-and-scroll-bars/
description: This article demonstrates how to programmatically display and hide Excel worksheet rows and columns using the C++ language and the Aspose.Cells API. The visibility of scroll bars can be adjusted, and several rows and columns can be hidden.
---

{{% alert color="primary" %}}

Aspose.Cells provides ways to control the visibility of rows, columns, and scroll bars of a worksheet.

{{% /alert %}}

## **Show and Hide Rows and Columns**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) collection that allows developers to access each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/) collection that represents all cells in the worksheet. The [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/) collection provides several methods for managing rows or columns in a worksheet. A few of these are discussed below.

### **Show Rows and Columns**

Developers can show any hidden row or column by calling the [**UnhideRow**](https://reference.aspose.com/cells/go-cpp/cells/unhiderow/) and [**UnhideColumn**](https://reference.aspose.com/cells/go-cpp/cells/unhidecolumn/) methods of the [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/) collection respectively. Both methods take two parameters:

- **Row or column index** – the index of a row or column that is used to show the specific row or column.  
- **Row height or column width** – the row height or column width assigned to the row or column after unhiding.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShowAndHideRowsColumnsAndScrollBars.go" >}}

{{% alert color="primary" %}}

While making a hidden column visible, if you need to restore it to its previously assigned width or to its original width, you should unhide the column with a negative width. For example: `worksheet.GetCells().UnhideColumn(5, -1)`.

{{% /alert %}}

### **Hide Rows and Columns**

Developers can hide a row or column by calling the [**HideRow**](https://reference.aspose.com/cells/go-cpp/cells/hiderow/) and [**HideColumn**](https://reference.aspose.com/cells/go-cpp/cells/hidecolumn/) methods of the [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/) collection respectively. Both methods take the row or column index as a parameter to hide the specific row or column.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShowAndHideRowsColumnsAndScrollBars-1.go" >}}

{{% alert color="primary" %}}

It is also possible to hide a row or column by setting the row height or column width to 0, respectively.

{{% /alert %}}

### **Hide Multiple Rows and Columns**

Developers can hide multiple rows or columns at once by calling the [**HideRows**](https://reference.aspose.com/cells/go-cpp/cells/hiderows/) and [**HideColumns**](https://reference.aspose.com/cells/go-cpp/cells/hidecolumns/) methods of the [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/) collection respectively. Both methods take the starting row or column index and the number of rows or columns that should be hidden as parameters.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShowAndHideRowsColumnsAndScrollBars-2.go" >}}

## **Show and Hide Scroll Bars**

Scroll bars are used to navigate the contents of a worksheet. Normally, there are two kinds of scroll bars:

- Vertical scroll bars  
- Horizontal scroll bars

Microsoft Excel provides both horizontal and vertical scroll bars so that users can scroll through worksheet contents. Using Aspose.Cells, developers can control the visibility of both types of scroll bars in Excel files.

### **Controlling the Visibility of Scroll Bars**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class provides a wide range of properties and methods for managing an Excel file. To control the visibility of scroll bars, use the [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class's [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/go-cpp/workbooksettings/isvscrollbarvisible/) and [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/go-cpp/workbooksettings/ishscrollbarvisible/) properties. Both are Boolean properties, which means they can store only **true** or **false** values.

#### **Making Scroll Bars Visible**

Make scroll bars visible by setting the [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class's [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/go-cpp/workbooksettings/isvscrollbarvisible/) or [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/go-cpp/workbooksettings/ishscrollbarvisible/) property to **true**.

#### **Hiding Scroll Bars**

Hide scroll bars by setting the [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class's [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/go-cpp/workbooksettings/isvscrollbarvisible/) or [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/go-cpp/workbooksettings/ishscrollbarvisible/) property to **false**.

**Sample Code**

Below is a complete code example that opens an Excel file (`book1.xls`), hides both scroll bars, and then saves the modified file as `output.xls`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShowAndHideRowsColumnsAndScrollBars-3.go" >}}
{{< app/cells/assistant language="go" >}}
