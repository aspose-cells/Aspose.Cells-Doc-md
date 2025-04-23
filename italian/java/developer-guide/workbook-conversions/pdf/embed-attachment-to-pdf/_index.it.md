---
title: Incorpora allegato in PDF
type: docs
weight: 370
url: /it/java/embed-attachment-to-pdf/

---

In Excel, puoi inserire un Oggetto Ole con dati sorgente ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)) . Fai doppio clic sull'Ole Object, il file incorporato verrà aperto.

In generale, durante la conversione in pdf, l'Ole Object sarà renderizzato come un'icona o una miniatura senza i dati sorgente dell'Ole Object. Con l'opzione [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-), puoi incorporare i dati sorgente dell'Ole Object come allegato nel PDF. Puoi fare doppio clic sull'icona o sulla miniatura nel PDF per aprire il file di origine dell'Ole Object.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}

![embedded-attachment.png](embedded-attachment.png)

{{< app/cells/assistant language="java" >}}
