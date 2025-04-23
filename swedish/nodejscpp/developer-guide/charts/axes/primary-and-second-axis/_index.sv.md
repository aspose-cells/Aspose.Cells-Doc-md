---
title: Primär och sekundär axel med Node.js via C++
description: Lär dig hur du förstår och arbetar med primära och sekundära axlar i Aspose.Cells for Node.js via C++. Vår guide hjälper dig att förstå skillnaderna mellan primära och sekundära axlar, samt hur du konfigurerar och använder dem effektivt i dina diagram.
keywords: Aspose.Cells for Node.js via C++, primära axlar, sekundära axlar, förståelse, skillnader, konfiguration, användning.
type: docs
weight: 190
url: /sv/nodejs-cpp/primary-and-second-axis/
---

## **Möjliga användningsscenario**
När siffrorna i ett diagram varierar kraftigt mellan data serier eller när du har blandade typer av data (pris och volym), plotta en eller flera data serier på en sekundär vertikal (värde) axel. Skalan för den sekundära vertikala axeln visar värdena för de associerade data serierna. En sekundär axel fungerar bra i ett diagram som visar en kombination av stapel- och linjediagram.

## **Hantera primär- och sekundäraxel som i Microsoft Excel**
Se följande kodexempel som skapar en ny Excel-fil och placerar diagramvärden i det första arket. 
Sedan lägger vi till ett diagram och visar den sekundära axeln.

![todo:image_alt_text](excel.png)

## **Exempelkod**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Put the sample values used in a chart
worksheet.getCells().get("A1").putValue("Region");
worksheet.getCells().get("A2").putValue("Peking");
worksheet.getCells().get("A3").putValue("New York");
worksheet.getCells().get("A4").putValue("Paris");
worksheet.getCells().get("B1").putValue("Sales Volume");
worksheet.getCells().get("C1").putValue("Growth Rate");
worksheet.getCells().get("B2").putValue(100);
worksheet.getCells().get("B3").putValue(80);
worksheet.getCells().get("B4").putValue(140);
worksheet.getCells().get("C2").putValue(0.7);
worksheet.getCells().get("C3").putValue(0.8);
worksheet.getCells().get("C4").putValue(1.0);

// Create a Scatter chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Scatter, 6, 6, 15, 11);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:C4", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$4");
// Set the Second-Axis
chart.getNSeries().get(1).setPlotOnSecondAxis(true);
// Show the Second-Axis
chart.getSecondValueAxis().setIsVisible(true);
// Set the second series ChartType to line
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);
// Set the series name
chart.getNSeries().get(0).setName("Sales Volume");
chart.getNSeries().get(1).setName("Growth Rate");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the file
workbook.save("PrimaryandSecondaryAxis.xlsx");
```
