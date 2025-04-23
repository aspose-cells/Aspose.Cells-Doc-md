---
title: استخدام وظيفة FormulaText في Aspose.Cells مع Python.NET
linktitle: استخدام وظيفة FormulaText
type: docs
weight: 60
url: /ar/python-net/using-formulatext-function-in-aspose-cells/
description: تعلم كيفية العمل مع دالة FORMULATEXT في Excel باستخدام Aspose.Cells لبايثون via .NET. الحصول على وتعيين صيغ الخلايا برمجياً مع الحفاظ على سلامة جدول البيانات.
keywords: Aspose.Cells، بايثون، إكسل، FORMULATEXT، التعامل مع الصيغ، أتمتة جداول البيانات
---

{{% alert color="primary" %}} 

FORMULATEXT هي وظيفة في Excel 2013 وما بعدها. غير مدعومة من قبل الإصدارات السابقة مثل Excel 2010 أو 2007 وما إلى ذلك. كما يوحي الاسم، تعرض نص الصيغة الموجودة في خلية معينة. يوضح هذا المقال كيفية استخدام هذه الوظيفة مع Aspose.Cells لبايثون via .NET.

{{% /alert %}} 

يوضح رمز النموذج التالي كيفية استخدام FORMULATEXT مع Aspose.Cells. يكتب الرمز أولاً صيغة في الخلية A1 ثم يعرض نص الصيغة باستخدام FORMULATEXT في الخلية A2.

```python
from aspose.cells import Workbook

# Create a workbook object
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Put some formula in cell A1
cell_a1 = worksheet.cells.get("A1")
cell_a1.formula = "=Sum(B1:B10)"

# Get the text of the formula in cell A2 using FORMULATEXT function
cell_a2 = worksheet.cells.get("A2")
cell_a2.formula = "=FormulaText(A1)"

# Calculate the workbook
workbook.calculate_formula()

# Print the results of A2, It will now print the text of the formula inside cell A1
print(cell_a2.string_value)
```

## **مخرجات الوحدة**
إليك الإخراج في وحدة التحكم للكود أعلاه:

{{< highlight python >}}
=SUM(B1:B10)
{{< /highlight >}}
