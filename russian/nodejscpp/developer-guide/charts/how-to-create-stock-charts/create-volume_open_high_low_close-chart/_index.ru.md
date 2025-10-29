---
title: Создайте график акций Volume Open High Low Close (VOHLC) с помощью Node.js через C++
description: Узнайте, как создать график акций volume open high low close, используя Aspose.Cells for Node.js via C++. Наше руководство покажет, как отобразить данные фондового рынка, включая объем, открытые, максимальные, минимальные и закрывающие цены, на графике для лучшего анализа и визуализации.
keywords: Aspose.Cells for Node.js via C++, график акций Volume Open High Low Close, данные фондового рынка, анализ, визуализация.
type: docs
weight: 184
url: /ru/nodejs-cpp/create-volume-open-high-low-close-stock-chart/
---

## **Возможные сценарии использования**
Четвертый график акций — это график Volume Open High Low Close. Опять же, важно повторить, что данные должны быть в правильном порядке. Если необходимо переставить таблицу данных, сделайте это до настройки графика. Этот график включает столбец для объема сразу после первого (категорийного) столбца, а графики включают столбчатую диаграмму по первичной оси, показывающую этот объем, в то время как цены перемещены на вторичную ось.

![todo:image_alt_text](data.png)
## **График объема-открытия-максимума-минимума-закрытия (VHLC)**

![todo:image_alt_text](sample.png)
## **Образец кода**
Следующий образец кода загружает [образец excel-файла](Volume-Open-High-Low-Close.xlsx) и создает [выходной excel-файл](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Volume-Open-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeOpenHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Volume-Open-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:F9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set Color for the first series (Volume) data 
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(79, 129, 189));
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
