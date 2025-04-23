---
title: Hur man skapar vattenfallsdiagram med Node.js via C++
linktitle: Hur man skapar en vattenfallstabell
type: docs
weight: 160
url: /sv/nodejs-cpp/creating-waterfall-chart/
description: Skapa vattenfallsdiagram i Excel med Node.js och Aspose.Cells for Node.js via C++.
keywords: skapa vattenfallsdiagram i excel Node.js via C++, skapa vattenfallsdiagram i excel Node.js via C++, hur man skapar vattenfallsdiagram i excel Node.js via C++
---

{{% alert color="primary" %}}

Ett vattenfallsdiagram är en speciell typ av diagram som vanligtvis används för att visa hur startpositionen antingen ökar eller minskar. Microsoft Excel har många fördefinierade diagramtyper, inklusive kolumn, linje, pie, stapel, radard, etc., men vattenfallsdiagram ligger utanför de grundläggande graferna och kan skapas med befintliga diagramtyper med liten eller mer anpassning.

{{% /alert %}} 

Aspose.Cells API:er tillåter att skapa ett vattenfallsdiagram med hjälp av linjediagram. API:et möjliggör också att anpassa diagrammets utseende för att ge det formen av ett vattenfall genom att ställa in [**Series.getUpBars()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getUpBars--) och [**Series.getDownBars()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getDownBars--) egenskaper.

Nedan anges kodsnutten som demonstrerar användningen av Aspose.Cells for Node.js via C++ för att skapa ett vattenfallsdiagram från grunden.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook();

// Retrieve the first Worksheet in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Retrieve the Cells of the first Worksheet
const cells = worksheet.getCells();

// Input some data which chart will use as source
cells.get("A1").putValue("Previous Year");
cells.get("A2").putValue("January");
cells.get("A3").putValue("March");
cells.get("A4").putValue("August");
cells.get("A5").putValue("October");
cells.get("A6").putValue("Current Year");

cells.get("B1").putValue(8.5);
cells.get("B2").putValue(1.5);
cells.get("B3").putValue(7.5);
cells.get("B4").putValue(7.5);
cells.get("B5").putValue(8.5);
cells.get("B6").putValue(3.5);

cells.get("C1").putValue(1.5);
cells.get("C2").putValue(4.5);
cells.get("C3").putValue(3.5);
cells.get("C4").putValue(9.5);
cells.get("C5").putValue(7.5);
cells.get("C6").putValue(9.5);

// Add a Chart of type Waterfall in same worksheet as of data
const idx = worksheet.getCharts().add(AsposeCells.ChartType.Waterfall, 4, 4, 25, 13);

// Retrieve the Chart object
const chart = worksheet.getCharts().get(idx);

// Add Series
chart.getNSeries().add("$B$1:$C$6", true);

// Add Category Data
chart.getNSeries().setCategoryData("$A$1:$A$6");

// Series has Up Down Bars
chart.getNSeries().get(0).setHasUpDownBars(true);

// Set the colors of Up and Down Bars
chart.getNSeries().get(0).getUpBars().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(0).getDownBars().getArea().setForegroundColor(AsposeCells.Color.Red);

// Make both Series Lines invisible
chart.getNSeries().get(0).getBorder().setIsVisible(false);
chart.getNSeries().get(1).getBorder().setIsVisible(false);

// Set the Plot Area Formatting Automatic
chart.getPlotArea().getArea().setFormatting(AsposeCells.FormattingType.Automatic);

// Delete the Legend
chart.getLegend().getLegendEntries().get(0).setIsDeleted(true);
chart.getLegend().getLegendEntries().get(1).setIsDeleted(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

## Relaterade artiklar

- [Skapa diagram](/cells/sv/nodejs-cpp/creating-charts/)
- [Anpassa diagram](/cells/sv/nodejs-cpp/customizing-charts/)
