---
title: X axel vs. kategori axel med Node.js via C++
linktitle: X axel vs. Kategori axel
description: Lär dig hur du skiljer mellan X axeln och kategori axeln i Aspose.Cells for Node.js via C++. Vår guide hjälper dig att förstå skillnaderna i deras användning och egenskaper, samt hur du konfigurerar dem efter behov.
keywords: Aspose.Cells for Node.js via C++, X axel, kategori axel, skillnad, användning, egenskaper, konfiguration.
type: docs
weight: 180
url: /sv/nodejs-cpp/X-axis-vs-category-axis/
---

## **Möjliga användningsscenario**
Det finns olika typer av X-axlar. Medan Y-axeln är en Värde typ axel kan X-axeln vara en Kategori typ axel eller en Värde typ axel. Genom att använda en Värde-axel behandlas datan som kontinuerligt varierande numerisk data, och markören placeras vid en punkt längs axeln som varierar enligt dess numeriska värde. Genom att använda en Kategori-axel behandlas datan som en följd av icke-numeriska textetiketter, och markören placeras vid en punkt längs axeln enligt dess position i följden. Exemplet nedan illustrerar skillnaden mellan Värde- och Kategori-axlar.
Vår provdata visas i [provtabellfilen](sample.png) nedan. Den första kolumnen innehåller våra X-axeldata, som kan behandlas som Kategorier eller som Värden. Observera att siffrorna inte är jämnt fördelade, och de förekommer inte ens i numerisk ordning.

![todo:image_alt_text](sample.png)
## **Hantera X- och Kategori-axeln som i Microsoft Excel**
Vi kommer visa denna data på två typer av diagram, det första är XY (Scatter) diagram med X som värdeaxel, det andra är linjediagram med X som kategorilänk.

![todo:image_alt_text](compare.png)
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

// Put the sample values used in charts
worksheet.getCells().get("A2").putValue(1);
worksheet.getCells().get("A3").putValue(3);
worksheet.getCells().get("A4").putValue(2.5);
worksheet.getCells().get("A5").putValue(3.5);
worksheet.getCells().get("B1").putValue("Cats");
worksheet.getCells().get("C1").putValue("Dogs");
worksheet.getCells().get("D1").putValue("Fishes");
worksheet.getCells().get("B2").putValue(7);
worksheet.getCells().get("B3").putValue(6);
worksheet.getCells().get("B4").putValue(5);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("C2").putValue(7);
worksheet.getCells().get("C3").putValue(5);
worksheet.getCells().get("C4").putValue(4);
worksheet.getCells().get("C5").putValue(3);
worksheet.getCells().get("D2").putValue(8);
worksheet.getCells().get("D3").putValue(7);
worksheet.getCells().get("D4").putValue(3);
worksheet.getCells().get("D5").putValue(2);

// Create Line Chart: X as Category Axis
let pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 6, 15, 20, 21);
// Retrieve the Chart object
let chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$5");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);

// Create XY (Scatter) Chart: X as Value Axis
pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);
// Retrieve the Chart object
chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set X values for series 
chart.getNSeries().get(0).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(1).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(2).setXValues("{1,3,2.5,3.5}");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("XAxis.xlsx");
```
