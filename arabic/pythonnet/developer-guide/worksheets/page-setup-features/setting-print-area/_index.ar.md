---
title: كيفية تعيين منطقة الطباعة باستخدام Python.NET
linktitle: كيفية تعيين منطقة الطباعة
type: docs
weight: 200
url: /ar/python-net/how-to-set-print-area/
description: تعلم كيفية تعيين ومسح مناطق الطباعة في ملفات إكسل باستخدام Aspose.Cells لـ Python via .NET.
keywords: تعيين منطقة الطباعة في وثيقة يساعد على التحكم في المحتوى المطلوب طباعته. الأسباب الرئيسية تتضمن 
---

## **سيناريوهات الاستخدام المحتملة**

تعيين منطقة الطباعة في مستند يساعد على التحكم في المحتوى المطبوعة. الأسباب الرئيسية تشمل:

1. التركيز على بيانات معينة: طباعة الأقسام ذات الصلة فقط
1. تحسين التخطيط: تنظيم المحتوى بشكل أنيق عبر الصفحات
1. توفير الموارد: تقليل استهلاك الورق/الحبر
1. تقديم عرض احترافي: ضمان مخرجات مصقولة
1. الثبات: الحفاظ على مخرجات طباعة موحدة

## **كيفية تعيين منطقة الطباعة في Excel**

لتعيين منطقة الطباعة برمجيًا:

1. الوصول إلى خصائص إعداد صفحة ورقة العمل
1. تحديد منطقة الطباعة باستخدام تدوين نطاق الخلية
1. حفظ المصنف المعدل

```python
# Sample image reference remains unchanged
<img src="3.png" width=60% />
```

## **كيفية مسح مجال الطباعة في إكسل**

لإزالة قيود منطقة الطباعة:

1. الوصول إلى خصائص إعداد الصفحة
1. إعادة تعيين منطقة الطباعة إلى سلسلة فارغة
1. حفظ التغييرات

```python
# Sample image reference remains unchanged
<img src="4.png" width=60% />
```

## **ماذا يحدث بعد مسح مجال الطباعة**

مسح منطقة الطباعة يؤدي إلى:

1. الطباعة الافتراضية لكل ورقة عمل
1. إزالة قيود النطاق السابقة
1. تضمين جميع الخلايا المنسقة

## **كيفية ضبط مجال الطباعة باستخدام Aspose.Cells**

تعيين منطقة الطباعة من خلال إعداد صفحة ورقة العمل:

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set print area to A1:D10
worksheet.page_setup.print_area = "A1:D10"

# Save modified workbook
workbook.save("output_set_print_area.xlsx")
```

```python
# Output image reference
<img src="1.png" width=60% />
```

## **كيفية مسح مجال الطباعة باستخدام Aspose.Cells**

إزالة تعريف منطقة الطباعة الموجود:

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Clear print area
worksheet.page_setup.print_area = ""

# Save modified workbook
workbook.save("output_clear_print_area.xlsx")
```

```python
# Output image reference
<img src="2.png" width=60% />
```

```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Set the print area - specify the range you want to print
worksheet.page_setup.print_area = "A1:D10"

# Save the workbook
workbook.save("set_print_area.pdf")
```
```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Clear the print area
worksheet.page_setup.print_area = ""

# Save the workbook
workbook.save("clear_print_area.pdf")
```
