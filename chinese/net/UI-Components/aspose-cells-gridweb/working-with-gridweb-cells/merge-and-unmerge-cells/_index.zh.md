---
title: 合并和取消合并 Cells
type: docs
weight: 60
url: /zh/net/merge-and-unmerge-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 具有一项方便的实用程序功能，可让您将单元格合并为一个大单元格。本主题介绍如何以编程方式合并单元格。

{{% /alert %}} 
## **合并 Cells**
通过调用 Cells 集合的 Merge 方法，将工作表中的多个单元格合并为一个单元格。指定调用 Merge 方法时要合并的单元格范围。

{{% alert color="primary" %}} 

如果合并多个单元格并且每个单元格都包含数据，则合并后仅保留区域中左上角单元格的内容。其他单元格中的数据不会丢失。如果取消合并单元格，每个单元格都会恢复其数据。

{{% /alert %}} 

**四个单元格合并为一个** 

![待办事项：图像_替代_文本](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **取消合并 Cells**
要取消合并单元格，请使用 Cells 集合的 UnMerge 方法，该方法采用与 Merge 方法相同的参数并执行单元格的取消合并。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
