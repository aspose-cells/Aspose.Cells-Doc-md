---
title: إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells for Node.js عبر Java
linktitle: إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells for Node.js عبر Java
description: تعلم كيفية إضافة الحقول الأساسية إلى منطقتي الصفوف والأعمدة في الجدول المحوري، والتحكم في المجاميع الفرعية لحقول الجدول المحوري باستخدام PivotField.setSubtotals في Aspose.Cells for Node.js عبر Java
keywords: Aspose.Cells, Node.js, Java, جدول محوري, حقل صف, حقل عمود, PivotField, setSubtotals, PivotFieldSubtotalType, مجاميع فرعية
type: docs
weight: 220
url: /ar/nodejs-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **إضافة حقل إلى منطقة الصفوف أو الأعمدة**
تنقل الطريقة `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` حقلًا أساسيًا من بيانات المصدر إلى إحدى مناطق الجدول المحوري الأربع. ويقبل الوسيط `fieldType` إحدى قيم `PivotFieldType` التالية.
- `ROW` — حقول موضوعة عموديًا على اليسار
- `COLUMN` — حقول موضوعة أفقيًا في الأعلى
- `DATA` — حقول يتم تجميع قيمها
- `PAGE` — حقول مستخدمة كمرشحات للتقرير
يكون ترتيب تداخل الحقول مهمًا. تؤدي إضافة `Category` إلى منطقة الصفوف أولًا، ثم إضافة `Item`، إلى إنشاء جدول محوري يكون فيه التجميع الخارجي حسب `Category` والتجميع الداخلي حسب `Item`. ويؤدي عكس الترتيب إلى عكس التسلسل الهرمي.

## **المجاميع الفرعية لحقل الجدول المحوري**
تتحكم الطريقة `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` في صفوف المجاميع الفرعية التي تظهر لحقل الجدول المحوري. يبدّل كل استدعاء حالة نوع واحد من المجاميع الفرعية بشكل مستقل. تمرير `shown = true` يعرض المجموع الفرعي، بينما تمرير `shown = false` يخفيه. وبما أن كل استدعاء يؤثر في نوع واحد فقط، فإن استدعاء الطريقة عدة مرات بقيم مختلفة لـ`subtotalType` ينشئ مجموعة فرعية مخصصة من المجاميع الفرعية.
يحدد التعداد `PivotFieldSubtotalType` أنواع المجاميع الفرعية المتاحة.
- `AUTOMATIC` — يختار Aspose.Cells التحديد الافتراضي (عادةً `SUM` للحقول الرقمية)
- `NONE` — يمنع عرض جميع صفوف المجاميع الفرعية
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
لا تظهر المجاميع الفرعية إلا عندما يكون في منطقة الصفوف (أو الأعمدة) حقلان أو أكثر من حقول الجدول المحوري. ولا يوجد عند الحقل الواحد ما يمكن حساب مجموع فرعي ذي دلالة له، لذلك لا يكون لاستدعاءات `setSubtotals` أي تأثير مرئي في هذه الحالة. ولذلك يضع هذا المقال حقلين للصفوف في كل مثال، ويكون `Category` هو الحقل الخارجي و`Item` هو الحقل الداخلي، حتى يتضح حد المجموع الفرعي بين كل مجموعة `Category`.
{{% /alert %}}

