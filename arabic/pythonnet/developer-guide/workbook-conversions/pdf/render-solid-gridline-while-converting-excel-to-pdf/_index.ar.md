---
title: عرض خطوط الشبكة الصلبة أثناء تحويل Excel إلى PDF باستخدام Python.NET
linktitle: عرض خطوط الشبكة الصلبة
type: docs
weight: 390
url: /ar/python-net/render-solid-gridline-while-converting-excel-to-pdf/
description: تعرف على كيفية عرض خطوط الشبكة الصلبة أثناء تحويل Excel إلى PDF باستخدام Aspose.Cells لـ Python via .NET.

---

للتوافق مع الإصدارات الأقدم، يقوم Aspose.Cells بعرض خطوط الشبكة كنقاط منقطة بشكل افتراضي أثناء تحويل Excel إلى PDF. ومع ذلك، تعرض إصدارات Excel الحديثة خطوط الشبكة كخطوط صلبة في الوقت الحاضر.

مع خيار [PdfSaveOptions.gridline_type](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/gridline_type/)، يمكن لـ Aspose.Cells أيضًا عرض خطوط الشبكة كخطوط صلبة.

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
