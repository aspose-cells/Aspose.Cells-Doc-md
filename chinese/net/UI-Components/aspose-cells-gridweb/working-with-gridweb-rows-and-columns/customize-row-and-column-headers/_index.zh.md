---
title: 自定义行和列标题
type: docs
weight: 40
url: /zh/net/aspose-cells-gridweb/customize-row-and-column-headers/
keywords: GridWeb,标题,行标题,列标题
description: 本文介绍了如何在 GridWeb 中自定义行标题和列标题。
---

{{% alert color="primary" %}} 

与 Microsoft Excel 类似，Aspose.Cells.GridWeb 也使用标准的行标题或列标题（行号如1、2、3等，列号如A、B、C等）。Aspose.Cells.GridWeb 还可以自定义标题。本主题讨论了如何使用 Aspose.Cells.GridWeb API 在运行时自定义行和列标题。

{{% /alert %}} 
## **自定义行标题**
要自定义行的标题或说明：

1. 将Aspose.Cells.GridWeb控件添加到Web表单中。
1. 访问 GridWorksheetCollection 中的工作表。
1. 设置任何指定行的标题。

**行1和2的标题已经被自定义** 

![todo:image_alt_text](customize-row-and-column-headers_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CustomizeHeaders.aspx-CustomizeRowHeader.cs" >}}
## **自定义列标题**
要自定义列的标题或说明：

1. 将Aspose.Cells.GridWeb控件添加到Web表单中。
1. 访问 GridWorksheetCollection 中的工作表。
1. 设置任何指定列的标题。

**列1、2和3的标题已经被自定义** 

![todo:image_alt_text](customize-row-and-column-headers_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CustomizeHeaders.aspx-CustomizeColumnHeader.cs" >}}
