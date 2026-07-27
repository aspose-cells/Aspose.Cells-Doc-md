---
title: إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells لـ .NET
linktitle: حقول الصفوف والأعمدة
description: تعرّف على كيفية إضافة حقول أساسية إلى منطقتي الصفوف والأعمدة في الجدول المحوري والتحكم في الإجماليات الفرعية لحقول المحور باستخدام PivotField.set_subtotals في Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET, pivot table, row field, column field, PivotField, set_subtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /ar/python-net/pivot-table-add-row-column-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

تُعد حقول الصفوف والأعمدة اللبنات الأساسية للجدول المحوري. يظهر الحقل الموضوع في منطقة الصفوف عموديًا على يسار الجدول المحوري، بينما يظهر الحقل الموضوع في منطقة الأعمدة أفقيًا عبر الجزء العلوي. توضح هذه المقالة كيفية إضافة الحقول الأساسية إلى تلك المناطق برمجيًا وكيفية التحكم في الإجماليات الفرعية التي تظهر بين مجموعات الحقول باستخدام طريقة `PivotField.set_subtotals`.

## **إضافة حقل إلى منطقة الصفوف أو الأعمدة**

تقوم طريقة `PivotTable.add_field_to_area(PivotFieldType field_type, string field_name)` بنقل حقل أساسي من بيانات المصدر إلى إحدى مناطق الجدول المحوري الأربع. تقبل وسيط `field_type` إحدى قيم `PivotFieldType` التالية.

- `ROW` — الحقول الموضوعة عموديًا على اليسار
- `COLUMN` — الحقول الموضوعة أفقيًا عبر الجزء العلوي
- `DATA` — الحقول التي يتم تجميع قيمها
- `PAGE` — الحقول المستخدمة كمرشحات تقرير

بعد إضافة الحقول، يمكنك الوصول إليها من خلال خصائص `PivotTable.row_fields` و`PivotTable.column_fields`. تُرجع كل خاصية `PivotFieldCollection`. الحقل الموجود في الفهرس 0 من `row_fields` هو حقل الصف الأبعد، وتمثل الفهارس اللاحقة الحقول المتداخلة داخله. ينطبق نفس اصطلاح الفهرسة على `column_fields`.

يهم ترتيب تداخل الحقول. تؤدي إضافة `Category` إلى منطقة الصفوف أولاً ثم `Item` إلى إنشاء جدول محوري تكون فيه المجموعة الخارجية هي `Category` والمجموعة الداخلية هي `Item`. يؤدي عكس الترتيب إلى عكس التسلسل الهرمي.

## **الإجماليات الفرعية لحقول المحور**

تتحكم طريقة `PivotField.set_subtotals(PivotFieldSubtotalType subtotal_type, bool shown)` في صفوف الإجمالي الفرعي التي تظهر لحقل المحور. يقوم كل استدعاء بتبديل نوع إجمالي فرعي واحد بشكل مستقل. يؤدي تمرير `shown = True` إلى عرض الإجمالي الفرعي، بينما يؤدي تمرير `shown = False` إلى إخفائه. نظرًا لأن كل استدعاء يؤثر فقط على نوع واحد، فإن استدعاء الطريقة عدة مرات بقيم `subtotal_type` مختلفة ينشئ مجموعة فرعية مخصصة من الإجماليات الفرعية.

يُعرّف التعداد `PivotFieldSubtotalType` أنواع الإجمالي الفرعي المتاحة.

- `AUTOMATIC` — يختار Aspose.Cells التحديد الافتراضي (عادةً `SUM` للحقول الرقمية)
- `NONE` — منع كل صفوف الإجمالي الفرعي
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STDDEV`
- `STDDEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
لا تظهر الإجماليات الفرعية إلا عندما يكون هناك حقلان محوريان أو أكثر في منطقة الصفوف (أو في منطقة الأعمدة). الحقل الواحد ليس لديه شيء ذو معنى للتجميع الفرعي بينه، لذلك لا يكون لاستدعاءات `set_subtotals` أي تأثير مرئي في هذه الحالة. لذلك تضع هذه المقالة حقلين للصفوف (`Category` خارجي، `Item` داخلي) في كل مثال بحيث يكون حدود الإجمالي الفرعي بين كل مجموعة `Category` مرئية.
{{% /alert %}}

## **السيناريو 1 — الإجماليات الفرعية التلقائية (الافتراضية)**

عندما لا تستدعي `set_subtotals` على الإطلاق، يطبق Aspose.Cells تحديد `AUTOMATIC` على الحقول الرقمية. يؤكد المثال التالي هذا السلوك صراحةً من خلال استدعاء `set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)` على حقل الصف الخارجي `Category`.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")

worksheet.cells[1, 0].put_value("Fruit")
worksheet.cells[1, 1].put_value("Apple")
worksheet.cells[1, 2].put_value(2020)
worksheet.cells[1, 3].put_value(100)

worksheet.cells[2, 0].put_value("Fruit")
worksheet.cells[2, 1].put_value("Apple")
worksheet.cells[2, 2].put_value(2021)
worksheet.cells[2, 3].put_value(150)

worksheet.cells[3, 0].put_value("Fruit")
worksheet.cells[3, 1].put_value("Banana")
worksheet.cells[3, 2].put_value(2020)
worksheet.cells[3, 3].put_value(80)

worksheet.cells[4, 0].put_value("Fruit")
worksheet.cells[4, 1].put_value("Banana")
worksheet.cells[4, 2].put_value(2021)
worksheet.cells[4, 3].put_value(90)

