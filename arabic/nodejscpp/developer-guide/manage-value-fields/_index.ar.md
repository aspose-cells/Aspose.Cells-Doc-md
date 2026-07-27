---
title: حقول القيم في Aspose.Cells for Node.js via C++
linktitle: حقول القيم في Aspose.Cells for Node.js via C++
description: تعرّف على كيفية إضافة الحقول الأساسية إلى منطقة البيانات في الجدول المحوري، وتغيير دالة التلخيص باستخدام PivotField.Function، وعرض حقل القيمة على محور الصفوف أو الأعمدة في Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Node.js, C++, جدول محوري, حقل قيمة, PivotField, PivotField.Function, حقل بيانات, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ar/nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

حقول القيم هي جوهر كل جدول محوري، فهي التجمّعات العددية التي تلخّص بيانات المصدر. في Aspose.Cells for Node.js via C++، تُملأ منطقة البيانات في الجدول المحوري بإضافة الحقول الأساسية إليها عبر `PivotTable.addFieldToArea`، ويمكن أن يكون لكل حقل موضوع في تلك المنطقة دالة تلخيص خاصة به. عندما يوجد حقلا بيانات أو أكثر، يوفّر Aspose.Cells حقلاً تجميعيًا خاصًا، وهو `PivotTable.ValuesField`، يمكن عرضه على محور الصفوف أو الأعمدة كحقل أساسي، مما يمنحك تحكمًا أدق في كيفية ظهور حقول القيم في التخطيط.

## إضافة حقل إلى منطقة البيانات

تُعد إضافة حقل أساسي إلى منطقة البيانات (القيم) الخطوة الأولى في تشكيل كيفية تجميع الجدول المحوري لبيانات المصدر. يوفّر Aspose.Cells overload الدالة `PivotTable.addFieldToArea(PivotFieldType, string)` التي تقبل الثابت `PivotFieldType.Data` واسم عمود المصدر. بمجرد إضافة حقل إلى منطقة البيانات، يعرضه الـ API من خلال مجموعة `PivotTable.DataFields`، بالترتيب الذي أُضيفت به الحقول. افتراضيًا، يتم تلخيص عمود رقمي في المصدر باستخدام `ConsolidationFunction.Sum`، بينما يكون العمود غير الرقمي افتراضيًا على `Count`.

## تغيير دالة التلخيص

كل حقل موضوع في منطقة البيانات يُغلّف داخليًا كمثيل `PivotField`، وتُرجع خاصية `Function` الخاصة به قيمة من تعداد `ConsolidationFunction`. تتيح لك أداة الإعداد `Function` ذاتها التبديل بين التجمّعات المتاحة، بما في ذلك `Sum`، و`Count`، و`Average`، و`Max`، و`Min`، و`Product`، و`StdDev`، و`StdDevp`، و`Var`، و`Varp`.

{{% alert color="primary" %}}
تؤثر تغييرات `Function` على التجمّع فقط، ولا يتغير عمود المصدر.
{{% /alert %}}

يمكنك بالتالي ترك حقل بيانات واحد كـ `Sum` بينما تُضيف حقل بيانات ثانٍ يستهدف عمود المصدر ذاته لكنه يستخدم `Count` أو `Average`، وذلك جميعه في جدول محوري واحد.

## عرض حقول القيم على محور الصفوف أو الأعمدة

عندما يحتوي الجدول المحوري على حقلَي بيانات أو أكثر، يعرض Aspose.Cells حقلًا افتراضيًا إضافيًا يُسمى `PivotTable.ValuesField`. يمثّل هذا الحقل الافتراضي تجمّع كل حقل بيانات موجود في منطقة البيانات. يمكنك سحبه إلى منطقة الصفوف أو الأعمدة كحقل محوري أساسي، وهو أمر مفيد لتخطيط مقاييس متعددة جنبًا إلى جنب.

{{% alert color="primary" %}}
لا يعمل `PivotTable.ValuesField` في حال عدم وجود حقل قيمة أو وجود حقل واحد فقط.
{{% /alert %}}

تستعرض السيناريوهات أدناه ثلاثة أمثلة شاملة توضح كل ميزة من الميزات الموصوفة أعلاه على نفس بنية الجدول المحوري.

## السيناريو 1 — سحب حقل أساسي إلى منطقة القيم

