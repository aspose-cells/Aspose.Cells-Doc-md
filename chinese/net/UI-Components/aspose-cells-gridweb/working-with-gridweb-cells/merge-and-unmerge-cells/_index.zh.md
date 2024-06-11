---
title: 合并和取消合并单元格
type: docs
weight: 60
url: /zh/net/aspose-cells-gridweb/merge-and-unmerge-cells/
keywords: GridWeb,合并,取消合并
description: 本文介绍了如何在GridWeb中合并/取消合并单元格。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb提供了一个方便的实用功能，可以将单元格合并成一个大单元格。本主题描述了如何以编程方式合并单元格。

{{% /alert %}} 
## **合并单元格**
通过调用Cells集合的Merge方法，将工作表中的多个单元格合并成一个单元格。在调用Merge方法时，指定要合并的单元格范围。

{{% alert color="primary" %}} 

如果合并多个单元格，且每个单元格都包含数据，则在合并后仅保留范围中左上角单元格的内容。其他单元格中的数据不会丢失。如果取消合并单元格，则每个单元格都会恢复其数据。

{{% /alert %}} 

四个单元格合并为一个 

![todo:image_alt_text](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **取消合并单元格**
要取消合并单元格，使用Cells集合的UnMerge方法，其参数与Merge方法相同，并执行取消合并单元格的操作。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
