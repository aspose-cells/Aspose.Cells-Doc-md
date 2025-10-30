---
title: Creare grafico azioni Volume Open High Low Close (VOHLC) con Node.js tramite C++
description: Impara come creare un grafico azioni volume open high low close usando Aspose.Cells for Node.js via C++. La nostra guida dimostrerà come tracciare dati di mercato azionario, incluso volume, apertura, massimo, minimo e chiusura, per una migliore analisi e visualizzazione.
keywords: Aspose.Cells for Node.js via C++, Grafico Azioni Volume Open High Low Close, Dati di Borsa, Analisi, Visualizzazione.
type: docs
weight: 184
url: /it/nodejs-cpp/create-volume-open-high-low-close-stock-chart/
---

## **Possibili Scenari di Utilizzo**
Il quarto grafico azionario che esamineremo è il grafico Volume Open High Low Close. Ancora una volta, è importante ripetere che i dati devono essere nell'ordine corretto. Se è necessario riorganizzare la tabella dei dati, fattelo prima di impostare il grafico. Questo grafico include una colonna per il volume immediatamente dopo la prima colonna (categoria), e i grafici includono un grafico a colonne sull'asse principale che mostra questo volume, mentre i prezzi sono spostati sull'asse secondario.

![todo:image_alt_text](data.png)
## **Grafico Azionario Volume-Apri-Alto-Basso-Chiusura (VHLC)**

![todo:image_alt_text](sample.png)
## **Codice di Esempio**
Il codice di esempio seguente carica il [file Excel di esempio](Volume-Open-High-Low-Close.xlsx) e genera il [file Excel di output](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Volume-Open-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeOpenHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Volume-Open-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:F9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set Color for the first series (Volume) data 
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(79, 129, 189));
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
