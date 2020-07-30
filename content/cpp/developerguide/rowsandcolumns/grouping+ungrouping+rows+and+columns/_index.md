---
title : "Grouping Ungrouping Rows and Columns" 
description : "" 
weight : 12023 
toc : false
type: docs
url: /cpp/developerguide/rowsandcolumns/grouping+ungrouping+rows+and+columns/
---

# Aspose.Cells for C++ : Grouping, Ungrouping Rows and Columns


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#introduction)
*   2 [Group Management of Rows & Columns](#group-management-of-rows-&-columns)
    *   2.1 [Grouping Rows & Columns](#grouping-rows-&-columns)
        *   2.1.1 [Group Settings](#group-settings)
*   3 [Ungrouping Rows & Columns](#ungrouping-rows-&-columns)
{{< /panel >}}
 

## Introduction

In a Microsoft Excel file, you can create an outline for the data to let you show and hide levels of detail with a single mouse click.

Click the **Outline Symbols**, 1,2,3, + and - to quickly display only the rows or columns that provide summaries or headings for sections in a worksheet, or you can use the symbols to see details under an individual summary or heading.

## Group Management of Rows & Columns

Aspose.Cells provides a class, [IWorkbook](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/) that represents a Microsoft Excel file. The [IWorkbook](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/) class contains a [IWorksheets](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet_collection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [IWorksheet](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet/) class. The [IWorksheet](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet/) class provides an [ICells](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/) collection that represents all cells in the worksheet.

The [ICells](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/) collection provides several methods to manage rows or columns in a worksheet, few of these are discussed below in more detail.

### Grouping Rows & Columns

It is possible to group rows or columns by calling the [GroupRows](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/#a88e0180ed1a4a423e0bd3ac599ef9332) and [GroupColumns](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/#aaa14179e2a84ba5c2857f8434570d3d8) methods of the [ICells](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/) collection. Both methods take the following parameters:

*   The first row/column index, the first row or column in the group.
*   The last row/column index, the last row or column in the group.
*   Is hidden, a Boolean parameter that specifies whether to hide rows/columns after grouping or not.

#### Group Settings

Microsoft Excel allows you to configure group settings for displaying:

*   Summary rows below detail.
*   Summary columns to the right of detail.

## Ungrouping Rows & Columns

To ungroup any grouped rows or columns, call the [ICells](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/) collection's [UngroupRows](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/#adc1f6418506854ab41707bfef453ddb1) and [UngroupColumns](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_cells/#aa3bf9a9510d4e85f68db9ebdcadc8406) methods. Both methods take two parameters:

*   The first row or column index, the first row/column to be ungrouped.
*   The last row or column index, the last row/column to be ungrouped.