## **السيناريو 1 — المجاميع الفرعية التلقائية (الافتراضية)**
عند عدم استدعاء `setSubtotals` إطلاقًا، يطبق Aspose.Cells التحديد `AUTOMATIC` على الحقول الرقمية. ويؤكد المثال التالي هذا السلوك صراحةً من خلال استدعاء `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` على حقل الصف الخارجي `Category`.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");
worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);
worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);
worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);
worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);
worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);
worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);
worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);
worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);
let pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AUTOMATIC, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **السيناريو 2 — منع جميع المجاميع الفرعية (None)**
يزيل استدعاء `setSubtotals(PivotFieldSubtotalType.NONE, true)` جميع صفوف المجاميع الفرعية من الجدول المحوري، ولا يترك سوى صفوف الحقول والإجمالي الكلي في الأسفل. وهذا مفيد عند الرغبة في عرض البيانات المجمعة الخام دون أي صفوف ملخص.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
let headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
let data = [
    ["Fruit", "Apple", 2020, 100],
    ["Fruit", "Apple", 2021, 150],
    ["Fruit", "Banana", 2020, 80],
    ["Fruit", "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];
for (let i = 0; i < data.length; i++)
{
    for (let j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
let pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.NONE, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **السيناريو 3 — مجموعة فرعية مخصصة من المجاميع الفرعية (Sum + Average)**
لا تقتصر على نوع واحد من المجاميع الفرعية. يعمل كل استدعاء لـ`setSubtotals` بشكل مستقل على نوع واحد. لذلك، يؤدي استدعاء الطريقة مرتين، مرة واحدة باستخدام `SUM` ومرة أخرى باستخدام `AVERAGE`، إلى إنشاء مجموعة فرعية مخصصة من صفين للمجاميع الفرعية لكل مجموعة `Category`.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");
worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);
worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);
worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);
worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);
worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);
worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);
worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);
worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);
let pivotTables = worksheet.getPivotTables();
let pivotTable = pivotTables.add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AVERAGE, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **ملخص**
تختلف السيناريوهات الثلاثة في عنصر واحد فقط: استدعاءات `setSubtotals`. أما كل شيء آخر — مثل مجموعة البيانات، والحقول، والمناطق التي تُعيَّن إليها — فهو متطابق، وهذا هو ما يجعل التوزيعات مقارنة مباشرة.
- **وضع الحقول.** ينقل `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, fieldName)` عمود مصدر إلى منطقة معينة. وترتيب هذه الاستدعاءات داخل منطقة واحدة يُحدِّد ترتيب العرض، لذا فإن أول استدعاء يصبح المجموعة الخارجية. وتحتاج القيم الفرعية إلى حقلين أو أكثر داخل نفس المنطقة: فمع وجود حقل واحد لا توجد أي قيمة تُحسب بين المجموعات لتكون قيمة فرعية.
- **السيناريو 1 — القيم الفرعية التلقائية.** تترك القيم الفرعية على خيار إكسل إذا لم تُستدعَ `setSubtotals`، حيث يُطبِّق إكسل القيمة الفرعية التلقائية الافتراضية الخاصة به على الحقول الرقمية. بينما يُسجَّل هذا الاختيار صراحة عند استدعاء `setSubtotals` باستخدام `AsposeCells.PivotFieldSubtotalType.AUTOMATIC`، بدلاً من تركه ضمنياً.
- **السيناريو 2 — عدم وجود قيم فرعية.** يُعطِّل استدعاء `setSubtotals` باستخدام `AsposeCells.PivotFieldSubtotalType.NONE` القيمة الفرعية الافتراضية، ليبقى الجدول المحوري يحتفظ بصفوف الحقول والقيمة الإجمالية الكبرى، لكنه يحذف صفوف القيم الفرعية التي كان إكسل سيُدخلها بينها.
- **السيناريو 3 — مجموعة مختارة.** يفعّل أو يعطّل كل استدعاء نوعًا واحدًا من القيم الفرعية بالضبط، وتت tích الاستدعاءات بدلًا من إعادة ضبط بعضها البعض. لذا فإن استدعاء `setSubtotals` مرة واحدة باستخدام `AsposeCells.PivotFieldSubtotalType.SUM` ومرة أخرى باستخدام `AsposeCells.PivotFieldSubtotalType.AVERAGE` يُبقي كلا النوعين مفعّلين، فيعرض الجدول المحوري قيمة فرعية للمجموع، وقيمة فرعية للمتوسط، والقيمة الإجمالية الكبرى.

{{% alert color="primary" %}}
لا يوجد شيء في القيم الفرعية مرتبط بالمنطقة الصفية فقط. فالاستدعاءات نفسها `setSubtotals` المطبَّقة على حقل مأخوذ من `PivotTable.ColumnFields` تُنتج نفس التوزيعات الثلاثة على محور الأعمدة، لأن الإعداد ينتمي إلى الحقل المحوري نفسه وليس إلى المحور الذي يقبع عليه.
{{% /alert %}}

## **مقالات ذات صلة**
- [حقول الصفحة في الجداول المحورية](/cells/ar/nodejs-java/add-page-field-in-pivot-table/)
- [تحديث الجداول المحورية في Aspose.Cells for Node.js عبر Java](/cells/ar/nodejs-java/refresh-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية](/cells/ar/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}