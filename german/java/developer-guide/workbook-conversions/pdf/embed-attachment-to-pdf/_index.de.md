---
title: Anhang in PDF einbetten
type: docs
weight: 370
url: /de/java/embed-attachment-to-pdf/

---

In Excel können Sie ein OLE-Objekt mit Quelldaten ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)) einfügen. Doppelklicken Sie auf das OLE-Objekt, um die eingebettete Datei zu öffnen.

Im Allgemeinen wird beim Konvertieren in PDF das OLE-Objekt als Symbol oder als Miniaturansicht ohne die OLE-Objekt-Quelldaten dargestellt. Mit der Option [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-) können Sie die OLE-Objekt-Quelldaten als Anhang in PDF einbetten. Sie können im PDF auf das Symbol oder die Miniatur klicken, um die Quelldatei des OLE-Objekts zu öffnen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}

![embedded-attachment.png](embedded-attachment.png)

