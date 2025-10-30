---  
title: Crea Grafico Stock High Low Close (HLC) con Node.js tramite C++  
linktitle: Crea un grafico di scorta High Low Close (HLC)  
description: Impara come creare un grafico stock High Low Close usando Aspose.Cells for Node.js via C++. La nostra guida passo passo dimostrerà come tracciare i dati di mercato azionario, inclusi i prezzi high, low e closing, su un grafico per una migliore analisi e visualizzazione.  
keywords: Aspose.Cells per Node.js, Grafico Stock High Low Close, Dati di Mercato Azionario, Analisi, Visualizzazione.  
type: docs  
weight: 181  
url: /it/nodejs-cpp/create-high-low-close-stock-chart/  
---  

## **Possibili Scenari di Utilizzo**  
 Il grafico stock High-Low-Close (HLC) utilizza quattro colonne di dati. La prima colonna è una categoria, di solito una data ma possono essere utilizzati anche nomi di azioni. Le altre tre colonne in ordine sono per high, low e prezzi di chiusura. L'intervallo di prezzo per ogni categoria è indicato da una linea verticale da low a high, e il prezzo di chiusura viene mostrato utilizzando un segno di tick che si estende a destra di questa linea.  

![todo:image_alt_text](sample.png)  
## **Miglioramenti della visibilità nel grafico**  
A volte, per rendere il grafico più intuitivo, possiamo modificare l'aspetto del marcatore (chiusura), o farlo visualizzare sull'asse secondario.  

![todo:image_alt_text](sample2.png)  
## **Codice di Esempio**  
Il codice di esempio seguente carica il [file Excel di esempio](High-Low-Close.xlsx) e genera il [file Excel di output](out.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:D9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set the marker with the built-in data 
chart.getNSeries().get(2).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Dash);
chart.getNSeries().get(2).getMarker().setMarkerSize(20);
chart.getNSeries().get(2).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(2).getMarker().getArea().setForegroundColor(AsposeCells.Color.Maroon);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
