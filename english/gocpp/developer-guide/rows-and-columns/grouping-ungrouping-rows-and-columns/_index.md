---
title: Grouping, Ungrouping Rows and Columns
type: docs
weight: 30
url: /go-cpp/grouping-ungrouping-rows-and-columns/
---

## **Introduction**

In a Microsoft Excel file, you can create an outline for the data to let you show and hide levels of detail with a single mouse click.

Click the **Outline Symbols** (1, 2, 3, +, and -) to quickly display only the rows or columns that provide summaries or headings for sections in a worksheet, or use the symbols to view details under an individual summary or heading.

## **Group Management of Rows & Columns**

Aspose.Cells provides a class, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class. The [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides a [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection that represents all cells in the worksheet.

The [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection provides several methods to manage rows or columns in a worksheet; a few of these are discussed below in more detail.

### **Grouping Rows & Columns**

It is possible to group rows or columns by calling the [GroupRows](https://reference.aspose.com/cells/go-cpp/cells/grouprows/) and [GroupColumns](https://reference.aspose.com/cells/go-cpp/cells/groupcolumns/) methods of the [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection. Both methods take the following parameters:

- The first row/column index, the first row or column in the group.
- The last row/column index, the last row or column in the group.
- Is hidden, a Boolean parameter that specifies whether to hide rows/columns after grouping.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupingRowsColumns.go" >}}

#### **Group Settings**

Microsoft Excel allows you to configure group settings for displaying:

- Summary rows below detail.
- Summary columns to the right of detail.

## **Ungrouping Rows & Columns**

To ungroup any grouped rows or columns, call the [Cells](https://reference.aspose.com/cells/go-cpp/cells/) collection's [UngroupRows](https://reference.aspose.com/cells/go-cpp/cells/ungrouprows/) and [UngroupColumns](https://reference.aspose.com/cells/go-cpp/cells/ungroupcolumns/) methods. Both methods take two parameters:

- The first row or column index, the first row/column to be ungrouped.
- The last row or column index, the last row/column to be ungrouped.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UnGroupingRowsColumns.go" >}}