worksheet.cells[5, 0].put_value("Vegetable")
worksheet.cells[5, 1].put_value("Carrot")
worksheet.cells[5, 2].put_value(2020)
worksheet.cells[5, 3].put_value(50)

worksheet.cells[6, 0].put_value("Vegetable")
worksheet.cells[6, 1].put_value("Carrot")
worksheet.cells[6, 2].put_value(2021)
worksheet.cells[6, 3].put_value(60)

worksheet.cells[7, 0].put_value("Vegetable")
worksheet.cells[7, 1].put_value("Daikon")
worksheet.cells[7, 2].put_value(2020)
worksheet.cells[7, 3].put_value(40)

worksheet.cells[8, 0].put_value("Vegetable")
worksheet.cells[8, 1].put_value("Daikon")
worksheet.cells[8, 2].put_value(2021)
worksheet.cells[8, 3].put_value(45)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
category_field.set_subtotals(ac.PivotFieldSubtotalType.AUTOMATIC, True)

pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output_automatic.xlsx")
```

## **السيناريو 2 — منع جميع الإجماليات الفرعية (None)**

يقوم استدعاء `set_subtotals(PivotFieldSubtotalType.NONE, True)` بإزالة كل صفوف الإجمالي الفرعي من الجدول المحوري، تاركًا فقط صفوف الحقول والإجمالي الكلي في الأسفل. يكون هذا مفيدًا عندما تريد البيانات المجمعة الأولية دون أي صفوف ملخص.

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
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45],
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

category_field = pivot_table.row_fields[0]
for st in [ac.PivotFieldSubtotalType.SUM, ac.PivotFieldSubtotalType.COUNT, ac.PivotFieldSubtotalType.AVERAGE, ac.PivotFieldSubtotalType.MAX, ac.PivotFieldSubtotalType.MIN, ac.PivotFieldSubtotalType.PRODUCT]:
    category_field.set_subtotals(st, True)
pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output_none.xlsx")
```

## **السيناريو 3 — مجموعة الإجمالي الفرعي المخصصة (Sum + Average)**

لست محدودًا بنوع إجمالي فرعي واحد. يعمل كل استدعاء لـ `set_subtotals` بشكل مستقل على نوع واحد، لذلك ينتج عن استدعاء الطريقة مرتين — مرة بـ `SUM` ومرة بـ `AVERAGE` — مجموعة فرعية مخصصة من صفّي إجمالي فرعي لكل مجموعة `Category`.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

worksheet.cells["A1"].put_value("Category")
worksheet.cells["B1"].put_value("Item")
worksheet.cells["C1"].put_value("Year")
worksheet.cells["D1"].put_value("Amount")

worksheet.cells[1, 0].put_value("Fruit")
worksheet.cells[1, 1].put_value("Apple")
worksheet.cells[1, 2].put_value(2020)
worksheet.cells[1, 3].put_value(100)

worksheet.cells[2, 0].put_value("Fruit")
worksheet.cells[2, 1].put_value("Apple")
worksheet.cells[2, 2].put_value(2021)
worksheet.cells[2, 3].put_value(150)

worksheet.cells[3, 0].put_value("Fruit")
worksheet.cells[3, 1].put_value("Banana")
worksheet.cells[3, 2].put_value(2020)
worksheet.cells[3, 3].put_value(80)

worksheet.cells[4, 0].put_value("Fruit")
worksheet.cells[4, 1].put_value("Banana")
worksheet.cells[4, 2].put_value(2021)
worksheet.cells[4, 3].put_value(90)

worksheet.cells[5, 0].put_value("Vegetable")
worksheet.cells[5, 1].put_value("Carrot")
worksheet.cells[5, 2].put_value(2020)
worksheet.cells[5, 3].put_value(50)

worksheet.cells[6, 0].put_value("Vegetable")
worksheet.cells[6, 1].put_value("Carrot")
worksheet.cells[6, 2].put_value(2021)
worksheet.cells[6, 3].put_value(60)

worksheet.cells[7, 0].put_value("Vegetable")
worksheet.cells[7, 1].put_value("Daikon")
worksheet.cells[7, 2].put_value(2020)
worksheet.cells[7, 3].put_value(40)

worksheet.cells[8, 0].put_value("Vegetable")
worksheet.cells[8, 1].put_value("Daikon")
worksheet.cells[8, 2].put_value(2021)
worksheet.cells[8, 3].put_value(45)

pivot_tables = worksheet.pivot_tables
pivot_index = pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
category_field.set_subtotals(ac.PivotFieldSubtotalType.SUM, True)
category_field.set_subtotals(ac.PivotFieldSubtotalType.AVERAGE, True)

pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output_custom.xlsx")
```

## **ملخص**

تتشارك السيناريوهات الثلاثة أعلاه في نفس مجموعة البيانات وهيكل الجدول المحوري. الفرق الوحيد بينها هو استدعاء `set_subtotals` المطبق على حقل الصف الخارجي `Category`. تذكر قاعدة الحقلين: الحقل الواحد في المنطقة لا يوجد لديه شيء للتجميع الفرعي بينه، لذلك ضع دائمًا حقلين على الأقل في منطقة الصفوف أو الأعمدة عندما تريد أن يكون لـ `set_subtotals` تأثير مرئي.

## **مقالات ذات صلة**

- [حقول الصفحات في الجداول المحورية](/cells/ar/python-net/add-page-field-in-pivot-table/)
- [تحديث الجداول المحورية في Aspose.Cells for Python via .NET](/cells/ar/python-net/refresh-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية](/cells/ar/python-net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
