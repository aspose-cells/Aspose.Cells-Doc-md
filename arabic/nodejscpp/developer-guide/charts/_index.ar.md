---
title: إنشاء وإدارة المخططات باستخدام Node.js عبر C++
linktitle: رسوم بيانية
description: تعلم كيفية استخدام Aspose.Cells لـ Node.js لإنشاء مخططات في Microsoft Excel. سيعرض دليلنا أنواع المخططات المختلفة وكيفية تخصيص مظهرها وتنسيقها.
keywords: Aspose.Cells لـ Node.js، إنشاء مخططات، Microsoft Excel، أنواع المخططات، التخصيص، المظهر، التنسيق.
type: docs
weight: 130
url: /ar/nodejs-cpp/creating-charts/
---

{{% alert color="primary" %}}

من الممكن إضافة مجموعة متنوعة من الرسوم البيانية إلى جداول البيانات باستخدام Aspose.Cells. توفر Aspose.Cells العديد من كائنات الرسم البياني المرنة. يتناول هذا الموضوع كائنات الرسم البياني في Aspose.Cells.

{{% /alert %}}

## **إنشاء الرسوم البيانية**

### **ببساطة إنشاء رسم بياني**
إنشاء مخطط بسيط باستخدام Aspose.Cells يمكن تحقيقه باستخدام أكواد الأمثلة التالية:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Adding sample values to cells
worksheet.getCells().get("A2").putValue("Category1");
worksheet.getCells().get("A3").putValue("Category2");
worksheet.getCells().get("A4").putValue("Category3");

