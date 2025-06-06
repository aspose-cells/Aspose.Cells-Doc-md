---
title: كيفية إنشاء مخطط مركب باستخدام Node.js عبر C++
linktitle: كيفية إنشاء رسم بياني مختلط
description: تعلم كيفية إنشاء مخطط مركب باستخدام Aspose.Cells for Node.js via C++. سيُظهر دليلنا الشامل كيفية دمج أنواع مخططات مختلفة في مخطط مركب واحد لعرض أكثر فاعلية للبيانات.
keywords: Aspose.Cells for Node.js via C++، مخطط مركب، دمج أنواع المخططات، عرض البيانات، التصور الفعّال.
type: docs
weight: 73
url: /ar/nodejs-cpp/create-combo-chart/
---

## **سيناريوهات الاستخدام المحتملة**
تتيح لك رسوم الكومبو في Excel الاستفادة من هذا الخيار لأنك يمكنك دمج نوعين أو أكثر من أنواع الرسوم البيانية بسهولة لجعل بياناتك مفهومة. تكون رسوم الكومبو مفيدة عندما تحتوي بياناتك على أنواع متعددة من القيم بما في ذلك السعر والحجم. علاوة على ذلك، تكون رسوم الكومبو ممكنة عندما تتغير أرقام بياناتك بشكل واسع من سلسلة إلى سلسلة.
من خلال اعتبار مجموعة البيانات التالية كمثال، يمكننا ملاحظة أن هذه البيانات مشابهة تمامًا للبيانات المذكورة في [**VHCL**](https://docs.aspose.com/cells/nodejs-cpp/create-volume-high-low-close-stock-chart/). إذا كنا نريد تصوير series0، والتي تتوافق مع "إجمالي الإيرادات"، كرسم بياني خطي، فكيف يجب أن نقدم؟

![todo:image_alt_text](sample.png)
## **رسم بياني مختلط**
بعد تشغيل الرمز أدناه، سترون الرسم البياني المختلط كما هو موضح أدناه.

![todo:image_alt_text](result.png)
## **الكود المثالي**
يقوم الرمز العيني التالي بتحميل [ملف Excel العيني] التالي(combo.xlsx) وإنتاج [ملف Excel الإخراج المعني] التالي(out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "combo.xlsx");

// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a stock volume (VHLC)
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeHighLowClose, 15, 0, 34, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Combo Chart");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E12", true);
// Set category data 
chart.getNSeries().get(0).setXValues("A2:A12");  // Corrected method

// Set the Series[1] Series[2] and Series[3] to different Marker Style
for (let j = 0; j < chart.getNSeries().getCount(); j++) {
switch (j) {
case 1:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Circle);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.Pink);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
case 2:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Dash);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.Orange);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
case 3:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Square);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.LightBlue);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
}
}
// Set the chart type for Series[0] 
chart.getNSeries().get(0).setType(AsposeCells.ChartType.Line);
// Set style for the border of first series
chart.getNSeries().get(0).getBorder().setStyle(AsposeCells.LineType.Solid);
// Set Color for the first series
chart.getNSeries().get(0).getBorder().setColor(AsposeCells.Color.DarkBlue);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().setFormatting(AsposeCells.FormattingType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
