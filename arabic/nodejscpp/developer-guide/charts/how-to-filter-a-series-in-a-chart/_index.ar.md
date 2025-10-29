---
title: ثلاث طرق لتصفية بيانات المخطط باستخدام Node.js عبر C++
linktitle: ثلاثة أساليب لتصفية بيانات الرسم البياني
description: تعلم كيف تصفّي المخططات في إكسل باستخدام Aspose.Cells for Node.js via C++. دليلنا الشامل سيعرض كيفية تطبيق الفلاتر على المخططات، تخصيص عناصر المخطط، واستخدام أدوات تحليل البيانات للحصول على رؤى أفضل واتخاذ قرارات مستنيرة.
keywords: Aspose.Cells for Node.js via C++، تصفية المخططات في إكسل، تحليل البيانات، اتخاذ القرارات، التصور.
type: docs
weight: 2210
url: /ar/nodejs-cpp/filtering-charts-in-excel/
---


## **1. تصفية السلاسل لعرض رسم بياني**

### **خطوات تصفية السلاسل من رسم بياني في إكسل**
يمكننا في إكسل تصفية سلسلة معينة من المخطط، مما يؤدي إلى عدم عرض تلك السلاسل المصفاة في المخطط. يُعرض المخطط الأصلي في **الشكل 1**. ومع ذلك، عند تصفية **Testseries2** و**Testseries4**، سيظهر المخطط كما هو موضح في **الشكل 2**.

في Aspose.Cells for Node.js via C++، يمكننا تنفيذ عملية مماثلة. لملف [نموذج](seriesFiltered.xlsx) كهذا، إذا أردنا تصفية **Testseries2** و**Testseries4**، يمكننا تنفيذ الرمز التالي. بالإضافة إلى ذلك، سنحتفظ بقائمتين: واحدة ([Chart.getNSeries()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getNSeries--)) لتخزين جميع السلاسل المختارة.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **الكود المثالي**
تحميل ملف إكسل العيني ([ملف إكسل مرشّحة.xlsx](seriesFiltered.xlsx)).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "seriesFiltered.xlsx");
// Create an instance of existing Workbook
let workbook = new AsposeCells.Workbook(filePath);
// Get filtered series list
let nSeriesFiltered = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getFilteredNSeries();
// Get selected series list
let nSeries = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getNSeries();
// Should be 0
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 6
console.log("Visible Series count: " + nSeries.getCount());
// Process from the end to the beginning
nSeries.get(1).setIsFiltered(true);
nSeries.get(0).setIsFiltered(true);
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
workbook.save("seriesFiltered-out.xlsx");
workbook = new AsposeCells.Workbook("seriesFiltered-out.xlsx");
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
```

## **2. مرشّح البيانات واسمح للرسم البياني بالتغيير**

تصفية بياناتك هي طريقة رائعة للتعامل مع مرشحات المخططات التي تحتوي على الكثير من البيانات. عندما تقوم بتصفية البيانات، سيتغير المخطط. إحدى القضايا التي سنواجهها هي التأكد من بقاء المخطط على الشاشة. عند التصفية، تحصل على صفوف مخفية، وأحيانًا، سيكون المخطط في تلك الصفوف المخفية.

![todo:image_alt_text](Figure3.png)

### **خطوات استخدام مرشحات البيانات لتغيير الرسم البياني في إكسل**

1. انقر داخل نطاق البيانات الخاص بك.
2. انقر على علامة التبويب **البيانات**، وقم بتشغيل المرشحات بالنقر فوق المرشحات. ستحتوي الصف المسمى على السهم المنسدل.
3. إنشاء رسم بياني من خلال الانتقال إلى علامة التبويب **إدراج** وتحديد رسم بياني للأعمدة.
4. الآن قم بتصفية بياناتك باستخدام السهوم المنسدلة في البيانات. لا تستخدم مرشحات الرسم البياني.

### **الكود المثالي**
يعرض رمز النموذج التالي نفس الميزة باستخدام Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of Worksheet
const sheet = workbook.getWorksheets().get("Sheet1");
// Add data into details cells.
sheet.getCells().get(0, 0).putValue("Fruits Name");
sheet.getCells().get(0, 1).putValue("Fruits Price");
sheet.getCells().get(1, 0).putValue("Apples");
sheet.getCells().get(2, 0).putValue("Bananas");
sheet.getCells().get(3, 0).putValue("Grapes");
sheet.getCells().get(4, 0).putValue("Oranges");
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(2, 1).putValue(2);
sheet.getCells().get(3, 1).putValue(1);
sheet.getCells().get(4, 1).putValue(4);

// Add a chart to the worksheet
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
// Access the instance of the newly added chart
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B5", true);
// Set AutoFilter range
sheet.getAutoFilter().setRange("A1:B5");
// Add filters for a filter column.
sheet.getAutoFilter().addFilter(0, "Bananas");
sheet.getAutoFilter().addFilter(0, "Oranges");
// Apply the filters
sheet.getAutoFilter().refresh();
chart.toImage("Autofilter.png");
workbook.save("Autofilter.xlsx");
```

## **3. فلتر البيانات باستخدام جدول واسمح للرسم البياني بالتغيير**

استخدام جدول مشابه للطريقة 2، استخدام نطاق، ولكن لكم مزايا مع الجداول على النطاقات. عند تغيير النطاق إلى جدول وإضافة البيانات، سيقوم الرسم البياني بالتحديث تلقائيًا. مع نطاق، سيتعين عليك تغيير مصدر البيانات.

### **تنسيق باعتباره جدولاً في إكسل**

انقر داخل بياناتك واستخدم **CTRL + T** أو استخدم علامة التبويب الرئيسية، **تنسيق باعتبارها جدولاً**

![todo:image_alt_text](Figure4.png)

### **الكود المثالي**
يرفع الرمز النموذجي التالي [ملف إكسل النموذجي](TableFilters.xlsx) ويظهر نفس الميزة باستخدام Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "TableFilters.xlsx");
// Create a workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet
const sheet = workbook.getWorksheets().get(0);
// Access the instance of the newly added chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B7", true);
// Convert the chart to image
chart.toImage("TableFilters.before.png");
// Add a new List Object to the worksheet
const listObject = sheet.getListObjects().get(sheet.getListObjects().add("A1", "B7", true));
// Add default style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);
// Show Total
listObject.setShowTotals(false);
// Add filters for a filter column.
listObject.getAutoFilter().addFilter(0, "James");
// Apply the filters
listObject.getAutoFilter().refresh();
// After adding new value the chart will change
listObject.putCellValue(7, 0, "Me");
listObject.putCellValue(7, 1, 1000);
// Check the changed images
chart.toImage("TableFilters.after.png");
// Saving the Excel file
workbook.save("TableFilter.out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
