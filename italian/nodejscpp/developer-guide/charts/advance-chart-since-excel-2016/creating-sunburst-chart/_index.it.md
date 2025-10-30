---
title: Come creare un grafico Sunburst con Node.js tramite C++
linktitle: Come creare un grafico Sunburst
description: Impara come creare un grafico sunburst in Aspose.Cells for Node.js via C++, un grafico che presenta i dati in un cerchio. La nostra guida ti aiuterà a configurare varie proprietà e formattazioni del tuo grafico, inclusi etichette dati, legende, colori e altro.
keywords: Aspose.Cells for Node.js via C++, grafico sunburst, crea, imposta proprietà, etichette dati, legenda, formato, colore, cerchio, rendering dei dati.
type: docs
weight: 162
url: /it/nodejs-cpp/creating-sunburst-chart/
---

## **Possibili Scenari di Utilizzo**
I grafici a mappa ad albero sono utili per confrontare le proporzioni all’interno della gerarchia; tuttavia, i grafici a mappa ad albero non sono ottimali per mostrare i livelli gerarchici tra le categorie più grandi e ogni punto dati. Un grafico sunburst è molto più efficace per mostrare ciò. Il grafico sunburst è ideale per visualizzare dati gerarchici. Ogni livello della gerarchia è rappresentato da un anello o cerchio, con il cerchio più interno come il vertice della gerarchia. Un grafico sunburst senza dati gerarchici (un livello di categorie) assomiglia a un grafico a ciambella. Tuttavia, un grafico sunburst con più livelli di categorie mostra come gli anelli esterni si relazionano con quelli interni. Il grafico sunburst è più efficace nel mostrare come un anello si suddivide nei suoi componenti, mentre un altro tipo di grafico gerarchico, il grafico mappa ad albero, è ideale per confrontare le dimensioni relative.

![todo:image_alt_text](sample.png)
## **Grafico sunburst**
Dopo aver eseguito il codice qui sotto, vedrai il grafico Sunburst come mostrato di seguito.

![todo:image_alt_text](result.png)
## **Codice di Esempio**
Il seguente codice di esempio carica il [file Excel di esempio](sunburst.xlsx) e genera il [file Excel di output](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sunburst.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Sunburst Chart");
// Add series data range
chart.getNSeries().add("D2:D16", true);
// Set category data (A2:A16 is incorrect, as hierarchical category)
chart.getNSeries().setCategoryData("A2:C16");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
