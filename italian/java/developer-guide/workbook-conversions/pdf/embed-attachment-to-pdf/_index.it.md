---
title: Incorpora Allegato in PDF
type: docs
weight: 370
url: /it/java/embed-attachment-to-pdf/

---

In Excel, è possibile inserire un Oggetto OLE con dati di origine ([esempio-di-allegati-inseriti.xlsx](esempio-di-allegati-inseriti.xlsx)) . Fare doppio clic sull'Oggetto OLE, il file incorporato verrà aperto.

In generale, durante la conversione in pdf, l'Oggetto OLE verrà rappresentato come icona o miniatura senza i dati di origine dell'Oggetto OLE. Con l'opzione [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-), è possibile incorporare i dati di origine dell'Oggetto OLE come allegato in PDF. È possibile fare doppio clic sull'icona o sulla miniatura in PDF per aprire il file di origine dell'Oggetto OLE.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}

![allegato-incorporato.png](allegato-incorporato.png)

