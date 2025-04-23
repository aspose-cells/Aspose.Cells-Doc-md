---
title: إنشاء رسم سوق الأسهم المفتوح العالي المنخفض الإغلاق (OHLC) باستخدام Node.js عبر C++
description: تعلم كيفية إنشاء رسم سوق الأسهم المفتوح العالي المنخفض الإغلاق باستخدام Aspose.Cells for Node.js via C++. سيرينا دليلنا كيفية رسم بيانات سوق الأسهم، بما في ذلك أسعار الفتح، أعلى، أدنى، والإغلاق، على رسم بياني لتحليل أفضل وتصوّر.
keywords: Aspose.Cells for Node.js via C++, مخطط الأسهم فتح عالي منخفض إغلاق، بيانات سوق الأسهم، التحليل، التصور.
type: docs
weight: 182
url: /ar/nodejs-cpp/create-open-high-low-close-stock-chart/
---

## **سيناريوهات الاستخدام المحتملة**
يستخدم مخطط Open-High-Low-Close (OHLC) خمسة أعمدة من البيانات، بالترتيب: الفئة، فتح، عالي، منخفض، وإغلاق. يتم إشارة نطاق الأسعار في كل فئة مرة أخرى بخط عمودي، بينما يتم تقديم نطاق بين الفتح والإغلاق بشريط عائم أوسع؛ إذا زاد السعر في الفئة (الإغلاق أعلى من الفتح)، يتم ملؤه بلون واحد، بينما إذا انخفض السعر، يتم ملؤه بلون آخر. يطلق على هذا النوع من الرسم البياني كثيرًا اسم الرسم الشمعي.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **تحسينات الرؤية في الرسم البياني**
 غالبًا ما نستخدم الألوان بدلاً من الأبيض والأسود للإشارة إلى ارتفاع وانخفاض الأسعار. في مجموعة الشموع الأولى أدناه، يظهر اللون الأحمر ارتفاع الأسعار والأخضر انخفاضها.

![todo:image_alt_text](sample2.png)
## **الكود المثالي**
الكود العينة التالي يحمل [ملف إكسل العينة](Open-High-Low-Close.xlsx) ويولد [ملف إكسل الناتج](out.xlsx).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Open-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockOpenHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Open-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E9", true);
// Set category data 
chart.getNSeries().getCategoryData("A2:A9");
// Set the DownBars and UpBars with different color
chart.getNSeries().get(0).getDownBars().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(0).getUpBars().getArea().setForegroundColor(AsposeCells.Color.Red);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
