---  
title: إدارة بيانات العلامات لمخططات Excel باستخدام Node.js عبر C++  
description: تعلم كيفية إدارة علامات البيانات بشكل فعال في مخططات Excel باستخدام Aspose.Cells for Node.js via C++. يغطي دليلنا الشامل مهام الإدارة المختلفة، بما في ذلك إضافة وإزالة وتعديل العلامات لتعزيز وضوح واستخدام المخطط.  
keywords: Aspose.Cells لـ Node.js، مخططات Excel، علامات البيانات، الإدارة، سهولة القراءة، سهولة الاستخدام، الإضافة، الحذف، التعديل.  
linktitle: علامات البيانات  
type: docs  
weight: 50  
url: /ar/nodejs-cpp/insert-datalabels-to-chart/  
---  

{{% alert color="primary" %}}  

تعتبر علامات البيانات جزءًا هامًا من الرسم البياني.  
يمكننا بسهولة معرفة القيمة، النسبة المئوية، إلخ، لكل سلسلة.  

{{% /alert %}}  

## **خيارات علامات البيانات**  
يتيح Aspose.Cells for Node.js via C++ أيضًا إدارة علامات البيانات في المخطط في وقت التشغيل، باستخدام كائن [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/)، الأمر بسيط لنقل، تحديث وتنسيق علامات البيانات للمخطط.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **إدارة علامات البيانات في الرسم البياني**  
من السهل إدارة علامات البيانات للمخطط باستخدام [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/) الخاص بـ Aspose.Cells.  

يوضح الكود التالي كيفية إدارة علامات البيانات:  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Show value labels
chart.getNSeries().get(0).getDataLabels().setShowValue(true);
// Show series name labels
chart.getNSeries().get(1).getDataLabels().setShowSeriesName(true);
// Move labels to center
chart.getNSeries().get(1).getDataLabels().setPosition(AsposeCells.LabelPositionType.Center);

// Save the file
workbook.save("chart_datalabels.xlsx");
```  

## **مواضيع متقدمة**  
- [إضافة تسميات مخصصة إلى نقاط البيانات في سلسلة الرسم البياني](/cells/ar/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [تعطيل التفاف النص لعلامات البيانات في الرسم البياني](/cells/ar/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [تغيير شكل تسمية بيانات الرسم البياني لتناسب النص](/cells/ar/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [تسمية بيانات مخصصة نصية غنية الرسم البياني](/cells/ar/nodejs-cpp/rich-text-custom-data-label-of-chart-point/)  
- [تعيين نوع الشكل لتسميات بيانات الرسم البياني](/cells/ar/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [عرض نطاق الخلايا كعلامات البيانات](/cells/ar/nodejs-cpp/showing-cell-range-as-the-data-labels/)  

