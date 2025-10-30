---
title: Incorpora Allegato in PDF con Python.NET
linktitle: Incorpora allegato in PDF
type: docs
weight: 380
url: /it/python-net/embed-attachment-to-pdf/
description: Scopri come incorporare allegati Oggetto OLE nei file PDF usando Aspose.Cells per Python via .NET.
---

In Excel, puoi inserire un Oggetto OLE con dati sorgente ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Fai doppio clic sull'OLE per aprire il file incorporato.

Durante la conversione in PDF, l'Ole Object viene tipicamente rappresentato come un'icona o miniatura senza dati di origine. Usando la proprietà [PdfSaveOptions.embed_attachments](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/embed_attachments/), puoi incorporare i dati sorgente dell'Ole come allegato nel PDF. Gli utenti possono fare doppio clic sull'icona/miniatura nel PDF per accedere al file incorporato.

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
