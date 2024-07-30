---
title: Bädda in bilaga i PDF
type: docs
weight: 370
url: /sv/java/embed-attachment-to-pdf/

---

I Excel kan du sätta in ett OLE-objekt med källdata ([inbäddade-bilagor-exempel.xlsx](inbäddade-bilagor-exempel.xlsx)). Dubbelklicka på OLE-objektet, den inbäddade filen öppnas.

Vanligtvis, vid konvertering till pdf, renderas OLE-objektet som en ikon eller en miniatyrbild utan OLE-objektets källdata. Med alternativet [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-) kan du bädda in OLE-objektets källdata som bilaga i PDF. Du kan dubbelklicka på ikonen eller miniatyren i PDF för att öppna OLE-objektets källfil.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}

![inbäddad-bilaga.png](inbäddad-bilaga.png)

