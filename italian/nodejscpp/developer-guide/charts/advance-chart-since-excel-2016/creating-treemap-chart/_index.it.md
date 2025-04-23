---  
title: Come creare un grafico TreeMap con Node.js tramite C++  
linktitle: Come creare un grafico TreeMap  
description: Impara come creare un grafico Treemap in Aspose.Cells for Node.js via C++. La nostra guida ti aiuterà a capire le varie proprietà e opzioni di formattazione disponibili per i grafici Treemap, inclusi colori, etichette e rappresentazione dei dati.  
keywords: Aspose.Cells per Node.js, grafico Treemap, crea, proprietà, formattazione, colori, etichette, rappresentazione dei dati, grafico circolare, grafici gerarchici.  
type: docs  
weight: 161  
url: /it/nodejs-cpp/creating-treemap-chart/  
---  

## **Possibili Scenari di Utilizzo**  
Un grafico a mappa a riquadri fornisce una visualizzazione gerarchica dei tuoi dati e rende facile individuare modelli, ad esempio quali articoli sono i più venduti in un negozio. I rami dell'albero sono rappresentati da rettangoli e ogni sotto-ramo è mostrato come un rettangolo più piccolo. Il grafico a mappa a riquadri visualizza le categorie per colore e prossimità e può facilmente mostrare molti dati che sarebbero difficili da visualizzare con altri tipi di grafico.  

![todo:image_alt_text](sample.png)  
## **Grafico TreeMap**  
Dopo aver eseguito il codice qui sotto, vedrai il grafico TreeMap come mostrato di seguito.  

![todo:image_alt_text](result.png)  
## **Codice di Esempio**  
Il seguente codice di esempio carica il [file Excel di esempio](treemap.xlsx) e genera il [file Excel di output](out.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "treemap.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Treemap, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("TreeMap Chart");
// Add series data range(D2:D13,actually)
chart.getNSeries().add("D2:F13", true);
// Set category data(A2:A13 is incorrect )
chart.getNSeries().setCategoryData("A2:C13");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

