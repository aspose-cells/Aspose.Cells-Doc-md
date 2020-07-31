---
title : "Grouping and Ungrouping Rows and Columns" 
description : "" 
weight : 12185 
toc : false
type: docs
url: /net/developerguide/rowsandcolumns/grouping+and+ungrouping+rows+and+columns/
---

# Aspose.Cells for .NET : Grouping and Ungrouping Rows and Columns


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#introduction)
*   2 [Group Management of Rows and Columns](#group-management-of-rows-and-columns)
    *   2.1 [Grouping Rows and Columns](#grouping-rows-and-columns)
        *   2.1.1 [Group Settings](#group-settings)
    *   2.2 [Summary Rows to Below of Detail](#summary-rows-to-below-of-detail)
    *   2.3 [Summary Columns to Right of Detail](#summary-columns-to-right-of-detail)
*   3 [Ungrouping Rows and Columns](#ungrouping-rows-and-columns)
{{< /panel >}}
 

## Introduction

In a Microsoft Excel file, you can create an outline for the data to let you show and hide levels of detail with a single mouse click.

Click the **Outline Symbols**, 1,2,3, + and - to quickly display only the rows or columns that provide summaries or headings for sections in a worksheet, or you can use the symbols to see details under an individual summary or heading as shown below in the figure:

{{< table style="table-striped" >}}
|Grouping Rows and Columns.|
|:----|
|![](https://docs2.aspose.com/cells/net/attachments/5013587/5115161.png)|
{{< /table >}}

## Group Management of Rows and Columns

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [WorksheetCollection](https://apireference.aspose.com/net/cells/aspose.cells/worksheetcollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection that represents all cells in the worksheet.

The [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection provides several methods to manage rows or columns in a worksheet, few of these are discussed below in more detail.

### Grouping Rows and Columns

It is possible to group rows or columns by calling the [GroupRows](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/grouprows/index) and [GroupColumns](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/groupcolumns/index) methods of the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection. Both methods take the following parameters:

*   First row/column index, the first row or column in the group.
*   Last row/column index, the last row or column in the group.
*   Is hidden, a Boolean parameter that specifies whether to hide rows/columns after grouping or not.

#### Group Settings

Microsoft Excel allows you to configure group settings for displaying:

*   Summary rows below detail.
*   Summary columns to the right of detail.

Developers can configure these group settings using the [Outline](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/outline) property of the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class.

### Summary Rows to Below of Detail

It is possible to control whether summary rows are displayed below detail by setting the [Outline](https://apireference.aspose.com/net/cells/aspose.cells/outline) class' [SummaryRowBelow](https://apireference.aspose.com/net/cells/aspose.cells/outline/fields/summaryrowbelow) property to **true **or **false**.

### Summary Columns to Right of Detail

Developers can also control displaying summary columns to the right of detail by setting the [SummaryColumnRight](https://apireference.aspose.com/net/cells/aspose.cells/outline/fields/summarycolumnright) property of [Outline](https://apireference.aspose.com/net/cells/aspose.cells/outline) class to **true** or **false**.

## Ungrouping Rows and Columns

To ungroup any grouped rows or columns, call the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection's [UngroupRows](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/ungrouprows/index) and [UngroupColumns](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/ungroupcolumns) methods. Both methods take two parameters:

*   First row or column index, the first row/column to be ungrouped.
*   Last row or column index, the last row/column to be ungrouped.

[UngroupRows](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/ungrouprows/index) has an overload that takes a boolean third parameter. Setting it to **true** removes all grouped information. Otherwise, only the outer group information is removed.

