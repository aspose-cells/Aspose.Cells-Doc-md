---
title: 行尾和文本换行
description: 如何使用Aspose.Cells库在C#中实现文本换行和自动换行。通过使用Aspose.Cells库，您可以轻松地在单元格中插入文本并设置文本换行方法，例如手动换行、自动换行等。本文详细介绍了如何实现这些功能，并提供了示例代码供参考。
keywords: Aspose.Cells，行尾，文本换行，文本布局
type: docs
weight: 60
url: /zh/net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

为了确保单元格中的文本可以被读取，可以应用明确的行尾和文本换行。文本换行将单元格中的一行变成了多行，而明确的行尾则将文本换行放在您想要的确切位置。

{{% /alert %}}

## **将单元格中的文本自动换行**

要将单元格中的文本自动换行，请使用 [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) 属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **使用显式换行符**

您可以在 C# 中使用 '\n'，在 VB.NET 中使用 ' vbLf' 来在单元格中插入显式换行符。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
