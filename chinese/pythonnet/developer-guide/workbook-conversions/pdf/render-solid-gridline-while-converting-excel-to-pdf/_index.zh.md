---
title: 在将 Excel 转换为 PDF 时渲染实心网格线（Render Solid Gridlines）使用 Python.NET
linktitle: 渲染实心网格线
type: docs
weight: 390
url: /zh/python-net/render-solid-gridline-while-converting-excel-to-pdf/
description: 学习如何在使用 Aspose.Cells for Python via .NET 转换 Excel 为 PDF 时显示实线网格线。

---

为了兼容旧版本，Aspose.Cells在将Excel转换为PDF时默认渲染网格线为点线。然而，现代Excel现在将网格线渲染为实线。

通过 [PdfSaveOptions.gridline_type](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/gridline_type/) 选项，Aspose.Cells 还可以将网格线渲染为实线。

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
