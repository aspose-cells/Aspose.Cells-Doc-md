---
title: التجميع المنفصل لعناصر حقول الجدول المحوري
linktitle: التجميع المنفصل
description: تعلّم كيفية تجميع عناصر حقول الجدول المحوري في مجموعات مخصصة ذات أسماء، مثل الفاكهة والخضروات، باستخدام DiscreteGroupItem وPivotFieldGroupOptions.getDiscreteGroupItems في Aspose.Cells for Python عبر Java.
keywords: Aspose.Cells, جدول محوري, تجميع منفصل, DiscreteGroupItem, PivotFieldGroupOptions, تجميع عناصر الحقل المحوري, مجموعات مخصصة, PivotField.group, Python عبر Java, Excel جدول محوري
type: docs
weight: 90
url: /ar/python-java/discrete-group-pivot-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
- يقوم التجميع التلقائي بجمع العناصر حسب نوع البيانات، مثل تجميع التواريخ في الأشهر والربعيات أو الأرقام في نطاقات. يعالج التجميع المنفصل المشكلة المعاكسة، إذ يجمع عناصر محددة وغير مترابطة في مجموعات مخصصة ذات أسماء، مثل تجميع المنتجات في مجموعات الفاكهة والخضروات، والمتاجر في مناطق، والحسابات في مناطق. توفر Aspose.Cells التجميع المنفصل من خلال فئة `DiscreteGroupItem` وطريقة `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- يمثل `DiscreteGroupItem` اسم مجموعة مع العناصر التي تنتمي إليها. يمكن تحديد العناصر بطريقتين: حسب أسمائها (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) أو حسب مواضعها المرقّمة من الصفر في بيانات المصدر (`DiscreteGroupItem("fruit", [0, 3])`). ويؤدي كل من الشكليين إلى النتيجة نفسها.
- يُطبَّق التجميع المنفصل على حقل في منطقة الصفوف أو الأعمدة في الجدول المحوري عن طريق تمرير الخيارات إلى `PivotField.group(PivotFieldGroupOptions)`.

## **تجميع عناصر حقول الجدول المحوري حسب أسماء العناصر**
يبني المثال التالي قائمة مبيعات صغيرة (المنتج والتاريخ والمبلغ)، وينشئ منها جدولاً محوريًا يضع `product` في منطقة الصفوف و`date` في منطقة الأعمدة و`amount` في منطقة البيانات، ثم يحدد مجموعتين مخصصتين حسب أسماء العناصر: الفاكهة (عنب، كرز) والخضروات (جزر، بطاطس). تعرض النتيجة تخطيطًا للصفوف من مستويين، يكون فيه اسم المجموعة في المستوى الخارجي، وتظهر العناصر الأصلية في مستوى فرعي تحته، مما يتيح قراءة الاتجاهات لكل مجموعة مخصصة ولكل عنصر.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    DiscreteGroupItem,
    PivotFieldGroupOptions,
    PivotFieldType,
    PivotTableStyleType,
)
GregorianCalendar = jpype.JPackage("java.util").GregorianCalendar
def create_date(year, month, day):
    calendar = GregorianCalendar(year, month - 1, day)
    return calendar.getTime()
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(create_date(2021, 2, 5))
cells.get(2, 1).putValue(create_date(2022, 3, 8))
cells.get(3, 1).putValue(create_date(2023, 4, 10))
cells.get(4, 1).putValue(create_date(2024, 5, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
# Group specific items into custom groups by item names
fruit = DiscreteGroupItem("fruit", ["grape", "cherry"])
vegetable = DiscreteGroupItem("vegetable", ["carrot", "potato"])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.calculateData()
pivot_table.getRowFields().get(0).group(group_options)
wb.save("outputDiscreteGroupPivotField.xlsx")
jpype.shutdownJVM()
```

