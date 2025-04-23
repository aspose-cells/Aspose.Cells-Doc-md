---
title: Создать график акций Open High Low Close (OHLC) с помощью Node.js через C++
description: Узнайте, как создать график акций open high low close с помощью Aspose.Cells for Node.js via C++. Наш гид покажет, как отображать данные рынка акций, включая открытие, максимум, минимум и закрытие на диаграмме для лучшего анализа и визуализации.
keywords: Aspose.Cells for Node.js via C++, График акций с открытым, высоким, низким и закрытым ценами, данные фондового рынка, анализ, визуализация.
type: docs
weight: 182
url: /ru/nodejs-cpp/create-open-high-low-close-stock-chart/
---

## **Возможные сценарии использования**
График цен акций Open-High-Low-Close (OHLC) использует пять столбцов данных по порядку: категория, открытие, максимум, минимум и закрытие. Диапазон цен в каждой категории снова указан вертикальной линией, а интервал между открытием и закрытием отображается более широким плавающим баром; если цена увеличивается в категории (закрытие выше открытия), бар заполняется одним цветом, а если цена уменьшается, бар заполняется другим. Этот тип графика часто называется графиком свечей.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Улучшения видимости на графике**
Мы часто используем цвета, а не черно-белую палитру, чтобы обозначить рост и снижение цен. В первом наборе свечей ниже красный показывает рост, а зеленый — снижение цен.

![todo:image_alt_text](sample2.png)
## **Образец кода**
Нижеприведенный образец кода загружает [образец файла Excel](Open-High-Low-Close.xlsx) и генерирует [файл Excel вывода](out.xlsx).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Open-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockOpenHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Open-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E9", true);
// Set category data 
chart.getNSeries().getCategoryData("A2:A9");
// Set the DownBars and UpBars with different color
chart.getNSeries().get(0).getDownBars().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(0).getUpBars().getArea().setForegroundColor(AsposeCells.Color.Red);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