worksheet.getCells().get("B1").putValue("Column1");
worksheet.getCells().get("B2").putValue(4);
worksheet.getCells().get("B3").putValue(20);
worksheet.getCells().get("B4").putValue(50);
worksheet.getCells().get("C1").putValue("Column2");
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("C3").putValue(100);
worksheet.getCells().get("C4").putValue(150);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Setting chart data source as the range "A1:C4"
chart.setChartDataRange("A1:C4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **الأشياء التي يجب معرفتها لإنشاء مخطط**

قبل إنشاء المخططات، من المهم فهم بعض المفاهيم الأساسية التي تساعد عند إنشاء المخططات باستخدام Aspose.Cells.

#### **كائنات المخطط**

المبالغ الخاصة بالمخططات مذكورة أدناه:

- Series، سلسلة بيانات واحدة في المخطط.
- Axis، محور المخطط.
- Chart، مخطط Excel واحد.
- ChartArea، منطقة المخطط في ورقة العمل.
- ChartDataTable، جدول بيانات المخطط.
- ChartFrame، كائن الإطار في المخطط.
- ChartPoint، نقطة واحدة في سلسلة في المخطط.
- ChartPointCollection، مجموعة تحتوي على جميع النقاط في سلسلة واحدة.
- Charts، مجموعة من كائنات المخطط.
- DataLabels، مجموعة من جميع كائنات DataLabel للسلسلة المحددة.
- FillFormat، تنسيق الملء للشكل.
- Floor، الطابق لمخطط ثلاثي الأبعاد.
- Legend، وسام المخطط.
- Line، خط المخطط.
- SeriesCollection، مجموعة من كائنات Series.
- تسميات العلامات، علامات العلامة المرتبطة بعلامات ضبط على محور الرسم البياني.
- العنوان، عنوان الرسم البياني أو المحور.
- خط الاتجاه، خط اتجاه في الرسم البياني.
- مجموعة خطوط الاتجاه، مجموعة من جميع كائنات خط الاتجاه لسلسلة البيانات المحددة.
- الجدران، الجدران في رسم بياني ثلاثي الأبعاد.

#### **استخدام كائنات الرسم البياني**

كما ذكر أعلاه، جميع كائنات الرسم البياني هي حالات من فئاتها الخاصة وتوفر خصائص وأساليب محددة لأداء مهام محددة. استخدم كائنات الرسم البياني لإنشاء رسوم بيانية.

أضف أي نوع من المخططات إلى ورقة العمل باستخدام مجموعة [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--). يمثل كل عنصر في مجموعة [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--) كائن [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/). ي encapsulate كائن [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) كل كائنات المخطط الأخرى اللازمة لتخصيص مظهر المخطط. يوضح القسم التالي كيفية استخدام بعض الكائنات الأساسية للمخطط لإنشاء مخطط بسيط.

### **إنشاء رسم بياني باستخدام Aspose.Cells**

**الخطوات:**

1. أضف بعض البيانات إلى خلايا ورقة العمل باستخدام طريقة [**putValue(string)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-string-) الخاصّة بكائن [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell/).
   سيتم استخدام هذا كمصدر بيانات للرسم البياني.
1. أضف مخططًا إلى ورقة العمل عن طريق استدعاء طريقة [**add**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection/#add-charttype-number-number-number-number-) لمجموعة [**ChartCollection**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection)، مغلفة في الكائن [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/).
1. حدد نوع المخطط باستخدام التعداد [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/).
   على سبيل المثال، يستخدم المثال أدناه قيمة [**ChartType.Pyramid**](https://reference.aspose.com/cells/nodejs-cpp/charttype) كنمط للمخطط.
1. الوصول إلى الكائن [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) الجديد من مجموعة [**Charts**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection) عن طريق تمرير فهرسه.
1. استخدم أي من كائنات المخطط الم encapsulate في كائن [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) لإدارة المخطط.
   يستخدم المثال أدناه كائن [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/) للمخطط لتحديد مصدر بيانات المخطط.

عند إضافة بيانات المصدر إلى الرسم البياني، يمكن أن يكون مصدر البيانات مجال خلايا (مثل "A1:C3")، أو تسلسل خلايا غير متجاورة (مثل "A1، A3، A5")، أو تسلسل من القيم (مثل "1،2،3").

تتيح لك هذه الخطوات العامة إنشاء أي نوع من الرسم البياني. استخدم كائنات الرسم البياني المختلفة لإنشاء رسوم بيانية مختلفة.

من الممكن إنشاء العديد من أنواع الرسوم البيانية المختلفة باستخدام Aspose.Cells. جميع الرسوم البيانية القياسية المدعومة بواسطة Aspose.Cells محددة مسبقًا في تعداد يسمى [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/).

تخطيطات الرسوم البيانية المحددة مسبقًا هي:

|**أنواع الرسوم البيانية**|**الوصف**|
| :- | :- |
|Column| يمثل مخطط الأعمدة المتجانبة
|ColumnStacked| يمثل مخطط الأعمدة المكدسة
|Column100PercentStacked| يمثل مخطط الأعمدة المكدسة بنسبة 100%
|Column3DClustered| يمثل مخطط الأعمدة المتجانبة ثلاثي الأبعاد
|Column3DStacked| يمثل مخطط الأعمدة المكدسة ثلاثي الأبعاد
|Column3D100PercentStacked| يمثل مخطط الأعمدة المكدسة بنسبة 100% ثلاثي الأبعاد
|Column3D| يمثل مخطط الأعمدة ثلاثي الأبعاد
|Bar| يمثل مخطط الأعمدة المتجانبة الأفقية
|BarStacked| يمثل مخطط الأعمدة المكدسة الأفقية
|Bar100PercentStacked| يمثل مخطط الأعمدة المكدسة بنسبة 100% الأفقية
|Bar3DClustered| يمثل مخطط الأعمدة المتجانبة ثلاثي الأبعاد الأفقية
|Bar3DStacked| يمثل مخطط الأعمدة المكدسة ثلاثي الأبعاد الأفقية
|Bar3D100PercentStacked| يمثل مخطط الأعمدة المكدسة بنسبة 100% ثلاثي الأبعاد الأفقية
|Line| يمثل مخطط الخطوط
|LineStacked| يمثل مخطط الخطوط المكدسة
|Line100PercentStacked| يمثل مخطط الخطوط المكدسة بنسبة 100%
|LineWithDataMarkers| يمثل مخطط الخط مع علامات البيانات
|LineStackedWithDataMarkers|تمثل مخطط خطوط مكدسة مع علامات البيانات|
|Line100PercentStackedWithDataMarkers|تمثل مخطط خطوط مكدسة 100% مع علامات البيانات|
|Line3D|تمثل مخطط خطوط ثلاثي الأبعاد|
|Pie|تمثل مخطط دائري|
|Pie3D|تمثل مخطط دائري ثلاثي الأبعاد|
|PiePie|تمثل مخطط دائري فوق الدائرة|
|PieExploded|تمثل مخطط دائري منفجر|
|Pie3DExploded|تمثل مخطط دائري منفجر ثلاثي الأبعاد|
|PieBar|تمثل مخطط بارز فوق القطعة من البيتزا|
|Scatter|تمثل مخطط النقاط|
|ScatterConnectedByCurvesWithDataMarker|تمثل مخطط النقاط متصلة بالخطوط المنحنية، مع علامات البيانات|
|ScatterConnectedByCurvesWithoutDataMarker|تمثل مخطط النقاط متصلة بالخطوط المنحنية، بدون علامات البيانات|
|ScatterConnectedByLinesWithDataMarker|تمثل مخطط النقاط متصلة بخطوط، مع علامات البيانات|
|ScatterConnectedByLinesWithoutDataMarker|تمثل مخطط النقاط متصلة بخطوط، بدون علامات البيانات|
|Area|تمثل مخطط المساحة|
|AreaStacked|تمثل مخطط المساحة المكدسة|
|Area100PercentStacked|تمثل مخطط المساحة المكدسة 100%|
|Area3D|تمثل مخطط المساحة ثلاثي الأبعاد|
|Area3DStacked|تمثل مخطط المساحة المكدسة ثلاثي الأبعاد|
|Area3D100PercentStacked|تمثل مخطط المساحة المكدسة 100% ثلاثي الأبعاد|
|Doughnut|يمثل مخطط الدونات|
|DoughnutExploded|يمثل مخطط الدونات المتفجر|
|Radar|يمثل مخطط الرادار|
|RadarWithDataMarkers|يمثل مخطط الرادار مع علامات البيانات|
|RadarFilled|يمثل مخطط الرادار المملوء|
|Surface3D|يمثل مخطط السطح ثلاثي الأبعاد|
|SurfaceWireframe3D|يمثل مخطط سطح ثلاثي الأبعاد بالأسلاك|
|SurfaceContour|يمثل مخطط التكهف|
|SurfaceContourWireframe|يمثل مخطط التكهف بالأسلاك|
|Bubble|يمثل مخطط الفقاعات|
|Bubble3D|يمثل مخطط الفقاعات ثلاثي الأبعاد|
|Cylinder|يمثل مخطط الأسطوانة|
|CylinderStacked|يمثل مخطط الأسطوانة المكدسة|
|Cylinder100PercentStacked|يمثل المخطط الأسطواني المكدس بنسبة 100٪|
|CylindericalBar|يمثل مخطط الأعمدة الأسطوانية|
|CylindericalBarStacked|يمثل مخطط الأعمدة الأسطوانية المكدسة|
|CylindericalBar100PercentStacked|يمثل المخطط الأسطواني المكدس بنسبة 100٪|
|CylindericalColumn3D|يمثل مخطط الأعمدة الأسطوانية ثلاثي الأبعاد|
|Cone|يمثل مخطط المخروط|
|ConeStacked|يمثل مخطط المخروط المكدس|
|Cone100PercentStacked|يمثل 100% حجم الرسم البياني المكدس المخروطي|
|ConicalBar|يمثل رسم بياني شريطي مخروطي|
|ConicalBarStacked|يمثل رسم بياني شريطي مكدس مخروطي|
|ConicalBar100PercentStacked|يمثل رسم بياني شريطي مخروطي مكدس بنسبة 100%|
|ConicalColumn3D|يمثل رسم بياني أعمدة مخروطي ثلاثي الأبعاد|
|Pyramid|يمثل رسم بياني الهرم|
|PyramidStacked|يمثل رسم بياني الهرم المكدس|
|Pyramid100PercentStacked|يمثل رسم بياني الهرم المكدس بنسبة 100%|
|PyramidBar|يمثل رسم بياني شريطي هرمي|
|PyramidBarStacked|يمثل رسم بياني شريطي هرمي مكدس|
|PyramidBar100PercentStacked|يمثل رسم بياني شريطي هرمي مكدس بنسبة 100%|
|PyramidColumn3D|يمثل رسم بياني أعمدة هرمي ثلاثي الأبعاد|
{{% alert color="primary" %}}

عندما تُسند نطاقًا من الخلايا كمصدر للبيانات، يمكنك تعيين النطاق فقط من الزاوية العلوية اليسرى إلى الزاوية السفلى اليمنى. على سبيل المثال، "A1:C3" صالح بينما "C3:A1" غير صالح.

{{% /alert %}}

#### **رسم بياني الهرم**

عند تنفيذ الشيفرة المرجعية، يتم إضافة رسم بياني للهرم إلى ورقة العمل.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Pyramid, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **رسم بياني خطي**

في المثال أعلاه، ببساطة تغيير [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) إلى *Line* ينشئ مخطط خطي. المصدر الكامل موفر أدناه. عند تنفيذ الكود، يتم إضافة مخطط خطي إلى ورقة العمل.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **رسم بياني فقاعي**

لإنشاء مخطط فقاعه، يجب إعداد [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) إلى [**ChartType.Bubble**](https://reference.aspose.com/cells/nodejs-cpp/charttype) وبعض الخصائص الإضافية مثل BubbleSizes و Values و XValues وفقًا لذلك. عند تنفيذ الكود التالي، يتم إضافة مخطط فقاعه إلى ورقة العمل.

#### **رسم بياني خطي بمؤشرات البيانات**

لإنشاء مخطط بخط مع علامة البيانات، يجب إعداد [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) إلى *ChartType.LineWithDataMarkers* وبعض الخصائص الإضافية مثل المنطقة الخلفية، علامات السلسلة، القيم و XValues وفقًا لذلك. عند تنفيذ الكود التالي، يتم إضافة مخطط بخط مع علامة البيانات إلى ورقة العمل.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set columns title 
worksheet.getCells().get(0, 0).putValue("X");
worksheet.getCells().get(0, 1).putValue("Y");

// Random data shall be used for generating the chart
// Create random data and save in the cells
for (let i = 1; i < 21; i++) {
worksheet.getCells().get(i, 0).putValue(i);
worksheet.getCells().get(i, 1).putValue(0.8);
}

for (let i = 21; i < 41; i++) {
worksheet.getCells().get(i, 0).putValue(i - 20);
worksheet.getCells().get(i, 1).putValue(0.9);
}
// Add a chart to the worksheet
const idx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

// Access the newly created chart
const chart = worksheet.getCharts().get(idx);

// Set chart style
chart.setStyle(3);

// Set autoscaling value to true
chart.setAutoScaling(true);

// Set foreground color white
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Set Properties of chart title
chart.getTitle().setText("Sample Chart");

// Set chart type
chart.setType(AsposeCells.ChartType.LineWithDataMarkers);

// Set Properties of categoryaxis title
chart.getCategoryAxis().getTitle().setText("Units");

//Set Properties of nseries
const s2_idx = chart.getNSeries().add("A2:A2", true);
const s3_idx = chart.getNSeries().add("A22:A22", true);

// Set IsColorVaried to true for varied points color
chart.getNSeries().setIsColorVaried(true);

// Set properties of background area and series markers
chart.getNSeries().get(s2_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s2_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Yellow);
chart.getNSeries().get(s2_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s2_idx).setXValues("A2:A21");
chart.getNSeries().get(s2_idx).setValues("B2:B21");

// Set properties of background area and series markers
chart.getNSeries().get(s3_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s3_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(s3_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s3_idx).setXValues("A22:A41");
chart.getNSeries().get(s3_idx).setValues("B22:B41");

// Save the workbook
workbook.save(path.join(dataDir, "LineWithDataMarkerChart.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **مواضيع متقدمة**
- [قراءة وتلاعب شكل بيانات Excel 2016](/cells/ar/nodejs-cpp/read-and-manipulate-excel-2016-charts/)
- [إدارة محاور مخططات Excel](/cells/ar/nodejs-cpp/chart-axes/)
- [ضبط مظهر الرسم البياني](/cells/ar/nodejs-cpp/setting-chart-appearance/)
- [أنواع المخططات](/cells/ar/nodejs-cpp/chart-types/)
- [تخصيص المخططات](/cells/ar/nodejs-cpp/customizing-charts/)
- [تعيين مصدر البيانات للمخطط](/cells/ar/nodejs-cpp/data-formatting-in-charts/)
- [إدارة تسميات البيانات في مخططات Excel](/cells/ar/nodejs-cpp/insert-datalabels-to-chart/)
- [الحصول على ورقة العمل من المخطط](/cells/ar/nodejs-cpp/get-worksheet-of-the-chart/)
- [إدارة الأسطورة في مخططات Excel](/cells/ar/nodejs-cpp/chart-legend/)
- [تلاعب بموقع وحجم وتصميم المخطط](/cells/ar/nodejs-cpp/manipulate-position-size-and-designer-chart/)
- [إنشاء مخطط دائري مع خطوط قيادة](/cells/ar/nodejs-cpp/creating-pie-chart-with-leader-lines/)
- [الأشكال في المخططات](/cells/ar/nodejs-cpp/controls-in-charts/)
- [إدارة عناوين مخططات Excel](/cells/ar/nodejs-cpp/chart-and-axis-titles/)
- [عرض الرسم البياني](/cells/ar/nodejs-cpp/chart-rendering/)
- [الحصول على نص المعادلة لخط اتجاه المخطط](/cells/ar/nodejs-cpp/get-equation-text-of-chart-trendline/)
{{< app/cells/assistant language="nodejs-cpp" >}}
