---
title: 将附件嵌入到PDF中
type: docs
weight: 380
url: /zh/net/embed-attachment-to-pdf/

---

在Excel中，您可以插入一个Ole对象，源数据为([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx))。双击Ole对象，嵌入的文件将被打开。

通常在转换为pdf时，Ole对象会被渲染为图标或缩略图，不包含Ole对象的源数据。使用 [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/)，您可以将Ole对象的源数据作为附件嵌入到PDF中。双击PDF中的图标或缩略图即可打开Ole对象的源文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="csharp" >}}
