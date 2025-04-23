---
title: Inbädda bilaga till PDF
type: docs
weight: 370
url: /sv/java/embed-attachment-to-pdf/

---

I Excel kan du infoga ett Ole-objekt med källdata ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Dubbelklicka på Ole-objektet för att öppna den inbäddade filen.

Generellt, vid konvertering till PDF, kommer Ole-objektet att renderas som en ikon eller miniatyrbild utan Ole-objektets käll data. Med alternativet [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-), kan du bädda in Ole-objektets källdata som bilaga i PDF. Du kan dubbelklicka på ikonen eller miniatyrbilden i PDF för att öppna källa filen för Ole-objektet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}

![embedded-attachment.png](embedded-attachment.png)

{{< app/cells/assistant language="java" >}}
