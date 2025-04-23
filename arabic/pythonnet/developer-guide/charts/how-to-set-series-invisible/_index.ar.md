---
title: كيفية تعيين إخفاء السلسلة باستخدام Python.NET
linktitle: كيفية إخفاء سلسلة
type: docs
weight: 74
url: /ar/python-net/how-to-set-series-invisible/
description: تعلم كيف تخفي سلاسل المخططات في Excel باستخدام Aspose.Cells لبايثون via .NET مع هذا الدليل خطوة بخطوة.
keywords: مخطط إكسل، إخفاء السلسلة، خاصية is_filtered، Aspose.Cells لبايثون
---

## **كيفية تعيين السلسلة غير مرئية في مخطط Excel**

في رسم بياني في إكسل، يمكنك النقر بزر الماوس الأيمن على الرسم البياني، والنقر على "اختيار البيانات"، وفي النافذة المنبثقة، اضبط ما إذا كانت السلسلة مرئية عن طريق تحديدها أو إلغاء تحديدها.
يمكنك تنزيل الملف النموذجي التالي [ملف عينة](SeriesFiltered.xlsx) وتشغيله في إكسل كما هو موضح في الصورة لتحقيق هذه الوظيفة. بعد ذلك، سنوضح لك كيفية إنجاز ذلك باستخدام مكتبة Aspose.Cells للبايثون via .NET.

![todo:image_alt_text](series-invisible.png)

## **كيفية ضبط سلسلة غير مرئية باستخدام Aspose.Cells**

استخدم الكود التالي لضبط السلسلة غير مرئية باستخدام Aspose.Cells للبايثون via .NET:

```python
import os
from aspose.cells import Workbook

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Load sample workbook
workbook = Workbook(os.path.join(data_dir, "SeriesFiltered.xlsx"))

# Access charts from first worksheet
charts = workbook.worksheets[0].charts
chart = charts.get("Chart 1")

# Get series collections
n_series_filtered = chart.filtered_n_series
n_series = chart.n_series

# Filter series by marking them as filtered
n_series[1].is_filtered = True
n_series[0].is_filtered = True

# Save modified workbook
workbook.save(os.path.join(data_dir, "output.xlsx"))
```

يمكنك الحصول على الملف المدخل التالي [Input file](SeriesFiltered.xlsx) وملف الإخراج [output file](output.xlsx).

كما هو موضح في الصورة أدناه، السلسلتان الأوليان اللتان كانت مرئيتين أصلاً أصبحتا غير مرئيتين في الملف الناتج.
![todo:image_alt_text](output.png)
