---
title: Ось X против категориальной оси с помощью Node.js через C++
linktitle: Ось X против категориальной оси
description: Узнайте, как различать ось X и категориальную ось в Aspose.Cells for Node.js via C++. Наш гид поможет понять различия в их использовании и свойствах, а также как настраивать их в соответствии с вашими требованиями.
keywords: Aspose.Cells for Node.js via C++, ось X, категориальная ось, различие, использование, свойства, настройка.
type: docs
weight: 180
url: /ru/nodejs-cpp/X-axis-vs-category-axis/
---

## **Возможные сценарии использования**
Существуют разные типы осей X. В то время как ось Y является осью типа значения, ось X может быть осью типа категории или осью типа значения. Используя ось значения, данные рассматриваются как непрерывно изменяющиеся числовые данные, и маркер располагается в точке вдоль оси, которая изменяется в соответствии с их числовым значением. Используя категориальную ось, данные рассматриваются как последовательность нечисловых текстовых меток, и маркер располагается в точке вдоль оси в соответствии с ее положением в последовательности. Приведенный ниже пример иллюстрирует разницу между осями значения и категории.
Наши примерные данные показаны в [файле примеров таблиц](sample.png) ниже. Первый столбец содержит наши данные оси X, которые могут рассматриваться как категории или как значения. Обратите внимание, что числа не равномерно распределены, и они даже не появляются в числовом порядке.

![todo:image_alt_text](sample.png)
## **Обрабатывайте ось X и категориальную ось, подобно Microsoft Excel**
Мы отобразим эти данные на двух типах диаграмм, первая - XY (точечная) с осью X как осью значений, вторая - линейная с осью X как категориальной.

![todo:image_alt_text](compare.png)
## **Образец кода**
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
