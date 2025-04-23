---
title: Intégrer une pièce jointe dans un PDF avec Python.NET
linktitle: Intégrer la pièce jointe dans le PDF
type: docs
weight: 380
url: /fr/python-net/embed-attachment-to-pdf/
description: Apprenez comment intégrer des pièces jointes d objets Ole dans des fichiers PDF utilisant Aspose.Cells pour Python via .NET.
---

Dans Excel, vous pouvez insérer un Ole Object avec des données source ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Double-cliquez sur l'Ole Object pour ouvrir le fichier intégré.

Lors de la conversion en PDF, l’Ole Object est généralement rendu sous forme d’icône ou de vignette sans données source. En utilisant la propriété [PdfSaveOptions.embed_attachments](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/embed_attachments/), vous pouvez intégrer les données source de l'Ole Object en tant que pièce jointe en PDF. Les utilisateurs peuvent double-cliquer sur l'icône/vignette dans le PDF pour accéder au fichier intégré.

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
