---
title: أضف خلايا إلى نافذة مراقبة الصيغ في Microsoft Excel باستخدام Python.NET
linktitle: إضافة خلايا إلى نافذة المراقبة للصيغ
type: docs
weight: 60
url: /ar/python-net/add-cells-to-microsoft-excel-formula-watch-window/
description: تعلم كيفية مراقبة الخلايا في نافذة مراقبة الصيغ في Excel باستخدام Aspose.Cells لـ Python via .NET. يشمل أمثلة برمجية ومراجع API.
keywords: بايثون Excel، نافذة مراقبة الصيغ، مراقبة الخلايا، aspose.cells، Python.net
---

## **سيناريوهات الاستخدام المحتملة**

 تعتبر نافذة المراقبة في Microsoft Excel أداة مفيدة لمراقبة قيم الخلايا والصيغ بسهولة في نافذة مخصصة. يمكنك فتح *نافذة المراقبة* في Microsoft Excel بالتنقل إلى *الصيغ > نافذة المراقبة*. يتيح زر *إضافة مراقبة* إضافة خلايا للفحص. وبالمثل، يمكنك استخدام طريقة [**Worksheet.cell_watches.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/cellwatchcollection/add/) لإضافة خلايا يدويًا إلى نافذة المراقبة باستخدام API من Aspose.Cells.

## **إضافة الخلايا إلى نافذة مراقبة صيغ Microsoft Excel**

 يحدد الكود النموذجي التالي الصيغ للخلية C1 و E1، ثم يضيف كلاهما إلى نافذة المراقبة. يحفظ ملف العمل كـ [ملف Excel الناتج](67338481.xlsx). عند فتح الملف الناتج في Excel، ستظهر الخليتان في نافذة المراقبة كما هو موضح:

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **الكود المثالي**

```python
from aspose.cells import Workbook, SaveFormat

# Create empty workbook.
wb = Workbook()

# Access first worksheet.
ws = wb.worksheets[0]

# Put some integer values in cell A1 and A2.
ws.cells.get("A1").put_value(10)
ws.cells.get("A2").put_value(30)

# Access cell C1 and set its formula.
c1 = ws.cells.get("C1")
c1.formula = "=Sum(A1,A2)"

# Add cell C1 into cell watches by name.
ws.cell_watches.add(c1.name)

# Access cell E1 and set its formula.
e1 = ws.cells.get("E1")
e1.formula = "=A2*A1"

# Add cell E1 into cell watches by its row and column indices.
ws.cell_watches.add(e1.row, e1.column)

# Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat.XLSX)
```
{{< app/cells/assistant language="python-net" >}}
