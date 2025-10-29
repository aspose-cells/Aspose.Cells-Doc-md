---
title: تحديد الأرقام الهامة التي يجب تخزينها في ملف إكسل باستخدام Python.NET
linktitle: تحديد الأرقام المهمة
type: docs
weight: 30
url: /ar/python-net/specifying-significant-digits-to-be-stored-in-excel-file/
description: تعلم كيفية التحكم في الأرقام الهامة المخزنة في ملفات إكسل باستخدام API الخاص بـ Aspose.Cells لبايثون via .NET.
---

## **سيناريوهات الاستخدام المحتملة**

بشكل افتراضي، يخزن Aspose.Cells 17 رقمًا هامًا من قيم المزدوج داخل ملف إكسل، على عكس MS-Excel الذي يخزن فقط 15 رقمًا هامًا. يمكنك تغيير هذا السلوك من 17 إلى 15 رقمًا هامًا باستخدام الخاصية [**CellsHelper.significant_digits**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/significant_digits/).

## **تحديد عدد الأرقام المعنوية التي سيتم تخزينها في ملف Excel**

الكود التالي يفرض على Aspose.Cells استخدام 15 رقمًا هامًا عند تخزين القيم المزدوجة. تحقق من ملف الإكسل الناتج [مرفق](22774105.xlsx) (غير الامتداد إلى .zip لفحص القيم المخزنة). تُظهر الصورة أدناه كيف يؤثر هذا الإعداد على القيم المخزنة:

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **الكود المثالي**

```python
from aspose.cells import Workbook, CellsHelper
import aspose.cells
import os
import pytest

# Set significant digits to 15
CellsHelper.set_significant_digits(15)

# Create new workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set value with extended precision
cell = worksheet.cells.get("A1")
cell.put_value(1234567890123456.001234567890123456)

# Save modified workbook
workbook.save("output.xlsx")
```

```python
import os
from aspose.cells import Workbook, CellsHelper

# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Set significant digits to 15 like MS-Excel
CellsHelper.set_significant_digits(15)

# Create workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Access cell A1
c = worksheet.cells.get("A1")

# Put double value with 15 significant digits
c.put_value(1234567890.123451711)

# Save the workbook
output_dir = os.path.join(current_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook.save(os.path.join(output_dir, "out_SignificantDigits.xlsx"))
```
{{< app/cells/assistant language="python-net" >}}
