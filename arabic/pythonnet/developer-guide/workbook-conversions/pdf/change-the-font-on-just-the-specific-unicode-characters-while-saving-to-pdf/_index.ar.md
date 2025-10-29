---
title: تغيير نوع الخط على أحرف يونيكود محددة عند الحفظ إلى PDF باستخدام Python.NET
linktitle: تغيير نوع الخط على أحرف يونيكود محددة
type: docs
weight: 260
url: /ar/python-net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: تعرف على كيفية تعديل الخطوط لأحرف يونيكود محددة أثناء تحويل PDF باستخدام Aspose.Cells لـ Python via .NET. ضمان دقة عرض النص مع استبدال الخط على مستوى الحرف.
---

{{% alert color="primary" %}}

بعض أحرف يونيكود غير قابلة للعرض بواسطة الخطوط المحددة من قبل المستخدم. أحد هذه الأحرف هو **الشرطة غير المتماسكة** (U+2011) برقم يونيكود 8209. لا يمكن عرض هذا الحرف مع **Times New Roman** ولكن يمكن عرضه مع خطوط مثل **Arial Unicode MS**.

عندما تظهر مثل هذه الأحرف في نص منسق باستخدام خط معين (مثل Times New Roman)، يقوم Aspose.Cells تلقائيًا بتغيير خط الكلمة/الجملة بأكملها إلى خط متوافق (مثل Arial Unicode MS). للمستخدمين الذين يرغبون في تغيير خط الحرف غير القابل للعرض فقط، نوفر تحكمًا دقيقًا من خلال الخاصية **PdfSaveOptions.is_font_substitution_char_granularity**.

{{% /alert %}}

## **مقارنة أمثلة**

تعرض لقطات الشاشة أدناه المخرجات مع إعدادات مختلفة. يُظهر ملف PDF الأول استبدال الخط الكامل للنص، بينما يغير الملف الثاني خط الحرف المحدد فقط.

|**الاستبدال الكامل للنص**|**الاستبدال على مستوى الحرف**|
| :- | :- |
|![تغيير الخط الكامل](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|![تغيير الخط الانتقائي](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

## **خطوات التنفيذ**

لتمكين استبدال الخط على مستوى الحرف:

1. إنشاء كائن [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)
2. الوصول إلى خلايا ورقة العمل باستخدام خاصية [**Worksheet.cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)
3. تعيين قيم الخلايا التي تحتوي على رموز يونيكود خاصة
4. تكوين [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) مع:
   - `is_font_substitution_char_granularity = True`
5. حفظ ملف العمل بامتداد PDF

```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Create workbook object
workbook = Workbook()

# Access the first worksheet
worksheet = workbook.worksheets[0]

# Access cells
cell1 = worksheet.cells.get("A1")
cell2 = worksheet.cells.get("B1")

# Set the styles of both cells to Times New Roman
style = cell1.get_style()
style.font.name = "Times New Roman"
cell1.set_style(style)
cell2.set_style(style)

# Put the values inside the cell
cell1.put_value("Hello without Non-Breaking Hyphen")
cell2.put_value("Hello" + chr(8209) + " with Non-Breaking Hyphen")

# Autofit the columns
worksheet.auto_fit_columns()

# Save to Pdf without setting PdfSaveOptions.is_font_substitution_char_granularity
workbook.save(os.path.join(data_dir, "SampleOutput_out.pdf"))

# Save to Pdf after setting PdfSaveOptions.is_font_substitution_char_granularity to true
opts = PdfSaveOptions()
opts.is_font_substitution_char_granularity = True
workbook.save(os.path.join(data_dir, "SampleOutput2_out.pdf"), opts)
```

## **مفتاح التكوين**

استخدم مكونات واجهة برمجة التطبيقات الأساسية التالية:

- فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) لإعدادات عرض PDF
- خاصية **is_font_substitution_char_granularity** لاستبدال الخطوط على مستوى الأحرف
- طريقة [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/) لإنشاء المخرجات

{{% alert color="note" %}} 
**ملاحظة الفرق في واجهة برمجة التطبيقات**: في Python.NET، تستخدم خصائص المنطق المنطقي snake_case (`is_font_substitution_char_granularity`) بدلاً من PascalCase المستخدمة في .NET.
{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
