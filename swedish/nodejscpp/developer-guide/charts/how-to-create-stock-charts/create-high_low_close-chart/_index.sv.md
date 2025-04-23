---  
title: Skapa High Low Close(HLC) aktiediagram med Node.js via C++  
linktitle: Skapa High Low Close (HLC) Stock Chart  
description: Lär dig hur man skapar ett High Low Close aktiediagram med Aspose.Cells for Node.js via C++. Vår steg för steg guide visar hur man plottar aktiemarknadsdata, inklusive höga, låga och stängningspriser, på ett diagram för bättre analys och visualisering.  
keywords: Aspose.Cells för Node.js, High Low Close aktiediagram, Aktiemarknadsdata, Analys, Visualisering.  
type: docs  
weight: 181  
url: /sv/nodejs-cpp/create-high-low-close-stock-chart/  
---  

## **Möjliga användningsscenario**  
 High-Low-Close (HLC) aktiediagram använder fyra kolumner av data. Den första kolumnen är en kategori, oftast ett datum men aktie namn kan också användas. Nästa tre kolumner är för höga, låga och stängningspriser. Prisintervallet för varje kategori indikeras av en vertikal linje från lågt till högt, och stängningspriset visas med ett tickmärke som sträcker sig till höger om denna linje.  

![todo:image_alt_text](sample.png)  
## **Synlighetsförbättringar i diagrammet**  
Ibland, för att göra diagrammet mer intuitivt, kan vi ändra utseendet på markören (stäng) eller få den att visas på den sekundära axeln.  

![todo:image_alt_text](sample2.png)  
## **Exempelkod**  
Följande exempelkod laddar [exempel Excel-filen](High-Low-Close.xlsx) och genererar [utdatamappar Excel-filen](out.xlsx).  

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

