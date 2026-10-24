---
title: إضافة حقول الصفوف والأعمدة إلى الجدول المحوري في Aspose.Cells for Python via .NET
description: تعلم كيفية إضافة الحقول الأساسية إلى منطقتي الصفوف والأعمدة في الجدول المحوري والتحكم في المجاميع الفرعية لحقول PivotTable باستخدام PivotField.set_subtotals في Aspose.Cells for Python via .NET.
linktitle: حقول الصفوف والأعمدة
keywords: Aspose.Cells, Python via .NET, جدول محوري, حقل صف, حقل عمود, PivotField, set_subtotals, PivotFieldSubtotalType, المجاميع الفرعية
type: docs
weight: 220
url: /ar/python-net/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **إضافة حقل إلى منطقة الصفوف أو الأعمدة**
تنقل طريقة `PivotTable.add_field_to_area(PivotFieldType field_type, string field_name)` حقلًا أساسيًا من بيانات المصدر إلى إحدى مناطق الجدول المحوري الأربع. تقبل الوسيطة `field_type` إحدى قيم `PivotFieldType` التالية.
- `ROW` — حقول موضوعة عموديًا على اليسار
- `COLUMN` — حقول موضوعة أفقيًا في الأعلى
- `DATA` — حقول يتم تجميع قيمها
- `PAGE` — حقول مستخدمة كعوامل تصفية للتقرير
يؤثر ترتيب تداخل الحقول. تضيف `Category` إلى منطقة الصفوف أولًا ثم تضيف `Item`، مما ينتج جدولًا محوريًا تكون فيه المجموعة الخارجية هي `Category` والمجموعة الداخلية هي `Item`. وعكس الترتيب يعكس التسلسل الهرمي.

## **المجاميع الفرعية لحقول الجدول المحوري**
تتحكم طريقة `PivotField.set_subtotals(PivotFieldSubtotalType subtotal_type, bool shown)` في صفوف المجاميع الفرعية التي تظهر لحقل في الجدول المحوري. يبدّل كل استدعاء نوعًا واحدًا من المجاميع الفرعية بشكل مستقل. تمرير `shown = True` يعرض المجموع الفرعي، بينما يخفى `shown = False`. ولأن كل استدعاء يؤثر في نوع واحد فقط، فإن استدعاء الطريقة عدة مرات بقيم `subtotal_type` المختلفة يبني مجموعة مخصصة من المجاميع الفرعية.
يحدد تعداد `PivotFieldSubtotalType` أنواع المجاميع الفرعية المتاحة.
- `AUTOMATIC` — يختار Aspose.Cells التحديد الافتراضي (عادةً `SUM` للحقول الرقمية)
- `NONE` — يمنع عرض جميع صفوف المجاميع الفرعية
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
لا تظهر المجاميع الفرعية إلا عندما يوجد حقلان أو أكثر من حقول الجدول المحوري في منطقة الصفوف (أو منطقة الأعمدة). لا يوجد لدى الحقل المفرد أي نطاق ذي معنى لحساب المجاميع الفرعية، لذلك لا يكون لاستدعاءات `set_subtotals` أي تأثير مرئي في هذه الحالة. لذا يضع هذا المقال حقلَي صفوف (`Category` في الخارج و`Item` في الداخل) في كل مثال حتى تكون حدود المجاميع الفرعية بين كل مجموعة `Category` واضحة.
{{% /alert %}}

## **السيناريو 1 — المجاميع الفرعية التلقائية (الافتراضية)**
إذا لم تستدعِ `set_subtotals` على الإطلاق، فسيطبق Aspose.Cells تحديد `AUTOMATIC` على الحقول الرقمية. ويؤكد المثال التالي هذا السلوك صراحةً من خلال استدعاء `set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)` على حقل الصف الخارجي `Category`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get(0, 0).put_value("Category")
worksheet.cells.get(0, 1).put_value("Item")
worksheet.cells.get(0, 2).put_value("Year")
worksheet.cells.get(0, 3).put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)
pivot_table.calculate_data()
workbook.save("output_automatic.xlsx")
```

## **السيناريو 2 — منع جميع المجاميع الفرعية (None)**
يزيل استدعاء `set_subtotals(PivotFieldSubtotalType.NONE, True)` كل صفوف المجاميع الفرعية من الجدول المحوري، تاركًا حقول الصفوف فقط والإجمالي الكلي في الأسفل. يكون هذا مفيدًا عندما تريد البيانات المجمعة الخام دون أي صفوف ملخص.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells.get(0, j).put_value(headers[j])
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
        worksheet.cells.get(i + 1, j).put_value(data[i][j])
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
for st in [PivotFieldSubtotalType.SUM, PivotFieldSubtotalType.COUNT, PivotFieldSubtotalType.AVERAGE, PivotFieldSubtotalType.MAX, PivotFieldSubtotalType.MIN, PivotFieldSubtotalType.PRODUCT]:
    category_field.set_subtotals(st, True)
pivot_table.calculate_data()
workbook.save("output_none.xlsx")
```

