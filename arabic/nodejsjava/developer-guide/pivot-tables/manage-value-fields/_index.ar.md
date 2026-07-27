---
title: إدارة حقول القيم في الجدول المحوري في Aspose.Cells لـ .NET
linktitle: حقول القيم
description: تعلّم كيفية إضافة حقول أساسية إلى منطقة البيانات في الجدول المحوري، وتغيير دالة التلخيص باستخدام PivotField.Function، ورسم حقل القيم على محور الصفوف أو الأعمدة في Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Node.js via Java, جدول محوري, حقل القيم, PivotField, PivotField.Function, حقل البيانات, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ar/nodejs-java/pivot-table-manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## إضافة حقل إلى منطقة البيانات
تُعدّ إضافة حقل أساسي إلى منطقة البيانات (القيم) الخطوة الأولى في تشكيل كيفية تجميع الجدول المحوري لبياناتك المصدرية. يُوفّر Aspose.Cells حمولة زائدة للدالة `PivotTable.addFieldToArea(PivotFieldType, string)` تقبل الثابت `PivotFieldType.DATA` واسم عمود المصدر. بمجرد إضافة حقل إلى منطقة البيانات، تتيح لك الواجهة البرمجية الوصول إليه من خلال مجموعة `PivotTable.getDataFields()`، بالترتيب الذي أُضيفت به الحقول. افتراضيًا، يتم تلخيص عمود المصدر الرقمي باستخدام `ConsolidationFunction.SUM`، بينما يكون العمود غير الرقمي افتراضيًا `COUNT`.
## تغيير دالة التلخيص
يتم تغليف كل حقل يُوضع في منطقة البيانات داخليًا كنسخة من `PivotField`، وتُرجع خاصية `getFunction()` الخاصة به قيمة من تعداد `ConsolidationFunction`. تتيح لك دالة الإعداد `setFunction()` نفسها التبديل بين التجمّعات المتاحة، بما في ذلك `SUM`، و`COUNT`، و`AVERAGE`، و`MAX`، و`MIN`، و`PRODUCT`، و`STD_DEV`، و`STD_DEVP`، و`VAR`، و`VARP`.
{{% alert color="primary" %}}
تؤثر تغييرات `Function` على التجميع فقط، ولا يتغير عمود المصدر.
{{% alert %}}
لذا يمكنك ترك حقل بيانات واحد كـ `SUM` بينما تُضيف حقل بيانات ثانٍ يستهدف عمود المصدر نفسه ولكنه يستخدم `COUNT` أو `AVERAGE`، كل ذلك في جدول محوري واحد.
## رسم حقول القيم على محور الصفوف أو الأعمدة
عندما يحتوي الجدول المحوري على حقلَي بيانات أو أكثر، يعرض Aspose.Cells حقلًا افتراضيًا إضافيًا يُسمى `PivotTable.getValuesField()`. يمثّل هذا الحقل الافتراضي تجميع كل حقل بيانات موجود في منطقة البيانات. يمكنك سحبه إلى منطقة الصفوف أو الأعمدة كحقل محوري أساسي، وهو أمر مفيد لترتيب مقاييس متعددة جنبًا إلى جنب.
{{% alert color="primary" %}}
لا يعمل `PivotTable.getValuesField()` إذا لم يكن هناك حقل قيم أو إذا كان هناك حقل قيم واحد فقط.
{{% alert %}}
تستعرض السيناريوهات أدناه ثلاثة أمثلة شاملة تُوضّح كل قدرة موصوفة أعلاه على نفس بنية الجدول المحوري.
## السيناريو 1 — سحب حقل أساسي إلى منطقة القيم
يُوضّح هذا السيناريو كيفية وضع حقل أساسي واحد (`Amount`) في منطقة البيانات لجدول محوري موجود. تضع بنية الجدول المحوري المشتركة `Category` و`Item` على محور الصفوف، و`Year` على محور الأعمدة. بعد العملية، يظهر `Amount` في منطقة البيانات ويُحسب كـ `Sum` لـ `Amount` افتراضيًا.
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// العناوين في A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// صفوف البيانات A2:D9 باستخدام حلقات متداخلة مع التفريع على j
for (let i = 1; i <= 8; i++) {
 for (let j = 0; j < 4; j++) {
 switch (j) {
 case 0:
 worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i == 3 || i == 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i == 5 || i == 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i == 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i == 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i == 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i == 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i == 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i == 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// إضافة جدول محوري عند F3 بالاسم PivotTable1
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// تخطيط الجدول المحوري: Category و Item في الصف، Year في العمود، Amount كحقل بيانات
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```
## السيناريو 2 — تغيير دالة التلخيص
يبدأ هذا السيناريو من نفس بنية الجدول المحوري مثل السيناريو 1 ولكنه يُضيف حقل `Amount` إلى منطقة البيانات مرتين. يشير كلا حقلَي البيانات إلى نفس عمود المصدر، ومع ذلك فإن الحقل الثاني يتم تجاوزه باستخدام دالة الإعداد `PivotField.setFunction()` ليصبح `COUNT` بدلاً من `SUM` الافتراضي.
## السيناريو 3 — رسم حقول القيم على محور الصفوف أو الأعمدة
مع وجود حقلَي بيانات في مكانهما، يصبح `PivotTable.getValuesField()` قابلاً للاستخدام. يسحب هذا السيناريو حقل التجميع الافتراضي هذا إلى منطقة الأعمدة بحيث يظهر كل مقياس في منطقة البيانات كمجموعة أعمدة خاصة به بجانب `Year`.
معًا، تغطي هذه السيناريوهات الثلاثة كل جانب من جوانب معالجة حقول القيم في Aspose.Cells for Node.js via Java، من حقل بيانات واحد بالـ `SUM` الافتراضي إلى جدول محوري متعدد المقاييس يتحكم فيه حقل `ValuesField` الافتراضي في التخطيط على محور الصفوف أو الأعمدة.
## مقالات ذات صلة
- [حقول الصفوف والأعمدة في الجدول المحوري في Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/row-and-column-fields/)
- [حقول الصفحات في الجداول المحورية](/cells/ar/nodejs-java/add-page-field-in-pivot-table/)
- [تحديث الجداول المحورية في Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/refresh-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية](/cells/ar/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript" >}}
