---
title: Ось Z с помощью Node.js через C++
description: Узнайте, как работать с осью Z в Aspose.Cells for Node.js via C++. Наш гид поможет вам понять, как настроить и кастомизировать ось Z, включая масштаб и метки, для улучшения ваших диаграмм.
keywords: Aspose.Cells for Node.js via C++, ось Z, создание графиков, настройка, кастомизация, масштаб, метки.
type: docs
weight: 210
url: /ru/nodejs-cpp/z-axis/
---

## **Возможные сценарии использования**
Для некоторых 3D-диаграмм, таких как 3D-колонка, 3D-конус или 3D-пирамида, у которых есть ось глубины (серии), также называемая осью Z, которую вы можете изменить. Вы можете задать интервал между метками, метки оси и другие операции.

## **Обработка первичных и вторичных осей, как в Microsoft Excel**
Пожалуйста, посмотрите следующий пример кода, который создает новый Excel файл и помещает значения диаграммы в первый рабочий лист. Затем добавляется диаграмма с типом Column3D, и вы можете увидеть ось Z, также называемую глубиной. 

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
