---
title: Hur man skapar ett Sunburst diagram med Node.js via C++
linktitle: Hur man skapar Solifjäderdiagram
description: Lär dig hur du skapar ett sunburst diagram i Aspose.Cells for Node.js via C++, ett diagram som presenterar data i en cirkel. Vår guide hjälper dig att ställa in olika egenskaper och formatering av ditt diagram, inklusive datapresentation, legender, färger och mer.
keywords: Aspose.Cells for Node.js via C++, sunburst diagram, skapa, ställ in egenskaper, datapresentation, legend, format, färg, cirkel, datarendering.
type: docs
weight: 162
url: /sv/nodejs-cpp/creating-sunburst-chart/
---

## **Möjliga användningsscenario**
Treemap-diagram är bra för att jämföra proportioner inom hierarkin; dock är treemap-diagram inte bra på att visa hierarkiska nivåer mellan de största kategorierna och varje datapunkt. Ett sunburst-diagram är mycket bättre för att visa detta. Sunburst-diagrammet är idealiskt för att visa hierarkiska data. Varje nivå av hierarkin representeras av en ring eller cirkel, där den innersta cirkeln är toppen av hierarkin. Ett sunburst-diagram utan hierarkiska data (en nivå av kategorier) liknar ett hålkakardiagram. Men ett sunburst-diagram med flera kategorinivåer visar hur de yttre ringarna relaterar till de inre. Sunburst-diagrammet är mest effektivt för att visa hur en ring är uppdelad i dess bidragande delar, medan en annan typ av hierarkiskt diagram, treemap, är idealiskt för att jämföra relativa storlekar.

![todo:image_alt_text](sample.png)
## **Solfjäderdiagram**
Efter att ha kört koden nedan kommer du att se solfjäderdiagrammet som visas nedan.

![todo:image_alt_text](result.png)
## **Exempelkod**
Följande exempelkod läser in [provkalkylbladet](sunburst.xlsx) och genererar [utmatningskalkylbladet](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sunburst.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Sunburst Chart");
// Add series data range
chart.getNSeries().add("D2:D16", true);
// Set category data (A2:A16 is incorrect, as hierarchical category)
chart.getNSeries().setCategoryData("A2:C16");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
