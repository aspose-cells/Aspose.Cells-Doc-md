---
title: Bädda in bilaga i PDF
type: docs
weight: 380
url: /sv/net/embed-attachment-to-pdf/

---

I Excel kan du sätta in ett OLE-objekt med källdata ([inbäddade-bilagor-exempel.xlsx](inbäddade-bilagor-exempel.xlsx)). Dubbelklicka på OLE-objektet, den inbäddade filen öppnas.

Generellt sett kommer OLE-objektet vid konvertering till PDF att renderas som en ikon eller en miniatyrbild utan OLE-objektets källdata. Med alternativet [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/) kan du bädda in OLE-objektets källdata som bilaga i PDF. Du kan dubbelklicka på ikonen eller miniatyrbilden i PDF för att öppna källdokumentet för OLE-objektet.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![inbäddad-bilaga.png](inbäddad-bilaga.png)
