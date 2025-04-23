---
title: Agregar adjunto a PDF
type: docs
weight: 380
url: /es/net/embed-attachment-to-pdf/

---

En Excel, puedes insertar un Objeto Ole con datos fuente ([ejemplo de adjuntos incrustados.xlsx](embedded-attachments-example.xlsx)). Haz doble clic en el Objeto Ole, el archivo incrustado se abrirá.

Por lo general, al convertir a pdf, el Objeto Ole se renderizará como un ícono o una miniatura sin los datos fuente del Objeto Ole. Con la opción [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/), puedes incrustar los datos fuente del Objeto Ole como un adjunto en el PDF. Puedes hacer doble clic en el ícono o la miniatura en el PDF para abrir el archivo fuente del Objeto Ole.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="csharp" >}}
