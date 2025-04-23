---
title: كيفية إنشاء رسم بياني ديناميكي باستخدام القائمة المنسدلة باستخدام Node.js عبر C++
linktitle: كيفية إنشاء رسم بياني ديناميكي مع قائمة منسدلة
description: تعلم كيفية إنشاء رسم بياني ديناميكي يتحدث استنادًا إلى اختيار من القائمة المنسدلة باستخدام Aspose.Cells for Node.js via C++. سيُوضح دليلنا خطوة بخطوة كيفية دمج قائمة منسدلة في الرسم البياني الخاص بك لتصور البيانات بشكل مرن.
keywords: Aspose.Cells for Node.js via C++، الرسم البياني الديناميكي، القائمة المنسدلة، تصور البيانات، الدمج، التصور المرن.
type: docs
weight: 76
url: /ar/nodejs-cpp/create-dynamic-chart-with-dropdownlist/
---

## **سيناريوهات الاستخدام المحتملة**
رسم بياني ديناميكي مع قائمة منسدلة في إكسل هو أداة قوية تتيح للمستخدمين إنشاء رسوم بيانية تفاعلية يمكن تحديثها بناءً على البيانات المحددة. تكون هذه الميزة مفيدة بشكل خاص في الحالات التي تحتاج فيها إلى تحليل مجموعات بيانات متعددة أو مقارنة سيناريوات مختلفة.

تطبيق شائع آخر لرسم بياني ديناميكي بقائمة منسدلة في التحليل المالي. على سبيل المثال ، قد تحتوي شركة على مجموعات متعددة من البيانات المالية لسنوات أو أقسام مختلفة. من خلال استخدام قائمة منسدلة ، يمكن للمستخدمين تحديد مجموعة البيانات المحددة التي يرغبون في تحليلها ، وسيتم تحديث الرسم البياني تلقائيًا لعرض المعلومات المقابلة. يُسمح بذلك بسهولة المقارنة والتعرف على الاتجاهات أو الأنماط.

تطبيق آخر هو في المبيعات والتسويق. قد تحتوي شركة على بيانات مبيعات لمنتجات أو مناطق مختلفة. باستخدام رسم بياني ديناميكي مع قائمة منسدلة ، يمكن للمستخدمين اختيار منتج محدد أو منطقة من القائمة المنسدلة ، وسيتم تحديث الرسم البياني بشكل ديناميكي لعرض أداء المبيعات للاختيار المحدد. يساعد ذلك في تحديد المناطق أو المنتجات الأكثر أداءً واتخاذ قرارات تستند إلى البيانات.

باختصار ، يوفر رسم بياني ديناميكي مع قائمة منسدلة في إكسل وسيلة مرنة وتفاعلية لتصور وتحليل البيانات. إنه قيم في الحالات التي تحتاج فيها إلى مقارنة مجموعات بيانات متعددة أو استكشاف سيناريوات مختلفة ، مما يجعله أداة متعددة الاستخدامات للتحليل المالي والمبيعات والتسويق والعديد من التطبيقات الأخرى.

## **استخدم Aspose Cells لإنشاء رسم بياني ديناميكي مع قائمة منسدلة**
في الفقرات التالية، سنوضح لك كيفية إنشاء رسم بياني ديناميكي باستخدام القائمة المنسدلة باستخدام Aspose.Cells for Node.js via C++. سنعرض لك رمز المثال، بالإضافة إلى ملف Excel الذي تم إنشاؤه باستخدام هذا الرمز.

## **الكود المثالي**
سيقوم الكود العيني التالي بتوليد [ملف رسم بياني ديناميكي مع قائمة منسدلة](DynamicChartWithDropdownlist.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A3").putValue("Tea");
sheet.getCells().get("A4").putValue("Coffee");
sheet.getCells().get("A5").putValue("Sugar");

// In this example, we will add 12 months of data
sheet.getCells().get("B2").putValue("Jan");
sheet.getCells().get("C2").putValue("Feb");
sheet.getCells().get("D2").putValue("Mar");
sheet.getCells().get("E2").putValue("Apr");
sheet.getCells().get("F2").putValue("May");
sheet.getCells().get("G2").putValue("Jun");
sheet.getCells().get("H2").putValue("Jul");
sheet.getCells().get("I2").putValue("Aug");
sheet.getCells().get("J2").putValue("Sep");
sheet.getCells().get("K2").putValue("Oct");
sheet.getCells().get("L2").putValue("Nov");
sheet.getCells().get("M2").putValue("Dec");
const allMonths = 12;
const iCount = 3;
for (let i = 0; i < iCount; i++) {
for (let j = 0; j < allMonths; j++) {
const _row = i + 2;
const _column = j + 1; 
sheet.getCells().get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
}
}

// This is the Dropdownlist for Dynamic Data
const ca = AsposeCells.CellArea.createCellArea(9, 0, 9, 0);
const _index = sheet.getValidations().add(ca);
const _va = sheet.getValidations().get(_index);
_va.setType(AsposeCells.ValidationType.List);
_va.setInCellDropDown(true);
_va.setFormula1("=$B$2:$M$2");
sheet.getCells().get("A9").putValue("Current Month");
sheet.getCells().get("A10").putValue("Jan");
const _style = sheet.getCells().get("A10").getStyle();
_style.getFont().setIsBold(true);
_style.setPattern(AsposeCells.BackgroundType.Solid);
_style.setForegroundColor(AsposeCells.Color.Yellow);
sheet.getCells().get("A10").setStyle(_style);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtMonthData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtXLabels");
sheets.getNames().get(index).setRefersTo("=Sheet1!$A$3:$A$5");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 8, 2, 20, 8);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("month", true);
chart.getNSeries().get(0).setName("=Sheet1!$A$10");
chart.getNSeries().get(0).setValues("Sheet1!ChtMonthData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtXLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicChartWithDropdownlist.xlsx"));
```

## **ملاحظات**
في الملف الذي تم إنشاؤه، سيقوم الرسم البياني بحساب البيانات ديناميكيًا بالنسبة للشهر المحدد. يتم ذلك باستخدام صيغة "OFFSET" في الكود العيني:

```
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

يمكنك محاولة تغيير قيمة القائمة المنسدلة في الخلية "Sheet1!$A$10"، وسوف ترى التغيير الديناميكي في الرسم البياني. الآن لقد قمنا بإنشاء رسم بياني ديناميكي مع قائمة منسدلة باستخدام Aspose.Cells بنجاح.
