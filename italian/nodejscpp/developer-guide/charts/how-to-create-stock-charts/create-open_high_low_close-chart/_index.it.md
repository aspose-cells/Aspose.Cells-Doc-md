---
title: Crea Grafico Stock Open High Low Close (OHLC) con Node.js tramite C++
description: Impara come creare un grafico stock open high low close usando Aspose.Cells for Node.js via C++. La nostra guida mostrerà come tracciare i dati di mercato azionario, inclusi i prezzi open, high, low e close, su un grafico per una migliore analisi e visualizzazione.
keywords: Aspose.Cells for Node.js via C++, Grafico Azioni Open High Low Close, Dati di Borsa, Analisi, Visualizzazione.
type: docs
weight: 182
url: /it/nodejs-cpp/create-open-high-low-close-stock-chart/
---

## **Possibili Scenari di Utilizzo**
Il grafico Open-High-Low-Close (OHLC) utilizza cinque colonne di dati, in ordine: categoria, apertura, alta, bassa e chiusura. L'intervallo di prezzi in ogni categoria è nuovamente indicato da una linea verticale, mentre l'intervallo tra apertura e chiusura è dato da una barra galleggiante più ampia; se il prezzo aumenta nella categoria (chiusura è superiore all'apertura), la barra è riempita con un colore, mentre se il prezzo diminuisce, la barra è riempita con un altro. Questo tipo di grafico è spesso chiamato grafico a candela.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Miglioramenti della visibilità nel grafico**
Spesso usiamo colori anziché bianco e nero per indicare prezzi in aumento e diminuzione. Nel primo set di candlestick sottostante, il rosso mostra prezzi in aumento e il verde in diminuzione.

![todo:image_alt_text](sample2.png)
## **Codice di Esempio**
Il codice di esempio seguente carica il [file Excel di esempio](Open-High-Low-Close.xlsx) e genera il [file Excel di output](out.xlsx).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Open-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockOpenHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Open-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E9", true);
// Set category data 
chart.getNSeries().getCategoryData("A2:A9");
// Set the DownBars and UpBars with different color
chart.getNSeries().get(0).getDownBars().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(0).getUpBars().getArea().setForegroundColor(AsposeCells.Color.Red);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
