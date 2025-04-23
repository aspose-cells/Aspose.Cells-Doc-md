---  
title: تعيين مصدر البيانات للمخطط باستخدام Node.js عبر C++  
description: تعرف على مصادر البيانات المختلفة المدعومة بواسطة Aspose.Cells for Node.js via C++. سيقوم دليلنا بشرح أنواع مصادر البيانات المتاحة وكيفية الاتصال بها واسترجاع البيانات منها لملء أوراق العمل الخاصة بك.  
keywords: Aspose.Cells for Node.js via C++، الرسم البياني، تنسيق البيانات، التسميات، الألوان، الخطوط، المظهر، سهولة الاستخدام.  
linktitle: مصدر البيانات  
type: docs  
weight: 10  
url: /ar/nodejs-cpp/data-formatting-in-charts/  
---  

في موضوعاتنا السابقة، قدمنا العديد من الأمثلة لتوضيح كيفية تعيين مصدر بيانات لمخططك، ولكن في هذا الموضوع سنقدم مزيدًا من التفاصيل حول أنواع البيانات التي يمكن تعيينها للمخطط.

## **ضبط بيانات الرسم البياني**

هناك نوعان من البيانات التي يتعين التعامل معها أثناء العمل على الرسوم البيانية باستخدام Aspose.Cells وهي كما يلي:

- بيانات الرسم البياني.
- بيانات الفئة.

### **بيانات الرسم البياني**

بيانات الرسم البياني هي البيانات التي نستخدمها كمصدر بيانات لبناء مخططاتنا. يمكننا إضافة نطاق من الخلايا (التي تحتوي على بيانات المخطط) من خلال استدعاء طريقة [**add(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#add-string-boolean-) على كائن [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(300);
worksheet.getCells().get("B1").putValue(160);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **بيانات الفئة**

تستخدم بيانات الفئة لتسمية بيانات المخطط ويمكن إضافتها إلى [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) باستخدام خاصيتها [**getCategoryData()**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#getCategoryData--). تم تقديم مثال كامل أدناه لشرح استخدام بيانات المخطط والفئة. بعد تنفيذ رمز المثال أعلاه، سيتم إضافة مخطط عمودي إلى ورقة العمل كما هو موضح أدناه.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(10);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(200);
worksheet.getCells().get("B1").putValue(120);
worksheet.getCells().get("B2").putValue(320);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the data source for the category data of SeriesCollection
chart.getNSeries().setCategoryData("C1:C4");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **مواضيع متقدمة**  
- [تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق](/cells/ar/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)  
- [إنشاء رسوم بيانية ديناميكية](/cells/ar/nodejs-cpp/create-dynamic-charts/)  
- [طريقة سهلة لضبط الرسوم البيانية باستخدام طريقة Chart.SetChartDataRange](/cells/ar/nodejs-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)  
- [البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني](/cells/ar/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)  
