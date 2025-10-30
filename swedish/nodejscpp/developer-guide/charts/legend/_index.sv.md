---
title: Hantera legend för Excel diagram med Node.js via C++
description: Lär dig hur du använder Aspose.Cells for Node.js via C++ för att effektivt använda och anpassa diagramlegender i Microsoft Excel. Vår omfattande guide förklarar legendens funktion, hur man får tillgång till och modifierar den samt hur man förbättrar visualisering och dataförståelse med legender.
keywords: Aspose.Cells for Node.js via C++, Diagramlegender, Microsoft Excel, Visualisering, Dataförståelse.
linktitle: Teckenförklaring
type: docs
weight: 50
url: /sv/nodejs-cpp/chart-legend/
---

## **Teckenförklaringsalternativ**
Aspose.Cells for Node.js via C++ möjliggör också hantering av ett diagramlegende i realtid. Objektet [Legend](https://reference.aspose.com/cells/nodejs-cpp/legend/) kan flyttas, uppdateras och formateras.

|![todo:image_alt_text](chart_legend.png)|

## **Inställning av diagrammets teckenförklaring**
Det är enkelt att hantera diagramlegenden med Aspose.Cells [Legend](https://reference.aspose.com/cells/nodejs-cpp/legend/).

Följande kodsnutt visar hur man hanterar legenden:


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Move the legend to left
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Left);

// Set font color of the legend
chart.getLegend().getFont().setColor(AsposeCells.Color.Blue);

// Save the file
workbook.save("chart_legend.xlsx");
```

## **Fortsatta ämnen**
- [Ställ in texten för diagrammets teckenförklaringspostfyllning till ingen med hjälp av Aspose.Cells](/cells/sv/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
{{< app/cells/assistant language="nodejs-cpp" >}}
