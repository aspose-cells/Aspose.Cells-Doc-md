---  
title: Gestione delle DataLabels dei grafici Excel con Node.js tramite C++  
description: Impara come gestire efficacemente le etichette dei dati nei grafici Excel usando Aspose.Cells for Node.js via C++. Questa guida completa copre varie operazioni di gestione, inclusa l aggiunta, la rimozione e la modifica delle etichette per migliorare la leggibilità e l usabilità del grafico.  
keywords: Aspose.Cells per Node.js, grafici Excel, etichette dei dati, gestione, leggibilità, usabilità, aggiunta, rimozione, modifica.  
linktitle: Etichette dei dati  
type: docs  
weight: 50  
url: /it/nodejs-cpp/insert-datalabels-to-chart/  
---  

{{% alert color="primary" %}}  

Le etichette dei dati sono una parte importante di un grafico.  
Possiamo conoscere facilmente il valore, la percentuale, ecc. di ciascuna serie  

{{% /alert %}}  

## **Opzioni delle etichette dei dati**  
Aspose.Cells for Node.js via C++ consente anche di gestire le etichette dei dati del grafico in runtime, con l'oggetto [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/), è semplice spostare, aggiornare e formattare le etichette dei dati del grafico.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **Gestisci le etichette dei dati del grafico**  
È semplice gestire le etichette dei dati del grafico con Aspose.Cells [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/).  

Il seguente snippet di codice dimostra come gestire le DataLabels:  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

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

// Show value labels
chart.getNSeries().get(0).getDataLabels().setShowValue(true);
// Show series name labels
chart.getNSeries().get(1).getDataLabels().setShowSeriesName(true);
// Move labels to center
chart.getNSeries().get(1).getDataLabels().setPosition(AsposeCells.LabelPositionType.Center);

// Save the file
workbook.save("chart_datalabels.xlsx");
```  

## **Argomenti avanzati**  
- [Aggiunta di etichette personalizzate ai punti dati della serie del grafico](/cells/it/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [Disabilita il testo a capo per le etichette dei dati del grafico](/cells/it/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [Ridimensiona la forma dell'etichetta dati del grafico per adattarla al testo](/cells/it/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [Etichetta dati personalizzata in formato testo ricco del punto del grafico](/cells/it/nodejs-cpp/rich-text-custom-data-label-of-chart-point/)  
- [Imposta il tipo di forma delle etichette dati del grafico](/cells/it/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [Mostra l'intervallo di celle come etichette dati](/cells/it/nodejs-cpp/showing-cell-range-as-the-data-labels/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
