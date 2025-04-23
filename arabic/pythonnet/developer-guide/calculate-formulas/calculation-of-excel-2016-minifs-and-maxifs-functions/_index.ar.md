---
title: حساب دوال MINIFS و MAXIFS في إكسل 2016 باستخدام Python.NET
linktitle: حساب وظائف MINIFS وMAXIFS في Excel 2016
type: docs
weight: 300
url: /ar/python-net/calculation-of-excel-2016-minifs-and-maxifs-functions/
description: تعلم كيفية حساب دوال MINIFS و MAXIFS في إكسل 2016 باستخدام Aspose.Cells لواجهة برمجية بايثون via .NET مع أمثلة على الكود.
keywords: بايثون إكسل، minifs maxifs، حساب الصيغ، aspose.cells
---

## **سيناريوهات الاستخدام المحتملة**
يدعم ميكروسوفت إكسل 2016 دالتي MINIFS و MAXIFS. لا تدعم هذه الدوال في إكسل 2013 أو الإصدارات الأقدم. كما يدعم Aspose.Cells حساب هذه الدوال. يوضح لقطة الشاشة التالية استخدام هذه الدوال. يرجى قراءة التعليقات الحمراء داخل لقطة الشاشة لفهم كيفية عمل هذه الدوال.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **حساب وظائف MINIFS و MAXIFS في Excel 2016**
حمّل الكود النموذجي ملف إكسل عينة، واستدعي طريقة workbook.calculate_formula() لأداء حساب الصيغة عبر Aspose.Cells، ثم احفظ النتائج في ملف PDF الناتج.


```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "data")
output_dir = os.path.join(current_dir, "output")

# Load your source workbook containing MINIFS and MAXIFS functions
workbook = Workbook(os.path.join(source_dir, "sampleMINIFSAndMAXIFS.xlsx"))

# Perform Aspose.Cells formula calculation
workbook.calculate_formula()

# Save the calculations result in pdf format
options = PdfSaveOptions()
options.one_page_per_sheet = True

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook.save(os.path.join(output_dir, "outputMINIFSAndMAXIFS.pdf"), options)
```
