---
title: Visa solida rutnätlinjer vid konvertering av Excel till PDF med Python.NET
linktitle: Visa solida rutnätlinjer
type: docs
weight: 390
url: /sv/python-net/render-solid-gridline-while-converting-excel-to-pdf/
description: Lär dig hur du visar solida rutnätlinjer under konvertering av Excel till PDF med Aspose.Cells för Python via .NET.

---

För kompatibilitet med äldre versioner, konverterar Aspose.Cells rutnätslinjer som prickade linjer som standard när du konverterar Excel till PDF. Moderna Excel-versioner visar dock rutnätslinjer som solida linjer numera.

Med alternativet [PdfSaveOptions.gridline_type](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/gridline_type/) kan Aspose.Cells också rendera rutnätslinjer som solida linjer.

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
