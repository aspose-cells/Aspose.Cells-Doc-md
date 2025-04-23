---
title: Rendre des lignes de quadrillage solides lors de la conversion Excel en PDF avec Python.NET
linktitle: Rendre des lignes de quadrillage solides
type: docs
weight: 390
url: /fr/python-net/render-solid-gridline-while-converting-excel-to-pdf/
description: Apprenez comment afficher des lignes de quadrillage solides lors de la conversion Excel en PDF en utilisant Aspose.Cells pour Python via .NET.

---

Pour la compatibilité avec les versions plus anciennes, Aspose.Cells rend par défaut les lignes de grille en pointillés lors de la conversion d'Excel en PDF. Cependant, Excel moderne rend maintenant les lignes de grille en lignes solides.

 Avec l’option [PdfSaveOptions.gridline_type](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/gridline_type/), Aspose.Cells peut également rendre les lignes de quadrillage comme des lignes solides.

```python
import os
from aspose.cells import Workbook, PdfSaveOptions, GridlineType

# Create an empty Workbook
wb = Workbook()

# Prepare data
worksheet = wb.worksheets[0]
worksheet.cells.get("D9").put_value("gridline")

# Enable to print gridline
worksheet.page_setup.print_gridlines = True

# Set to render gridline as solid line
pdf_save_options = PdfSaveOptions()
pdf_save_options.gridline_type = GridlineType.HAIR

# Save the pdf file with PdfSaveOptions
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, "output")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

wb.save(os.path.join(output_dir, "test_Cs.pdf"), pdf_save_options)
```

![solid-gridline.png](solid-gridline.png)
