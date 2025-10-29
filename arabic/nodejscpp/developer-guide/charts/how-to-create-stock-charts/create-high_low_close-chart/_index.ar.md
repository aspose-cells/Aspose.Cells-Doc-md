---  
title: إنشاء رسم بياني أسهم عالي منخفض إغلاق (HLC) باستخدام Node.js عبر C++  
linktitle: إنشاء رسم بياني لأسهم High Low Close (HLC)  
description: تعلم كيفية إنشاء رسم بياني لأسهم عالي منخفض إغلاق باستخدام Aspose.Cells for Node.js via C++. سيتم إظهار كيف يمكن رسم بيانات سوق الأسهم، بما في ذلك أعلى، أدنى، وأسعار الإغلاق، على الرسم البياني لتحليل أفضل وتصوّر.  
keywords: Aspose.Cells لـ Node.js، رسم بياني لأسهم عالي منخفض إغلاق، بيانات سوق الأسهم، التحليل، التصور.  
type: docs  
weight: 181  
url: /ar/nodejs-cpp/create-high-low-close-stock-chart/  
---  

## **سيناريوهات الاستخدام المحتملة**  
 يستخدم رسم الأسهم عالي-منخفض-إغلاق أربعة أعمدة من البيانات. العمود الأول هو فئة، عادةً تاريخ لكن يمكن استخدام أسماء الأسهم أيضًا. الأعمدة الثلاثة التالية، بالترتيب، هي للأسعار العليا، الدنيا، والإغلاق. يُشار إلى نطاق السعر لكل فئة بخط عمودي من أدنى إلى أعلى، ويُعرض سعر الإغلاق باستخدام علامة مميزة تمتد إلى يمين هذا الخط.  

![todo:image_alt_text](sample.png)  
## **تحسينات الرؤية في الرسم البياني**  
في بعض الأحيان، لجعل الرسم البياني يبدو أكثر تفاعلية، يمكننا تعديل مظهر العلامة (الإغلاق)، أو جعلها تظهر على المحور الثانوي.  

![todo:image_alt_text](sample2.png)  
## **الكود المثالي**  
الكود العينة التالي يحمل [ملف إكسل العينة](High-Low-Close.xlsx) ويولد [ملف إكسل الناتج](out.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:D9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set the marker with the built-in data 
chart.getNSeries().get(2).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Dash);
chart.getNSeries().get(2).getMarker().setMarkerSize(20);
chart.getNSeries().get(2).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(2).getMarker().getArea().setForegroundColor(AsposeCells.Color.Maroon);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
