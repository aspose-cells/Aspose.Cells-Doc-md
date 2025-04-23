---  
title: Aggiunta di etichette personalizzate ai punti dati nella serie del grafico con Node.js via C++  
linktitle: Aggiunta di etichette personalizzate ai punti dati della serie del grafico  
description: Impara come aggiungere etichette personalizzate ai punti dati nella serie di un grafico usando Aspose.Cells for Node.js via C++. Questa guida dimostrerà come modificare l aspetto, la posizione e la formattazione delle etichette, collegandole alla tua fonte dati per una rappresentazione accurata.  
keywords: Aspose.Cells per Node.js, creazione grafici, etichette personalizzate, punti dati, serie, aspetto, posizione, formattazione, fonte dati, rappresentazione.  
type: docs  
weight: 100  
url: /it/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/  
---  

{{% alert color="primary" %}}  

Puoi aggiungere etichette personalizzate ai punti dati della serie del grafico. Aspose.Cells fornisce la proprietà [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) per aggiungere queste etichette personalizzate. Questo articolo spiegherà come utilizzare questa proprietà per aggiungere etichette personalizzate ai punti dati della serie del grafico.

{{% /alert %}}  

Il seguente codice crea un **Grafico a dispersione collegato da linee con marcatori di dati** e poi aggiunge **etichette personalizzate** ai **punti dati** nella **serie** del **grafico**. Ogni etichetta personalizzata mostra il **nome della serie** e il **nome del punto**. Puoi usare qualsiasi altro testo invece di questo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Put data
sheet.getCells().get(0, 0).putValue(1);
sheet.getCells().get(0, 1).putValue(2);
sheet.getCells().get(0, 2).putValue(3);

sheet.getCells().get(1, 0).putValue(4);
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(1, 2).putValue(6);

sheet.getCells().get(2, 0).putValue(7);
sheet.getCells().get(2, 1).putValue(8);
sheet.getCells().get(2, 2).putValue(9);

// Generate the chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 5, 1, 24, 10);
const chart = sheet.getCharts().get(chartIndex);

chart.getTitle().setText("Test");
chart.getCategoryAxis().getTitle().setText("X-Axis");
chart.getValueAxis().getTitle().setText("Y-Axis");

chart.getNSeries().setCategoryData("A1:C1");

// Insert series
chart.getNSeries().add("A2:C2", false);

let series = chart.getNSeries().get(0);

let pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 1" + "\n" + "Point " + i);
}

// Insert series
chart.getNSeries().add("A3:C3", false);

series = chart.getNSeries().get(1);

pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 2" + "\n" + "Point " + i);
}

workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

