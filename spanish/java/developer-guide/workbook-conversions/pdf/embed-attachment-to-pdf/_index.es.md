---
title: Agregar adjunto a PDF
type: docs
weight: 370
url: /es/java/embed-attachment-to-pdf/

---

En Excel, puedes insertar un Objeto Ole con datos fuente ([ejemplo de adjuntos incrustados.xlsx](embedded-attachments-example.xlsx)). Haz doble clic en el Objeto Ole, el archivo incrustado se abrirá.

Por lo general, al convertir a PDF, el Objeto Ole se renderiza como un ícono o una miniatura sin los datos de origen del Objeto Ole. Con la opción [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-), puedes incrustar los datos de origen del Objeto Ole como adjunto en el PDF. Puedes hacer doble clic en el ícono o la miniatura en el PDF para abrir el archivo fuente del Objeto Ole.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}

![embedded-attachment.png](embedded-attachment.png)

{{< app/cells/assistant language="java" >}}
