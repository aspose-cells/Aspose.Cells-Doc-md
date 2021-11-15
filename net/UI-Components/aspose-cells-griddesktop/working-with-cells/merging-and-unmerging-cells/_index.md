---
title: Merging  and  Unmerging Cells
type: docs
weight: 90
url: /net/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

In this topic, we will discuss a utility feature of merging and unmerging cells of a worksheet. This feature is useful in those cases when we need to span some rows or columns to enhance the readability of data.

{{% /alert %}} 
## **Merging Cells**
To merge cells into a single large cell, please follow the steps below:

- Access any desired **Worksheet**
- Create a **Range of Cells** to be merged
- **Merge** the range of cells into a large cell

You can use **Merge** method of **Worksheet** to merge cells. However, a range of cells can be defined using **CellRange** object.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **Unmerging Cells**
To unmerge a large cell into many cells, please follow the steps below:

- Access any desired **Worksheet**
- Access the merged cell that needs to be unmerged
- **Unmerge** the large cell into many cells using the location of merged cell

You can use **Unmerge** method of **Worksheet** to unmerge a cell using its location.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

When you merge cells into a single cell then the formatting settings of top left cell (in the range of cells) are applied on the merged cell but when the cell is unmerged, all unmerged cells maintain their formatting settings.

{{% /alert %}}
