---
title: 将附件嵌入到PDF
type: docs
weight: 380
url: /zh/net/embed-attachment-to-pdf/

---

在Excel中，您可以插入带有源数据的OLE对象（[embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)）。双击OLE对象，嵌入的文件将被打开。

通常，在转换为PDF时，OLE对象将呈现为图标或缩略图，而不包含OLE对象源数据。使用选项[PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/)，您可以将OLE对象源数据嵌入到PDF中的附件中。您可以在PDF中双击图标或缩略图以打开OLE对象的源文件。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![embedded-attachment.png](embedded-attachment.png)
