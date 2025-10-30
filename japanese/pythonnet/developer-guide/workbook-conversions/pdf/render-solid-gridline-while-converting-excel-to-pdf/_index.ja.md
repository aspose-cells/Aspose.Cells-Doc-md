---
title: Python.NETを使ったExcelからPDFへの変換時にサイドグリッドラインを描画する
linktitle: サイドグリッドラインの描画
type: docs
weight: 390
url: /ja/python-net/render-solid-gridline-while-converting-excel-to-pdf/
description: Aspose.Cells for Python via .NETを使用して、ExcelからPDFへの変換中にグリッドラインを実線で表示する方法を学びます。

---

古いバージョンとの互換性のため、Aspose.Cellsはデフォルトでは点線のラインとしてグリッドラインをレンダリングします。ただし、現代のExcelではグリッドラインは実線としてレンダリングされます。

[PdfSaveOptions.gridline_type](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/gridline_type/) オプションを使用すると、Aspose.Cellsはグリッドラインを実線としてレンダリングすることもできます。

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
