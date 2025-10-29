---
title: إدارة عناوين مخططات Excel باستخدام Node.js عبر C++
description: تعلم كيفية استخدام Aspose.Cells for Node.js via C++ لإضافة وتنسيق عناوين المخططات والمحاور في Microsoft Excel. سيظهر دليلنا كيفية تعيين أنواع مختلفة من العناوين، وتعديل مظهرها، وتغيير عناوين المحاور لتحسين تمثيل البيانات ووضوحها.
keywords: Aspose.Cells for Node.js via C++، عناوين المخطط، عناوين المحاور، Microsoft Excel، تمثيل البيانات، المظهر.
linktitle: العناوين
type: docs
weight: 50
url: /ar/nodejs-cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

في رسوم بيانية Excel، هناك نوعان من العناوين:
1. عنوان الرسم البياني 
1. عناوين المحاور

{{% /alert %}}

## **خيارات العنوان**
كما يسمح Aspose.Cells for Node.js via C++ بإدارة عناوين المخططات في وقت التشغيل. باستخدام كائن [Title](https://reference.aspose.com/cells/nodejs-cpp/title/)، يمكنك تغيير النص، والخط، وتنسيق التعبئة للعناوين.

|![todo:image_alt_text](chart_title.png)|

## **ضبط عناوين الرسوم البيانية أو المحاور**
 يمكنك استخدام Microsoft Excel لضبط عناوين مخططك ومحاورك في بيئة WYSIWYG. كما يتيح Aspose.Cells for Node.js via C++ للمطورين ضبط عناوين المخطط ومحاوره في وقت التشغيل. تحتوي جميع المخططات ومحاورها على خاصية [Title](https://reference.aspose.com/cells/nodejs-cpp/title/) التي يمكن استخدامها لضبط عناوينها كما هو موضح في المثال أدناه.

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

## **مواضيع متقدمة**
- [قراءة عنوان الرسم البياني من ملف ODS](/cells/ar/nodejs-cpp/read-chart-subtitle-from-ods-file/)
{{< app/cells/assistant language="nodejs-cpp" >}}
