---
title: Anhang in PDF mit Golang via C++ einbetten
linktitle: Anhang in PDF einbetten
type: docs
weight: 380
url: /de/go-cpp/embed-attachment-to-pdf/
description: Lernen Sie, wie Sie Anhänge mit Aspose.Cells unter Golang via C++ in PDF einbetten.
---

In Excel können Sie ein Ole-Objekt mit Quelldaten einfügen ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Doppelklicken Sie auf das Ole-Objekt, um die eingebettete Datei zu öffnen.

 Generell wird bei der Konvertierung in PDF das Ole-Objekt als Symbol oder Vorschaubild ohne die Quelldaten des Ole-Objekts dargestellt. Mit der Option [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getembedattachments/) können Sie die Quelldaten des Ole-Objekts als Anhang in PDF einbetten. Sie können im PDF auf das Symbol oder die Vorschaubild doppelklicken, um die Quelldatei des Ole-Objekts zu öffnen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EmbedAttachmentToPdf.go" >}}
![embedded-attachment.png](embedded-attachment.png)
