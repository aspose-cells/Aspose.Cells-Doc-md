---
title: Skapa Open High Low Close(OHLC) aktiediagram med Node.js via C++
description: Lär dig hur man skapar ett öppet högt lågt stäng aktiediagram med Aspose.Cells for Node.js via C++. Vår guide visar hur man plottar aktiemarknadsdata, inklusive öppnings, högsta, lägsta och stängningspriser, på ett diagram för bättre analys och visualisering.
keywords: Aspose.Cells for Node.js via C++, Öppna Hög Lågt Stäng Aktiediagram, Aktiemarknadsdata, Analys, Visualisering.
type: docs
weight: 182
url: /sv/nodejs-cpp/create-open-high-low-close-stock-chart/
---

## **Möjliga användningsscenario**
Det öppen-hög-låg-stänga (OHLC) diagrammet använder fem datakolumner, i ordning: kategori, öppen, hög, låg och stänga. Prisintervallet i varje kategori indikeras igen av en vertikal linje, medan intervallet mellan öppen och stänga ges av en bredare stångformad stapel; om priset ökar i kategorin (stänga är högre än öppen), fylls stapeln med en färg, medan om priset minskar, fylls stapeln med en annan färg. Den här typen av diagram kallas ofta ett ljusstakdiagram.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Synlighetsförbättringar i diagrammet**
Vi använder ofta färger snarare än svart och vitt för att indikera ökande och minskande priser. I den första uppsättningen av candlesticks nedan visar rött stigande priser och grönt fallande priser.

![todo:image_alt_text](sample2.png)
## **Exempelkod**
Följande exempelkod laddar den [exempelfil för Excel](Open-High-Low-Close.xlsx) och genererar den [utfärdade Excelfilen](out.xlsx).

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
{{< app/cells/assistant language="nodejs-cpp" >}}
