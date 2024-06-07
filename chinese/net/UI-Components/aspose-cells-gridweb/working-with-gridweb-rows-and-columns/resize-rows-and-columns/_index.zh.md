---
title: 调整行和列大小
type: docs
weight: 30
url: /zh/net/aspose-cells-gridweb/resize-rows-and-columns/
keywords: GridWeb，宽度，高度，行高，列宽
description: 本文介绍了如何在GridWeb中设置行高和列宽。
---

{{% alert color="primary" %}} 

有时，单元格的值比其所在的单元格更宽，或者跨越多行。除非改变行和列的高度和宽度，否则这些值对用户来说不够清晰可见。Aspose.Cells.GridWeb完全支持设置行高和列宽。本主题通过示例详细讨论了这些功能。

{{% /alert %}} 
## **处理行高和列宽**
### **设置行高**
要设置行高：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问工作表的Cells集合。
1. 设置指定行中所有单元格的高度。

{{% alert color="primary" %}} 

Cells集合的SetRowHeight和SetColumnWidth方法还提供了将行高和列宽测量单位设置为英寸和像素的变体。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetRowHeight.cs" >}}
### **设置列宽**
要设置列宽：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问工作表的Cells集合。
1. 设置指定列中所有单元格的宽度。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetColumnWidth.cs" >}}
