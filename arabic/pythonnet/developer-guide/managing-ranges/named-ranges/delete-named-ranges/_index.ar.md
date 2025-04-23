---
title: حذف المدى المسمى
type: docs
weight: 90
url: /ar/python-net/delete-named-ranges/
description: يمكنك معرفة كيفية إزالة أسماء محددة أو نطاقات مسماة من ملفات Excel أو OpenOffice باستخدام Aspose.Cells for Python عبر .Net.
keywords: مكتبة بيثون لإكسل، إزالة أسماء محددة مكررة بيثون، حذف أسماء محددة مكررة بيثون.
---

## **مقدمة**
إذا كان هناك الكثير من الأسماء المحددة أو النطاقات المسماة في ملفات Excel، يجب علينا مسح بعضها لأنها لم يتم الرجوع إليها مرة أخرى.

## **إزالة النطاق المسمى في MS Excel**

لإزالة نطاق مسمى من Excel، يمكنك اتباع هذه الخطوات:
1. افتح Microsoft Excel وافتح المصنف الذي يحتوي على النطاق المسمى.
2. انتقل إلى علامة "الصيغ" في شريط أدوات Excel.
3. انقر على زر "مدير الأسماء" في مجموعة "الأسماء المحددة". سيفتح ذلك صندوق حوار مدير الأسماء.
4. في صندوق حوار مدير الأسماء، حدد النطاق المسمى الذي تريد إزالته.
5. انقر على الزر "حذف". قم بتأكيد الحذف عندما يُطلب.
6. انقر على الزر "إغلاق" لإغلاق صندوق حوار مدير الأسماء.
7. احفظ المصنف للحفاظ على التغييرات.

## **حذف نطاقات المسمى باستخدام Aspose.Cells لـ.Net**
مع Aspose.Cells لبایتون .NET، يمكنك إزالة المجموعات المسماة أو الأسماء المعرفة باستخدام [النص](https://reference.aspose.com/cells/python-net/aspose.cells/namecollection/remove_a_name/#str) في القائمة.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# The path to the documents directory
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a new Workbook
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete a named range by text
worksheets.names.remove_a_name("NamedRange")


# Save the workbook to retain the changes
workbook.save(os.path.join(data_dir, "Book2.xlsx"))
```

ملاحظة: إذا تم الرجوع إلى الاسم المحدد بواسطة الصيغ، فلن يمكن إزالته. يمكننا فقط إزالة الصيغة للأسم المحدد.

## **إزالة بعض النطاقات المسماة**
عندما نقوم بإزالة اسم محدد، يجب علينا التحقق مما إذا كانت تتم الرجوع إليه في جميع الصيغ في الملف.
من أجل تحسين أداء إزالة النطاقات المسماة، يمكننا إزالة بعضها معًا.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete some defined names
worksheets.names.remove_names_by_array(["NamedRange1", "NamedRange2"])

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```


## **إزالة الأسماء المحددة المكررة**
يتلف بعض ملفات Excel لأن بعض الأسماء المحددة مكررة. لذلك يمكننا إزالة هذه الأسماء المكررة لإصلاح الملف.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete duplicate defined names
worksheets.names.remove_duplicate_names()

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```
