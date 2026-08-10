---
title: حقول القيم في Aspose.Cells for Node.js via Java
linktitle: حقول القيم في Aspose.Cells for Node.js via Java
description: تعلم كيفية إضافة الحقول الأساسية إلى منطقة البيانات في الجدول المحوري، وتغيير دالة التلخيص باستخدام PivotField.Function، ورسم حقل القيمة على محور الصف أو العمود في Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Node.js via Java, جدول محوري, حقل القيمة, PivotField, PivotField.Function, حقل البيانات, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ar/nodejs-java/manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

حقول القيم هي جوهر كل جدول محوري، فهي التجمعات العددية التي تلخص بيانات المصدر. في Aspose.Cells for Node.js via Java، يتم ملء منطقة البيانات في الجدول المحوري بإضافة الحقول الأساسية إليها عبر `PivotTable.addFieldToArea`، ويمكن لكل حقل موضوع في تلك المنطقة أن تكون له دالة التلخيص الخاصة به. عند وجود حقلين أو أكثر من حقول البيانات، يتيح Aspose.Cells الوصول إلى حقل تجميعي خاص وهو `PivotTable.getValuesField()`، يمكن رسمه على محور الصف أو العمود كحقل أساسي، مما يمنحك تحكمًا أدق في كيفية ظهور حقول القيم في التخطيط.
## إضافة حقل إلى منطقة البيانات
تُعد إضافة حقل أساسي إلى منطقة البيانات (القيم) الخطوة الأولى في تشكيل كيفية تجميع الجدول المحوري لبيانات المصدر. يُتيح Aspose.Cells الوصول إلى `PivotTable.addFieldToArea(PivotFieldType, string)`، وهي دالة محملة بشكل زائد تقبل الثابت `PivotFieldType.DATA` واسم عمود المصدر. بمجرد إضافة حقل إلى منطقة البيانات، تعرضه API من خلال مجموعة `PivotTable.getDataFields()`، بالترتيب الذي أُضيفت به الحقول. افتراضيًا، يتم تلخيص عمود المصدر الرقمي باستخدام `ConsolidationFunction.SUM`، بينما يكون العمود غير الرقمي افتراضيًا `COUNT`.

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

## تغيير دالة التلخيص
يتم تغليف كل حقل موضوع في منطقة البيانات داخليًا كنسخة من `PivotField`، وترجع الخاصية `getFunction()` الخاصة به قيمة من تعداد `ConsolidationFunction`. تتيح لك دالة setter نفسها `setFunction()` التبديل بين التجمعات المتاحة، بما في ذلك `SUM` و`COUNT` و`AVERAGE` و`MAX` و`MIN` و`PRODUCT` و`STD_DEV` و`STD_DEVP` و`VAR` و`VARP`.
{{% alert color="primary" %}}
تغيير `Function` يؤثر فقط على التجميع، ولا يتغير عمود المصدر.
{{% /alert %}}
لذلك يمكنك ترك حقل بيانات واحد كـ `SUM` بينما تضيف حقل بيانات ثانٍ يستهدف عمود المصدر نفسه ولكنه يستخدم `COUNT` أو `AVERAGE`، كل ذلك في جدول محوري واحد.

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

## رسم حقول القيم على محور الصف أو العمود
عندما يحتوي الجدول المحوري على حقلين أو أكثر من حقول البيانات، يتيح Aspose.Cells الوصول إلى حقل افتراضي إضافي يُسمى `PivotTable.getValuesField()`. يمثل هذا الحقل الافتراضي تجميع كل حقل بيانات موجود في منطقة البيانات. يمكنك سحبه إلى منطقة الصف أو العمود كحقل محوري أساسي، وهو أمر مفيد لتخطيط مقاييس متعددة جنبًا إلى جنب.
{{% alert color="primary" %}}
`PivotTable.getValuesField()` لا يعمل إذا لم يكن هناك حقل قيمة أو كان هناك حقل قيمة واحد فقط.
{{% /alert %}}
تمضي السيناريوهات أدناه في ثلاثة أمثلة شاملة تُظهر كل قدرة موصوفة أعلاه على نفس بنية الجدول المحوري.

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

{{< app/cells/assistant language="javascript" >}}