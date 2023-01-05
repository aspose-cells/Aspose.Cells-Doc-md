---
title: 换行和文字换行
type: docs
weight: 60
url: /zh/net/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

为确保可以读取单元格中的文本，可以应用明确的换行符和文本换行。文本换行将单元格中的一行变成多行，明确的换行符正好放在你想要的地方。

{{% /alert %}}

## **在 Cell 中换行**

要在单元格中换行文本，请使用[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **使用显式换行符**

您可以使用 C# 中的“\n”和 VB.NET 中的“vbLf”在单元格中插入明确的换行符。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
