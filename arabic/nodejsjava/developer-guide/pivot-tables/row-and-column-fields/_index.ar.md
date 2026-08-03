---
title: إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells لـ .NET
linktitle: حقول الصفوف والأعمدة
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.setSubtotals in Aspose.Cells for Node.js via Java
keywords: Aspose.Cells, Node.js, Java, pivot table, row field, column field, PivotField, setSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /ar/nodejs-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **إضافة حقل إلى منطقة الصفوف أو الأعمدة**

تقوم طريقة `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` بنقل حقل أساسي من بيانات المصدر إلى إحدى مناطق الجدول المحوري الأربعة. تقبل وسيط `fieldType` إحدى قيم `PivotFieldType` التالية.

- `ROW` — الحقول الموضوعة عموديًا على اليسار
- `COLUMN` — الحقول الموضوعة أفقيًا عبر الأعلى
- `DATA` — الحقول التي يتم تجميع قيمها
- `PAGE` — الحقول المستخدمة كمرشحات للتقرير

بعد إضافة الحقول، يمكنك الوصول إليها من خلال خصائص `PivotTable.getRowFields()` و `PivotTable.getColumnFields()`. تُرجع كل خاصية `PivotFieldCollection`. الحقل في الفهرس 0 من `RowFields` هو حقل الصف الأبعد، وتمثل الفهارس اللاحقة الحقول المتداخلة داخله. ينطبق نفس اصطلاح الفهرسة على `ColumnFields`.

يهم ترتيب تداخل الحقول. تؤدي إضافة `Category` إلى منطقة الصفوف أولاً ثم `Item` إلى إنتاج جدول محوري يكون فيه التجميع الخارجي `Category` والتجميع الداخلي `Item`. يؤدي عكس الترتيب إلى عكس التسلسل الهرمي.

## **المجاميع الفرعية لحقول الجدول المحوري**

تقوم طريقة `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` بالتحكم في صفوف المجاميع الفرعية التي تظهر لحقل الجدول المحوري. يقوم كل استدعاء بتبديل نوع مجموع فرعي واحد بشكل مستقل. يعرض تمرير `shown = true` المجموع الفرعي، بينما يُخفيه `shown = false`. نظرًا لأن كل استدعاء يؤثر فقط على نوع واحد، فإن استدعاء الطريقة عدة مرات بقيم `subtotalType` مختلفة يُنشئ مجموعة فرعية مخصصة من المجاميع الفرعية.

يُعرّف التعداد `PivotFieldSubtotalType` أنواع المجاميع الفرعية المتاحة.

- `AUTOMATIC` — يختار Aspose.Cells التحديد الافتراضي (عادةً `SUM` للحقول الرقمية)
- `NONE` — إلغاء كل صف من صفوف المجاميع الفرعية
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
لا تظهر المجاميع الفرعية إلا عند وجود حقلين أو أكثر من حقول الجدول المحوري في منطقة الصفوف (أو في منطقة الأعمدة). الحقل الواحد ليس لديه ما يمكن حساب مجموع فرعي له بينه، لذا فإن استدعاءات `setSubtotals` ليس لها تأثير مرئي في هذه الحالة. لذلك يضع هذا المقال حقلين للصفوف (`Category` خارجي، `Item` داخلي) في كل مثال بحيث يكون الحد الفاصل للمجموع الفرعي بين كل مجموعة `Category` مرئيًا.
{{% /alert %}}

## **السيناريو 1 — المجاميع الفرعية التلقائية (الافتراضية)**

عندما لا تستدعي `setSubtotals` على الإطلاق، يطبق Aspose.Cells تحديد `AUTOMATIC` على الحقول الرقمية. يؤكد المثال التالي صراحةً هذا السلوك من خلال استدعاء `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` على حقل الصف الخارجي `Category`.

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

## **السيناريو 2 — إلغاء جميع المجاميع الفرعية (لا شيء)**

يؤدي استدعاء `setSubtotals(PivotFieldSubtotalType.NONE, true)` إلى إزالة كل صف من صفوف المجاميع الفرعية من الجدول المحوري، تاركًا فقط صفوف الحقول والإجمالي الكلي في الأسفل. يكون هذا مفيدًا عندما تريد البيانات المجمعة الخام دون أي صفوف ملخص.

```javascript
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

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **السيناريو 3 — مجموعة فرعية مخصصة من المجاميع الفرعية (المجموع + المتوسط)**

لست مقيدًا بنوع مجموع فرعي واحد. يعمل كل استدعاء لـ `setSubtotals` بشكل مستقل على نوع واحد، لذا فإن استدعاء الطريقة مرتين — مرة بـ `SUM` ومرة بـ `AVERAGE` — ينتج مجموعة فرعية مخصصة من صفين للمجاميع الفرعية لكل مجموعة `Category`.

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

تتشارك السيناريوهات الثلاثة أعلاه في نفس مجموعة البيانات وهيكل الجدول المحوري. الفرق الوحيد بينها هو استدعاء `setSubtotals` المطبق على حقل الصف الخارجي `Category`. تذكر قاعدة الحقلين: الحقل الواحد في المنطقة ليس لديه ما يمكن حساب مجموع فرعي له بينه، لذا ضع دائمًا حقلين على الأقل في منطقة الصفوف أو الأعمدة عندما تريد أن يكون لـ `setSubtotals` تأثير مرئي.
{{< app/cells/assistant language="nodejs-java" >}}
