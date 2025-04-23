---  
title: تحويل المخطط إلى PDF باستخدام Node.js عبر C++  
linktitle: تحويل الرسم البياني إلى PDF  
description: تعلم كيفية استخدام Aspose.Cells for Node.js via C++ لتحويل مخطط إلى مستند PDF. يوضح دليلنا كيفية تصدير مخطط من Microsoft Excel وحفظه كملف PDF للمشاركة والأرشفة لاحقًا.  
keywords: Aspose.Cells for Node.js via C++، تحويل المخطط إلى PDF، Microsoft Excel، تحويل إلى PDF، التصدير، المشاركة، الأرشفة.  
type: docs  
weight: 47  
url: /ar/nodejs-cpp/chart-to-pdf/  
---  

## **عرض الرسم البياني إلى PDF**

لتحويل المخطط إلى تنسيق PDF، قامت واجهات برمجة التطبيقات Aspose.Cells بالكشف عن طريقة [**Chart.toPdf(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toPdf-string-) مع القدرة على تخزين ملف PDF الناتج على مسار القرص أو تدفق البيانات.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Adding a new worksheet to the Workbook
const sheetIndex = workbook.getWorksheets().add();
// Obtaining the reference of the newly added worksheet by passing its index to WorksheetCollection
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);
// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Converting chart to PDF
chart.toPdf(path.join(dataDir, "chartPDF_out.pdf"));
```

## **إنشاء رسم بياني PDF بحجم الصفحة المطلوب**  
يمكنك إنشاء ملف PDF للمخطط بحجم الصفحة المرغوب باستخدام Aspose.Cells وتحديد كيفية محاذاة المخطط داخل الصفحة من الأعلى، الأسفل، الوسط، اليسار، اليمين، إلخ. بالإضافة إلى ذلك، يمكن إنشاء المخطط الناتج في تدفق أو على القرص. يرجى الاطلاع على المثال التالي الذي يحمّل [ملف إكسل النموذجي](64716906.xlsx)، ويصل إلى المخطط الأول داخل ورقة العمل ثم يحولها إلى [ملف PDF الناتج](64716907.pdf) بحجم الصفحة المطلوب. يوضح الصورة الملتقطة أدناه أن حجم الصفحة في ملف PDF الناتج هو 7×7 كما هو محدد داخل الكود وأن المخطط محاذى في الوسط أفقياً وعمودياً.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)  
## **الكود المثالي**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file containing the chart.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateChartPDFWithDesiredPageSize.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet.
const chart = worksheet.getCharts().get(0);

// Create chart pdf with desired page size.
chart.toPdf(path.join(outputDir, "outputCreateChartPDFWithDesiredPageSize.pdf"), 7, 7, AsposeCells.PageLayoutAlignmentType.Center, AsposeCells.PageLayoutAlignmentType.Center);
```  


