---
title: كيفية طباعة إكسل كصفحات ملائمة عرضها وارتفاعها باستخدام Python.NET
linktitle: كيفية طباعة إكسل كصفحات مناسبة للعرض بشكل واسع ومرتفعة
type: docs
weight: 200
url: /ar/python-net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: تعلم كيفية تعيين خصائص fit_to_pages_wide و fit_to_pages_tall لطباعة إكسل باستخدام API الخاص بـ Aspose.Cells للبايثون via .NET.
keywords: طباعة إكسل بلغة بايثون، إعدادات التوافق للطباعة، Fit to Pages Wide، Fit to Pages Tall، طباعة ورقة عمل كصفحة واحدة، طباعة جميع الأعمدة في صفحة واحدة
---

## **مقدمة**

تتحكم إعدادات fit_to_pages_wide و fit_to_pages_tall في مقياس استيعاب ورقة العمل أثناء الطباعة. تضمن هذه الإعدادات أن يتناسب الناتج المطبوع مع أبعاد الصفحة المحددة:

1. **fit_to_pages_wide**: يحدد عدد الصفحات الأفقية للطباعة
1. **fit_to_pages_tall**: يحدد عدد الصفحات الرأسية للطباعة

## **لماذا نستخدم FitToPagesWide و FitToPagesTall**
تشمل المزايا الرئيسية:
1. تحكم دقيق في تنسيق الطباعة
1. تنسيق متناسق لورقات متعددة
1. تقديم وثيقة احترافية

## **كيفية طباعة الملف كصفحات مناسبة عريضة وطويلة في Excel**
للتكوين في Microsoft Excel:
1. افتح دفتر العمل واختر ورقة العمل
1. انتقل إلى **تخطيط الصفحة** → حوار **إعداد الصفحة**
1. في علامة التبويب **صفحة** تحت **تحجيم**:
   - اختر "ملائمة لـ"
   - حدد عدد الصفحات عرضيًا (أفقيًا) وعموديًا (رأسيًا)

<br>
<img src="2.png" width=60% />

## **كيفية طباعة Excel كصفحات مناسبة عريضة وطويلة باستخدام Aspose.Cells**
للتكوين برمجيًا:
1. حمّل [ملف النموذج](input.xlsx)
1. الوصول إلى كائن ورقة العمل [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/)
1. تعيين خصائص [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall/) و [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide/)

```python
from aspose.cells import Workbook

# Instantiating a Workbook object
workbook = Workbook("input.xlsx")

# Accessing the first worksheet in the Excel file
worksheet = workbook.worksheets[0]

# Setting the number of pages to which the length of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_tall = 1

# Setting the number of pages to which the width of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_wide = 1

# Save the workbook
workbook.save("out_net.pdf")
```

النتيجة المخرجة:
<br>
<img src="1.png" width=60% />

## **كيفية طباعة ورقة العمل كصفحة واحدة**
لفرض إخراج صفحة واحدة:
1. استخدم [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. قم بتعيين خاصية [**one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/one_page_per_sheet/)

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting OnePagePerSheet option
options.one_page_per_sheet = True

# Save the workbook with options
workbook.save("OnePagePerSheet.pdf", options)
```

النتيجة المخرجة:
<br>
<img src="3.png" width=60% />

## **كيفية طباعة جميع الأعمدة في صفحة واحدة**
لدمج الأعمدة أفقياً:
1. تكوين [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. تفعيل خاصية [**all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/all_columns_in_one_page_per_sheet/)

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting all columns in one page per sheet
options.all_columns_in_one_page_per_sheet = True

# Save the workbook
workbook.save("AllColumnsInOnePagePerSheet.pdf", options)
```

النتيجة المخرجة:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="python-net" >}}
