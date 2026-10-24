---
title: إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells for Node.js via C++
linktitle: إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells for Node.js via C++
description: تعلّم كيفية إضافة الحقول الأساسية إلى منطقتي الصفوف والأعمدة في جدول محوري والتحكم في المجاميع الفرعية لحقول الجدول المحوري باستخدام PivotField.SetSubtotals في Aspose.Cells for Node.js via C++
keywords: Aspose.Cells, Node.js, C++, جدول محوري, حقل صف, حقل عمود, PivotField, SetSubtotals, PivotFieldSubtotalType, مجاميع فرعية
type: docs
weight: 220
url: /ar/nodejs-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **إضافة حقل إلى منطقة الصفوف أو الأعمدة**
تنقل طريقة `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` حقلًا أساسيًا من بيانات المصدر إلى إحدى مناطق الجدول المحوري الأربع. تقبل الوسيطة `fieldType` إحدى قيم `PivotFieldType` التالية.
- `Row` — الحقول الموضوعة رأسيًا على الجانب الأيسر
- `Column` — الحقول الموضوعة أفقيًا في أعلى الجدول
- `Data` — الحقول التي يتم تجميع قيمها
- `Page` — الحقول المستخدمة كمرشحات للتقرير
ترتيب تداخل الحقول مهم. تؤدي إضافة `Category` إلى منطقة الصفوف أولًا، ثم `Item`، إلى إنشاء جدول محوري يكون التجميع الخارجي فيه هو `Category` والتجميع الداخلي هو `Item`. ويؤدي عكس الترتيب إلى عكس التسلسل الهرمي.

## **المجاميع الفرعية لحقول الجدول المحوري**
تتحكم طريقة `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` في صفوف المجاميع الفرعية الظاهرة لحقل في الجدول المحوري. يبدّل كل استدعاء حالة نوع واحد من أنواع المجاميع الفرعية بشكل مستقل. يؤدي تمرير `shown = true` إلى عرض المجموع الفرعي، بينما يؤدي `shown = false` إلى إخفائه. وبناءً على أن كل استدعاء يؤثر في نوع واحد فقط، فإن استدعاء الطريقة عدة مرات بقيم `subtotalType` مختلفة ينشئ مجموعة مخصصة من المجاميع الفرعية.
يحدد التعداد `PivotFieldSubtotalType` أنواع المجاميع الفرعية المتاحة.
- `Automatic` — يختار Aspose.Cells الخيار الافتراضي (عادةً `Sum` للحقول الرقمية)
- `None` — يمنع عرض جميع صفوف المجاميع الفرعية
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
لا تظهر المجاميع الفرعية إلا عند وجود حقلين أو أكثر في الجدول المحوري ضمن منطقة الصفوف (أو منطقة الأعمدة). لا يوجد عند الحقل المفرد أي حد يمكن أن تظهر عنده المجاميع الفرعية بصورة ذات معنى، لذلك لا يظهر لاستدعاءات `setSubtotals` أي تأثير مرئي في هذه الحالة. تضع هذه المقالة حقلين في منطقة الصفوف (`Category` هو الحقل الخارجي و`Item` هو الحقل الداخلي) في كل مثال، حتى يكون الحد الفاصل للمجاميع الفرعية بين كل مجموعة `Category` واضحًا.
{{% /alert %}}

## **السيناريو 1 — المجاميع الفرعية التلقائية (الافتراضية)**
عند عدم استدعاء `setSubtotals` إطلاقًا، يطبق Aspose.Cells الخيار `Automatic` على الحقول الرقمية. يؤكد المثال التالي هذا السلوك صراحةً من خلال استدعاء `setSubtotals(PivotFieldSubtotalType.Automatic, true)` على حقل الصف الخارجي `Category`.

