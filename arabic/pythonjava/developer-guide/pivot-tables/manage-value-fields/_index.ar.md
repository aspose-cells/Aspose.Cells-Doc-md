---
title: إدارة حقول قيم الجدول المحوري في Aspose.Cells for Python عبر Java
linktitle: إدارة حقول قيم الجدول المحوري في Aspose.Cells for Python عبر Java
description: تعلّم كيفية إضافة الحقول الأساسية إلى منطقة بيانات الجدول المحوري، وتغيير دالة التلخيص باستخدام PivotField.Function، ورسم حقل القيمة على محور الصفوف أو الأعمدة في Aspose.Cells for Python عبر Java.
keywords: Aspose.Cells, Python عبر Java, جدول محوري, حقل قيمة, PivotField, PivotField.Function, حقل بيانات, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ar/python-java/manage-value-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## إضافة حقل إلى منطقة البيانات
تُعد إضافة حقل أساسي إلى منطقة البيانات (القيم) الخطوة الأولى في تحديد طريقة تجميع بيانات المصدر في الجدول المحوري. يتيح Aspose.Cells استخدام الدالة `PivotTable.AddFieldToArea(PivotFieldType, string)` من خلال إحدى صور التحميل الزائد لها، حيث تقبل هذه الصورة الثابت `PivotFieldType.DATA` واسم عمود المصدر. وبمجرد إضافة حقل إلى منطقة البيانات، تتيح API الوصول إليه من خلال مجموعة `PivotTable.DataFields`، التي تعكس ترتيب إضافة الحقول. افتراضيًا، تُستخدم الدالة `Sum` لتلخيص عمود المصدر الرقمي، بينما تُستخدم الدالة `Count` للعمود غير الرقمي.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.getCells().get(0, j).putValue(h)
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.getCells().get(i + 1, j).putValue(val)
pivot_index = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.getPivotTables().get(pivot_index)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Category")
pivot_table.addFieldToArea(PivotFieldType.ROW, "Item")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
workbook.save("output_drag.xlsx")
jpype.shutdownJVM()
```

## تغيير دالة التلخيص
بعد إضافة حقل إلى منطقة البيانات، يتيح Aspose.Cells الوصول إليه عبر كائن `PivotField` في `PivotTable.DataFields`. يمتلك كل كائن `PivotField` خاصية `Function` قابلة للكتابة، من النوع `ConsolidationFunction`، وتتحكم هذه الخاصية في التجميع المطبق على القيم المصدرية للحقل. ويُعد `ConsolidationFunction` نوع تعداد يتضمّن الأعضاء `Sum` و`Count` و`Average` و`Max` و`Min` و`Product` و`StdDev` و`StdDevp` و`Var` و`Varp`؛ وتغطي الأعضاء الستة الأولى معظم حالات الاستخدام الواقعية، بينما تمثل الأعضاء الأربعة الأخيرة تجميعات إحصائية مفيدة في تحليل التباين.

{{% alert color="primary" %}}
لا يؤثر تغيير `Function` على شيء سوى التجميع؛ ولا يُعدَّل عمود المصدر أو بنية الصفوف/الأعمدة في الجدول المحوري. لتبديل التجميع في حقل بيانات موجود، عيّن `pivotTable.DataFields[i].Function = ConsolidationFunction.<X>;` ثم استدعِ `pivotTable.calculateData()` لإعادة عرض الجدول المحوري.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, ConsolidationFunction
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.getCells().get(0, j).putValue(h)
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.getCells().get(i + 1, j).putValue(val)
pivot_index = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.getPivotTables().get(pivot_index)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Category")
pivot_table.addFieldToArea(PivotFieldType.ROW, "Item")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT)
pivot_table.calculateData()
workbook.save("output_function.xlsx")
jpype.shutdownJVM()
```

## رسم حقول القيم على محور الصفوف أو الأعمدة
عندما يحتوي الجدول المحوري على حقلين أو أكثر من حقول البيانات، يتيح Aspose.Cells الوصول إلى حقل افتراضي إضافي يُعرف باسم `PivotTable.ValuesField`. يمثل هذا الحقل الافتراضي تجميع كل حقل بيانات موجود في منطقة البيانات. يمكنك سحبه إلى منطقة الصفوف أو الأعمدة بوصفه حقلًا أساسيًا في الجدول المحوري، وهو أمر مفيد لتخطيط مقاييس متعددة جنبًا إلى جنب.

{{% alert color="primary" %}}
لا يعمل `PivotTable.ValuesField` في حالة عدم وجود أي حقل قيم أو وجود حقل قيم واحد فقط.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, ConsolidationFunction
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.getCells().get(0, j).putValue(h)
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.getCells().get(i + 1, j).putValue(val)
pivot_index = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.getPivotTables().get(pivot_index)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Category")
pivot_table.addFieldToArea(PivotFieldType.ROW, "Item")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT)
pivot_table.addFieldToArea(PivotFieldType.COLUMN, pivot_table.getValuesField())
pivot_table.calculateData()
workbook.save("output_plot.xlsx")
jpype.shutdownJVM()
```

{{< app/cells/assistant language="python" >}}