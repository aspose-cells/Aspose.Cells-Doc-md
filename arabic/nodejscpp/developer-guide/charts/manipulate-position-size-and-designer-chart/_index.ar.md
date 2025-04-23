---
title: تعديل الموقع والحجم وتصميم المخطط باستخدام Node.js عبر C++
linktitle: تلاعب بموقع الرسمة وحجمها وتصميم الرسم البياني
description: تعلّم كيفية استخدام Aspose.Cells for Node.js via C++ للتلاعب بشكل فعال بموقع، حجم وتصميم المخطط في Microsoft Excel. سيرشدك دليلنا إلى كيفية ضبط هذه الخصائص لتحسين التنسيق والتصور.
keywords: Aspose.Cells for Node.js via C++، الموقع، الحجم، تصميم المخطط، Microsoft Excel، التخطيط، التصور.
type: docs
weight: 45
url: /ar/nodejs-cpp/manipulate-position-size-and-designer-chart/
---

## **الموقع والحجم للرسم البياني**
أحيانًا، تريد تغيير موضع أو حجم المخطط الجديد أو الموجود داخل ورقة العمل. توفر Aspose.Cells الخاصية [Chart.getChartObject()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getChartObject--) لتحقيق ذلك. يمكنك استخدام خصائصها الفرعية لتغيير حجم المخطط بـ **الارتفاع** و **العرض** الجديدين أو إعادة موضعه باستخدام إحداثيات **X** و **Y** الجديدة.

### **التحكم في موقع الرسم البياني وحجمه**
لاستخدام هذه الخصائص وتغيير موقع الرسم البياني (إحداثيات X و Y) أو حجمه (ارتفاع وعرض):

1. [Shape.getX()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getX--)
1. [Shape.getY()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getY--)
1. [Shape.getHeight()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getHeight--)
1. [Shape.getWidth()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getWidth--)

يوضح المثال التالي كيفية استخدام واجهات برمجة التطبيقات المذكورة أعلاه؛ حيث يقوم بتحميل ملف العمل الموجود الذي يحتوي على مخطط في الأوراق الأولى. ثم يعيد تصغير وتغيير موضع المخطط باستخدام Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart.xls");

// Loads the workbook which contains the chart
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(1);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

// Resize the chart
chart.getChartObject().setWidth(400);
chart.getChartObject().setHeight(300);

// Reposition the chart
chart.getChartObject().setX(250);
chart.getChartObject().setY(150);

// Output the file
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **تلاعب الرسوم البيانية للمصمم**
في بعض الأحيان، تحتاج إلى التلاعب أو تعديل المخططات في ملفات نماذج المصمم. يدعم Aspose.Cells بشكل كامل التلاعب بمحتوى عناصر مخطط المصمم. يمكن الحفاظ على البيانات، محتوى المخطط، صورة الخلفية، والتنسيق بدقة.

### **تلاعب الرسوم البيانية لملفات القوالب المصممة**
لتلاعب بمخططات المصمم في ملفات القالب، استخدم واجهة برمجة التطبيقات المرتبطة بالمخطط. على سبيل المثال، يمكنك استخدام خاصية Worksheet.charts للحصول على مجموعة المخططات الموجودة في ملف القالب.

#### **إنشاء رسم بياني**
المثال التالي يوضح كيفية إنشاء رسم بياني هرمي. سوف نقوم بتلاعب بهذا الرسم لاحقًا.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
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
workbook.save(path.join(dataDir, "book1.out.xls"));
```

#### **تلاعب الرسم البياني**
المثال التالي يوضح كيفية تلاعب الرسم البياني الحالي. في هذا المثال، نقوم بتعديل الرسم البياني الذي تم إنشاؤه أعلاه. في الناتج المولد، لاحظ أن تسمية التاريخ لأحد نقاط البيانات تم تعيينها إلى 'المملكة المتحدة، 30 ألف'.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "piechart.xls");

// Loads the existing file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Get the data labels in the data series of the third data point.
const dataLabels = chart.getNSeries().get(0).getPoints().get(2).getDataLabels();

// Change the text of the label.
dataLabels.setText("Unided Kingdom, 400K ");

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

#### **تلاعب رسم بياني الخط في القالب المصمم**
في هذا المثال، سنقوم بتلاعب رسم بياني خطي. سنضيف بعض سلاسل البيانات إلى الرسم البياني الحالي وتغيير ألوان خطوطها.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Get the designer chart in the first worksheet.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Add the third data series to it.
chart.getNSeries().add("{60, 80, 10}", true);

// Add another data series (fourth) to it.
chart.getNSeries().add("{0.3, 0.7, 1.2}", true);

// Plot the fourth data series on the second axis.
chart.getNSeries().get(3).setPlotOnSecondAxis(true);

// Change the Border color of the second data series.
chart.getNSeries().get(1).getBorder().setColor(AsposeCells.Color.Green);

// Change the Border color of the third data series.
chart.getNSeries().get(2).getBorder().setColor(AsposeCells.Color.Red);

// Make the second value axis visible.
chart.getSecondValueAxis().setIsVisible(true);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

