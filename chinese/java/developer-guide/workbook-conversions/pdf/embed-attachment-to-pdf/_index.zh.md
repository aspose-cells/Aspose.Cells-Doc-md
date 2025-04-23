---
title: 将附件嵌入到PDF中
type: docs
weight: 370
url: /zh/java/embed-attachment-to-pdf/

---

在Excel中，您可以插入一个Ole对象，源数据为([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx))。双击Ole对象，嵌入的文件将被打开。

一般来说，在转换为pdf时，OLE对象会作为图标或缩略图渲染，不包括OLE对象的源数据。通过选项 [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-)，你可以将OLE对象的源数据作为附件嵌入到pdf中。可以双击pdf中的图标或缩略图来打开OLE对象的源文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}

![embedded-attachment.png](embedded-attachment.png)

{{< app/cells/assistant language="java" >}}
