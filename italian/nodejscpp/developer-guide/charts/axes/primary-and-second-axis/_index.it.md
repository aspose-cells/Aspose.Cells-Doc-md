---
title: Asse principale e secondario con Node.js tramite C++
description: Impara come comprendere e lavorare con assi principali e secondari in Aspose.Cells for Node.js via C++. La nostra guida ti aiuterà a capire le differenze tra assi principali e secondari, e come configurarli e utilizzarli efficacemente nei tuoi grafici.
keywords: Aspose.Cells for Node.js via C++, assi principali, assi secondari, comprensione, differenze, configurazione, uso.
type: docs
weight: 190
url: /it/nodejs-cpp/primary-and-second-axis/
---

## **Possibili Scenari di Utilizzo**
Quando i numeri in un grafico variano ampiamente da serie di dati a serie di dati, o quando hai tipi di dati misti (prezzo e volume), rappresenta una o più serie di dati su un asse verticale (valore) secondario. La scala dell'asse verticale secondario mostra i valori per le serie di dati associate. Un asse secondario funziona bene in un grafico che mostra una combinazione di grafici a colonne e a linee.

## **Gestire gli assi primario e secondario come Microsoft Excel**
Vedi il seguente esempio di codice che crea un nuovo file Excel e inserisce i valori del grafico nel primo foglio di lavoro. 
Quindi aggiungiamo un grafico e mostriamo l'asse secondario.

![todo:image_alt_text](excel.png)

## **Codice di Esempio**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Put the sample values used in a chart
worksheet.getCells().get("A1").putValue("Region");
worksheet.getCells().get("A2").putValue("Peking");
worksheet.getCells().get("A3").putValue("New York");
worksheet.getCells().get("A4").putValue("Paris");
worksheet.getCells().get("B1").putValue("Sales Volume");
worksheet.getCells().get("C1").putValue("Growth Rate");
worksheet.getCells().get("B2").putValue(100);
worksheet.getCells().get("B3").putValue(80);
worksheet.getCells().get("B4").putValue(140);
worksheet.getCells().get("C2").putValue(0.7);
worksheet.getCells().get("C3").putValue(0.8);
worksheet.getCells().get("C4").putValue(1.0);

// Create a Scatter chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Scatter, 6, 6, 15, 11);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:C4", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$4");
// Set the Second-Axis
chart.getNSeries().get(1).setPlotOnSecondAxis(true);
// Show the Second-Axis
chart.getSecondValueAxis().setIsVisible(true);
// Set the second series ChartType to line
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);
// Set the series name
chart.getNSeries().get(0).setName("Sales Volume");
chart.getNSeries().get(1).setName("Growth Rate");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the file
workbook.save("PrimaryandSecondaryAxis.xlsx");
```
