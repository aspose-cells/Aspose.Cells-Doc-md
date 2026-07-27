---
title: إدارة حقول القيم في الجدول المحوري في Aspose.Cells لـ .NET
linktitle: حقول القيم
description: تعلم كيفية إضافة الحقول الأساسية إلى منطقة البيانات في الجدول المحوري، وتغيير دالة التلخيص باستخدام PivotField.Function، ورسم حقل القيمة على محور الصفوف أو الأعمدة في Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Node.js via C++, جدول محوري, حقل قيمة, PivotField, PivotField.Function, حقل بيانات, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ar/nodejs-cpp/pivot-table-manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## إضافة حقل إلى منطقة البيانات
تُعد إضافة حقل أساسي إلى منطقة البيانات (القيم) هي الخطوة الأولى في تشكيل كيفية تجميع الجدول المحوري لبيانات المصدر. يعرض Aspose.Cells الطريقة `PivotTable.addFieldToArea(PivotFieldType, string)`، وهي نسخة محمّلة تقبل الثابت `PivotFieldType.Data` واسم عمود المصدر. بمجرد إضافة حقل إلى منطقة البيانات، تكشفه الواجهة البرمجية من خلال مجموعة `PivotTable.getDataFields()`، بالترتيب الذي تمت به إضافة الحقول. افتراضيًا، يتم تلخيص عمود رقمي في المصدر باستخدام `ConsolidationFunction.Sum`، بينما يكون العمود غير الرقمي افتراضيًا على `Count`.
## تغيير دالة التلخيص
يتم تغليف كل حقل يوضع في منطقة البيانات داخليًا كمثيل من `PivotField`، وتُرجع خاصية `getFunction()` الخاصة به قيمة من تعداد `ConsolidationFunction`. تتيح لك أداة الإعداد `setFunction()` نفسها التبديل بين التجميعات المتاحة، بما في ذلك `Sum` و`Count` و`Average` و`Max` و`Min` و`Product` و`StdDev` و`StdDevp` و`Var` و`Varp`.
{{% alert color="primary" %}}
لا يؤثر تغيير دالة التلخيص إلا على التجميع، بينما يظل عمود المصدر دون تغيير.
{{% /alert %}}
يمكنك بالتالي ترك حقل بيانات واحد على `Sum` بينما تضيف حقل بيانات ثانٍ يستهدف نفس عمود المصدر لكنه يستخدم `Count` أو `Average`، كل ذلك في جدول محوري واحد.
## رسم حقول القيم على محور الصفوف أو الأعمدة
عندما يحتوي الجدول المحوري على حقلَي بيانات أو أكثر، يعرض Aspose.Cells حقلًا افتراضيًا إضافيًا يُسمى `PivotTable.getValuesField`. يمثل هذا الحقل الافتراضي تجميع كل حقل بيانات موجود في منطقة البيانات. يمكنك سحبه إلى منطقة الصفوف أو الأعمدة باعتباره حقل محوري أساسي، وهو أمر مفيد لعرض مقاييس متعددة جنبًا إلى جنب.
{{% alert color="primary" %}}
لا تعمل `PivotTable.getValuesField()` في حالة عدم وجود حقل قيمة أو وجود حقل واحد فقط.
{{% /alert %}}
تستعرض السيناريوهات أدناه ثلاثة أمثلة شاملة من البداية إلى النهاية توضح كل قدرة موصوفة أعلاه على نفس بنية الجدول المحوري.
## السيناريو 1 — سحب حقل أساسي إلى منطقة القيم
يوضح هذا السيناريو كيفية وضع حقل أساسي واحد (`Amount`) في منطقة البيانات لجدول محوري موجود. تضع بنية الجدول المحوري المشتركة `Category` و`Item` على محور الصفوف و`Year` على محور الأعمدة. بعد العملية، يظهر `Amount` في منطقة البيانات ويُحسب باعتباره `Sum` لـ `Amount` افتراضيًا.
```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// العناوين في A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// صفوف البيانات من A2 إلى D9 باستخدام حلقات متداخلة تتفرع على j
for (let i = 1; i <= 8; i++) {
 for (let j = 0; j < 4; j++) {
 switch (j) {
 case 0:
 worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i === 1 || i === 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i === 3 || i === 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i === 5 || i === 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i === 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i === 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i === 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i === 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i === 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i === 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i === 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// أضف جدولاً محورياً في F3 بالاسم PivotTable1
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// تخطيط الجدول المحوري: الفئة والعنصر في الصف، والسنة في العمود، والمبلغ كحقل بيانات
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```
## السيناريو 2 — تغيير دالة التلخيص
يبدأ هذا السيناريو من نفس بنية الجدول المحوري كما في السيناريو 1، لكنه يضيف حقل `Amount` إلى منطقة البيانات مرتين. يشير كلا حقلي البيانات إلى نفس عمود المصدر، ومع ذلك يتم تجاوز الحقل الثاني باستخدام أداة الإعداد `setFunction()` بحيث يصبح `Count` بدلاً من `Sum` الافتراضي.
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