بعد `calculateData()`، تعرض منطقة الصفوف في الجدول المحوري الفاكهة (عنب 50، كرز 80) والخضار (جزر 60، بطاطس 70) مع الإجمالي الكلي 260، بينما تظهر في تسميات الأعمدة التواريخ الأربعة (2/5/2021، 3/8/2022، 4/10/2023، 5/16/2024).

## **تجميع عناصر حقول الجدول المحوري حسب فهارس العناصر**
عندما تكون أسماء العناصر طويلة أو مُعرَّبة، يحدد المُنشئ الثاني لـ `DiscreteGroupItem` العناصر حسب الفهرس. الفهارس هي مواضع العناصر المرقّمة من الصفر وفق ترتيب ظهورها في بيانات المصدر، لا وفق الترتيب الأبجدي. في بيانات العينة أعلاه، العنب هو العنصر 0، والجزر هو العنصر 1، والبطاطس هي العنصر 2، والكرز هو العنصر 3؛ لذلك، تكون مجموعة الفاكهة `{ 0, 3 }` ومجموعة الخضار `{ 1, 2 }`. والنتيجة مطابقة لمثال التجميع حسب الأسماء.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotTableStyleType,
)
Date = jpype.JClass("java.util.Date")
DiscreteGroupItem = jpype.JClass("com.aspose.cells.DiscreteGroupItem")
PivotFieldGroupOptions = jpype.JClass("com.aspose.cells.PivotFieldGroupOptions")
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(Date(2021 - 1900, 2 - 1, 5))
cells.get(2, 1).putValue(Date(2022 - 1900, 3 - 1, 8))
cells.get(3, 1).putValue(Date(2023 - 1900, 4 - 1, 10))
cells.get(4, 1).putValue(Date(2024 - 1900, 5 - 1, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
pivot_table.calculateData()
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.getRowFields().get(0).group(group_options)
pivot_table.calculateData()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
jpype.shutdownJVM()
```

## **ملاحظة**

{{% alert color="primary" %}}
- لا تُفقد العناصر التي لم تُسنَد إلى أي مجموعة مخصصة. وتبقى في الجدول المحوري عند المستوى نفسه الذي توجد فيه المجموعات المخصصة، في هيئة إدخالات مستقلة، كل منها لعنصر واحد. في المثال أعلاه، يؤدي تعريف مجموعة الفاكهة فقط إلى ترك الجزر والبطاطس في منطقة الصفوف كإدخالات مستقلة إلى جانب مجموعة الفاكهة.
- تتحكم الطريقتان `getNewPivotField()` و`setNewPivotField()` في تخطيط التجميع المنفصل. القيمة الافتراضية لـ `getNewPivotField()` هي `true`، ما يضيف الحقل المجمَّع كحقل جديد في المستوى الخارجي إلى جانب الحقل الأصلي، وينتج عن ذلك تخطيط من مستويين، كما هو موضح أعلاه (يبلغ عدد الحقول التي تعيدها `getRowFields()` 2). استخدم `setNewPivotField(false)` لاستبدال الحقل الأصلي؛ عندئذ، تعرض منطقة الصفوف مستوى واحدًا يحتوي فقط على أسماء المجموعات وقيمها المجمعة: الفاكهة 130 (50 + 80) والخضار 130 (60 + 70).
- يمكن مزج المُنشئين المعتمدين على الاسم والفهرس لـ `DiscreteGroupItem` ضمن المجموعة `getDiscreteGroupItems()` نفسها.
{{% /alert %}}

## **مقالات ذات صلة**
- [تجميع حقول الجدول المحوري داخل الجدول المحوري](/cells/ar/python-java/group-pivot-fields-in-the-pivot-table/)
- [إضافة حقول الصفوف والأعمدة إلى الجدول المحوري](/cells/ar/python-java/pivot-table-add-row-and-column-fields/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/python-java/filter-by-label-or-value-of-pivot-table/)
- [تطبيق `Style` على الجدول المحوري](/cells/ar/python-java/apply-style-to-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}