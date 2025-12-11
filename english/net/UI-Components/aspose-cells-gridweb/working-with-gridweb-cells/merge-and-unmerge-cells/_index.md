---
title: Merge and Unmerge Cells
type: docs
weight: 60
url: /net/aspose-cells-gridweb/merge-and-unmerge-cells/
keywords: GridWeb,merge,unmerge
description: This article introduces how to merge/unmerge cells in GridWeb.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb has a handy utility feature that lets you merge cells into one large cell. This topic describes how to merge cells programmatically.

{{% /alert %}} 
## **Merging Cells**
Merge multiple cells in a worksheet into a single cell by calling the Cells collection's Merge method. Specify the range of cells to be merged when calling the Merge method.

{{% alert color="primary" %}} 

If you merge multiple cells and each cell contains data, only the content of the top left cell in the range is retained after the merge. Data in the other cells is not lost. If you unmerge the cells, each cell recovers its data.

{{% /alert %}} 

**Four cells merged into one** 

![todo:image_alt_text](merge-and-unmerge-cells_1.png)

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **Unmerging Cells**
To unmerge cells, use the Cells collection's UnMerge method that takes the same parameters as the Merge method and performs the unmerging of cells.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
