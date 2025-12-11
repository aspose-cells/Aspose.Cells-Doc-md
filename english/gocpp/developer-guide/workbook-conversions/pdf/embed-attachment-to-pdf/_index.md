---
title: Embed Attachment to PDF with Golang via C++
linktitle: Embed Attachment to PDF
type: docs
weight: 380
url: /go-cpp/embed-attachment-to-pdf/
description: Learn how to embed attachments into PDF using Aspose.Cells with Golang via C++.
---

In Excel, you can insert an OLE object with source data ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Double‑click the OLE object; the embedded file will be opened.

Generally, while converting to PDF, the OLE object will be rendered as an icon or a thumbnail without the OLE object's source data. With the option [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getembedattachments/), you can embed the OLE object's source data as an attachment in the PDF. You can double‑click the icon or the thumbnail in the PDF to open the source file of the OLE object.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EmbedAttachmentToPdf.go" >}}
![embedded-attachment.png](embedded-attachment.png)