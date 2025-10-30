---
title: Infoga bilaga i PDF med Golang via C++
linktitle: Inbädda bilaga till PDF
type: docs
weight: 380
url: /sv/go-cpp/embed-attachment-to-pdf/
description: Lär dig hur du infogar bilagor i PDF med Aspose.Cells med Golang via C++.
---

I Excel kan du infoga ett Ole-objekt med källdata ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Dubbelklicka på Ole-objektet, det inbäddade filen öppnas.

Generellt, vid konvertering till PDF, kommer Ole-objekt att renderas som en ikon eller miniatyrbild utan Ole-objektets källdata. Med alternativet [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getembedattachments/) kan du bädda in Ole-objektets källdata som en bilaga i PDF. Dubbelklicka på ikonen eller miniatyrbilden i PDF för att öppna källfilen för Ole-objektet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EmbedAttachmentToPdf.go" >}}
![embedded-attachment.png](embedded-attachment.png)
