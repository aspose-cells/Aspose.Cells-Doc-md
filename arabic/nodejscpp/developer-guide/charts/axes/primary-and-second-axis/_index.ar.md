---
title: المحور الرئيسي والثانوي مع Node.js عبر C++
description: تعلم كيف تفهم وتعمل مع المحاور الرئيسية والثانوية في Aspose.Cells for Node.js via C++. سيساعدك دليلنا على فهم الاختلافات بين المحاور الرئيسية والثانوية وكيفية تكوينها واستخدامها بشكل فعال في مخططاتك.
keywords: Aspose.Cells for Node.js via C++، المحاور الرئيسية، المحاور الثانوية، الفهم، الاختلافات، التكوين، الاستخدام.
type: docs
weight: 190
url: /ar/nodejs-cpp/primary-and-second-axis/
---

## **سيناريوهات الاستخدام المحتملة**
عندما تتفاوت الأرقام في الرسم البياني بشكل كبير بين سلاسل البيانات، أو عندما تحتوي على أنواع مختلطة من البيانات (السعر والحجم)، ارسم سلسلة بيانات واحدة أو أكثر على محور عمودي (قيمة) ثانوي. مقياس المحور العمودي الثانوي يظهر القيم لسلاسل البيانات المرتبطة. يعمل المحور الثانوي بشكل جيد في رسم بياني يظهر فيه مزيج من رسوم الأعمدة والخطوط.

## **قم بالتعامل مع المحور الأساسي والثانوي على غرار Microsoft Excel**
 يرجى مراجعة رمز العينة التالي الذي ينشئ ملف إكسل جديد ويضع قيم الرسم البياني في ورقة العمل الأولى. 
ثم نضيف رسم بياني ونعرض المحور الثانوي.

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

// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Put the sample values used in a chart
worksheet.getCells().get("A1").putValue("Region");
worksheet.getCells().get("A2").putValue("Peking");
worksheet.getCells().get("A3").putValue("New York");
worksheet.getCells().get("A4").putValue("Paris");
worksheet.getCells().get("B1").putValue("Sales Volume");
worksheet.getCells().get("C1").putValue("Growth Rate");
worksheet.getCells().get("B2").putValue(100);
worksheet.getCells().get("B3").putValue(80);
worksheet.getCells().get("B4").putValue(140);
worksheet.getCells().get("C2").putValue(0.7);
worksheet.getCells().get("C3").putValue(0.8);
worksheet.getCells().get("C4").putValue(1.0);

// Create a Scatter chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Scatter, 6, 6, 15, 11);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:C4", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$4");
// Set the Second-Axis
chart.getNSeries().get(1).setPlotOnSecondAxis(true);
// Show the Second-Axis
chart.getSecondValueAxis().setIsVisible(true);
// Set the second series ChartType to line
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);
// Set the series name
chart.getNSeries().get(0).setName("Sales Volume");
chart.getNSeries().get(1).setName("Growth Rate");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the file
workbook.save("PrimaryandSecondaryAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
