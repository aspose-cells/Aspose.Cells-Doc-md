---
title: 换行和文本换行
description: C#中如何使用Aspose.Cells库实现文本换行和自动换行。通过使用Aspose.Cells库，您可以轻松地在单元格中插入文本并设置文本换行方式，例如手动换行、自动换行等。本文档详细介绍了如何实现实现这些功能并提供示例代码供您参考。
keywords: Aspose.Cells, line breaks, text wraps, text layout
type: docs
weight: 60
url: /zh/net/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

为了确保可以读取单元格中的文本，可以应用显式换行和文本换行。文本换行将单元格中的一行变成多行，其中显式换行符将精确地放置在您想要的位置。

{{% /alert %}}

##  **将文本换行为 Cell**

要将文本换行到单元格中，请使用[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##  **使用显式换行符**

您可以使用 C# 中的“\n”和 VB.NET 中的“vbLf”在单元格中插入显式换行符。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
