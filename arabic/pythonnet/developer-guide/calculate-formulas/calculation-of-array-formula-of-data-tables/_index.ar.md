---
title: حساب الصيغة المصفوفة لبيانات الجداول باستخدام Python.NET
linktitle: حساب الصيغة الصفيفية لجداول البيانات
type: docs
weight: 70
url: /ar/python-net/calculation-of-array-formula-of-data-tables/
description: تعلم كيفية حساب الصيغ المصفوفية لجداول بيانات Excel باستخدام Aspose.Cells لـ Python via .NET API. تعديل وحفظ جداول البيانات برمجياً.
keywords: جداول بيانات إكسل في بايثون، صيغ المصفوفة في بايثون، Aspose.Cells بايثون، حساب الجداول البياناتية في بايثون، أتمتة إكسل بايثون
---

{{% alert color="primary" %}}

يمكنك إنشاء جدول بيانات في ميكروسوفت إكسل باستخدام البيانات > تحليل ما-لو > جدول البيانات.... يتيح Aspose.Cells لـ Python via .NET حساب صيغة المصفوفة لجدول البيانات. يرجى استخدام [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) كالمعتاد لحساب أي نوع من الصيغ.

{{% /alert %}}

في المثال التالي، نستخدم ملف إكسل المصدر (5115535.xlsx). إذا قمت بتغيير قيمة الخلية B1 إلى 100، ستتحدث قيم جدول البيانات (المحدد باللون الأصفر) إلى 120 كما هو موضح في لقطات الشاشة أدناه. يقوم كود البايثون بتوليد هذا (ملف PDF الناتج) (5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

فيما يلي تنفيذ بايثون يُظهر كيفية توليد ملف PDF الناتج (5115538.pdf) من ملف إكسل المصدر (5115535.xlsx):

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create workbook from source excel file
workbook = Workbook(os.path.join(data_dir, "DataTable.xlsx"))

# Access first worksheet
worksheet = workbook.worksheets[0]

# When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.cells.get("B1").put_value(100)

# Calculate formula, now it also calculates Data Table array formula
workbook.calculate_formula()

# Save the workbook in pdf format
workbook.save(os.path.join(data_dir, "output_out.pdf"))
```

**شرح كود بايثون:**
```python
import aspose.cells as ac

# Load source workbook
workbook = ac.Workbook("5115535.xlsx")

# Calculate formulas using Python.NET API
workbook.calculate_formula()

# Save the workbook in PDF format
workbook.save("5115538.pdf", ac.SaveFormat.PDF)
```
{{< app/cells/assistant language="python-net" >}}
