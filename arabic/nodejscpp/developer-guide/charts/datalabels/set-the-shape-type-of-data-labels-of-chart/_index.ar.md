---
title: تعيين نوع الشكل لتسميات البيانات في المخططات باستخدام Node.js عبر C++
linktitle: تعيين نوع الشكل لتسميات بيانات الرسم البياني
description: تعلم كيفية تعيين نوع شكل تسميات البيانات في المخططات باستخدام Aspose.Cells for Node.js via C++. ستوضح لك هذه الدليل أنواع الأشكال المتاحة وكيفية اختيار الشكل المناسب لتسميات البيانات الخاصة بك لتعزيز العرض وسهولة الاستخدام.
keywords: Aspose.Cells for Node.js via C++، رسم بياني، تسميات بيانات، أنواع الأشكال، العرض التقديمي، سهولة الاستخدام.
type: docs
weight: 110
url: /ar/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك تغيير نوع شكل تسميات البيانات على الرسم البياني باستخدام خاصية `DataLabels.shapeType`. تأخذ قيمة من تعداد `DataLabelShapeType` وتغير نوع شكل تسميات البيانات وفقًا لذلك. بعض من قيمها هي

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **تعيين نوع الشكل لتسميات بيانات الرسم البياني**
يعرض الكود النموذجي التالي تغيير نوع شكل تسميات البيانات على الرسم البياني إلى `DataLabelShapeType.WedgeEllipseCallout`. يرجى الاطلاع على ملف Excel النموذجي [الملف](60489778.xlsx) المستخدم في هذا الكود وملف Excel الناتج [الملف](60489779.xlsx) الذي تم إنشاؤه بواسطة الكود. يُظهر لقطة شاشة تأثير الكود على ملف Excel النموذجي.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **الكود المثالي**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetShapeTypeOfDataLabelsOfChart.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Access first series
const series = chart.getNSeries().get(0);

// Set the shape type of data labels i.e. Speech Bubble Oval
series.getDataLabels().setShapeType(AsposeCells.DataLabelShapeType.WedgeEllipseCallout);

// Save the output Excel file
workbook.save(path.join(dataDir, "outputSetShapeTypeOfDataLabelsOfChart.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
