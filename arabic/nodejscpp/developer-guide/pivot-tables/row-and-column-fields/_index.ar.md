---
title: إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells لـ .NET
linktitle: حقول الصفوف والأعمدة
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.SetSubtotals in Aspose.Cells for Node.js via C++
keywords: Aspose.Cells, Node.js, C++, pivot table, row field, column field, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /ar/nodejs-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **إضافة حقل إلى منطقة الصفوف أو الأعمدة**

تنقل طريقة `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` حقلًا أساسيًا من البيانات المصدر إلى إحدى مناطق الجدول المحوري الأربع. تقبل وسيط `fieldType` إحدى قيم `PivotFieldType` التالية.

- `Row` — الحقول الموضوعة عموديًا على اليسار
- `Column` — الحقول الموضوعة أفقيًا عبر الأعلى
- `Data` — الحقول التي يتم تجميع قيمها
- `Page` — الحقول المستخدمة كمرشحات للتقرير

بعد إضافة الحقول، يمكنك الوصول إليها من خلال خصائص `PivotTable.RowFields` و`PivotTable.ColumnFields`. تُرجع كل خاصية كائن `PivotFieldCollection`. الحقل في الفهرس 0 من `RowFields` هو حقل الصف الخارجي، وتمثل الفهارس اللاحقة الحقول المتداخلة داخله. ينطبق نفس اصطلاح الفهرسة على `ColumnFields`.

يهم ترتيب تداخل الحقول. تؤدي إضافة `Category` إلى منطقة الصفوف أولًا، ثم إضافة `Item`، إلى إنتاج جدول محوري يكون فيه التجميع الخارجي هو `Category` والتجميع الداخلي هو `Item`. يؤدي عكس الترتيب إلى عكس التسلسل الهرمي.

## **إجماليات الحقول المحورية الفرعية**

تتحكم طريقة `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` في صفوف الإجمالي الفرعي التي تظهر لحقل محوري. يعمل كل استدعاء على تبديل نوع إجمالي فرعي واحد بشكل مستقل. يعرض تمرير `shown = true` الإجمالي الفرعي، بينما يخفيه `shown = false`. نظرًا لأن كل استدعاء يؤثر على نوع واحد فقط، فإن استدعاء الطريقة عدة مرات بقيم `subtotalType` مختلفة يُنشئ مجموعة فرعية مخصصة من الإجماليات الفرعية.

يحدد التعداد `PivotFieldSubtotalType` أنواع الإجماليات الفرعية المتاحة.

- `Automatic` — يختار Aspose.Cells التحديد الافتراضي (عادةً `Sum` للحقول الرقمية)
- `None` — إلغاء جميع صفوف الإجمالي الفرعي
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
لا تظهر الإجماليات الفرعية إلا عند وجود حقلين محوريين أو أكثر في منطقة الصفوف (أو في منطقة الأعمدة). لا يوفّر حقل واحد منفردًا ما يمكن حساب إجمالي فرعي له بين المجموعات، لذلك لا يكون لاستدعاءات `SetSubtotals` أي تأثير مرئي في هذه الحالة. لذلك تضع هذه المقالة حقلَي صفوف (`Category` خارجي، `Item` داخلي) في كل مثال بحيث تكون حدود الإجمالي الفرعي بين كل مجموعة `Category` مرئية.
{{% /alert %}}

## **السيناريو 1 — الإجماليات الفرعية التلقائية (الافتراضية)**

عندما لا تستدعي `SetSubtotals` على الإطلاق، يطبق Aspose.Cells تحديد `Automatic` على الحقول الرقمية. يؤكد المثال التالي هذا السلوك صراحةً عن طريق استدعاء `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` على حقل الصف الخارجي `Category`.

```javascript
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

## **السيناريو 2 — إلغاء جميع الإجماليات الفرعية (None)**

يؤدي استدعاء `SetSubtotals(PivotFieldSubtotalType.None, true)` إلى إزالة جميع صفوف الإجمالي الفرعي من الجدول المحوري، مع ترك صفوف الحقول والإجمالي الكلي فقط في الأسفل. يكون هذا مفيدًا عندما تريد البيانات المجمّعة الأولية بدون أي صفوف ملخص.

```javascript
const AsposeCells = require("aspose.cells");

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

## **السيناريو 3 — مجموعة الإجماليات الفرعية المخصصة (Sum + Average)**

لستَ مقيدًا بنوع إجمالي فرعي واحد. يعمل كل استدعاء `SetSubtotals` بشكل مستقل على نوع واحد، لذلك يؤدي استدعاء الطريقة مرتين — مرة باستخدام `Sum` ومرة باستخدام `Average` — إلى إنتاج مجموعة فرعية مخصصة من صفّي إجمالي فرعي لكل مجموعة `Category`.

```javascript
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

تتشارك السيناريوهات الثلاثة أعلاه في نفس مجموعة البيانات وبنية الجدول المحوري. الاختلاف الوحيد بينها هو استدعاء `SetSubtotals` المطبق على حقل الصف الخارجي `Category`. تذكّر قاعدة الحقلين: حقل منفرد واحد في منطقة ما لا يوفّر ما يمكن حساب إجمالي فرعي له بين المجموعات، لذلك ضع دائمًا حقلين على الأقل في منطقة الصفوف أو الأعمدة عندما تريد أن يكون لاستدعاء `SetSubtotals` تأثير مرئي.
{{< app/cells/assistant language="nodejs-cpp" >}}
