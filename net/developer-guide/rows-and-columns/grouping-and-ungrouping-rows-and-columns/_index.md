---
title: Grouping and Ungrouping Rows and Columns
type: docs
weight: 50
url: /net/grouping-and-ungrouping-rows-and-columns/
---

## **Introduction**

In a Microsoft Excel file, you can create an outline for the data to let you show and hide levels of detail with a single mouse click.

Click the **Outline Symbols**, 1,2,3, + and - to quickly display only the rows or columns that provide summaries or headings for sections in a worksheet, or you can use the symbols to see details under an individual summary or heading as shown below in the figure:

|**Grouping Rows and Columns.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Group Management of Rows and Columns**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection that represents all cells in the worksheet.

The [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection provides several methods to manage rows or columns in a worksheet, few of these are discussed below in more detail.

### **Grouping Rows and Columns**

It is possible to group rows or columns by calling the [**GroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index) and [**GroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index) methods of the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection. Both methods take the following parameters:

- First row/column index, the first row or column in the group.
- Last row/column index, the last row or column in the group.
- Is hidden, a Boolean parameter that specifies whether to hide rows/columns after grouping or not.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **Group Settings**

Microsoft Excel allows you to configure group settings for displaying:

- Summary rows below detail.
- Summary columns to the right of detail.

Developers can configure these group settings using the [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) property of the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class.

### **Summary Rows to Below of Detail**

It is possible to control whether summary rows are displayed below detail by setting the [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline) class' [**SummaryRowBelow**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) property to **true** or **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **Summary Columns to Right of Detail**

Developers can also control displaying summary columns to the right of detail by setting the [**SummaryColumnRight**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) property of [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline) class to **true** or **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **Ungrouping Rows and Columns**

To ungroup any grouped rows or columns, call the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection's [**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) and [**UngroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns) methods. Both methods take two parameters:

- First row or column index, the first row/column to be ungrouped.
- Last row or column index, the last row/column to be ungrouped.

[**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) has an overload that takes a Boolean third parameter. Setting it to **true** removes all grouped information. Otherwise, only the outer group information is removed.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
