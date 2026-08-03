---
title: إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells لـ .NET
linktitle: حقول الصفوف والأعمدة
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.setSubtotals in Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java, pivot table, row field, column field, PivotField, setSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /ar/python-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **إضافة حقل إلى منطقة الصفوف أو الأعمدة**

ينقل أسلوب `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` حقلًا أساسيًا من بيانات المصدر إلى إحدى مناطق الجدول المحوري الأربع. تقبل وسيطة `fieldType` إحدى قيم `PivotFieldType` التالية.

- `ROW` — الحقول الموضوعة عموديًا على اليسار
- `COLUMN` — الحقول الموضوعة أفقيًا عبر الجزء العلوي
- `DATA` — الحقول التي يتم تجميع قيمها
- `PAGE` — الحقول المستخدمة كمرشحات للتقرير

بعد إضافة الحقول، يمكنك الوصول إليها من خلال أسلوبي `PivotTable.getRowFields()` و`PivotTable.getColumnFields()`. يُرجع كل أسلوب كائن `PivotFieldCollection`. يُعدّ الحقل عند الفهرس 0 في `RowFields` هو حقل الصف الأبعد، وتمثل الفهارس اللاحقة الحقول المتداخلة داخله. ينطبق نفس اصطلاح الفهرسة على `ColumnFields`.

يهمّ ترتيب تداخل الحقول. تؤدي إضافة `Category` إلى منطقة الصفوف أولًا ثم إضافة `Item` إلى إنشاء جدول محوري يكون فيه التجميع الخارجي `Category` والتجميع الداخلي `Item`. يؤدي عكس الترتيب إلى عكس التسلسل الهرمي.

## **الإجماليات الفرعية لحقول الجدول المحوري**

يتحكم أسلوب `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` في صفوف الإجمالي الفرعي التي تظهر لحقل محوري. يبدّل كل استدعاء نوع إجمالي فرعي واحدًا بشكل مستقل. يعرض تمرير `shown = true` الإجمالي الفرعي، بينما يخفيه `shown = false`. نظرًا لأن كل استدعاء يؤثر فقط على نوع واحد، فإن استدعاء الأسلوب عدة مرات بقيم `subtotalType` مختلفة يُنشئ مجموعة فرعية مخصصة من الإجماليات الفرعية.

يحدد التعداد `PivotFieldSubtotalType` أنواع الإجماليات الفرعية المتاحة.

- `AUTOMATIC` — يختار Aspose.Cells التحديد الافتراضي (عادةً `SUM` للحقول الرقمية)
- `NONE` — إلغاء عرض جميع صفوف الإجمالي الفرعي
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
لا تظهر الإجماليات الفرعية إلا عند وجود حقلين محوريين أو أكثر في منطقة الصفوف (أو في منطقة الأعمدة). لا يوجد لدى حقل واحد ما يستحق الإجمالي الفرعي بينه وبين غيره، لذلك لا يكون لاستدعاءات `setSubtotals` أي تأثير مرئي في هذه الحالة. لذلك تضع هذه المقالة حقلَي صفوف (`Category` خارجي، و`Item` داخلي) في كل مثال لكي يكون حد الإجمالي الفرعي بين كل مجموعة `Category` مرئيًا.
{{% /alert %}}

## **السيناريو 1 — الإجماليات الفرعية التلقائية (الافتراضية)**

عندما لا تستدعي `setSubtotals` على الإطلاق، يطبق Aspose.Cells التحديد `AUTOMATIC` على الحقول الرقمية. يؤكد المثال التالي هذا السلوك صراحةً من خلال استدعاء `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` على حقل الصف الخارجي `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
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

## **السيناريو 2 — إلغاء جميع الإجماليات الفرعية (لا شيء)**

يؤدي استدعاء `setSubtotals(PivotFieldSubtotalType.NONE, true)` إلى إزالة كل صف إجمالي فرعي من الجدول المحوري، تاركًا فقط صفوف الحقول والإجمالي الكلي في الأسفل. يكون ذلك مفيدًا عندما تريد بيانات مجمّعة خام دون أي صفوف ملخص.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
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

## **السيناريو 3 — مجموعة فرعية مخصصة من الإجماليات الفرعية (المجموع + المتوسط)**

لستَ مقيدًا بنوع إجمالي فرعي واحد. يعمل كل استدعاء `setSubtotals` بشكل مستقل على نوع واحد، لذلك يؤدي استدعاء الأسلوب مرتين — مرة باستخدام `SUM` ومرة باستخدام `AVERAGE` — إلى إنشاء مجموعة فرعية مخصصة من صفّي إجمالي فرعي لكل مجموعة `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
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

pivotTable.addFieldToArea(PivotFieldType.Row, "Category")
pivotTable.addFieldToArea(PivotFieldType.Row, "Item")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.Sum, True)
categoryField.setSubtotals(PivotFieldSubtotalType.Average, True)

pivotTable.calculateData()

workbook.save("output_custom.xlsx")

jpype.shutdownJVM()
```
## **ملخص**

تتشارك السيناريوهات الثلاثة أعلاه في نفس مجموعة البيانات وهيكل الجدول المحوري. الفرق الوحيد بينها هو استدعاء `setSubtotals` المطبق على حقل الصف الخارجي `Category`. تذكّر قاعدة الحقلين: لا يوجد لدى حقل واحد في منطقة ما ما يمكن الإجمالي الفرعي بينه وبين غيره، لذلك ضع دائمًا حقلين على الأقل في منطقة الصفوف أو الأعمدة عندما تريد أن يكون لاستدعاء `setSubtotals` تأثير مرئي.
{{< app/cells/assistant language="python" >}}
