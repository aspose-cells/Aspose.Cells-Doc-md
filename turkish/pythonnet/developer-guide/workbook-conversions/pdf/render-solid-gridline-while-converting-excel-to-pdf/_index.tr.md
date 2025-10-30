---
title: Python.NET kullanarak Excel i PDF ye dönüştürürken Katı Izgaraları Çiz.
linktitle: Katı Izgaraları Çiz
type: docs
weight: 390
url: /tr/python-net/render-solid-gridline-while-converting-excel-to-pdf/
description: Aspose.Cells for Python via .NET kullanarak Excel den PDF ye dönüştürürken katı ızgaraları nasıl göstereceğinizi öğrenin.

---

Uyumluluk için eski sürümlerle, Aspose.Cells varsayılan olarak çizgili çizgiler olarak ızgaraları render ederken, modern Excel artık ızgaraları katı çizgiler olarak gösterir.

[PdfSaveOptions.gridline_type](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/gridline_type/) seçeneği ile Aspose.Cells ızgaraları da katı çizgiler olarak gösterebilir.

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
{{< app/cells/assistant language="python-net" >}}
