---  
title: إدارة محاور مخططات Excel باستخدام Node.js عبر ++C  
description: تعلم كيفية تكوين محاور المخططات في Aspose.Cells for Node.js via C++. ستوضح لك أدلتنا كيفية ضبط المحاور الأساسية والثانوية، تحديد نطاقاتها، وتعديل خصائصها لتعزيز مخططاتك.  
keywords: Aspose.Cells for Node.js via C++، محاور المخططات، التكوين، المحاور الأساسية، المحاور الثانوية، النطاق، الخصائص.  
linktitle: المحاور  
type: docs  
weight: 50  
url: /ar/nodejs-cpp/chart-axes/  
---  

{{% alert color="primary" %}}  

في رسوم بيانية Excel، هناك 3 أنواع من المحاور:  
1. المحور الأفقي (الفئة): محور X  
1. المحور الرأسي (القيمة): محور Y  
1. المحور العمق (السلسلة): محور Z  

{{% /alert %}}  

## **خيارات المحور**  
Aspose.Cells for Node.js via C++ يسمح لك أيضًا بإدارة محاور المخطط في وقت التشغيل. باستخدام كائن [Axis](https://reference.aspose.com/cells/nodejs-cpp/axis/)، يمكنك تغيير جميع خيارات المحور كما هو موضح في Excel.  

|![todo:image_alt_text](chart_axes.png)|  

## **إدارة محاور X و Y**  
في مخطط Excel، المحور الأفقي والمحور العمودي هما الأكثر شعبية للاستخدام.  

يوضح مقتطف الشفرة التالي كيفية تعيين خيارات محاور X و Y.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart_axes.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue("Series1");
worksheet.getCells().get("A2").putValue(50);
worksheet.getCells().get("A3").putValue(100);
worksheet.getCells().get("A4").putValue(150);
worksheet.getCells().get("B1").putValue("Series2");
worksheet.getCells().get("B2").putValue(60);
worksheet.getCells().get("B3").putValue(32);
worksheet.getCells().get("B4").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);

// Hiding X axis
chart.getCategoryAxis().setIsVisible(false);

// Setting max value of Y axis
chart.getValueAxis().setMaxValue(200);
// Setting major unit
chart.getValueAxis().setMajorUnit(50);

// Save the file
workbook.save(filePath);
```  

## **مواضيع متقدمة**  
- [تغيير اتجاه التسمية التلقائية](/cells/ar/nodejs-cpp/change-tick-label-direction/)  
- [تحديد أي محور موجود في الرسم البياني](/cells/ar/nodejs-cpp/determine-which-axis-exists-in-the-chart/)  
- [التعامل مع الوحدات التلقائية لمحور الرسم البياني مثل Microsoft Excel](/cells/ar/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [قراءة تسميات المحور بعد حساب الرسم البياني](/cells/ar/nodejs-cpp/read-axis-labels-after-calculating-the-chart/)  
- [كيفية تعيين محور الفئة في رسم بياني Excel](/cells/ar/nodejs-cpp/how-to-set-category-axis/)  

