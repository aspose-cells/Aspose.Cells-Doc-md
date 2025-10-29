---
title: كيفية إنشاء رسم بياني متدفق ديناميكي باستخدام Node.js عبر C++
linktitle: كيفية إنشاء رسم بياني ديناميكي متدحرج
description: تعلم كيفية إنشاء رسم بياني متدفق ديناميكي باستخدام Aspose.Cells for Node.js via C++. سيُظهر دليلنا كيفية تنفيذ انتقالات سلسة للبيانات والتمرير التلقائي في الرسم البياني الخاص بك لعرض مستمر ومُحول.
keywords: Aspose.Cells لـ Node.js، رسم بياني متدفق ديناميكي، انتقالات البيانات، التمرير السلس، عرض مستمر، تحديث التصور.
type: docs
weight: 75
url: /ar/nodejs-cpp/create-dynamic-scrolling-chart/
---

## **سيناريوهات الاستخدام المحتملة**
رسم بياني متدحرج ديناميكي هو نوع من التمثيل البياني المستخدم لعرض البيانات التي تتغير مع مرور الوقت. تم تصميمه لتوفير رؤية في الوقت الحقيقي للبيانات، مما يتيح للمستخدمين تتبع التحديثات المستمرة والاتجاهات. يقوم الرسم البياني بالتحديث بشكل مستمر كلما تمت إضافة بيانات جديدة، ويمرر تلقائيًا لعرض أحدث المعلومات.

يتم استخدام رسوم بيانية متدحرجة ديناميكية عادة في مختلف الصناعات، مثل التمويل، وتحليل سوق الأسهم، وتتبع الطقس، وتحليل وسائل التواصل الاجتماعي. إنها تمكن المستخدمين من تصور وتحليل أنماط البيانات واتخاذ قرارات مستنيرة استنادًا إلى المعلومات في الوقت الحقيقي.

عموما، تعتبر هذه الرسوم بيانية متدحرجة ديناميكية أدوات قيمة لمراقبة وتحليل البيانات الزمنية، وتسهيل اتخاذ القرارات في الوقت الحقيقي وتعزيز القدرات على تصور البيانات.

استخدام Aspose Cells لإنشاء رسم بياني ديناميكي متدحرج

## ** استخدم Aspose.Cells لإنشاء رسم بياني متدفق ديناميكي**
 في الفقرات التالية، سنوضح لك كيفية إنشاء رسم بياني متدفق ديناميكي باستخدام Aspose.Cells for Node.js via C++. سنعرض لك رمز المثال، بالإضافة إلى ملف Excel الذي تم إنشاؤه باستخدام هذا الرمز.

## **الكود المثالي**
سينشئ الكود العينة التالي [ملف الرسم البياني الديناميكي المتدحرج](DynamicScrollingChart.xlsx).

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
sheet.getCells().get("A1").putValue("Day");
sheet.getCells().get("B1").putValue("Sales");
// In this example, we will add 30 days of data
const allDays = 30;
const showDays = 10;
let currentDay = 1;

for (let i = 0; i < allDays; i++) {
const cellA = `A${i + 2}`;
const cellB = `B${i + 2}`;
sheet.getCells().get(cellA).putValue(i + 1);
sheet.getCells().get(cellB).putValue(50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3));
}

// This is the Dynamic Scrolling Control Data
sheet.getCells().get("G19").putValue("Start Day");
sheet.getCells().get("G20").putValue(currentDay);
sheet.getCells().get("H19").putValue("Show Days");
sheet.getCells().get("H20").putValue(showDays);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtScrollData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtScrollLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Add a ScrollBar for the Dynamic Scrolling Chart
const bar = sheet.getShapes().addScrollBar(2, 0, 3, 0, 200, 30);
bar.setMin(0);
bar.setMax(allDays - showDays);
bar.setCurrentValue(currentDay);
bar.setLinkedCell("$G$20");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 2, 4, 15, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtScrollData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtScrollLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicScrollingChart.xlsx"));
```

## **ملاحظات**
في الملف الذي تم إنشاؤه، يمكنك التشغيل على شريط التمرير، في حين يقوم الرسم البياني بحساب البيانات العشر مجموعات الأحدث تلقائيًا. يتم ذلك باستخدام صيغة "OFFSET" في الكود العينة:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

 يمكنك محاولة تغيير الرقم "10" إلى "15" في الخلية "Sheet1!$H$20"، وسيقوم الرسم البياني الديناميكي بعد ذلك بحساب أحدث 15 مجموعة من البيانات. لقد أنشأنا بنجاح رسمًا بيانيًا متدفقًا ديناميكيًا باستخدام Aspose.Cells for Node.js via C++.
{{< app/cells/assistant language="nodejs-cpp" >}}
