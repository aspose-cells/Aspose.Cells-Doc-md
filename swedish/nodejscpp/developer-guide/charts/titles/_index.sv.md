---
title: Hantera titlar på Excel diagram med Node.js via C++
description: Lär dig att använda Aspose.Cells for Node.js via C++ för att lägga till och formatera diagram och axeltitlar i Microsoft Excel. Vår guide visar hur du ställer in olika typer av titlar, justerar deras utseende och ändrar axeltitlar för bättre datavisualisering och tydlighet.
keywords: Aspose.Cells for Node.js via C++, Diagramtitlar, Axeltitlar, Microsoft Excel, Datavisualisering, Utseende.
linktitle: Titlar
type: docs
weight: 50
url: /sv/nodejs-cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

I Excel-diagram finns det 2 typer av titlar:
1. Diagramtitel 
1. Axeltitlar

{{% /alert %}}

## **Tillval för titlar**
Aspose.Cells for Node.js via C++ tillåter också att hantera diagramtitlar i realtid. Med `Title`-objekt kan du ändra text, font och fyllningsformat för titlar.

|![todo:image_alt_text](chart_title.png)|

## **Inställning av diagram- eller axeltitlar**
Du kan använda Microsoft Excel för att sätta titlar på ett diagram och dess axlar i en WYSIWYG-miljö. Aspose.Cells for Node.js via C++ tillåter även utvecklare att ange diagram- och axeltitlar vid körning. Alla diagram och deras axlar innehåller en `Title`-egenskap som kan användas för att ställa in deras titlar som visas nedan i ett exempel.

Följande kodexempel visar hur du kan ställa in titlar på diagram och axlar.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

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

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Setting the title of category axis of the chart
chart.getCategoryAxis().getTitle().setText("Category");

// Setting the title of value axis of the chart
chart.getValueAxis().getTitle().setText("Value");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Fortsatta ämnen**
- [Läs diagramunderrubrik från ODS-fil](/cells/sv/nodejs-cpp/read-chart-subtitle-from-ods-file/)