for (let i = 1; i <= 8; i++)
{
 for (let j = 0; j <= 3; j++)
 {
 if (j == 0)
 {
 worksheet.getCells().get(i, j).putValue(i <= 5 ? "Fruit" : "Vegetable");
 }
 else if (j == 1)
 {
 let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
 worksheet.getCells().get(i, j).putValue(items[i - 1]);
 }
 else if (j == 2)
 {
 let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
 worksheet.getCells().get(i, j).putValue(years[i - 1]);
 }
 else
 {
 let amounts = [100, 150, 80, 90, 50, 60, 40, 45];
 worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
 }
 }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let countField = pivotTable.getDataFields().get(1);
countField.setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.calculateData();

workbook.save("output_function.xlsx");
```
## السيناريو 3 — رسم حقول القيم على محور الصفوف أو الأعمدة
مع وجود حقلَي بيانات في مكانهما، تصبح `PivotTable.getValuesField()` قابلة للاستخدام. يسحب هذا السيناريو حقل التجميع الافتراضي هذا إلى منطقة الأعمدة بحيث يظهر كل مقياس في منطقة البيانات ككتلة عمود خاصة به بجوار `Year`.
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

let categories = ["Fruit", "Fruit", "Fruit", "Fruit", "Vegetable", "Vegetable", "Vegetable", "Vegetable"];
let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
let amounts = [100, 150, 80, 90, 50, 60, 40, 45];

for (let i = 1; i <= 8; i++)
{
 for (let j = 0; j <= 3; j++)
 {
 if (j == 0) worksheet.getCells().get(i, j).putValue(categories[i - 1]);
 else if (j == 1) worksheet.getCells().get(i, j).putValue(items[i - 1]);
 else if (j == 2) worksheet.getCells().get(i, j).putValue(years[i - 1]);
 else worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
 }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, pivotTable.getValuesField().getName());

pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```
معًا، تغطي هذه السيناريوهات الثلاثة كل جانب من جوانب معالجة حقل القيم في Aspose.Cells for Node.js via C++، بدءًا من حقل بيانات واحد بالقيمة الافتراضية `Sum` وصولاً إلى جدول محوري متعدد المقاييس يتحكم فيه حقل `ValuesField` الافتراضي في التخطيط على محور الصفوف أو الأعمدة.
## مقالات ذات صلة
- [Pivot Table Row and Column Fields in Aspose.Cells for Node.js via C++](/cells/ar/nodejs-cpp/row-and-column-fields/)
- [Page Fields in Pivot Tables](/cells/ar/nodejs-cpp/add-page-field-in-pivot-table/)
- [Refreshing Pivot Tables in Aspose.Cells for Node.js via C++](/cells/ar/nodejs-cpp/refresh-pivot-table/)
- [Applying Styles to Pivot Tables](/cells/ar/nodejs-cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="javascript" >}}
