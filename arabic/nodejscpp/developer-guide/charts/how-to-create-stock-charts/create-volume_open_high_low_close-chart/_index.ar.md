---
title: إنشاء مخطط سهم حجم فتح عالي منخفض إغلاق باستخدام Node.js عبر C++
description: تعلم كيفية إنشاء مخطط سهم حجم فتح عالي منخفض إغلاق باستخدام Aspose.Cells for Node.js via C++. ستوضح دليلنا كيفية رسم بيانات سوق الأسهم، بما في ذلك حجم، فتح، عالي، منخفض، وإغلاق الأسعار، على مخطط لتحليل وتصوير أفضل.
keywords: Aspose.Cells for Node.js via C++، مخطط سهم حجم فتح عالي منخفض إغلاق، بيانات سوق الأسهم، التحليل، التصور.
type: docs
weight: 184
url: /ar/nodejs-cpp/create-volume-open-high-low-close-stock-chart/
---

## **سيناريوهات الاستخدام المحتملة**
المخطط الرابع الذي سننظر إليه هو مخطط حجم فتح عالي منخفض إغلاق. من المهم تكرار أن البيانات يجب أن تكون بالترتيب الصحيح. إذا كنت بحاجة لإعادة ترتيب جدول البيانات الخاص بك، يجب أن تقوم بذلك قبل إعداد المخطط. يتضمن هذا المخطط عمودًا للحجم مباشرة بعد العمود الأول (الفئة)، ويشمل رسم بياني عمودي على المحور الرئيسي يُظهر هذا الحجم، بينما يتم نقل الأسعار إلى المحور الثانوي.

![todo:image_alt_text](data.png)
## **مخطط الأسهم لحجم فتح عالي منخفض إغلاق (VHLC)**

![todo:image_alt_text](sample.png)
## **الكود المثالي**
الكود العينة التالي يقوم بتحميل [ملف Excel عينة](Volume-Open-High-Low-Close.xlsx) وإنشاء [ملف Excel الخرج](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Volume-Open-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeOpenHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Volume-Open-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:F9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set Color for the first series (Volume) data 
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(79, 129, 189));
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
