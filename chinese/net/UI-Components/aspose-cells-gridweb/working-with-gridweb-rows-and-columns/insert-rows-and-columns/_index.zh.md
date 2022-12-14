---
title: 插入行和列
type: docs
weight: 10
url: /zh/net/insert-rows-and-columns/
---
{{% alert color="primary" %}} 

本主题说明如何使用 Aspose.Cells.GridWeb API 将新行和列插入到工作表中。可以在工作表中的任何位置插入行或列。

{{% /alert %}} 
## **插入行**
要在工作表中的任意位置插入一行：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问要向其添加行的工作表。
1. 通过指定要插入行的行索引来插入行。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-AddRowsColumns.aspx-AddRow.cs" >}}
## **插入列**
要在工作表中的任意位置插入一列：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问要向其添加列的工作表。
1. 通过指定要插入列的列索引来插入列。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-AddRowsColumns.aspx-AddColumn.cs" >}}

{{% alert color="primary" %}} 

您还可以使用 InsertRows/InsertColumns 方法将多个行/列相应地插入到工作表中。

{{% /alert %}}
