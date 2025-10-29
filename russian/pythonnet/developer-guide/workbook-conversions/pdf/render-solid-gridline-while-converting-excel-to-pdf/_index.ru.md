---
title: Отрисовка сплошных линий сетки при конвертации Excel в PDF с помощью Python.NET
linktitle: Отрисовать сплошные линии сетки
type: docs
weight: 390
url: /ru/python-net/render-solid-gridline-while-converting-excel-to-pdf/
description: Узнайте, как отображать сплошные линии сетки во время конвертации Excel в PDF с помощью Aspose.Cells для Python via .NET.

---

Для совместимости со старыми версиями Aspose.Cells по умолчанию отображает линии сетки пунктирными при преобразовании Excel в PDF. Однако современные версии Excel отображают линии сетки как сплошные линии.

С опцией [PdfSaveOptions.gridline_type](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/gridline_type/), Aspose.Cells также может отображать линии сетки как сплошные линии.

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
