---
title: تعطيل CSS أثناء الحفظ بصيغة HTML باستخدام Python.NET
linktitle: تعطيل CSS أثناء الحفظ بصيغة HTML
type: docs
weight: 320
url: /ar/python-net/disable-css-while-saving-to-html/
description: تعلم كيفية تعطيل أنماط CSS عند حفظ ملفات إكسل بصيغة HTML باستخدام API الخاص بـ Aspose.Cells for Python via .NET.
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف إكسل كصفحة HTML منفردة، عادةً سيتم تضمين عناصر CSS داخل ملف HTML وستكون موجودة في قسم HEAD. إذا قمت بإرفاق هذا الملف كمحتوى/جسم للبريد الإلكتروني، فسيتم stripout عناصر CSS من قبل معظم عملاء البريد الإلكتروني، مما يؤدي إلى عرض غير صحيح. يقدم API Aspose.Cells for Python via .NET خيارًا يتيح لك بشكل اختياري تعطيل CSS، مما يسمح بتطبيق الأنماط مباشرة داخل عناصر HTML. إذا كنت ترغب في تعيين HTML كمحتوى/جسم البريد الإلكتروني، يرجى استخدام الخاصية [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/) وتعيينها إلى **True**.

## **تعطيل CSS أثناء الحفظ بصيغة HTML**

يعرض مثال الكود التالي استخدام الخاصية [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/).

## **الكود المثالي**

```python
import os
from aspose.cells import Workbook, HtmlSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Load sample workbook
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "source")
output_dir = os.path.join(current_dir, "output")

wb = Workbook(os.path.join(source_dir, "sampleDisableCss.xlsx"))

# Disable CSS
opts = HtmlSaveOptions()
opts.disable_css = True

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Save the workbook in html
wb.save(os.path.join(output_dir, "outputDisable.html"), opts)
```
