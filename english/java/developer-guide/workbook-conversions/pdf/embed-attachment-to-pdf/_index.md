---
title: Embed Attachment to PDF
type: docs
weight: 370
url: /java/embed-attachment-to-pdf/

---

In Excel, you can insert an Ole Object with source data([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)) . Double click the Ole Object, the embedded file will be opened.

Generally, while converting to pdf, the Ole Object will be rendered as an icon or a thumbnail without the Ole Object source data. With option [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-), you can embed the Ole Object source data as attachment in PDF. You can double click the icon or the thumbnail in PDF to open the source file of the Ole Object.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}

![embedded-attachment.png](embedded-attachment.png)

{{< app/cells/assistant language="java" >}}