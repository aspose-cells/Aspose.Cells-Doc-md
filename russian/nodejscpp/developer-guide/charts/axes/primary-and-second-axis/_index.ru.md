---
title: Первичная и вторичная ось с помощью Node.js через C++
description: Узнайте, как понять и работать с первичными и вторичными осями в Aspose.Cells for Node.js via C++. Наш гид поможет вам понять различия между первичной и вторичной осями и как эффективно их настраивать и использовать в ваших диаграммах.
keywords: Aspose.Cells for Node.js via C++, первичные оси, вторичные оси, понимание, различия, настройка, использование.
type: docs
weight: 190
url: /ru/nodejs-cpp/primary-and-second-axis/
---

## **Возможные сценарии использования**
Когда числа в диаграмме значительно различаются в разных рядах данных, или когда у вас есть смешанные типы данных (цена и объем), отображайте один или несколько рядов данных на вторичной вертикальной (значений) оси. Масштаб вторичной вертикальной оси показывает значения соответствующих рядов данных. Вторичная ось работает хорошо в диаграмме, которая показывает комбинацию гистограмм и линейных диаграмм.

## **Работа с первичной и вторичной осями, как в Microsoft Excel**
Пожалуйста, посмотрите следующий пример кода, который создает новый Excel файл и помещает значения диаграммы в первый рабочий лист. 
Затем мы добавляем диаграмму и отображаем вторую ось.

![todo:image_alt_text](excel.png)

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
