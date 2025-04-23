---
title: Anhang in PDF einbetten
type: docs
weight: 370
url: /de/java/embed-attachment-to-pdf/

---

In Excel können Sie ein Ole-Objekt mit Quelldaten einfügen ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Durch Doppelklick auf das Ole-Objekt wird die eingebettete Datei geöffnet.

Im Allgemeinen wird beim Konvertieren in PDF das Ole-Objekt als Symbol oder Miniaturansicht dargestellt, ohne die Quelldaten des Ole-Objekts. Mit der Option [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-) können Sie die Quelldaten des Ole-Objekts als Anhang im PDF einbetten. Ein Doppelklick auf das Symbol oder die Miniaturansicht im PDF öffnet die Quelldatei des Ole-Objekts.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}

![embedded-attachment.png](embedded-attachment.png)

{{< app/cells/assistant language="java" >}}
