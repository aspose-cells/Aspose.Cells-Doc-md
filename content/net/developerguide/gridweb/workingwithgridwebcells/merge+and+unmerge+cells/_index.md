---
title : "Merge and Unmerge Cells" 
description : "" 
weight : 16715 
toc : false
type: docs
url: /net/developerguide/gridweb/workingwithgridwebcells/merge+and+unmerge+cells/
---

# Aspose.Cells for .NET : Merge and Unmerge Cells


Aspose.Cells.GridWeb has a handy utility feature that lets you merge cells into one large cell. This topic describes how to merge cells programmatically.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Merging Cells](#merging-cells)
*   2 [Unmerging Cells](#unmerging-cells)
{{< /panel >}}
 

## Merging Cells

Merge multiple cells in a worksheet into a single cell by calling the `Cells` collection's `Merge` method. Specify the range of cells that to be merged when calling the `Merge` method.

If you merge multiple cells and each cell contains data, only the content of the top left cell in the range is retained after the merge. Data in the other cells is not lost. If you unmerge the cells, each cell recovers its data.

**Four cells merged into one**  
![](https://docs2.aspose.com/cells/net/attachments/5013797/5115377.png)

## Unmerging Cells

To unmerge cells, use the `Cells` collection's `UnMerge` method that takes same parameters as of the `Merge` method and performs the unmerging of cells.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Merge and Unmerge Cells-001.png](https://docs2.aspose.com/cells/net/attachments/5013797/5115377.png) (image/png)  

