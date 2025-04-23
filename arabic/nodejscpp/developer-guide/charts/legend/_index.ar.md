---
title: إدارة أسطورة مخططات إكسل باستخدام Node.js عبر C++
description: تعلّم كيفيّة استخدام Aspose.Cells for Node.js via C++ للاستفادة بشكل فعال وتخصيص أساطير المخططات في Microsoft Excel. يشرح دليلنا الشامل وظيفة الأسطورة، كيفية الوصول إليها وتعديلها، بالإضافة إلى تحسين التصور وفهم البيانات باستخدام الأساطير.
keywords: Aspose.Cells for Node.js via C++، أساطير المخططات، Microsoft Excel، التصور، فهم البيانات.
linktitle: أسطورة
type: docs
weight: 50
url: /ar/nodejs-cpp/chart-legend/
---

## **خيارات الأسطورة**
 تتيح Aspose.Cells for Node.js via C++ أيضًا إدارة أسطورة المخطط أثناء التشغيل. يمكن نقل، وتحديث، وتنسيق كائن [Legend](https://reference.aspose.com/cells/nodejs-cpp/legend/).

|![todo:image_alt_text](chart_legend.png)|

## **ضبط أسطورة الرسم البياني**
من السهل إدارة أسطورة المخطط باستخدام Aspose.Cells [Legend](https://reference.aspose.com/cells/nodejs-cpp/legend/).

يوضح مقتطف الكود التالي كيفية إدارة الأسطورة:


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

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

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Move the legend to left
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Left);

// Set font color of the legend
chart.getLegend().getFont().setColor(AsposeCells.Color.Blue);

// Save the file
workbook.save("chart_legend.xlsx");
```

## **مواضيع متقدمة**
- [ضبط نص إدخال وسام الرسم البياني على لا شيء باستخدام Aspose.Cells](/cells/ar/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
