---
title: Solid Gitterlinien beim Konvertieren von Excel in PDF mit Python.NET rendern
linktitle: Solid Gitterlinien rendern
type: docs
weight: 390
url: /de/python-net/render-solid-gridline-while-converting-excel-to-pdf/
description: Lerne, wie man beim Excel zu PDF Konvertieren mit Aspose.Cells für Python via .NET Solid Gitterlinien anzeigt.

---

Aus Kompatibilitätsgründen rendern Aspose.Cells standardmäßig Gitterlinien als gepunktete Linien beim Konvertieren von Excel in PDF. Moderne Versionen von Excel rendern Gitterlinien jedoch als durchgezogene Linien.

Mit der Option [PdfSaveOptions.gridline_type](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/gridline_type/), kann Aspose.Cells Gitterlinien auch als durchgehende Linien rendern.

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
