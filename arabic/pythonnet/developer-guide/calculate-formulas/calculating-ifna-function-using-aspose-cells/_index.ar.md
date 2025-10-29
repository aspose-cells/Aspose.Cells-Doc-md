---
title: حساب وظيفة IFNA باستخدام Python.NET باستخدام Aspose.Cells
linktitle: حساب وظيفة IFNA
type: docs
weight: 40
url: /ar/python-net/calculating-ifna-function-using-aspose-cells/
description: تعلم كيف تحسب وظيفة IFNA في ملفات Excel باستخدام Aspose.Cells لـ Python.NET. تعامل مع أخطاء #N/A واحتفظ بالجداول المعدلة بكفاءة.
keywords: Python.NET، Excel، وظيفة IFNA، Aspose.Cells، معالجة الأخطاء، حساب جدول البيانات
---

{{% alert color="primary" %}}

 يدعم Aspose.Cells لـ Python.NET حساب وظيفة IFNA في Excel. تعيد وظيفة IFNA قيمة محددة إذا نتج عن صيغة خطأ #N/A؛ وإلا فإنها تُرجع نتيجة الصيغة.

{{% /alert %}}

## **حساب وظيفة IFNA في Python.NET**

يوضح المثال التالي كيفية حساب وظيفة IFNA باستخدام Aspose.Cells لـ Python.NET:


## **مخرجات الوحدة**
 سينتج الكود أعلاه المخرجات التالية في وحدة التحكم:

```
Not found
Orange
```

## ** شرح الخطوات الرئيسية**
1. إنشاء وحدة مصنف جديدة [`Workbook`](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)
2. الوصول إلى مجموعة أوراق العمل والخلايا
3. ملء بيانات المصدر في العمود أ
4. تعيين صيغ VLOOKUP التي قد تنتج أخطاء #N/A
5. استخدام IFNA لمعالجة الأخطاء المحتملة
6. حساب الصيغ باستخدام [`calculate_formula()`](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/)
7. استرداد وعرض النتائج من الخلايا المعالجة للأخطاء
8. حفظ المصنف المعدل بنتائج الحسابات

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create new workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Add data for VLOOKUP
cells = worksheet.cells
cells.get("A1").put_value("Apple")
cells.get("A2").put_value("Orange")
cells.get("A3").put_value("Banana")

# Access cell A5 and A6
cell_a5 = worksheet.cells.get("A5")
cell_a6 = worksheet.cells.get("A6")

# Assign IFNA formula to A5 and A6
cell_a5.formula = "=IFNA(VLOOKUP(\"Pear\",$A$1:$A$3,1,0),\"Not found\")"
cell_a6.formula = "=IFNA(VLOOKUP(\"Orange\",$A$1:$A$3,1,0),\"Not found\")"

# Calculate the formula of workbook
workbook.calculate_formula()

# Print the values of A5 and A6
print(cell_a5.string_value)
print(cell_a6.string_value)
```
{{< app/cells/assistant language="python-net" >}}
