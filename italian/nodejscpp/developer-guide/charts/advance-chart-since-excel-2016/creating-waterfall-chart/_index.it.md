---
title: Come creare un grafico cascata con Node.js tramite C++
linktitle: Come creare un grafico a cascata
type: docs
weight: 160
url: /it/nodejs-cpp/creating-waterfall-chart/
description: Crea grafici cascata in Excel con Node.js e Aspose.Cells for Node.js via C++.
keywords: crea grafico a cascata in Excel con Node.js tramite C++, creazione di grafico a cascata in Excel con Node.js tramite C++, come creare grafico a cascata in Excel con Node.js tramite C++
---

{{% alert color="primary" %}}

Un grafico a cascata è un tipo di grafico speciale che viene usato normalmente per dimostrare come la posizione iniziale aumenti o diminuisca. Microsoft Excel ha molti tipi di grafici predefiniti, tra cui colonna, linea, torta, barra, radar, ecc., ma il grafico a cascata va oltre i grafici di base e può essere creato utilizzando i tipi di grafico esistenti con qualche personalizzazione.

{{% /alert %}} 

Le API di Aspose.Cells permettono di creare un grafico a cascata utilizzando il grafico a linee. L'API consente anche di personalizzare l'aspetto del grafico per dargli la forma di una cascata impostando le proprietà [**Series.getUpBars()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getUpBars--) e [**Series.getDownBars()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getDownBars--).

Il codice di esempio sotto dimostra l'uso di Aspose.Cells for Node.js via C++ per creare un grafico a cascata da zero.

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

## Articoli correlati

- [Creazione di grafici](/cells/it/nodejs-cpp/creating-charts/)
- [Personalizzazione di Grafici](/cells/it/nodejs-cpp/customizing-charts/)
{{< app/cells/assistant language="nodejs-cpp" >}}
