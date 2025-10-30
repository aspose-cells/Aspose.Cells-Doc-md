---
title: Incrustar adjunto en PDF con Golang vía C++
linktitle: Agregar adjunto a PDF
type: docs
weight: 380
url: /es/go-cpp/embed-attachment-to-pdf/
description: Aprenda a incrustar archivos adjuntos en PDF usando Aspose.Cells con Golang vía C++.
---

En Excel, puedes insertar un Objeto OLE con datos de origen ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Haz doble clic en el Objeto OLE y el archivo incrustado se abrirá.

Generalmente, al convertir a PDF, el Objeto Ole se representará como un ícono o miniatura sin los datos de origen del Objeto Ole. Con la opción [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getembedattachments/), puede incrustar los datos de origen del Objeto Ole como un adjunto en el PDF. Puede hacer doble clic en el ícono o la miniatura en el PDF para abrir el archivo fuente del Objeto Ole.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EmbedAttachmentToPdf.go" >}}
![embedded-attachment.png](embedded-attachment.png)