يوضّح هذا السيناريو كيفية وضع حقل أساسي واحد (`Amount`) في منطقة البيانات لجدول محوري موجود. تضع بنية الجدول المحوري المشتركة `Category` و`Item` على محور الصفوف، و`Year` على محور الأعمدة. بعد العملية، يظهر `Amount` في منطقة البيانات ويُحسب كـ `Sum` لـ `Amount` افتراضيًا.

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

// صفوف البيانات A2:D9 باستخدام حلقات متداخلة تتفرع على j
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

// إضافة جدول محوري في F3 باسم PivotTable1
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// تخطيط الجدول المحوري: الفئة والعنصر في الصف، والسنة في العمود، والمبلغ كحقل بيانات
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## السيناريو 2 — تغيير دالة التلخيص

يبدأ هذا السيناريو من نفس بنية الجدول المحوري في السيناريو 1، لكنه يُضيف حقل `Amount` إلى منطقة البيانات مرتين. يشير حقلَا البيانات إلى عمود المصدر ذاته، ومع ذلك يتم تجاوز الحقل الثاني باستخدام أداة الإعداد `PivotField.Function` ليصبح `Count` بدلًا من القيمة الافتراضية `Sum`.

<!-- CODE_BLOCK:1:Build a complete end-to-end sample that starts with a require statement to load the Aspose.Cells Node.js module, then creates a Workbook instance, calls workbook.getWorksheets().get(0) to obtain the first worksheet, assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual worksheet.getCells().get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.Data, "Amount") twice so that pivotTable.getDataFields().getCount() equals 2. Retrieve the second data field via pivotTable.getDataFields().get(1) and assign countField.setFunction(ConsolidationFunction.Count) to change its summary function from the default Sum to Count; the first data field remains Sum of Amount. Demonstrate that the Function setter can also be assigned ConsolidationFunction.Average, Max, Min, etc. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_function.xlsx"). -->

## السيناريو 3 — عرض حقول القيم على محور الصفوف أو الأعمدة

مع وجود حقلَي بيانات في مكانهما، يصبح `PivotTable.ValuesField` قابلًا للاستخدام. يسحب هذا السيناريو حقل التجميع الافتراضي هذا إلى منطقة الأعمدة بحيث يظهر كل مقياس في منطقة البيانات ككتلة عمود خاصة به بجانب `Year`.

<!-- CODE_BLOCK:2:Build a complete end-to-end sample that starts with a require statement to load the Aspose.Cells Node.js module, then creates a Workbook instance, calls workbook.getWorksheets().get(0) to obtain the first worksheet, assigns worksheet.setName("Data"), and writes the same 4-column 9-row dataset (Category, Item, Year, Amount) using individual worksheet.getCells().get(i, j).putValue(...) calls for each cell, iterating row index i from 1 to 8 inclusive and column index j from 0 to 3 in nested loops, branching on j to pick the correct value, so A1:D1 contains the headers and A2:D9 contains the eight data rows. Add a pivot table by calling worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1"), place "Category" and "Item" on Row, place "Year" on Column, then call pivotTable.addFieldToArea(PivotFieldType.Data, "Amount") twice. Assign pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.Count) so the second data field becomes Count while the first remains Sum. Finally call pivotTable.addFieldToArea(PivotFieldType.Column, pivotTable.getValuesField().getName()) to plot the value fields onto the Column axis. Call pivotTable.refreshData() and pivotTable.calculateData() and save the workbook with workbook.save("output_plot.xlsx"). The final layout has Row region (Category, Item), Column region (Year + ValuesField), and Data region (Sum-of-Amount, Count-of-Amount). -->

تغطي هذه السيناريوهات الثلاثة مجتمعةً كل جانب من جوانب معالجة حقول القيم في Aspose.Cells for Node.js via C++، بدءًا من حقل بيانات واحد بالقيمة الافتراضية `Sum` وصولًا إلى جدول محوري متعدد المقاييس يتحكم فيه الحقل الافتراضي `ValuesField` في التخطيط على محور الصفوف أو الأعمدة.

## مقالات ذات صلة

- [حقول الصفوف والأعمدة في الجدول المحوري في Aspose.Cells for Node.js via C++](/cells/ar/nodejs-cpp/row-and-column-fields/)
- [حقول الصفحات في الجداول المحورية](/cells/ar/nodejs-cpp/add-page-field-in-pivot-table/)
- [تحديث الجداول المحورية في Aspose.Cells for Node.js via C++](/cells/ar/nodejs-cpp/refresh-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية](/cells/ar/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript" >}}