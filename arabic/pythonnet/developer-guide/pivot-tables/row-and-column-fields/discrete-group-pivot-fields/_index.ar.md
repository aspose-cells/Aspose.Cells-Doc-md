---
title: التجميع المتقطع لعناصر حقول الجدول المحوري
linktitle: التجميع المتقطع
description: تعلّم كيفية تجميع عناصر حقول الجدول المحوري في مجموعات مخصصة ذات أسماء مثل الفاكهة والخضروات باستخدام DiscreteGroupItem وpivot_field_group_options.discrete_group_items في Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python via .NET, جدول محوري, تجميع متقطع, DiscreteGroupItem, PivotFieldGroupOptions, تجميع عناصر حقول الجدول المحوري, مجموعات مخصصة, PivotField.group, Python, Excel جدول محوري
type: docs
weight: 90
url: /ar/python-net/discrete-group-pivot-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
- يجمع التجميع التلقائي العناصر حسب نوع البيانات، مثل تجميع التواريخ إلى أشهر وأرباع، أو الأرقام إلى نطاقات. يعالج التجميع المتقطع المشكلة المعاكسة، إذ يجمع عناصر محددة وغير مرتبطة في مجموعات مخصصة ذات أسماء، مثل تجميع المنتجات في مجموعتَي الفاكهة والخضروات، أو المتاجر في مناطق، أو الحسابات في نطاقات. تتيح Aspose.Cells التجميع المتقطع من خلال صنف `DiscreteGroupItem` وخاصية `pivot_field_group_options.discrete_group_items`.
- يتكون `DiscreteGroupItem` من اسم مجموعة وعناصر تنتمي إليها. يمكن تحديد العناصر إما بأسمائها (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) أو بمواضعها ذات الترقيم بدءًا من الصفر في بيانات المصدر (`DiscreteGroupItem("fruit", [0, 3])`). ينتج كلا الشكلين النتيجة نفسها.
- يُطبَّق التجميع المتقطع على حقل في منطقة الصفوف أو الأعمدة في الجدول المحوري عن طريق تمرير الخيارات إلى `pivot_field.group(PivotFieldGroupOptions)`.

## **تجميع عناصر حقول الجدول المحوري حسب أسماء العناصر**
يبني المثال التالي قائمة مبيعات صغيرة (المنتج والتاريخ والمبلغ)، وينشئ منها جدولاً محوريًا يضع `product` في منطقة الصفوف و`date` في منطقة الأعمدة و`amount` في منطقة البيانات، ثم يحدد مجموعتين مخصصتين بحسب أسماء العناصر: الفاكهة (عنب، كرز) والخضروات (جزر، بطاطس). تُظهر النتيجة تخطيط صفوف من مستويين، إذ يظهر اسم المجموعة في المستوى الخارجي وتُدرج العناصر الأصلية تحته، ما يتيح قراءة الاتجاهات لكل مجموعة مخصصة ولكل عنصر.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# Group specific items into custom groups using 0-based source-appearance indexes
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotField.xlsx")
```

بعد `calculate_data()`، تُظهر منطقة الصفوف في الجدول المحوري الفاكهة (عنب 50، كرز 80) والخضروات (جزر 60، بطاطس 70)، مع الإجمالي الكلي 260، بينما تحتفظ تسميات الأعمدة بالتواريخ الأربعة (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **تجميع عناصر حقول الجدول المحوري حسب فهارس العناصر**
إذا كانت أسماء العناصر طويلة أو معروضة بلغة محلية، يحدد المُنشئ الثاني لـ `DiscreteGroupItem` العناصر حسب الفهرس. تمثل الفهارس مواضع العناصر ذات الترقيم بدءًا من الصفر وفق ترتيب ظهورها في بيانات المصدر، لا وفق الترتيب الأبجدي. في بيانات العينة أعلاه، العنب هو العنصر 0، والجزر هو العنصر 1، والبطاطس هي العنصر 2، والكرز هو العنصر 3؛ لذلك تكون الفاكهة `{ 0, 3 }` والخضروات `{ 1, 2 }`. والنتيجة مطابقة لمثال التجميع حسب الأسماء.

```python
import aspose.cells as ac
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
from datetime import datetime
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
# (zero-based positions in the order the items appear in the source data)
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
```

## **ملاحظة**

{{% alert color="primary" %}}
- العناصر التي لم تُسند إلى أي مجموعة مخصصة لا تضيع. تظل في الجدول المحوري على مستوى المجموعات المخصصة نفسه، ويكون كل منها إدخالًا مستقلًا يتكون من عنصر واحد. في المثال أعلاه، يظل الجزر والبطاطس في منطقة الصفوف كإدخالات مستقلة بجوار مجموعة الفاكهة.
- تتحكم الخاصية `pivot_field_group_options.new_pivot_field` في تخطيط التجميع المتقطع. القيمة الافتراضية لها هي `True`، مما يضيف الحقل المُجمَّع كحقل خارجي جديد بجوار الحقل الأصلي، وينتج تخطيط الصفوف ذي المستويين الظاهر أعلاه (يزداد `row_fields` إلى 2). اضبطها على `False` لاستبدال الحقل الأصلي بدلاً من ذلك؛ عندئذٍ تعرض منطقة الصفوف مستوى واحدًا يحتوي فقط على أسماء المجموعات وقيمها المجمّعة، وهي الفاكهة 130 (50 + 80) والخضروات 130 (60 + 70).
- يمكن استخدام المُنشئ القائم على الاسم والمُنشئ القائم على الفهرس معًا في قائمة `discrete_group_items` نفسها.
{{% /alert %}}

## **مقالات ذات صلة**
- [تجميع حقول الجدول المحوري داخل الجدول المحوري](/cells/ar/python-net/group-pivot-fields-in-the-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى الجدول المحوري](/cells/ar/python-net/pivot-table-add-row-and-column-fields/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/python-net/filter-by-label-or-value-of-pivot-table/)
- [تطبيق النمط على الجدول المحوري](/cells/ar/python-net/apply-style-to-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}