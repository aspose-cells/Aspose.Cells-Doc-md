---
title: Anhang in PDF mit Python.NET einbetten
linktitle: Anhang in PDF einbetten
type: docs
weight: 380
url: /de/python-net/embed-attachment-to-pdf/
description: Lerne, wie man Ole Objekt Anhänge in PDF Dateien mit Aspose.Cells für Python via .NET einbettet.
---

In Excel kannst du ein Ole-Objekt mit Quell-Daten einfügen ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Doppelklicke auf das Ole-Objekt, um die eingebettete Datei zu öffnen.

Beim Konvertieren zu PDF wird das Ole-Objekt typischerweise als Symbol oder Miniaturansicht ohne Quelldaten dargestellt. Mit der Eigenschaft [PdfSaveOptions.embed_attachments](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/embed_attachments/) kannst du die Quelldaten des Ole-Objekts als Anhang in PDF einbetten. Benutzer können im PDF auf das Symbol/die Miniaturansicht doppelklicken, um die eingebettete Datei zu öffnen.

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
