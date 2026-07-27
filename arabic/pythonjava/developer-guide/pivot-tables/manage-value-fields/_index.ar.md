---
title: حقول القيم في Aspose.Cells for Python via Java
linktitle: حقول القيم في Aspose.Cells for Python via Java
description: تعرّف على كيفية إضافة الحقول الأساسية إلى منطقة البيانات في الجدول المحوري، وتغيير دالة التلخيص عبر PivotField.Function، وعرض حقل القيمة على محور الصفوف أو الأعمدة في Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java, pivot table, value field, PivotField, PivotField.Function, data field, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ar/python-java/manage-value-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## إضافة حقل إلى منطقة البيانات

تُعدّ إضافة حقل أساسي إلى منطقة البيانات (القيم) الخطوة الأولى في تشكيل كيفية تجميع الجدول المحوري لبيانات المصدر. يوفّر Aspose.Cells الحمل الزائد `PivotTable.addFieldToArea(PivotFieldType, string)` الذي يقبل الثابت `PivotFieldType.DATA` واسم عمود المصدر. بمجرد إضافة حقل إلى منطقة البيانات، يكشف لك الـ API عنه من خلال مجموعة `PivotTable.DataFields`، وذلك وفق الترتيب الذي أُضيفت به الحقول. افتراضيًا، يتم تلخيص عمود المصدر الرقمي باستخدام `ConsolidationFunction.SUM`، بينما يكون العمود غير الرقمي افتراضيًا على `COUNT`.

## تغيير دالة التلخيص

يتم تغليف كل حقل موضوع في منطقة البيانات داخليًا كنسخة من `PivotField`، وتُرجع خاصية `Function` الخاصة به قيمة من تعداد `ConsolidationFunction`. يتيح لك المُعيّن `Function` نفسه التبديل بين التجميعات المتاحة، بما في ذلك `SUM` و`COUNT` و`AVERAGE` و`MAX` و`MIN` و`PRODUCT` و`STDDEV` و`STDDEVP` و`VAR` و`VARP`.

{{% alert color="primary" %}}
لا يؤثّر تغيير `Function` إلا على التجميع، بينما يظل عمود المصدر دون تغيير.
{{% /alert %}}
يمكنك بالتالي الإبقاء على حقل بيانات واحد كـ `Sum` بينما تُضيف حقل بيانات ثانٍ يستهدف عمود المصدر نفسه لكنه يستخدم `Count` أو `Average`، وذلك جميعه ضمن جدول محوري واحد.

## عرض حقول القيم على محور الصفوف أو الأعمدة

عندما يحتوي الجدول المحوري على حقلين أو أكثر من حقول البيانات، يكشف Aspose.Cells عن حقل افتراضي إضافي يُسمى `PivotTable.ValuesField`. يمثّل هذا الحقل الافتراضي تجميع كل حقل بيانات موجود في منطقة البيانات. يمكنك سحبه إلى منطقة الصفوف أو الأعمدة باعتباره حقل محور أساسي، وهو أمر مفيد لتخطيط مقاييس متعددة جنبًا إلى جنب.

{{% alert color="primary" %}}
لا يعمل `PivotTable.ValuesField` إذا لم يكن هناك أي حقل قيمة أو إذا كان هناك حقل قيمة واحد فقط.
{{% /alert %}}
تستعرض السيناريوهات أدناه ثلاثة أمثلة شاملة تُوضّح كل قدرة من القدرات الموصوفة أعلاه على نفس بنية الجدول المحوري.

## السيناريو 1 — سحب حقل أساسي إلى منطقة القيم

يُوضّح هذا السيناريو كيفية وضع حقل أساسي واحد (`Amount`) في منطقة البيانات لجدول محوري موجود. تضع بنية الجدول المحوري المشتركة `Category` و`Item` على محور الصفوف، و`Year` على محور الأعمدة. بعد العملية، يظهر `Amount` في منطقة البيانات ويُحسب باعتباره `Sum` لـ `Amount` افتراضيًا.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)

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
        worksheet.cells.get(i + 1, j).put_value(val)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```

## السيناريو 2 — تغيير دالة التلخيص

يبدأ هذا السيناريو من نفس بنية الجدول المحوري في السيناريو 1، لكنه يضيف حقل `Amount` إلى منطقة البيانات مرتين. يشير كلا حقلَي البيانات إلى عمود المصدر نفسه، إلا أن الحقل الثاني يتم تجاوزه باستخدام مُعيّن `PivotField.Function` ليصبح `Count` بدلاً من `Sum` الافتراضية.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)

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
        worksheet.cells.get(i + 1, j).put_value(val)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT

pivot_table.calculate_data()
workbook.save("output_function.xlsx")
```

## السيناريو 3 — عرض حقول القيم على محور الصفوف أو الأعمدة

مع وجود حقلَي بيانات، يصبح `PivotTable.ValuesField` قابلًا للاستخدام. يسحب هذا السيناريو حقل التجميع الافتراضي إلى منطقة الأعمدة بحيث يظهر كل مقياس في منطقة البيانات ككتلة عمود خاصة به بجانب `Year`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)

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
        worksheet.cells.get(i + 1, j).put_value(val)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.add_field_to_area(PivotFieldType.COLUMN, pivot_table.values_field.name)

pivot_table.calculate_data()
workbook.save("output_plot.xlsx")
```

معًا، تغطي هذه السيناريوهات الثلاثة جميع جوانب التعامل مع حقول القيم في Aspose.Cells for Python via Java، بدءًا من حقل بيانات واحد مع `Sum` الافتراضية، وصولًا إلى جدول محوري متعدد المقاييس يتحكم فيه حقل `ValuesField` الافتراضي في التخطيط على محور الصفوف أو الأعمدة.

{{< app/cells/assistant language="python" >}}
