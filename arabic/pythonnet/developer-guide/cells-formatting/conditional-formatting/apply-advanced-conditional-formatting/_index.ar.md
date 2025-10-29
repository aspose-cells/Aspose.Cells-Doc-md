---
title: تطبيق التنسيق الشرطي المتقدم باستخدام Python.NET
linktitle: تطبيق التنسيق المشروط المتقدم
type: docs
weight: 70
url: /ar/python-net/apply-advanced-conditional-formatting/
description: تعلم كيفية تنفيذ ميزات التنسيق الشرطي المتقدمة في إكسل مثل أشرطة البيانات، موازنات الألوان، ومجموعات الرموز باستخدام Aspose.Cells للبايثون via .NET.
keywords: ت formatting excel للبايثون، التنسيق الشرطي للبايثون، أشرطة البيانات للبايثون، موازنات الألوان للبايثون، مجموعات الرموز للبايثون، Aspose.Cells للبايثون
---

{{% alert color="primary" %}} 

إصدارات Microsoft Excel 2007 وما بعدها (2010/2013/2016) توفر ميزات التنسيق الشرطي المتقدمة بما في ذلك تظليل الخلايا، الحدود، الرموز الملونة، الأسهم، الأعلام، وتنسيق الخط.

{{% /alert %}} 

## **تنفيذ التنسيق الشرطي المتقدم في ملفات إكسل**
يدعم Aspose.Cells للبايثون via .NET جميع ميزات التنسيق الشرطي المتقدمة بما في ذلك:

- إضافة شريط بيانات مظللة لتحسين الأرقام الأساسية بشكل بصري من خلال تضمين مخطط بياني بسيط في الخلايا.
- تظليل الخلايا تلقائيًا بمقاييس الألوان بناءً على علاقتها بقيم في خلايا أخرى في النطاق. تظليل الإعدادات الافتراضية القيمة الأدنى باللون الأحمر متحركًا صعودًا إلى القيمة الأعلى باللون الأخضر.
- استخدام مجموعات الرموز بالطريقة نفسها كمقاييس الألوان، ولكن بدلاً من تظليل الخلايا، يضيف رموز صغيرة، مثل السهام وأضواء المرور، إلى الخلايا.

تدعم Aspose.Cells بشكل كامل التنسيق المشروط المقدم من Microsoft Excel 2007 والأحدث في تنسيق XLSX على الخلايا في وقت التشغيل. يوضح هذا المثال تمرينًا لأنواع التنسيق المشروط المتقدمة بما في ذلك مجموعات الرموز، أشرطة البيانات، مقاييس الألوان، فترات الزمن، القاع/القمة وقواعد أخرى بمجموعات مختلفة من السمات.

- [**Adding Color Scale Conditional Formattings**](/cells/ar/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/ar/python-net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/ar/python-net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/ar/python-net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/ar/python-net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/ar/python-net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/ar/python-net/how-to-add-top10-conditional-formatting/)



### **حساب اختيار الألوان في إكسل لتنسيق موازن الألوان**
يعرض هذا الكود كيفية تحديد اللون المختار بواسطة إكسل لقواعد التنسيق الشرطي لموازن الألوان:

```python
import os
from aspose.cells import Workbook
from aspose.pydrawing import Color

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-Python
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a workbook object and open the template file
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))
# Get the first worksheet
worksheet = workbook.worksheets[0]
# Get the A1 cell
a1 = worksheet.cells.get("A1")

# Get the conditional formatting resultant object
cfr1 = a1.get_conditional_formatting_result()
# Get the ColorScale resultant color object
c = cfr1.color_scale_result

# Read and print the color values
print(c.to_argb())
print(c.name)
```
{{< app/cells/assistant language="python-net" >}}
