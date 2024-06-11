---
title: 调整行和列大小
type: docs
weight: 30
url: /zh/net/aspose-cells-gridweb/resize-rows-and-columns/
keywords: GridWeb，宽度，高度，行高，列宽
description: 本文介绍了如何在GridWeb中设置行高和列宽。
---

{{% alert color="primary" %}} 

有时单元格值比它们所在的单元格宽，或者跨越了几行。除非改变行和列的高度和宽度，否则这些值对最终用户来说不是完全可见的。Aspose.Cells.GridWeb完全支持设置行高和列宽。本主题将通过示例详细讨论这些特性。

{{% /alert %}} 
## **操作行高度和列宽度**
### **设置行高度**
设置行的高度：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问工作表的单元格集合。
1. 设置任意指定行中所有单元格的高度。

{{% alert color="primary" %}} 

Cells集合的SetRowHeight和SetColumnWidth方法还有可用于以英寸和像素设置行高和列宽度的变量。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetRowHeight.cs" >}}
### **设置列宽度**
要设置列的宽度：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问工作表的单元格集合。
1. 设置任意指定列中所有单元格的宽度。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetColumnWidth.cs" >}}
