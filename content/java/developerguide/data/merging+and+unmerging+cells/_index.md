---
title : "Merging and Unmerging Cells" 
description : "" 
weight : 12173 
toc : false
type: docs
url: /java/developerguide/data/merging+and+unmerging+cells/
---

# Aspose.Cells for Java : Merging and Unmerging Cells



{{< panel title="Contents Summary" style="primary" >}}
*   1 [Merging Cells in a Worksheet.](#merging-cells-in-a-worksheet.)
    *   1.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   1.2 [Using Aspose.Cells](#using-aspose.cells)
        *   1.2.1 [Code Example](#code-example)
*   2 [Unmerging (Splitting) Merged Cells](#unmerging-(splitting)-merged-cells)MergedCells)
    *   2.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   2.2 [Using Aspose.Cells](#using-aspose.cells)
        *   2.2.1 [Code Example](#code-example)
    *   2.3 [Related Articles](#related-articles)
{{< /panel >}}
 

You don't always want the same number of cells in every row or column. For example, you might want to put a title in a cell that spans several columns. Or, if creating an invoice, you might want fewer columns for the total. To make one cell from two or more cells, merge them. Microsoft Excel lets users select cells and merge them to structure the spreadsheet the way they want.

**The result of merging and then splitting a range of cells formatted as the cells to the left in Microsoft Excel**  
![](https://docs2.aspose.com/cells/java/attachments/5276718/5473133.png)

Aspose.Cells supports this feature and can also merge cells in a worksheet. You may unmerge, or split, the merged cells too. A merged cell's cell reference is the reference for the top-left cell in the originally selected range.

Note that when cells are merged, only the data in the top-left cell is retained. If there is data in the other cells in the range, that data is deleted.

Formatting, likewise, is based on the reference cell so that when you merge cells, the formatting settings of the top-left cell in the range are applied on the merged cell. When the cell is split, the new cells keep their original format settings.

### Merging Cells in a Worksheet.

#### Using Microsoft Excel

The following steps describe how to merge cells in the worksheet using Microsoft Excel.

1.  Copy the data you want into the upper-leftmost cell within the range.
2.  Select the cells you want to merge.
3.  To merge cells in a row or column and center the cell contents, click **Merge and Center** icon on the **Formatting** toolbar.

#### Using Aspose.Cells

The [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) class has some useful methods for the task. For example, the method [merge()](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) merges the cells into a single cell within a specified range of the cells.

The following output is generated after executing the code below.  
  
**The cells (C6:E7) have been merged**  
![](https://docs2.aspose.com/cells/java/attachments/5276718/5473132.png)

##### Code Example

The following example shows how to merge cells (C6:E7) in a worksheet.

### Unmerging (Splitting) Merged Cells

#### Using Microsoft Excel

The following steps describe how to split merged cells using Microsoft Excel.

1.  Select the merged cell.  
    When cells have been combined, **Merge and Center** is selected on the **Formatting** toolbar.
2.  Click **Merge and Center** on the **Formatting** toolbar.

#### Using Aspose.Cells

The [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells) class has a method named [unMerge()](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#unMerge(int,%20int,%20int,%20int)) that splits cells into their original state. The method unmerges the cells using the cell's reference in the merged cell range.

##### Code Example

The following example shows how to split the merged cells (C6). The example uses the file created in the previous example and splits the merged cells.

#### Related Articles

*   [Finding and splitting merged cells](https://docs2.aspose.com/cells/java/developerguide/technicalarticles/mngrowscolumnsandcells/detect+merged+cells+in+a+worksheet).
*   [Merge and splitting a cell range using the Range.merge() and Range.unMerge() methods](https://docs2.aspose.com/cells/java/developerguide/technicalarticles/mngrowscolumnsandcells/merge+or+unmerge+range+of+cells).

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Merging UnMerging Cells in the Worksheet-001.png](https://docs2.aspose.com/cells/java/attachments/5276718/5473132.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [merged-split.png](https://docs2.aspose.com/cells/java/attachments/5276718/5473133.png) (image/png)  

