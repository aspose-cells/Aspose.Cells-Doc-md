---
title: إرفاق المرفقات إلى PDF باستخدام Python.NET
linktitle: تضمين مرفق في ملف PDF
type: docs
weight: 380
url: /ar/python-net/embed-attachment-to-pdf/
description: تعلم كيفية إرفاق مرفقات كائن Ole في ملفات PDF باستخدام Aspose.Cells لـ Python via .NET.
---

في Excel، يمكنك إدراج كائن Ole مع بيانات المصدر (مثال: embedded-attachments-example.xlsx). انقر نقرًا مزدوجًا على كائن Ole لفتح الملف المدمج.

عند التحويل إلى PDF، يتم عادةً عرض كائن Ole كرمز أو صورة مصغرة بدون بيانات المصدر. باستخدام خاصية [PdfSaveOptions.embed_attachments](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/embed_attachments/)، يمكنك إرفاق بيانات مصدر كائن Ole كمرفق في PDF. يمكن للمستخدمين النقر نقرًا مزدوجًا على الرمز أو الصورة المصغرة في PDF للوصول إلى الملف المدمج.

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
{{< app/cells/assistant language="python-net" >}}
