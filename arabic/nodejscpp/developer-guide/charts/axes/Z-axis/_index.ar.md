---
title: محور Z باستخدام Node.js عبر C++
description: تعلم كيفية العمل مع محور Z في Aspose.Cells for Node.js via C++. سيساعدك دليلنا على فهم كيفية تكوين وتخصيص محور Z، بما في ذلك مقياسه وتسمياته، لتعزيز مخططاتك.
keywords: Aspose.Cells for Node.js via C++، محور Z، الرسومات، التكوين، التخصيص، المقياس، التسميات.
type: docs
weight: 210
url: /ar/nodejs-cpp/z-axis/
---

## **سيناريوهات الاستخدام المحتملة**
بالنسبة لبعض المخططات ثلاثية الأبعاد مثل الأعمدة ثلاثية الأبعاد، المخروط ثلاثي الأبعاد، أو الهرم ثلاثي الأبعاد الذي يحتوي على محور العمق (السلسلة)، المعروف أيضًا باسم محور Z، والذي يمكن تغييره. يمكنك تحديد الفاصل الزمني بين علامات الترقيم، وتسميات المحور، وعمليات أخرى.

## **معالجة المحاور الرئيسية والثانوية مثل Microsoft Excel**
يرجى مراجعة الكود النموذجي التالي الذي ينشئ ملف Excel جديد ويرتب قيم المخطط في الورقة الأولى. ثم نضيف مخططًا ونحدد نوع المخطط ليكون Column3D، ويمكنك رؤية محور Z أيضًا المسمى محور العمق. 

![todo:image_alt_text](excel.png)

## **الكود المثالي**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Put values to cells for creating chart
worksheet.getCells().get("A1").putValue("A");
worksheet.getCells().get("B1").putValue("B");
worksheet.getCells().get("C1").putValue("C");
worksheet.getCells().get("A2").putValue(2);
worksheet.getCells().get("A3").putValue(1);
worksheet.getCells().get("B2").putValue(2);
worksheet.getCells().get("B3").putValue(3);
worksheet.getCells().get("C2").putValue(2);
worksheet.getCells().get("C3").putValue(3);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column3D, 9, 6, 25, 16);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Calculate the chart
chart.calculate();
// Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
chart.setChartDataRange("A2:C3", true);
// Hide the CategoryAxis axis
chart.getCategoryAxis().setIsVisible(false);
// Hide the ValueAxis axis
chart.getValueAxis().setIsVisible(false);
// Save the file
workbook.save("ZAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
