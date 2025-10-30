---
title: Skapa volym hög låg stäng aktiediagram med Node.js via C++
linktitle: Skapa Volym Öppen Hög Låg Stäng (VOHLC) Aktiediagram
description: Lär dig att skapa ett volym hög låg stäng aktiediagram med Aspose.Cells for Node.js via C++. Vår guide visar hur man plotterar aktiemarknadsdata, inklusive volym, hög, låg och stängningspriser, på ett diagram för bättre analys och visualisering.
keywords: Aspose.Cells for Node.js via C++, Volym Hög Låg Stäng Aktiediagram, Aktiemarknadsdata, Analys, Visualisering.
type: docs
weight: 183
url: /sv/nodejs-cpp/create-volume-high-low-close-stock-chart/
---

## **Möjliga användningsscenario**
Det tredje aktiediagrammet vi tittar på är Volym Hög Låg Stäng diagrammet. Återigen är det viktigt att upprepa att du måste ha data i rätt ordning. Om du behöver omorganisera din datatabell bör du göra det innan du skapar ditt diagram.
Detta diagram inkluderar en kolumn för volym direkt efter den första (kategori) kolumnen, och diagrammen innehåller ett kolumn-diagram på den primära axeln som visar denna volym, medan priserna flyttas till den sekundära axeln.

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
const filePath = path.join(dataDir, "Volume-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Volume-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set Color for the first series(Volume) data 
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(79, 129, 189));
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
