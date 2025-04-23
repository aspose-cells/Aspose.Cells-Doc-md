---
title: Incorpora allegato in PDF
type: docs
weight: 380
url: /it/net/embed-attachment-to-pdf/

---

In Excel, puoi inserire un Oggetto Ole con dati sorgente ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)) . Fai doppio clic sull'Ole Object, il file incorporato verrà aperto.

In generale, durante la conversione in PDF, l'Ole Object verrà visualizzato come un'icona o un'anteprima senza i dati sorgente dell'Ole Object. Con l'opzione [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/), puoi incorporare i dati sorgente dell'Ole Object come allegato nel PDF. Puoi fare doppio clic sull'icona o sull'anteprima nel PDF per aprire il file sorgente dell'Ole Object.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="csharp" >}}
