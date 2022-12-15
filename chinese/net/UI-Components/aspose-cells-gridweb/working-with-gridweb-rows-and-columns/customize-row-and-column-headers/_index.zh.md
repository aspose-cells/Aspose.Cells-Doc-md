---
title: 自定义行和列标题
type: docs
weight: 40
url: /zh/net/customize-row-and-column-headers/
---
{{% alert color="primary" %}} 

与 Microsoft Excel 一样，Aspose.Cells.GridWeb 也对行（数字，如 1、2、3 等）和列（按字母顺序，如 A、B、C 等）使用标准标题或标题。 Aspose.Cells.GridWeb 还可以自定义标题。本主题讨论使用 Aspose.Cells.GridWeb API 在运行时自定义行和列标题。

{{% /alert %}} 
## **自定义行标题**
要自定义行的标题或标题：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问 GridWorksheetCollection 中的工作表。
1. 设置任何指定行的标题。

**第 1 行和第 2 行的标题已自定义** 

![待办事项：图像_替代_文本](customize-row-and-column-headers_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CustomizeHeaders.aspx-CustomizeRowHeader.cs" >}}
## **自定义列标题**
要自定义列的标题或标题：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问 GridWorksheetCollection 中的工作表。
1. 设置任何指定列的标题。

**第 1、2 和 3 列的标题已自定义** 

![待办事项：图像_替代_文本](customize-row-and-column-headers_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CustomizeHeaders.aspx-CustomizeColumnHeader.cs" >}}
