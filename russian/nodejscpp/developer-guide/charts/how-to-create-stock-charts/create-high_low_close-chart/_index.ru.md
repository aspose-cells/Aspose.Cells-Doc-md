---  
title: Создать график акций High Low Close (HLC) с помощью Node.js через C++  
linktitle: Создание диаграммы акций HLC (High Low Close)  
description: Узнайте, как создать график акций High Low Close, используя Aspose.Cells for Node.js via C++. Наш пошаговый гид покажет, как отображать данные рынка акций, включая высшие, низшие и закрывающие цены, на диаграмме для лучшего анализа и визуализации.  
keywords: Aspose.Cells для Node.js, график акций High Low Close, данные рынка акций, анализ, визуализация.  
type: docs  
weight: 181  
url: /ru/nodejs-cpp/create-high-low-close-stock-chart/  
---  

## **Возможные сценарии использования**  
График акций High-Low-Close (HLC) использует четыре столбца данных. Первый столбец — категория, обычно дата, но можно использовать и имена акций. Далее идут три столбца для высоких, низких и закрывающих цен. Диапазон цен для каждой категории обозначается вертикальной линией от низкого до высокого, а цена закрытия отображается с помощью метки, простирающейся вправо от этой линии.  

![todo:image_alt_text](sample.png)  
## **Улучшения видимости на графике**  
Иногда, чтобы сделать график более интуитивно понятным, мы можем изменить внешний вид маркера (закрытия) или отображать его на вторичной оси.  

![todo:image_alt_text](sample2.png)  
## **Образец кода**  
Нижеприведенный образец кода загружает [образец файла Excel](High-Low-Close.xlsx) и генерирует [файл Excel вывода](out.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:D9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set the marker with the built-in data 
chart.getNSeries().get(2).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Dash);
chart.getNSeries().get(2).getMarker().setMarkerSize(20);
chart.getNSeries().get(2).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(2).getMarker().getArea().setForegroundColor(AsposeCells.Color.Maroon);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

