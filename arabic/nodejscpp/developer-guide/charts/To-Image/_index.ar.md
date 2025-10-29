---  
title: تحويل المخطط إلى صورة باستخدام Node.js عبر C++  
description: تعلم كيفية استخدام Aspose.Cells for Node.js via C++ لتحويل المخطط إلى تنسيق صورة، مثل JPEG أو PNG. يوضح دليلنا كيفية تصدير المخطط من Microsoft Excel وحفظه كصورة مستقلة للاستخدام والمعالجة المستقبلة.  
keywords: Aspose.Cells for Node.js via C++، تحويل المخطط إلى صورة، Microsoft Excel، تحويل الصورة، التصدير، صورة مستقلة.  
linktitle: تحويل الرسم البياني إلى صورة  
type: docs  
weight: 46  
url: /ar/nodejs-cpp/chart-to-image/  
---  

## **عرض الرسوم البيانية**

 تدعم واجهات برمجة التطبيقات Aspose.Cells تحويل مخططات Excel إلى تنسيقات الصور دون الحاجة إلى أدوات أو تطبيقات إضافية. لضمان دعم التصيير، تكشف فئة [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) عن طرق [**toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) مع مجموعة من التحميلات المفرطة التي تلبي متطلبات التطبيق.

### **عرض الرسوم البيانية كصور**

 طريقة [**Chart.toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) لديها مجموعة متنوعة من التحميلات لدعم التصيير البسيط والمتقدم. إذا كان متطلب التطبيق هو تصيير المخطط بأبعاده الافتراضية، نوصي باستخدام طريقة [**Chart.toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) كما يلي.

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

// Converting chart to image
chart.toImage(path.join(dataDir, "chartEMF_out.emf"), AsposeCells.ImageType.Emf);

// Converting chart to Bitmap
chart.toImage(path.join(dataDir, "chartBMP_out.bmp"), AsposeCells.ImageType.Bmp);
```

من الممكن أيضًا تصيير المخططات إلى صور مع إعدادات متقدمة. تكشف APIات Aspose.Cells عن نسخة تحميل مفرطة من طريقة [**Chart.toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) التي تقبل كائن [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions)، مع السماح بتحديد معلمات مثل الدقة، وضع التنعيم، صيغة الصورة، وغيرها.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
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

// Create an instance of ImageOrPrintOptions and set a few properties
const options = new AsposeCells.ImageOrPrintOptions();
options.setVerticalResolution(300);
options.setHorizontalResolution(300);

// Convert chart to image with additional settings
chart.toImage(path.join(dataDir, "chartPNG_out.png"), options);
```

## **أنواع الرسوم البيانية المدعومة للعرض**

هناك بعض أنواع الرسوم البيانية التي لا تتم دعمها حاليًا للعرض. تحتوي مثل هذه الأنواع على **N** في العمود **مدعوم** للجدول أدناه.

|**نوع الرسم البياني**|**نوع الفرعي للرسم البياني**|**مدعوم**|  
| :- | :- | :- |  
|**Column**|Column|**Y**|  
| |ColumnStacked|**Y**|  
| |Column100PercentStacked|**Y**|  
| |Column3DClustered|**Y**|  
| |Column3DStacked|**Y**|  
| |Column3D100PercentStacked|**Y**|  
| |Column3D|**Y**|  
|**Bar**|Bar|**Y**|  
| |BarStacked|**Y**|  
| |Bar100PercentStacked|**Y**|  
| |Bar3DClustered|**Y**|  
| |Bar3DStacked|**Y**|  
| |Bar3D100PercentStacked|**Y**|  
|**Line**|Line|**Y**|  
| |LineStacked|**Y**|  
| |Line100PercentStacked|**Y**|  
| |LineWithDataMarkers|**Y**|  
| |LineStackedWithDataMarkers|**Y**|  
| |Line100PercentStackedWithDataMarkers|**Y**|  
| |Line3D|**Y**|  
|**Pie**|Pie|**Y**|  
| |Pie3D|**Y**|  
| |PiePie|**Y**|  
| |PieExploded|**Y**|  
| |Pie3DExploded|**Y**|  
| |PieBar|**Y**|  
|**Scatter**|Scatter|**Y**|  
| |ScatterConnectedByCurvesWithDataMarker|**Y**|  
| |ScatterConnectedByCurvesWithoutDataMarker|**Y**|  
| |ScatterConnectedByLinesWithDataMarker|**Y**|  
| |ScatterConnectedByLinesWithoutDataMarker|**Y**|  
|**Area**|Area|**Y**|  
| |AreaStacked|**Y**|  
| |Area100PercentStacked|**Y**|  
| |Area3D|**Y**|  
| |Area3DStacked|**Y**|  
| |Area3D100PercentStacked|**Y**|  
|**Doughnut**|Doughnut|**Y**|  
| |DoughnutExploded|**Y**|  
|**Radar**|Radar|**Y**|  
| |RadarWithDataMarkers|**Y**|  
| |RadarFilled|**Y**|  
|**Surface**|Surface3D|N|  
| |SurfaceWireframe3D|N|  
| |SurfaceContour|N|  
| |SurfaceContourWireframe|N|  
|**Bubble**|Bubble|**Y**|  
| |Bubble3D|N|  
|**Stock**|StockHighLowClose|**Y**|  
| |StockOpenHighLowClose|**Y**|  
| |StockVolumeHighLowClose|**Y**|  
| |StockVolumeOpenHighLowClose|**Y**|  
|**Cylinder**|Cylinder|**Y**|  
| |CylinderStacked|**Y**|  
| |Cylinder100PercentStacked|**Y**|  
| |CylindricalBar|**Y**|  
| |CylindricalBarStacked|**Y**|  
| |CylindricalBar100PercentStacked|**Y**|  
| |CylindricalColumn3D|**Y**|  
|**Cone**|Cone|**Y**|  
| |ConeStacked|**Y**|  
| |Cone100PercentStacked|**Y**|  
| |ConicalBar|**Y**|  
| |ConicalBarStacked|**Y**|  
| |ConicalBar100PercentStacked|**Y**|  
| |ConicalColumn3D|**Y**|  
|**Pyramid**|Pyramid|**Y**|  
| |PyramidStacked|**Y**|  
| |Pyramid100PercentStacked|**Y**|  
| |PyramidBar|**Y**|  
| |PyramidBarStacked|**Y**|  
| |PyramidBar100PercentStacked|**Y**|  
| |PyramidColumn3D|**Y**|  
|**BoxWhisker**|BoxWhisker|Y|  
|**Funnel**|Funnel|**Y**|  
|**ParetoLine**|ParetoLine|**Y**|  
|**Sunburst**|Sunburst|**Y**|  
|**Treemap**|Treemap|**Y**|  
|**Waterfall**|Waterfall|**Y**|  
|**Histogram**|Histogram|Y|  
|**Map**|Map|**N**|  

{{% alert color="primary" %}}  
في حال محاولة عرض أنواع الرسوم البيانية غير المدعومة إلى صورة أو PDF، قد تنتهي بصور بحجم 0 أو PDF فارغة.  
{{% /alert %}}  

## **مواضيع متقدمة**  
- [تحويل الرسم البياني إلى PDF](/cells/ar/nodejs-cpp/chart-to-pdf/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
