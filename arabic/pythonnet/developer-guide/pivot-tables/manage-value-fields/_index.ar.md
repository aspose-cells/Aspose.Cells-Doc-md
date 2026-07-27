---
title: إدارة حقول القيم في الجدول المحوري في Aspose.Cells لـ .NET
linktitle: حقول القيم
description: تعلّم كيفية إضافة الحقول الأساسية إلى منطقة البيانات في الجدول المحوري، وتغيير دالة التلخيص باستخدام PivotField.function، وعرض حقل القيمة على محور الصفوف أو الأعمدة في Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET, جدول محوري, حقل قيمة, PivotField, PivotField.function, حقل بيانات, PivotTable.values_field, Sum, Average
type: docs
weight: 230
url: /ar/python-net/pivot-table-manage-value-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## إضافة حقل إلى منطقة البيانات
تُعدّ إضافة حقل أساسي إلى منطقة البيانات (القيم) الخطوة الأولى في تشكيل كيفية تجميع الجدول المحوري لبيانات المصدر. يوفّر Aspose.Cells overload الخاص بـ `PivotTable.add_field_to_area(PivotFieldType, str)`، الذي يقبل الثابت `PivotFieldType.DATA` واسم عمود المصدر. بمجرد إضافة حقل إلى منطقة البيانات، يعرضه الـ API من خلال مجموعة `PivotTable.data_fields`، بالترتيب الذي تمت إضافة الحقول به. افتراضيًا، يتم تلخيص عمود المصدر الرقمي باستخدام `ConsolidationFunction.SUM`، بينما يكون العمود غير الرقمي افتراضيًا على `Count`.
## تغيير دالة التلخيص
كل حقل موضوع في منطقة البيانات يتم تغليفه داخليًا كنسخة من `PivotField`، وتُرجع خاصية `function` الخاصة به قيمة من تعداد `ConsolidationFunction`. يتيح لك المُعيّن `function` نفسه التبديل بين التجمّعات المتاحة، بما في ذلك `Sum`، و`Count`، و`Average`، و`Max`، و`Min`، و`Product`، و`StdDev`، و`StdDevp`، و`Var`، و`Varp`.
{{% alert color="primary" %}}
لا يؤثّر تغيير `function` إلا على التجمّع، بينما لا يتغيّر عمود المصدر.
{{% /alert %}}
يمكنك بالتالي إبقاء حقل بيانات واحد على `Sum` بينما تضيف حقل بيانات ثانٍ يستهدف عمود المصدر نفسه ولكن يستخدم `Count` أو `Average`، كل ذلك في جدول محوري واحد.
## عرض حقول القيم على محور الصفوف أو الأعمدة
عندما يحتوي الجدول المحوري على حقلَي بيانات أو أكثر، يوفّر Aspose.Cells حقلًا افتراضيًا إضافيًا يُسمى `PivotTable.values_field`. يمثّل هذا الحقل الافتراضي تجمّع كل حقل بيانات موجود في منطقة البيانات. يمكنك سحبه إلى منطقة الصفوف أو الأعمدة كحقل محوري أساسي، وهو أمر مفيد لتخطيط مقاييس متعددة جنبًا إلى جنب.
{{% alert color="primary" %}}
لا يعمل `PivotTable.values_field` إذا لم يكن هناك أي حقل قيمة أو إذا كان هناك حقل قيمة واحد فقط.
{{% /alert %}}
تستعرض السيناريوهات أدناه ثلاثة أمثلة شاملة توضّح كل قدرة من القدرات الموصوفة أعلاه على نفس بنية الجدول المحوري.
## السيناريو 1 — سحب حقل أساسي إلى منطقة القيم
يوضّح هذا السيناريو كيفية وضع حقل أساسي واحد (`Amount`) في منطقة البيانات لجدول محوري موجود. تضع بنية الجدول المحوري المشتركة `Category` و`Item` على محور الصفوف، و`Year` على محور الأعمدة. بعد العملية، يظهر `Amount` في منطقة البيانات ويُحسب افتراضيًا على أنه `Sum` لـ `Amount`.
```python
from aspose.cells.pivot import PivotFieldType

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# العناوين في A1:D1
worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")

# صفوف البيانات A2:D9 باستخدام حلقات متداخلة متفرعة على j
for i in range(1, 9):
    for j in range(4):
        if j == 0:
            worksheet.cells[i, j].put_value("Fruit" if i <= 4 else "Vegetable")
        elif j == 1:
            if i == 1 or i == 2:
                worksheet.cells[i, j].put_value("Apple")
            elif i == 3 or i == 4:
                worksheet.cells[i, j].put_value("Banana")
            elif i == 5 or i == 6:
                worksheet.cells[i, j].put_value("Carrot")
            else:
                worksheet.cells[i, j].put_value("Daikon")
        elif j == 2:
            worksheet.cells[i, j].put_value(2020 + ((i - 1) % 2))
        elif j == 3:
            if i == 1:
                worksheet.cells[i, j].put_value(100)
            elif i == 2:
                worksheet.cells[i, j].put_value(150)
            elif i == 3:
                worksheet.cells[i, j].put_value(80)
            elif i == 4:
                worksheet.cells[i, j].put_value(90)
            elif i == 5:
                worksheet.cells[i, j].put_value(50)
            elif i == 6:
                worksheet.cells[i, j].put_value(60)
            elif i == 7:
                worksheet.cells[i, j].put_value(40)
            else:
                worksheet.cells[i, j].put_value(45)

# إضافة جدول محوري في F3 باسم PivotTable1
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# تخطيط الجدول المحوري: الفئة والعنصر في الصف، السنة في العمود، المبلغ كحقل بيانات
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```
## السيناريو 2 — تغيير دالة التلخيص
يبدأ هذا السيناريو من نفس بنية الجدول المحوري في السيناريو 1، لكنه يضيف حقل `Amount` إلى منطقة البيانات مرتين. يشير حقلا البيانات إلى عمود المصدر نفسه، ومع ذلك يتم تجاوز الحقل الثاني باستخدام المُعيّن `PivotField.function` بحيث يصبح `Count` بدلاً من `Sum` الافتراضي.
```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")

pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

count_field = pivot_table.data_fields[1]
count_field.function = ac.ConsolidationFunction.COUNT

pivot_table.calculate_data()

workbook.save("output_function.xlsx")
```
## السيناريو 3 — عرض حقول القيم على محور الصفوف أو الأعمدة
مع وجود حقلَي بيانات في مكانهما، يصبح `PivotTable.values_field` قابلاً للاستخدام. يسحب هذا السيناريو هذا الحقل الافتراضي التجميعي إلى منطقة الأعمدة بحيث يظهر كل مقياس في منطقة البيانات ككتلة عمود خاصة به بجانب `Year`.
```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ac.ConsolidationFunction.COUNT

# ارسم حقول القيم على محور الأعمدة.
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, pivot_table.values_field.name)

pivot_table.calculate_data()

workbook.save("output_plot.xlsx")
```
معًا، تغطّي هذه السيناريوهات الثلاثة كل جانب من جوانب معالجة حقل القيم في Aspose.Cells for Python via .NET، بدءًا من حقل بيانات واحد بالـ `Sum` الافتراضي وصولاً إلى جدول محوري متعدد المقاييس يتحكم فيه `ValuesField` الافتراضي في التخطيط على محور الصفوف أو الأعمدة.

{{< app/cells/assistant language="python" >}}
