---
title: 行尾和文本换行
description: 如何使用Aspose.Cells for Python via .NET库实现文本换行和自动换行。通过该库，您可以轻松在单元格中插入文本并设置换行方式，例如手动换行、自动换行等。本文详细介绍如何实现这些功能，并提供示例代码供参考。
keywords: Aspose.Cells for Python via .NET，换行符，文本换行，文本布局
type: docs
weight: 60
url: /zh/python-net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

为了确保单元格中的文本可以被读取，可以应用明确的行尾和文本换行。文本换行将单元格中的一行变成了多行，而明确的行尾则将文本换行放在您想要的确切位置。

{{% /alert %}}

## **将单元格中的文本自动换行**

要将单元格中的文本自动换行，请使用 [**Style.is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) 属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

## **使用显式换行符**

您可以在 C# 中使用 '\n'，在 VB.NET 中使用 ' vbLf' 来在单元格中插入显式换行符。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-UseExplicitLineBreaks-1.py" >}}

