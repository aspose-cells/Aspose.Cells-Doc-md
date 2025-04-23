---
title: تحويل التواريخ إلى تواريخ يابانية باستخدام Python.NET
linktitle: تحويل التواريخ إلى تواريخ يابانية
type: docs
weight: 350
url: /ar/python-net/convert-dates-to-japanese-dates/
description: تعلّم كيفية تحويل التواريخ الميلادية إلى تواريخ يابانية في ملفات إكسل باستخدام Aspose.Cells لـ Python via .NET.
---

{{% alert color="primary" %}} 

في التقويم الياباني، يبدأ عصر جديد مع عهد إمبراطور جديد. في 1 مايو 2019، تولى إمبراطور جديد الحكم، والتي انتهى معها عهد هيسي وبدأ عهد ريو وا.

{{% /alert %}} 

يوفر Aspose.Cells طريقة لتحويل التواريخ الميلادية إلى تواريخ يابانية مع مراعاة تغييرات العهد. يوضح مقتطف الشفرة التالي تحويل ملف إكسل المصدر الذي يحتوي على تواريخ ميلادية إلى ملف PDF بإشارات يابانية للتواريخ:

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)

```python
import os
from aspose.cells import Workbook, LoadOptions, LoadFormat, SaveFormat, CountryCode

# Source directory
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "data")
output_dir = os.path.join(current_dir, "output")

# Create output directory if not exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize load options with XLSX format
options = LoadOptions(LoadFormat.XLSX)
options.region = CountryCode.JAPAN

# Load workbook with Japanese regional settings
workbook = Workbook(os.path.join(source_dir, "JapaneseDates.xlsx"), options)

# Save as PDF
workbook.save(os.path.join(output_dir, "JapaneseDates.pdf"), SaveFormat.PDF)
```

**تحويل Python.NET:**


ملاحظة: تأكد من تفعيل دعم اللغة اليابانية في بيئتك لضمان دقة تحويل العهود. تقدم فئة Workbook و PdfSaveOptions الوظائف اللازمة لهذا التحويل.
