---
title: Inbädda bilaga till PDF
type: docs
weight: 380
url: /sv/net/embed-attachment-to-pdf/

---

I Excel kan du infoga ett Ole-objekt med källdata ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Dubbelklicka på Ole-objektet för att öppna den inbäddade filen.

Allmänt, vid konvertering till PDF, kommer Ole-objektet att renderas som en ikon eller miniatyrbild utan källdata. Med alternativet [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/) kan du bädda in Ole-objektets källdata som bilaga i PDF. Dubbelklicka på ikonen eller miniatyrbilden i PDF för att öppna källfilen till Ole-objektet.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="csharp" >}}
