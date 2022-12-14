---
title: 调整行和列的大小
type: docs
weight: 30
url: /zh/net/resize-rows-and-columns/
---
{{% alert color="primary" %}} 

有时单元格值比它们所在的单元格更宽，或者位于多行上。除非更改行和列的高度和宽度，否则这些值对用户不完全可见。 Aspose.Cells.GridWeb完全支持设置行高和列宽。本主题借助示例详细讨论这些功能。

{{% /alert %}} 
## **使用行高和列宽**
### **设置行高**
设置行高：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问工作表的 Cells 集合。
1. 设置任何指定行中所有单元格的高度。

{{% alert color="primary" %}} 

Cells 集合的 SetRowHeight 和 SetColumnWidth 方法也有变体可用于以英寸和像素为单位设置行高和列宽测量值。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetRowHeight.cs" >}}
### **设置列宽**
要设置列的宽度：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问工作表的 Cells 集合。
1. 设置任何指定列中所有单元格的宽度。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetColumnWidth.cs" >}}
