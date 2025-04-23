---
title: Anhang in PDF einbetten
type: docs
weight: 380
url: /de/net/embed-attachment-to-pdf/

---

In Excel können Sie ein Ole-Objekt mit Quelldaten einfügen ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Durch Doppelklick auf das Ole-Objekt wird die eingebettete Datei geöffnet.

Beim Konvertieren in PDF wird das Ole-Objekt in der Regel als Symbol oder Thumbnail ohne die Quelldaten des Ole-Objekts dargestellt. Mit der Option [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/) können Sie die Quelldaten des Ole-Objekts als Anhang im PDF einbetten. Durch Doppelklicken auf das Symbol oder Thumbnail können Sie die Quelldatei des Ole-Objekts im PDF öffnen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="csharp" >}}
