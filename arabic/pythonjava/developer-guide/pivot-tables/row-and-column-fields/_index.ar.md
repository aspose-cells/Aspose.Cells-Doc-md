---
title: إضافة حقول الصفوف والأعمدة إلى الجدول المحوري في Aspose.Cells for Python عبر Java
linktitle: إضافة حقول الصفوف والأعمدة إلى الجدول المحوري في Aspose.Cells for Python عبر Java
description: تعلم كيفية إضافة الحقول الأساسية إلى منطقتي الصفوف والأعمدة في جدول محوري والتحكم في الإجماليات الفرعية لحقول PivotField باستخدام PivotField.setSubtotals في Aspose.Cells for Python عبر Java.
keywords: Aspose.Cells, Python عبر Java, جدول محوري, حقل صف, حقل عمود, PivotField, setSubtotals, PivotFieldSubtotalType, إجماليات فرعية
type: docs
weight: 220
url: /ar/python-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **إضافة حقل إلى منطقة الصفوف أو الأعمدة**
تنقل طريقة `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` حقلًا أساسيًا من بيانات المصدر إلى إحدى مناطق الجدول المحوري الأربع. تقبل الوسيطة `fieldType` إحدى قيم `PivotFieldType` التالية.
- `ROW` — حقول موضوعة رأسيًا على اليسار
- `COLUMN` — حقول موضوعة أفقيًا في الأعلى
- `DATA` — حقول يتم تجميع قيمها
- `PAGE` — حقول تُستخدم كعوامل تصفية للتقارير
ترتيب تداخل الحقول مهم. تُنتج إضافة `Category` أولًا إلى منطقة الصفوف ثم `Item` جدولًا محوريًا يكون التجميع الخارجي فيه هو `Category` والتجميع الداخلي هو `Item`. وعكس الترتيب يعكس التسلسل الهرمي.

## **الإجماليات الفرعية لحقل PivotField**
تتحكم طريقة `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` في صفوف الإجماليات الفرعية التي تظهر لحقل الجدول المحوري. يبدّل كل استدعاء نوعًا واحدًا من الإجماليات الفرعية بشكل مستقل. تمرير `shown = true` يعرض الإجمالي الفرعي، بينما يخفيه `shown = false`. ونظرًا لأن كل استدعاء يؤثر في نوع واحد فقط، فإن استدعاء الطريقة عدة مرات بقيم `subtotalType` مختلفة يبني مجموعة مخصصة من الإجماليات الفرعية.
يُعرّف التعداد `PivotFieldSubtotalType` أنواع الإجماليات الفرعية المتاحة.
- `AUTOMATIC` — يختار Aspose.Cells التحديد الافتراضي، وهو عادةً `SUM` للحقول الرقمية
- `NONE` — يمنع عرض جميع صفوف الإجماليات الفرعية
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
لا تظهر الإجماليات الفرعية إلا عندما يوجد حقلا جدول محوري أو أكثر في منطقة الصفوف أو في منطقة الأعمدة. لا يوفر الحقل الواحد أي أساس ذي معنى لحساب إجمالي فرعي بين المجموعات، لذا لا يظهر أي تأثير لاستدعاءات `setSubtotals` في هذه الحالة. لذلك تستخدم هذه المقالة حقلي صفوف، هما `Category` في الخارج و`Item` في الداخل، في كل مثال حتى يظهر الحد الفاصل للإجمالي الفرعي بين كل مجموعة `Category`.
{{% /alert %}}

## **السيناريو 1 — الإجماليات الفرعية التلقائية (الافتراضية)**
إذا لم تستدعِ `setSubtotals` إطلاقًا، فإن Aspose.Cells يطبق التحديد `AUTOMATIC` على الحقول الرقمية. يؤكد المثال التالي هذا السلوك صراحةً من خلال استدعاء `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` على حقل الصف الخارجي `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, PivotTable, PivotField, PivotFieldType, PivotFieldSubtotalType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
worksheet.getCells().get(0, 0).putValue("Category")
worksheet.getCells().get(0, 1).putValue("Item")
worksheet.getCells().get(0, 2).putValue("Year")
worksheet.getCells().get(0, 3).putValue("Amount")
worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)
worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)
worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)
worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)
worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)
worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)
worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)
worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)
pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, True)
pivotTable.calculateData()
workbook.save("output_automatic.xlsx")
jpype.shutdownJVM()
```

## **السيناريو 2 — منع جميع الإجماليات الفرعية (بدون إجماليات فرعية)**
يزيل استدعاء `setSubtotals(PivotFieldSubtotalType.NONE, true)` كل صف من صفوف الإجماليات الفرعية من الجدول المحوري، تاركًا فقط صفوف الحقول والإجمالي الكلي أسفل الجدول. يكون هذا مفيدًا عندما تريد البيانات المجمّعة الخام من دون أي صفوف ملخص.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFieldSubtotalType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.getCells().get(0, j).putValue(headers[j])
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80 ],
    ["Fruit",     "Banana", 2021, 90 ],
    ["Vegetable", "Carrot", 2020, 50 ],
    ["Vegetable", "Carrot", 2021, 60 ],
    ["Vegetable", "Daikon", 2020, 40 ],
    ["Vegetable", "Daikon", 2021, 45 ]
]
for i in range(len(data)):
    for j in range(len(data[0])):
        worksheet.getCells().get(i + 1, j).putValue(data[i][j])
pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, True)
pivotTable.calculateData()
workbook.save("output_none.xlsx")
jpype.shutdownJVM()
```

## **السيناريو 3 — مجموعة فرعية مخصصة من الإجماليات (المجموع + المتوسط)**
لا تقتصر على نوع واحد من الإجماليات الفرعية. يعمل كل استدعاء لـ `setSubtotals` بشكل مستقل على نوع واحد، لذلك يُنتج استدعاء الطريقة مرتين، مرة مع `SUM` ومرة مع `AVERAGE`، مجموعة مخصصة من صفَّي إجماليات فرعية لكل مجموعة `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableCollection, PivotTable, PivotFieldType, PivotField, PivotFieldSubtotalType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
worksheet.getCells().get("A1").putValue("Category")
worksheet.getCells().get("B1").putValue("Item")
worksheet.getCells().get("C1").putValue("Year")
worksheet.getCells().get("D1").putValue("Amount")
worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)
worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)
worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)
worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)
worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)
worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)
worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)
worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)
pivotTables = worksheet.getPivotTables()
pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.SUM, True)
categoryField.setSubtotals(PivotFieldSubtotalType.AVERAGE, True)
pivotTable.calculateData()
workbook.save("output_custom.xlsx")
jpype.shutdownJVM()
```

## **ملخص**

تختلف السيناريوهات الثلاثة في شيء واحد فقط: استدعاءات `setSubtotals`. وeverything else — أي مجموعة البيانات، والحقول، والمجالات التي تُعيَّن إليها — متطابقة تمامًا، وهذا ما يجعل التخطيطات قابلة للمقارنة مباشرة.
- **وضع الحقول.** ينقل `PivotTable.addFieldToArea(PivotFieldType.ROW, fieldName)` عمود مصدر إلى منطقة. وداخل منطقة واحدة، يحدد ترتيب الاستدعاءات ترتيب العرض، لذا يصبح أول استدعاء المجموعة الخارجية. وتحتاج التجميعات الفرعية إلى حقلين أو أكثر داخل نفس المنطقة: فبوجود حقل واحد لا يوجد شيء بين المجموعات يمكن تجميعه فرعيًا.
- **السيناريو 1 — التجميعات الفرعية التلقائية.** ترك `setSubtotals` دون استدعائها يترك الخيار لـ Excel، الذي يطبّق تجميعًا فرعيًا افتراضيًا خاصًا به على الحقول الرقمية. بينما يؤدي استدعاء `setSubtotals` مع `PivotFieldSubtotalType.AUTOMATIC` إلى تسجيل هذا الخيار بشكل صريح بدلًا من تركه ضمنيًا.
- **السيناريو 2 — عدم وجود تجميعات فرعية.** يؤدي استدعاء `setSubtotals` مع `PivotFieldSubtotalType.NONE` إلى إيقاف التجميع الفرعي الافتراضي، بحيث تحتفظ الجدول المحوري بصفوف الحقل والملخص الكلي، لكنه يحذف صفوف التجميع الفرعي التي يُدرجها Excel بشكل افتراضي بينها.
- **السيناريو 3 — مجموعة مختارة.** يؤدي كل استدعاء إلى تبديل نوع تجميع فرعي واحد فقط، وتتراكم الاستدعاءات بدلًا من أن تُعيد تعيين بعضها. لذا فإن استدعائها مرة واحدة مع `PivotFieldSubtotalType.SUM` ومرة أخرى مع `PivotFieldSubtotalType.AVERAGE` يُبقي كليهما مُفعَّلين، مما يؤدي إلى عرض تجميع فرعي مجموع (Sum)، وتجميع فرعي متوسط (Average)، والملخص الكلي معًا.

{{% alert color="primary" %}}
لا يوجد شيء خاص بالتجميعات الفرعية يتعلق بالمنطقة الصفية فقط. فاستدعاءات `setSubtotals` نفسها على حقل مأخوذ من `PivotTable.ColumnFields` تُنتج نفس التخطيطات الثلاثة على المحور العمودي، لأن الإعداد ينتمي إلى حقل PivotField بحد ذاته وليس للمحور الذي يقع عليه.
{{% /alert %}}
## **مقالات ذات صلة**
- [حقول الصفحة في الجداول المحورية](/cells/ar/python-java/add-page-field-in-pivot-table/)
- [تحديث الجداول المحورية في Aspose.Cells for Python عبر Java](/cells/ar/python-java/refresh-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية](/cells/ar/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}