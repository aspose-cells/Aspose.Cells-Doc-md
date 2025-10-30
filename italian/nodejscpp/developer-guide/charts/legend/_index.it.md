---
title: Gestisci Leggenda di Grafici Excel con Node.js tramite C++
description: Scopri come utilizzare Aspose.Cells for Node.js via C++ per utilizzare e personalizzare efficacemente le legende dei grafici in Microsoft Excel. La nostra guida completa spiega la funzionalità della leggenda, come accedervi e modificarla, oltre a come migliorare la visualizzazione e la comprensione dei dati con le legende.
keywords: Aspose.Cells for Node.js via C++, Legende dei grafici, Microsoft Excel, Visualizzazione, Comprensione dei dati.
linktitle: Legenda
type: docs
weight: 50
url: /it/nodejs-cpp/chart-legend/
---

## **Opzioni della Legenda**
Aspose.Cells for Node.js via C++ consente anche di gestire la leggenda di un grafico in runtime. L'oggetto [Legend](https://reference.aspose.com/cells/nodejs-cpp/legend/) può essere spostato, aggiornato e formattato.

|![todo:image_alt_text](chart_legend.png)|

## **Impostazione della Legenda del Grafico**
È semplice gestire la leggenda del grafico con Aspose.Cells [Legend](https://reference.aspose.com/cells/nodejs-cpp/legend/).

Il seguente frammento di codice mostra come gestire la leggenda:


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

## **Argomenti avanzati**
- [Impostare il riempimento dell'voce della legenda del grafico su nessuna utilizzando Aspose.Cells](/cells/it/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
{{< app/cells/assistant language="nodejs-cpp" >}}
