---
title: تحديد مظهر المخطط باستخدام Node.js عبر C++
description: تعلم كيفية تكوين مظهر المخططات في Aspose.Cells for Node.js via C++. ستظهر لك دليلك كيفية تعديل تخطيطات المخططات، والألوان، والخطوط، والتأثيرات لتحقيق النمط البصري المرغوب فيه وتعزيز أوراق العمل الخاصة بك.
keywords: Aspose.Cells for Node.js via C++، المخططات، مظهر المخطط، التخطيطات، الألوان، الخطوط، التأثيرات، أوراق العمل.
linktitle: تنسيق الرسم البياني
type: docs
weight: 20
url: /ar/nodejs-cpp/setting-chart-appearance/
---

## **ضبط مظهر الرسم البياني**
في كيفية إنشاء رسم بياني أعطينا مقدمة موجزة عن أنواع الرسوم البيانية وكائنات الرسم البياني التي تقدمها Aspose.Cells، ووصفنا كيفية إنشاء واحد. يتناول هذا المقال كيفية تخصيص مظهر الرسوم البيانية عن طريق تعيين خصائصها:

- تعيين منطقة الرسم البياني.
- تعيين خطوط الرسم البياني.
- تطبيق السمات.
- تعيين عناوين للرسوم البيانية والمحاور.
- العمل مع خطوط الشبكة.

### **تعيين منطقة الرسم البياني**
هناك أنواع مختلفة من المناطق في رسم بياني وتوفر Aspose.Cells قدرة للمطورين على تعديل مظهر كل منطقة. يمكن للمطورين تطبيق إعدادات تنسيق مختلفة على منطقة عن طريق تغيير لون الأمامية والخلفية وتنسيق الملء وما إلى ذلك.

في المثال الوارد أدناه، قمنا بتطبيق إعدادات تنسيق مختلفة على أنواع مختلفة من المناطق في رسم بياني. هذه المناطق تشمل:

- منطقة الرسم
- منطقة الرسم البياني
- منطقة مجموعات السلاسل
- منطقة نقطة واحدة في مجموعة سلاسل

الكود البرمجي التالي يوضح كيفية ضبط منطقة الرسم البياني.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

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

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(new AsposeCells.Color(0, 0, 255));

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(new AsposeCells.Color(255, 255, 0));

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(255, 0, 0));

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(new AsposeCells.Color(0, 255, 255));

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(new AsposeCells.Color(0, 255, 0), 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **تعيين خطوط الرسم البياني**
يمكن للمطورين أيضًا تطبيق أنواع مختلفة من الأنماط على الخطوط أو علامات البيانات في [SeriesCollection](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/). يوضح مقتطف الشفرة التالي كيفية تعيين خطوط المخطط باستخدام API الخاص بـ Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

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

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Applying a dotted line style on the lines of a SeriesCollection
chart.getNSeries().get(0).getBorder().setStyle(AsposeCells.LineType.Dot);

// Applying a triangular marker style on the data markers of a SeriesCollection
chart.getNSeries().get(0).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Triangle);

// Setting the weight of all lines in a SeriesCollection to medium
chart.getNSeries().get(1).getBorder().setWeight(AsposeCells.WeightType.MediumLine);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **تطبيق سمات مايكروسوفت اكسيل 2007/2010 على الرسوم البيانية**
يمكن للمطورين تطبيق سمات/ألوان مختلفة من Microsoft Excel على [SeriesCollection](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/) أو كائنات مخططات أخرى كما هو موضح في المثال أدناه.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_chart.xlsx");

// Loads the workbook containing the chart
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the first chart in the sheet
const chart = worksheet.getCharts().get(0);

// Specify the FillFormat's type to Solid Fill of the first series
chart.getNSeries().get(0).getArea().getFillFormat().setFillType(AsposeCells.FillType.Solid);

// Get the CellsColor of SolidFill
const cc = chart.getNSeries().get(0).getArea().getFillFormat().getSolidFill().getCellsColor();

// Create a theme in Accent style
cc.setThemeColor(new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent6, 0.6));

// Apply the theme to the series
chart.getNSeries().get(0).getArea().getFillFormat().getSolidFill().setCellsColor(cc);

// Save the Excel file
workbook.save(path.join(dataDir, "output.out.xlsx"));
```

### **ضبط عناوين الرسوم البيانية أو المحاور**
يمكنك استخدام Microsoft Excel لضبط عناوين المخطط ومحاورها في بيئة WYSIWYG. كما يسمح Aspose.Cells للمطورين بضبط عناوين المخطط ومحاوره أثناء التشغيل. تحتوي جميع المخططات ومحاورها على خاصية [Title](https://reference.aspose.com/cells/nodejs-cpp/title/) والتي يمكن استخدامها لضبط عناوينها كما هو موضح في مثال أدناه.

الرمز التالي يوضح كيفية ضبط عناوين المخططات والمحاور.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

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

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Setting the title of category axis of the chart
chart.getCategoryAxis().getTitle().setText("Category");

// Setting the title of value axis of the chart
chart.getValueAxis().getTitle().setText("Value");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **العمل مع خطوط الشبكة الرئيسية**
من الممكن تخصيص شكل خطوط الشبكة الرئيسية. يمكن إخفاء أو إظهار خطوط الشبكة أو تحديد لونها وإعدادات أخرى. فيما يلي، نُوضّح كيفية إخفاء خطوط الشبكة وكيفية تغيير لونها.

#### **إخفاء خطوط الشبكة الرئيسية**
يمكن للمطورين التحكم في رؤية خطوط الشبكة الكبرى من خلال تعيين خاصية [isVisible()](https://reference.aspose.com/cells/nodejs-cpp/line/#isVisible--) لكائن [Line](https://reference.aspose.com/cells/nodejs-cpp/line/) إلى **true** أو **false**.

يوضح مقتطف الشفرة التالي كيفية إخفاء خطوط الشبكة الكبرى. بعد إخفاء خطوط الشبكة الكبيرة، سيتم إضافة مخطط عمودي إلى ورقة العمل بدون خطوط شبكة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

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

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Hiding the major gridlines of Category Axis
chart.getCategoryAxis().getMajorGridLines().setIsVisible(false);

// Hiding the major gridlines of Value Axis
chart.getValueAxis().getMajorGridLines().setIsVisible(false);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

#### **تغيير إعدادات خطوط الشبكة الرئيسية**
لا يستطيع المطورون فقط التحكم في رؤية خطوط الشبكة الرئيسية ولكن أيضًا خصائص أخرى بما في ذلك لونها وما إلى ذلك.

يوضح مقتطف الشفرة التالي كيفية تغيير لون خطوط الشبكة الكبرى. بعد تعيين لون خطوط الشبكة الكبرى، سيتم إضافة مخطط عمودي إلى ورقة العمل مع خطوط شبكة معدلة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

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

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Setting the color of Category Axis' major gridlines to silver
chart.getCategoryAxis().getMajorGridLines().setColor(AsposeCells.Color.Silver);

// Setting the color of Value Axis' major gridlines to red
chart.getValueAxis().getMajorGridLines().setColor(AsposeCells.Color.Red);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **مواضيع متقدمة**
- [تعيين رمز تنسيق القيم لسلاسل الرسم البياني](/cells/ar/nodejs-cpp/set-the-values-format-code-of-chart-series/)
- [تعيين صورة كحشو خلفية في الرسم البياني](/cells/ar/nodejs-cpp/set-picture-as-background-fill-in-the-chart/)


{{< app/cells/assistant language="nodejs-cpp" >}}