## **السيناريو 3 — مجموعة مخصصة من المجاميع الفرعية (Sum + Average)**
لست مقيدًا بنوع واحد فقط من المجاميع الفرعية. يعمل كل استدعاء لـ `set_subtotals` بشكل مستقل على نوع واحد، لذلك يؤدي استدعاء الطريقة مرتين، مرة باستخدام `SUM` ومرة باستخدام `AVERAGE`، إلى إنشاء مجموعة مخصصة من صفَي مجاميع فرعية لكل مجموعة `Category`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get("A1").put_value("Category")
worksheet.cells.get("B1").put_value("Item")
worksheet.cells.get("C1").put_value("Year")
worksheet.cells.get("D1").put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_tables = worksheet.pivot_tables
pivot_index = pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.SUM, True)
category_field.set_subtotals(PivotFieldSubtotalType.AVERAGE, True)
pivot_table.calculate_data()
workbook.save("output_custom.xlsx")
```

## **ملخص**

تختلف السيناريوهات الثلاثة في أمرٍ واحد فقط: استدعاءات `set_subtotals`. أما بقية الأمور — مثل مجموعة البيانات، والحقول، والمناطق التي تُعيّن إليها — فهي متطابقة تمامًا، وهي ما يجعل التخطيطات قابلة للمقارنة المباشرة.
- **وضع الحقول.** ينقل `PivotTable.add_field_to_area(PivotFieldType.ROW, fieldName)` عمود المصدر إلى منطقة معينة. وداخل منطقة واحدة، يمثل ترتيب الاستدعاءات ترتيب العرض، لذا يصبح أول استدعاء هو المجموعة الخارجية. وتحتاج القيم الإجمالية الجزئية (subtotals) إلى حقلين أو أكثر في نفس المنطقة: فمع وجود حقل واحد، لا يوجد ما بين المجموعات لاجتيازه لحساب القيم الإجمالية الجزئية.
- **السيناريو ١ — القيم الإجمالية الجزئية التلقائية.** ترك استدعاء `set_subtotals` دون تنفيذه يُترك الخيار لبرنامج Excel، الذي يطبّق افتراضيًا قيمته الإجمالية الجزئية تلقائيًا على الحقول الرقمية. واستدعاء `set_subtotals` مع `PivotFieldSubtotalType.AUTOMATIC` يسجّل هذا الخيار بشكل صريح بدلاً من تركه ضمنيًا.
- **السيناريو ٢ — عدم وجود قيم إجمالية جزئية.** يُعطل استدعاء `set_subtotals` مع `PivotFieldSubtotalType.NONE` الافتراضي للقيم الإجمالية الجزئية، ليبقى الجدول المحوري مع صفوف الحقل والقيمة الإجمالية الكلية، لكنه يحذف صفوف القيمة الإجمالية الجزئية التي كان برنامج Excel سيُدخلها بينها في الوضع العادي.
- **السيناريو ٣ — مجموعة مختارة.** يُفعّل أو يُعطّل كل استدعاء نوعًا واحدًا من القيم الإجمالية الجزئية فقط، وتتراكم الاستدعاءات بدلاً من مسح بعضها البعض. لذا فإن استدعاء `set_subtotals` مرة بقيمة `PivotFieldSubtotalType.SUM` ومرة أخرى بقيمة `PivotFieldSubtotalType.AVERAGE` يُبقي كلا النوعين مفعّلين، مما يؤدي إلى عرض القيمة الإجمالية الجزئية للجمع (Sum)، والقيمة الإجمالية الجزئية للمتوسط (Average)، والقيمة الإجمالية الكلية معًا.

{{% alert color="primary" %}}
لا يوجد شيء في القيم الإجمالية الجزئية مرتبطًا بمنطقة الصفوف تحديدًا. فإن تنفيذ استدعاءات `set_subtotals` نفسها على حقل مأخوذ من `PivotTable.ColumnFields` ينتج نفس التخطيطات الثلاثة على المحور العمودي، لأن الإعداد ينتمي إلى حقل الجدول المحوري بحد ذاته وليس إلى المحور الذي يقع عليه.
{{% /alert %}}
## **مقالات ذات صلة**
- [حقول الصفحات في الجداول المحورية](/cells/ar/python-net/add-page-field-in-pivot-table/)
- [تحديث الجداول المحورية في Aspose.Cells for Python via .NET](/cells/ar/python-net/refresh-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية](/cells/ar/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}