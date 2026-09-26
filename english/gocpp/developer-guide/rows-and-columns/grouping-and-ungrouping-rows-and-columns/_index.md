---
title: Grouping and Ungrouping Rows and Columns with Golang via C++
linktitle: Grouping and Ungrouping Rows and Columns
type: docs
weight: 50
url: /go-cpp/grouping-and-ungrouping-rows-and-columns/
description: Learn how to group and ungroup rows and columns in Excel files using Aspose.Cells with Golang via C++.
---

## **Introduction**

In a Microsoft Excel file, you can create an outline for the data to let you show and hide levels of detail with a single mouse click.

Click the **Outline Symbols** (1, 2, 3, + and –) to quickly display only the rows or columns that provide summaries or headings for sections in a worksheet, or you can use the symbols to see details under an individual summary or heading, as shown below in the figure:

| **Grouping Rows and Columns.** |
| :- |
| ![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png) |

## **Group Management of Rows and Columns**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/) collection that represents all cells in the worksheet.

The [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/) collection provides several methods to manage rows or columns in a worksheet, a few of which are discussed below in more detail.

### **Grouping Rows and Columns**

It is possible to group rows or columns by calling the [**GroupRows**](https://reference.aspose.com/cells/go-cpp/cells/grouprows_int_int_bool/) and [**GroupColumns**](https://reference.aspose.com/cells/go-cpp/cells/groupcolumns_int_int/) methods of the [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/) collection. Both methods take the following parameters:

- First row/column index – the first row or column in the group.  
- Last row/column index – the last row or column in the group.  
- Is hidden – a Boolean parameter that specifies whether to hide rows/columns after grouping.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupingAndUngroupingRowsAndColumns.go" >}}

#### **Group Settings**

Microsoft Excel allows you to configure group settings for displaying:

- Summary rows below detail.  
- Summary columns to the right of detail.

Developers can configure these group settings using the [**GetOutline()**](https://reference.aspose.com/cells/go-cpp/worksheet/getoutline/) property of the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class.

### **Summary Rows Below Detail**

It is possible to control whether summary rows are displayed below the detail by setting the Outline class's [**GetSummaryRowBelow()**](https://reference.aspose.com/cells/go-cpp/outline/getsummaryrowbelow/) property to **true** or **false**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupingAndUngroupingRowsAndColumns-1.go" >}}

### **Summary Columns to the Right of Detail**

Developers can also control the display of summary columns to the right of the detail by setting the Outline class's [**GetSummaryColumnRight()**](https://reference.aspose.com/cells/go-cpp/outline/getsummarycolumnright/) property to **true** or **false**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupingAndUngroupingRowsAndColumns-2.go" >}}

## **Ungrouping Rows and Columns**

To ungroup any grouped rows or columns, call the [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/) collection's [**UngroupRows**](https://reference.aspose.com/cells/go-cpp/cells/ungrouprows_int_int_bool/) and [**UngroupColumns**](https://reference.aspose.com/cells/go-cpp/cells/ungroupcolumns/) methods. Both methods take two parameters:

- First row or column index – the first row/column to be ungrouped.  
- Last row or column index – the last row/column to be ungrouped.

[**UngroupRows**](https://reference.aspose.com/cells/go-cpp/cells/ungrouprows_int_int_bool/) has an overload that takes a Boolean third parameter. Setting it to **true** removes all grouped information; otherwise, only the outer group information is removed.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupingAndUngroupingRowsAndColumns-3.go" >}}
{{< app/cells/assistant language="go" >}}
