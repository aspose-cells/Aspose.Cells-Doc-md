---
title: Merge and Unmerge Cells in GridDesktop
linktitle: Merging and Unmerging Cells
type: docs
weight: 90
url: /net/aspose-cells-griddesktop/merge-and-unmerge-cells-griddesktop/
keywords: GridDesktop,merge,unmerge
description: This article introduces the merge and unmerge features in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

In this topic, we will discuss a utility feature of merging and unmerging cells of a worksheet. This feature is useful in cases when we need to span some rows or columns to enhance the readability of data.

{{% /alert %}} 
## **Merge Cells**
To merge cells into a single large cell, please follow the steps below:

- Access any desired **Worksheet**
- Create a **Range of Cells** to be merged
- **Merge** the range of cells into a large cell

You can use **the Merge** method of [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) to merge cells. However, a range of cells can be defined using **a CellRange** object.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **Unmerge Cells**
To unmerge a large cell into many cells, please follow the steps below:

- Access any desired **Worksheet**
- Access the merged cell that needs to be unmerged
- **Unmerge** the large cell into many cells using the location of the merged cell

You can use **the Unmerge** method of [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) to unmerge a cell using its location.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

When you merge cells into a single cell, the formatting settings of the top‑left cell (in the range of cells) are applied to the merged cell. However, when the cell is unmerged, all unmerged cells retain their original formatting settings.

{{% /alert %}}
