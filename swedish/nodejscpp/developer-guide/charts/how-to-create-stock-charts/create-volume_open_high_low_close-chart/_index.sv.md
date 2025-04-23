---
title: Skapa volym öppna hög låg stäng aktiediagram med Node.js via C++
description: Lär dig att skapa ett volym öppna hög låg stäng aktiediagram med Aspose.Cells for Node.js via C++. Vår guide visar hur man plotterar aktiemarknadsdata, inklusive volym, öppning, hög, låg och stängningspriser, på ett diagram för bättre analys och visualisering.
keywords: Aspose.Cells for Node.js via C++, Volym Öppna Hög Låg Stäng Aktiediagram, Aktiemarknadsdata, Analys, Visualisering.
type: docs
weight: 184
url: /sv/nodejs-cpp/create-volume-open-high-low-close-stock-chart/
---

## **Möjliga användningsscenario**
Det fjärde aktiediagrammet vi tittar på är Volume Open High Low Close-diagrammet. Återigen är det viktigt att påpeka att du måste ha data i rätt ordning. Om du behöver omarrangera din datatabell bör du göra det innan du skapar diagrammet. Detta diagram inkluderar en kolumn för volym precis efter den första (kategori-) kolumnen, och diagrammen inkluderar ett kolumndiagram på primäraxeln som visar denna volym, medan priserna flyttas till sekundäraxeln.

![todo:image_alt_text](data.png)
## **Volym-Öppen-Hög-Låg-Stäng (VOHLC) aktiediagram**

![todo:image_alt_text](sample.png)
## **Exempelkod**
Följande exempelkod laddar den [exempelfil för Excel](Volume-Open-High-Low-Close.xlsx) och genererar den [utfärdade Excelfilen](out.xlsx).

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
