---
title: Merging and Unmerging Cells
type: docs
weight: 190
url: /net/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells supports this feature and can also merge cells in a worksheet. You may unmerge, or split, the merged cells too. A merged cell's cell reference is the reference for the top left cell in the original selected range.

{{% /alert %}} 
## **Introduction**
You don't always want the same number of cells in every row or column. For example, you might want to put a title in a cell that spans several columns. Or, if creating an invoice, you might want fewer columns for the total. To make one cell from two or more cells, merge them. Microsoft Excel lets users select files and merge them to structure the spreadsheet the way they want.

{{% alert color="primary" %}} 

Note that when cells are merged, only the data in the top left cells is retained. If there is data in the other cells in the range, this data is deleted.
Formatting, likewise, is based on the reference cell so that when you merge cells, the formatting settings of the top left cell in the range are applied on the merged cell. When the cell is split, the new cells keep their original format settings.

{{% /alert %}} 
## **Merging Cells in a Worksheet**
### **Merging Cells in Microsoft Excel**
The following steps describe how to merge cells in the worksheet using MS Excel.

1. Copy the data you want into the upper-leftmost cell within the range.
1. Select the cells you want to merge.
1. To merge cells in a row or column and center the cell contents, click **Merge and Center** icon on the **Formatting** toolbar.
### **Merging Cells with Aspose.Cells**
The Aspose.Cells.Cells Class has some useful methods for the task. For example, the method Merge() merges the cells into a single cell within a specified range.

The following example shows how to merge cells (C6:E7) in a worksheet.



{{< gist "aspose-cells" "c326c6c668fc372e30569fa9e0f6bf4b" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
## **Unmerging (Splitting) Merged Cells**
### **Using Microsoft Excel**
The following steps describe how to split merged cells using Microsoft Excel.

1. Select the merged cell.
   When cells have been combined, **Merge and Center** is selected on the **Formatting** toolbar.
1. Click **Merge and Center** on the **Formatting** toolbar.
### **Using Aspose.Cells**
The class Aspose.Cells.Cells has a method named UnMerge() that splits the cells into their original state. The method unmerges the cells using the cell's reference in the merged cell range.

The following example shows how to split the merged cells (C6). The example uses the file created in the previous example and splits the merged cells.



{{< gist "aspose-cells" "c326c6c668fc372e30569fa9e0f6bf4b" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}
