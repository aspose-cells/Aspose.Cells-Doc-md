---
title: Incorporare Allegati in PDF con Golang tramite C++
linktitle: Incorpora allegato in PDF
type: docs
weight: 380
url: /it/go-cpp/embed-attachment-to-pdf/
description: Impara come incorporare allegati in PDF usando Aspose.Cells con Golang tramite C++.
---

In Excel, puoi inserire un Oggetto Ole con dati di origine ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Fai doppio clic sull’Ole Object, il file incorporato si aprirà.

 In generale, durante la conversione in PDF, l'Ole Object verrà rappresentato come un'icona o una miniatura senza i dati sorgente dell'Ole Object. Con l'opzione [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getembedattachments/), puoi incorporare i dati sorgente dell'Ole Object come allegato nel PDF. Puoi fare doppio clic sull'icona o sulla miniatura nel PDF per aprire il file sorgente dell'Ole Object.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EmbedAttachmentToPdf.go" >}}
![embedded-attachment.png](embedded-attachment.png)
