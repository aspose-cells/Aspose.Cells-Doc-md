---
title: محور التاريخ مع Node.js عبر C++
description: تعلم كيفية إدارة محور التاريخ في Aspose.Cells for Node.js via C++. سيساعدك دليلنا على فهم كيفية العمل مع تنسيقات التاريخ المختلفة، مقاييس الزمن، وترددات تسميات العلامات.
keywords: Aspose.Cells لـ Node.js، محور التاريخ، إدارة، تنسيقات التاريخ، مقاييس الزمن، ترددات تسميات العلامات.
type: docs
weight: 200
url: /ar/nodejs-cpp/date-axis/
---

## **سيناريوهات الاستخدام المحتملة**
عند إنشاء مخطط من بيانات ورقة العمل يستخدم التواريخ، وتُرسَم التواريخ على طول المحور الأفقي (الفئة) في المخطط، يتغير Aspose.Cells for Node.js via C++ تلقائيًا ليحول محور الفئة إلى محور تاريخ (مقياس زمني).
يعرض محور التاريخ التواريخ وفقًا للترتيب الزمني بفواصل زمنية محددة أو وحدات قاعدية، مثل عدد الأيام، أو الأشهر، أو السنوات، حتى إذا كانت التواريخ على ورقة العمل ليست بترتيب تسلسلي أو بنفس الوحدات القاعدية.
افتراضيًا، تحدد Aspose.Cells الوحدات الأساسية لمحور التاريخ استنادًا إلى أصغر فرق بين أي تاريخين في بيانات ورقة العمل. على سبيل المثال، إذا كانت لديك بيانات لأسعار الأسهم حيث يكون أقل اختلاف بين التواريخ سبعة أيام، فإن Excel يضبط الوحدة الأساسية على أيام، ويمكنك تغيير الوحدة الأساسية إلى أشهر أو سنوات إذا رغبت في رؤية أداء السهم على مدى أطول.

## **معاملة محور التاريخ مثل Microsoft Excel**
 يرجى مراجعة رمز العينة التالي الذي ينشئ ملف إكسل جديد ويضع قيم الرسم البياني في ورقة العمل الأولى. 
ثم نضيف رسم بياني ونعين نوع الـ [**Axis**](https://reference.aspose.com/cells/nodejs-cpp/axis/) 
إلى [**Axis.getCategoryType()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getCategoryType--) ومن ثم نضبط الوحدات الأساسية على الأيام.

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
// Add the sample values to cells
worksheet.getCells().get("A1").putValue("Date");
// 14 means datetime format
const style = worksheet.getCells().getStyle();
style.setNumber(14);
// Put values to cells for creating chart
worksheet.getCells().get("A2").setStyle(style);
worksheet.getCells().get("A2").putValue(new Date(Date.UTC(2022, 5, 26)));
worksheet.getCells().get("A3").setStyle(style);
worksheet.getCells().get("A3").putValue(new Date(Date.UTC(2022, 4, 22)));
worksheet.getCells().get("A4").setStyle(style);
worksheet.getCells().get("A4").putValue(new Date(Date.UTC(2022, 7, 3)));
worksheet.getCells().get("B1").putValue("Price");
worksheet.getCells().get("B2").putValue(40);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(60);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 9, 6, 21, 13);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);         
// Set the Axis type to Date time
chart.getCategoryAxis().setCategoryType(AsposeCells.CategoryType.TimeScale);
// Set the base unit for CategoryAxis to days
chart.getCategoryAxis().setBaseUnitScale(AsposeCells.TimeUnit.Days);
// Set the direction for the axis text to be vertical
chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Vertical);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set max value of Y axis.
chart.getValueAxis().setMaxValue(70);
// Set major unit.
chart.getValueAxis().setMajorUnit(10);
// Save the file
workbook.save("DateAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
