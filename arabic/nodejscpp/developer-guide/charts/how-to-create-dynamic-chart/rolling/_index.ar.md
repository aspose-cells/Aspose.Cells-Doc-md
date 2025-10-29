---
title: كيفية إنشاء رسم بياني متداول ديناميكي باستخدام Node.js عبر C++
linktitle: كيفية إنشاء رسم بياني ديناميكي متداول
description: تعلم كيفية إنشاء رسم بياني متداول ديناميكي باستخدام Aspose.Cells for Node.js via C++. سيرينا دليلنا كيفية تنفيذ انتقالات سلسة للبيانات ومتوسطات متداولة في رسمك البياني لعرض مستمر ومُحول.
keywords: Aspose.Cells لـ Node.js، رسم بياني متداول ديناميكي، انتقالات البيانات، متوسطات سلسة، عرض مستمر، تحديث التصور.
type: docs
weight: 74
url: /ar/nodejs-cpp/create-dynamic-rolling-chart/
---

## **سيناريوهات الاستخدام المحتملة**
يشير رسم البيانات المتداول الديناميكي إلى تمثيل بياني يعرض نقاط البيانات التي تتحرك باستمرار وتحديث عبر الوقت. إنه نوع من الرسم البياني الذي يحدث نفسه باستمرار، ويعرض نافذة متداولة لأحدث نقاط البيانات بينما يتخلص من نقاط البيانات القديمة مع دخول النقاط الجديدة.

يتم استخدام رسوم بيانية متداولة ديناميكية عادةً لتصور الاتجاهات والأنماط في الوقت الفعلي أو البيانات المتدفقة. إنها مفيدة بشكل خاص في السيناريوهات التي تكون فيها الجوانب الزمنية والتغييرات عبر الوقت حرجة، مثل تحليل سوق الأسهم، مراقبة الطقس، أو تتبع الأداء الحي.

عادةً ما تستخدم هذه الرسوم البيانية آليات الرسم المتحرك أو التمرير التلقائي لضمان تقديم أحدث المعلومات دائمًا. يمكن تخصيص طول النافذة المتداولة لعرض فترة زمنية محددة، مثل الساعة الأخيرة، أو اليوم، أو الأسبوع.

في الختام، يعد رسم بياني متداول ديناميكي تمثيلًا بيانيًا محدث باستمرار يعرض أحدث نقاط البيانات مع التخلص من النقاط القديمة، مما يسمح للمستخدمين بمراقبة الاتجاهات والأنماط الفعلية.

## **استخدام Aspose Cells لإنشاء رسم بياني متداول ديناميكي**
في الفقرات التالية، سنريك كيفية إنشاء رسم بياني متداول ديناميكي باستخدام Aspose.Cells. سنريك الكود للمثال، وكذلك ملف Excel الذي تم إنشاؤه بهذا الكود.

## **الكود المثالي**
سيقوم الكود العيني التالي بتوليد [ملف رسم بياني متداول ديناميكي](DynamicRollingChart.xlsx).

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
sheet.getCells().get("A1").putValue("Month");
sheet.getCells().get("A2").putValue(1);
sheet.getCells().get("A3").putValue(2);
sheet.getCells().get("A4").putValue(3);
sheet.getCells().get("A5").putValue(4);
sheet.getCells().get("A6").putValue(5);
sheet.getCells().get("A7").putValue(6);
sheet.getCells().get("A8").putValue(7);

sheet.getCells().get("B1").putValue("Sales");
sheet.getCells().get("B2").putValue(50);
sheet.getCells().get("B3").putValue(45);
sheet.getCells().get("B4").putValue(55);
sheet.getCells().get("B5").putValue(60);
sheet.getCells().get("B6").putValue(55);
sheet.getCells().get("B7").putValue(65);
sheet.getCells().get("B8").putValue(70);

// Set the dynamic range for the chart's data source.
let index = sheets.getNames().add("Sheet1!ChtData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

// Set the dynamic range for the chart's data labels.
index = sheets.getNames().add("Sheet1!ChtLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 10, 3, 25, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicRollingChart.xlsx"));
```

## **ملاحظات**
في الملف الذي تم إنشاؤه، يمكنك متابعة إضافة البيانات في الأعمدة A و B، بينما يحسب الرسم البياني ديناميكيًا أحدث 5 مجموعات من البيانات. يتم ذلك باستخدام صيغة "OFFSET" في الكود العيني:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

يمكنك محاولة تغيير الرقم "-5" إلى "-10" في الصيغة، وسوف يقوم الرسم الديناميكي بحساب أحدث 10 مجموعات من البيانات. الآن لقد قمنا بإنشاء رسم بياني متدحرج ديناميكي باستخدام Aspose.Cells بنجاح.
{{< app/cells/assistant language="nodejs-cpp" >}}
