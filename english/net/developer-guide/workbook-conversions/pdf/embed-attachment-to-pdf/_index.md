---
title: Embed Attachment to PDF
type: docs
weight: 380
url: /net/embed-attachment-to-pdf/

---

In Excel, you can insert an Ole Object with source data([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)) . Double click the Ole Object, the embedded file will be opened.

Generally, while converting to pdf, the Ole Object will be rendered as an icon or a thumbnail without the Ole Object source data. With option [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/), you can embed the Ole Object source data as attachment in PDF. You can double click the icon or the thumbnail in PDF to open the source file of the Ole Object.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="csharp" >}}