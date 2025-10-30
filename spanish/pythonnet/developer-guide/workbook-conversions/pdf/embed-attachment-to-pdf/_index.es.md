---
title: Agregar adjunto a PDF con Python.NET
linktitle: Agregar adjunto a PDF
type: docs
weight: 380
url: /es/python-net/embed-attachment-to-pdf/
description: Aprende cómo incrustar adjuntos de objetos Ole en archivos PDF usando Aspose.Cells para Python via .NET.
---

En Excel, puedes insertar un objeto Ole con datos fuente ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Haz doble clic en el objeto Ole para abrir el archivo incrustado.

Al convertir a PDF, generalmente el objeto Ole se renderiza como un ícono o miniatura sin datos fuente. Usando la propiedad [PdfSaveOptions.embed_attachments](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/embed_attachments/), puedes incrustar los datos fuente del objeto Ole como un adjunto en PDF. Los usuarios pueden hacer doble clic en el ícono/miniatura en el PDF para acceder al archivo incrustado.

```python
from aspose.cells import Workbook, PdfSaveOptions

# Open the template file
wb = Workbook("embedded-attachments-example.xlsx")

# Set to embed Ole Object attachment.
pdf_save_options = PdfSaveOptions()
pdf_save_options.embed_attachments = True

# Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdf_save_options)
```

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="python-net" >}}
