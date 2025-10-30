---
title: Asse X vs. Asse categoria con Node.js tramite C++
linktitle: Asse X vs. Asse delle categorie
description: Impara come differenziare tra l asse X e l asse categoria in Aspose.Cells for Node.js via C++. La nostra guida ti aiuterà a capire le differenze nel loro utilizzo e proprietà, e come configurarli secondo le tue esigenze.
keywords: Aspose.Cells for Node.js via C++, asse X, asse categoria, differenza, utilizzo, proprietà, configurazione.
type: docs
weight: 180
url: /it/nodejs-cpp/X-axis-vs-category-axis/
---

## **Possibili Scenari di Utilizzo**
Ci sono diversi tipi di assi X. Mentre l'asse Y è un asse di tipo Valore, l'asse X può essere un asse di tipo Categoria o un asse di tipo Valore. Utilizzando un asse di tipo Valore, i dati sono trattati come dati numerici continuamente variabili, e il marcatore è posizionato in un punto lungo l'asse che varia in base al suo valore numerico. Utilizzando un asse di tipo Categoria, i dati sono trattati come una sequenza di etichette di testo non numeriche, e il marcatore è posizionato in un punto lungo l'asse in base alla sua posizione nella sequenza. Il codice di esempio qui sotto illustra la differenza tra Assi di Valore e di Categoria.
I nostri dati di esempio sono mostrati nella [tabella di esempio](sample.png) di seguito. La prima colonna contiene i nostri dati asse X, che possono essere trattati come Categorie o come Valori. Nota che i numeri non sono equispaziati, né appaiono in ordine numerico.

![todo:image_alt_text](sample.png)
## **Gestire l'asse X e il'asse delle categorie come Microsoft Excel**
Mostreremo questi dati su due tipi di grafico, il primo grafico è XY (Scatter) con asse X come asse dei valori, il secondo grafico è a linee con asse X come asse Categoria.

![todo:image_alt_text](compare.png)
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

// Put the sample values used in charts
worksheet.getCells().get("A2").putValue(1);
worksheet.getCells().get("A3").putValue(3);
worksheet.getCells().get("A4").putValue(2.5);
worksheet.getCells().get("A5").putValue(3.5);
worksheet.getCells().get("B1").putValue("Cats");
worksheet.getCells().get("C1").putValue("Dogs");
worksheet.getCells().get("D1").putValue("Fishes");
worksheet.getCells().get("B2").putValue(7);
worksheet.getCells().get("B3").putValue(6);
worksheet.getCells().get("B4").putValue(5);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("C2").putValue(7);
worksheet.getCells().get("C3").putValue(5);
worksheet.getCells().get("C4").putValue(4);
worksheet.getCells().get("C5").putValue(3);
worksheet.getCells().get("D2").putValue(8);
worksheet.getCells().get("D3").putValue(7);
worksheet.getCells().get("D4").putValue(3);
worksheet.getCells().get("D5").putValue(2);

// Create Line Chart: X as Category Axis
let pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 6, 15, 20, 21);
// Retrieve the Chart object
let chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$5");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);

// Create XY (Scatter) Chart: X as Value Axis
pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);
// Retrieve the Chart object
chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set X values for series 
chart.getNSeries().get(0).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(1).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(2).setXValues("{1,3,2.5,3.5}");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("XAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
