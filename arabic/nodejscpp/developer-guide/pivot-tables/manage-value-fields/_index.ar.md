---
title: إدارة حقول القيم في الجدول المحوري في Aspose.Cells لـ .NET
description: تعلم كيفية إضافة الحقول الأساسية إلى منطقة البيانات في الجدول المحوري، وتغيير دالة التلخيص باستخدام PivotField.Function، ورسم حقل القيمة على محور الصفوف أو الأعمدة في Aspose.Cells for Node.js via C++.
linktitle: حقول القيم
keywords: Aspose.Cells, Node.js via C++, جدول محوري, حقل قيمة, PivotField, PivotField.Function, حقل بيانات, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ar/nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## إضافة حقل إلى منطقة البيانات
تُعد إضافة حقل أساسي إلى منطقة البيانات (القيم) هي الخطوة الأولى في تشكيل كيفية تجميع الجدول المحوري لبيانات المصدر. يعرض Aspose.Cells الطريقة `PivotTable.addFieldToArea(PivotFieldType, string)`، وهي نسخة محمّلة تقبل الثابت `PivotFieldType.Data` واسم عمود المصدر. بمجرد إضافة حقل إلى منطقة البيانات، تكشفه الواجهة البرمجية من خلال مجموعة `PivotTable.getDataFields()`، بالترتيب الذي تمت به إضافة الحقول. افتراضيًا، يتم تلخيص عمود رقمي في المصدر باستخدام `ConsolidationFunction.Sum`، بينما يكون العمود غير الرقمي افتراضيًا على `Count`.

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
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, pivotTable.getValuesField());
pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```

## تغيير دالة التلخيص
يتم تغليف كل حقل يوضع في منطقة البيانات داخليًا كمثيل من `PivotField`، وتُرجع خاصية `getFunction()` الخاصة به قيمة من تعداد `ConsolidationFunction`. تتيح لك أداة الإعداد `setFunction()` نفسها التبديل بين التجميعات المتاحة، بما في ذلك `Sum` و`Count` و`Average` و`Max` و`Min` و`Product` و`StdDev` و`StdDevp` و`Var` و`Varp`.

{{% alert color="primary" %}}
لا يؤثر تغيير دالة التلخيص إلا على التجميع، بينما يظل عمود المصدر دون تغيير.
{{% /alert %}}

يمكنك بالتالي ترك حقل بيانات واحد على `Sum` بينما تضيف حقل بيانات ثانٍ يستهدف نفس عمود المصدر لكنه يستخدم `Count` أو `Average`، كل ذلك في جدول محوري واحد.

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
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.getDataFields().get(1).setFunction(AsposeCells.ConsolidationFunction.Count);
pivotTable.calculateData();
workbook.save("output_function.xlsx");
```

## رسم حقول القيم على محور الصفوف أو الأعمدة
عندما يحتوي الجدول المحوري على حقلَي بيانات أو أكثر، يعرض Aspose.Cells حقلًا افتراضيًا إضافيًا يُسمى `PivotTable.getValuesField`. يمثل هذا الحقل الافتراضي تجميع كل حقل بيانات موجود في منطقة البيانات. يمكنك سحبه إلى منطقة الصفوف أو الأعمدة باعتباره حقل محوري أساسي، وهو أمر مفيد لعرض مقاييس متعددة جنبًا إلى جنب.

{{% alert color="primary" %}}
لا تعمل `PivotTable.getValuesField()` في حالة عدم وجود حقل قيمة أو وجود حقل واحد فقط.
{{% /alert %}}

تستعرض السيناريوهات أدناه ثلاثة أمثلة شاملة من البداية إلى النهاية توضح كل قدرة موصوفة أعلاه على نفس بنية الجدول المحوري.

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
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45]
];
for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}