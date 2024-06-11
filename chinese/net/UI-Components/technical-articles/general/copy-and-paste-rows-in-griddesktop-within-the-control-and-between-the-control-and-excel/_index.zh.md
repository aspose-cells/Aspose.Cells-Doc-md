---
title: 在 GridDesktop 中控件内部和控件与 Excel 之间复制和粘贴行
type: docs
weight: 70
url: /zh/net/aspose-cells-griddesktop/copy-and-paste-rows-in-griddesktop-within-the-control-and-between-the-control-and-excel/
keywords: GridDesktop，复制，粘贴
description: 本文介绍了 GridDesktop 中的复制和粘贴。
---

{{% alert color="primary" %}} 

如果您想在 GridDesktop 中启用控件内或控件与 Excel 之间的行复制和粘贴，请将 GridDesktop.ClipboardCopyPaste 属性设置为 true。您可以在设计时或在代码中设置此属性。此属性的默认值为 false。目前，它只能复制和粘贴单元格值，不会复制单元格的任何其他设置，如格式，边框样式等。

{{% /alert %}} 
## **在设计模式和运行时设置GridDesktop.ClipboardCopyPaste属性**
以下示例代码在**运行时**设置GridDesktop.ClipboardCopyPaste属性。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-CopyAndPasteRows-1.cs" >}}
