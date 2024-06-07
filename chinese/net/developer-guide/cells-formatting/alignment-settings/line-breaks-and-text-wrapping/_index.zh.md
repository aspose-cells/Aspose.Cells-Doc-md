---
title: 换行和文本换行
description: 如何在C#中使用Aspose.Cells库实现文本换行和自动换行。通过使用Aspose.Cells库，您可以轻松地在单元格中插入文本并设置文本换行方法，例如手动词换、自动词换等。本文详细介绍了如何实现这些功能，并提供了供您参考的示例代码。
keywords: Aspose.Cells, 换行，文本换行，文本布局
type: docs
weight: 60
url: /zh/net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

为确保单元格中的文本可读，可以应用显式换行和文本换行。文本换行将一个单行变成多行，而显式换行可将换行符插入到您想要的位置。

{{% /alert %}}

## **在单元格中换行文本**

要在单元格中换行文本，请使用[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **使用显式换行符**

您可以在C#中使用'\n'，在VB.NET中使用‘vbLf’来在单元格中插入显式换行符。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
