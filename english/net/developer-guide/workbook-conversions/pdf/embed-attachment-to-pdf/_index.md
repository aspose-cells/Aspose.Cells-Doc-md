---
title: Embed Attachment to PDF
type: docs
weight: 380
url: /net/embed-attachment-to-pdf/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

In Excel, you can insert an OLE object with source data (embedded-attachments-example.xlsx). Double‑click the OLE object, and the embedded file will be opened.

Generally, when converting to PDF, the OLE object is rendered as an icon or a thumbnail without the OLE object's source data. By using the option [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/), you can embed the OLE object's source data as an attachment in the PDF. You can double‑click the icon or the thumbnail in the PDF to open the source file of the OLE object.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="csharp" >}}
