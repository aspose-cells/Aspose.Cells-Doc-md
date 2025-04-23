---
title: Visualizza linee di griglia solide durante la conversione di Excel in PDF con Python.NET
linktitle: Renderizza linee di griglia solide
type: docs
weight: 390
url: /it/python-net/render-solid-gridline-while-converting-excel-to-pdf/
description: Scopri come visualizzare linee di griglia solide durante la conversione da Excel a PDF usando Aspose.Cells per Python via .NET.

---

Per compatibilità con versioni più vecchie, Aspose.Cells rende le linee di griglia come linee tratteggiate per impostazione predefinita durante la conversione di Excel in PDF. Tuttavia, Excel moderno rende le linee di griglia come linee solide al giorno d'oggi.

Con l'opzione [PdfSaveOptions.gridline_type](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/gridline_type/), Aspose.Cells può anche rendere le linee di griglia come linee solide.

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
