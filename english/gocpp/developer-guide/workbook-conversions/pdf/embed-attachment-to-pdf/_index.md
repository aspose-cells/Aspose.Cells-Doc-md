---
title: Embed Attachment to PDF with Golang via C++
linktitle: Embed Attachment to PDF
type: docs
weight: 380
url: /go-cpp/embed-attachment-to-pdf/
description: Learn how to embed attachments into PDF using Aspose.Cells with Golang via C++.
---

In Excel, you can insert an Ole Object with source data ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Double click the Ole Object, the embedded file will be opened.

Generally, while converting to PDF, the Ole Object will be rendered as an icon or a thumbnail without the Ole Object source data. With option [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getembedattachments/), you can embed the Ole Object source data as an attachment in PDF. You can double click the icon or the thumbnail in PDF to open the source file of the Ole Object.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EmbedAttachmentToPdf.go" >}}
![embedded-attachment.png](embedded-attachment.png)