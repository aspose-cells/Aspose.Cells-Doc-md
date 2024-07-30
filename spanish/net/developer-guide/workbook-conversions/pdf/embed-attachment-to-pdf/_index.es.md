---
title: Incluir adjunto en PDF
type: docs
weight: 380
url: /es/net/embed-attachment-to-pdf/

---

En Excel, puedes insertar un Objeto Ole con datos de origen ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Haz doble clic en el Objeto Ole y se abrirá el archivo incrustado.

Generalmente, al convertir a PDF, el Objeto Ole se representará como un ícono o una miniatura sin los datos de origen del Objeto Ole. Con la opción [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/), puedes incrustar los datos de origen del Objeto Ole como un adjunto en PDF. Puedes hacer doble clic en el ícono o la miniatura en el PDF para abrir el archivo fuente del Objeto Ole.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![archivo-incrustado.png](archivo-incrustado.png)
