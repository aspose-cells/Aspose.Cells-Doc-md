---
title: محور X مقابل محور الفئة باستخدام Node.js عبر C++
linktitle: المحور X مقابل محور الفئة
description: تعلم كيفية التمييز بين محور X ومحور الفئة في Aspose.Cells for Node.js via C++. سيساعدك دليلنا على فهم الاختلافات في الاستخدام والخصائص، وكيفية تكوينها وفقًا لاحتياجاتك.
keywords: Aspose.Cells for Node.js via C++، محور X، محور فئة، الاختلاف، الاستخدام، الخصائص، التكوين.
type: docs
weight: 180
url: /ar/nodejs-cpp/X-axis-vs-category-axis/
---

## **سيناريوهات الاستخدام المحتملة**
هناك أنواع مختلفة من المحاور X. بينما يكون المحور Y محور نوع قيمة، يمكن أن يكون المحور X محور نوع فئة أو محور نوع قيمة. باستخدام محور القيمة، يتم معاملة البيانات كبيانات عددية متغيرة بشكل مستمر، ويتم وضع العلامة في نقطة على طول المحور التي تتغير وفقًا لقيمتها العددية. باستخدام محور الفئة، يتم معاملة البيانات كسلسلة من علامات النص غير الرقمية، ويتم وضع العلامة في نقطة على طول المحور وفقًا لموقعها في التسلسل. يوضح المثال أدناه الفرق بين محاور القيمة والفئة.
يتم عرض البيانات العينية لدينا في [ملف الجدول العيني](sample.png) أدناه. تحتوي العمود الأول على بيانات محور X الخاصة بنا، والتي يمكن معاملتها كفئات أو قيم. لاحظ أن الأرقام ليست منتظمة بالتساوي، ولا تظهر حتى بترتيب عددي.

![todo:image_alt_text](sample.png)
## **قم بالتعامل مع المحور X ومحور الفئة على غرار Microsoft Excel**
 سنعرض هذه البيانات على نوعين من الرسوم البيانية، الرسم البياني الأول هو XY (نقطة الانتشار) مع المحور السيني كقيم، والرسم البياني الثاني هو مخطط خطي مع المحور السيني كتصنيف.

![todo:image_alt_text](compare.png)
## **الكود المثالي**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Put the sample values used in charts
worksheet.getCells().get("A2").putValue(1);
worksheet.getCells().get("A3").putValue(3);
worksheet.getCells().get("A4").putValue(2.5);
worksheet.getCells().get("A5").putValue(3.5);
worksheet.getCells().get("B1").putValue("Cats");
worksheet.getCells().get("C1").putValue("Dogs");
worksheet.getCells().get("D1").putValue("Fishes");
worksheet.getCells().get("B2").putValue(7);
worksheet.getCells().get("B3").putValue(6);
worksheet.getCells().get("B4").putValue(5);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("C2").putValue(7);
worksheet.getCells().get("C3").putValue(5);
worksheet.getCells().get("C4").putValue(4);
worksheet.getCells().get("C5").putValue(3);
worksheet.getCells().get("D2").putValue(8);
worksheet.getCells().get("D3").putValue(7);
worksheet.getCells().get("D4").putValue(3);
worksheet.getCells().get("D5").putValue(2);

// Create Line Chart: X as Category Axis
let pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 6, 15, 20, 21);
// Retrieve the Chart object
let chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$5");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);

// Create XY (Scatter) Chart: X as Value Axis
pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);
// Retrieve the Chart object
chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set X values for series 
chart.getNSeries().get(0).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(1).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(2).setXValues("{1,3,2.5,3.5}");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("XAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
