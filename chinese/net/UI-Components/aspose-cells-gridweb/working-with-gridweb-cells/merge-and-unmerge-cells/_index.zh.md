---
title: 合并和取消合并单元格
type: docs
weight: 60
url: /zh/net/aspose-cells-gridweb/merge-and-unmerge-cells/
keywords: GridWeb,合并,取消合并
description: 本文介绍了如何在 GridWeb 中合并/取消合并单元格。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 提供了一个方便的工具功能，可将单元格合并成一个大单元格。本主题介绍了如何以编程方式合并单元格。

{{% /alert %}} 
## **合并单元格**
调用 Cells 集合的 Merge 方法可将工作表中的多个单元格合并成一个单元格。在调用 Merge 方法时，指定要合并的单元格范围。

{{% alert color="primary" %}} 

如果合并了多个单元格并且每个单元格都包含数据，则合并后只保留范围中左上角单元格的内容。其他单元格中的数据不会丢失。如果取消合并单元格，则每个单元格都恢复其数据。

{{% /alert %}} 

**四个单元格合并成一个单元格** 

![todo:image_alt_text](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **取消合并单元格**
要取消合并单元格，使用 Cells 集合的 UnMerge 方法，该方法与 Merge 方法具有相同的参数，执行单元格的取消合并操作。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