```javascript
const AsposeCells = require("aspose.cells.node");
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
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **السيناريو 2 — تعطيل جميع المجاميع الفرعية (None)**
يزيل استدعاء `setSubtotals(PivotFieldSubtotalType.None, true)` جميع صفوف المجاميع الفرعية من الجدول المحوري، تاركًا فقط صفوف الحقول والإجمالي الكلي في الأسفل. ويكون هذا مفيدًا عند الرغبة في عرض البيانات الخام المجمّعة حسب الحقول دون أي صفوف ملخصات.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
const categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **السيناريو 3 — مجموعة مخصصة من أنواع المجاميع الفرعية (Sum + Average)**
لا تقتصر على نوع واحد من المجاميع الفرعية. يعمل كل استدعاء لـ `setSubtotals` على نوع واحد بشكل مستقل، لذا يؤدي استدعاء الطريقة مرتين — مرة مع `Sum` ومرة مع `Average` — إلى إنشاء مجموعة مخصصة من صفين للمجاميع الفرعية لكل مجموعة `Category`.

```javascript
const AsposeCells = require("aspose.cells.node");
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
let pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **ملخص**

تختلف السيناريوهات الثلاثة في أمرٍ واحد فقط: مكالمات `setSubtotals`. أما كل شيءٍ آخر — أي مجموعة البيانات، والحقول، والمجالات التي تُعين لها — فهو متطابق، وهو ما يجعل التخطيطات قابلة للمقارنة مباشرةً.
- **وضع الحقول.** تنقل `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, fieldName)` عمود المصدر إلى منطقةٍ معيّنة. وداخل منطقةٍ واحدة، يُحدد ترتيب المكالمات ترتيب العرض، لذا تصبح المكالمة الأولى هي المجموعة الخارجية الأعمّ. وتحتاج الحسابات الجزئية إلى حقلين أو أكثر في نفس المنطقة: فمع وجود حقلٍ واحد، لا يوجد ما يُحسب حسابه جزئيًا بين المجموعات.
- **السيناريو ١ — الحسابات الجزئية التلقائية.** ترك `setSubtotals` دون استدعاءٍ يترك الاختيار لـ Excel، الذي يطبّق حسابه الجزئي الافتراضي التلقائي على الحقول الرقمية. أما استدعاء `setSubtotals` مع `AsposeCells.PivotFieldSubtotalType.Automatic` فيسجّل هذا الاختيار صراحةً بدلاً من تركه ضمنيًا.
- **السيناريو ٢ — عدم وجود حسابات جزئية.** يؤدي استدعاء `setSubtotals` مع `AsposeCells.PivotFieldSubtotalType.None` إلى إيقاف الحساب الجزئي الافتراضي، بحيث يحتفظ الجدول المحوري بأسطر الحقل وحسابه الكلي، لكنه يحذف أسطر الحسابات الجزئية التي يُدرجها Excel عادةً بينها.
- **السيناريو ٣ — مجموعة مختارة.** تُفعّل أو تُعطّل كل مكالمة نوع حساب جزئيٍ واحد فقط، وتتراكم المكالمات بدلاً من إلغاء بعضها. ولذلك، يؤدي استدعاء المكتبة مرةً واحدةً مع `AsposeCells.PivotFieldSubtotalType.Sum` ومرةً أخرى مع `AsposeCells.PivotFieldSubtotalType.Average` إلى إبقاء كلا النوعين مفعلَين، فيُظهر الجدول المحوري حسابًا جزئيًا للمجموع (Sum)، وحسابًا جزئيًا للمتوسط (Average)، وحسابًا كليًا.

{{% alert color="primary" %}}
لا شيءٍ في الحسابات الجزئية مخصوصٌ بالمنطقة الصفية فقط. فالمكالمات نفسها على `setSubtotals` لحقلٍ مُؤخذ من `PivotTable.ColumnFields` تُنتج نفس التخطيطات الثلاثة على المحور العمودي، لأن الإعداد ينتمي إلى حقل الجدول المحوري وليس للمحور الذي يقع عليه.
{{% /alert %}}
## **المقالات ذات الصلة**
- [حقول الصفحات في الجداول المحورية](/cells/ar/nodejs-cpp/add-page-field-in-pivot-table/)
- [تحديث الجداول المحورية في Aspose.Cells for Node.js via C++](/cells/ar/nodejs-cpp/refresh-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية](/cells/ar/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}