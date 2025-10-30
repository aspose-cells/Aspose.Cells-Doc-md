---  
title: Hur man skapar ett TreeMap diagram med Node.js via C++  
linktitle: Hur man skapar Träddiagramdiagram  
description: Lär dig hur du skapar ett Treemap diagram i Aspose.Cells for Node.js via C++. Vår guide hjälper dig att förstå de olika egenskaper och formateringsalternativ som är tillgängliga för Treemap diagram, inklusive färger, etiketter och datagenerering.  
keywords: Aspose.Cells för Node.js, Treemap diagram, skapa, egenskaper, formatering, färger, etiketter, datagenerering, cirkeldiagram, hierarkisk diagramning.  
type: docs  
weight: 161  
url: /sv/nodejs-cpp/creating-treemap-chart/  
---  

## **Möjliga användningsscenario**  
Ett träd-diagram ger en hierarkisk vy av dina data och gör det lätt att upptäcka mönster, till exempel vilka objekt som är bästsäljare i en butik. Trädstammarna representeras av rektanglar och varje underavdelning visas som en mindre rektangel. Träddiagrammet visar kategorier med färg och närhet och kan enkelt visa mycket data som skulle vara svårt med andra diagramtyper.  

![todo:image_alt_text](sample.png)  
## **Träddiagram**  
Efter att ha kört koden nedan kommer du att se träddiagrammet som visas nedan.  

![todo:image_alt_text](result.png)  
## **Exempelkod**  
Följande exempelkod laddar den [prov Excel-fil](treemap.xlsx) och genererar [utdata Excel-fil](ut.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "treemap.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Treemap, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("TreeMap Chart");
// Add series data range(D2:D13,actually)
chart.getNSeries().add("D2:F13", true);
// Set category data(A2:A13 is incorrect )
chart.getNSeries().setCategoryData("A2:C13");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
