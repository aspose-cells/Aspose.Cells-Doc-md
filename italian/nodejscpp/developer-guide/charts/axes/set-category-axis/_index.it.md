---
title: Come impostare l asse categoria con Node.js tramite C++
linktitle: Come impostare l asse delle categorie
description: Impara come impostare l asse categoria in Aspose.Cells for Node.js via C++. La nostra guida ti aiuterà a capire come definire l intervallo dell asse categoria, regolare le sue proprietà e formattare le sue etichette.
keywords: Aspose.Cells for Node.js via C++, asse categoria, impostazione, intervallo, proprietà, formattazione.
type: docs
weight: 205
url: /it/nodejs-cpp/how-to-set-category-axis/
---

## **Possibili Scenari di Utilizzo**
Dopo aver creato un grafico in un foglio di lavoro, puoi impostare l'asse delle categorie. In questo articolo, ti mostreremo come impostare l'asse delle categorie per un grafico Excel utilizzando Aspose.Cells con esempio di codice.

## **I passaggi nel codice di esempio**

1. Crea un nuovo foglio di lavoro.

2. Crea un nuovo grafico nel primo foglio di lavoro.

3. Aggiungi alcuni valori alle celle nel primo foglio di lavoro.

4. Ora puoi impostare l'asse categoria; ci sono due metodi: usando i dati delle celle o usando direttamente le stringhe, entrambi mostrati nel codice di esempio.

5. Imposta l'asse dei valori e salva il workbook per visualizzare il risultato.

## **Codice di Esempio**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const dataDir = ""; // Update with your path

// Create a new workbook
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CHART");

// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 8, 0, 20, 10);
const chart = worksheet.getCharts().get(chartIndex);

// Add some values to cells
worksheet.getCells().get("A1").putValue("Sales");
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(130);
worksheet.getCells().get("A5").putValue(160);
worksheet.getCells().get("A6").putValue(150);
worksheet.getCells().get("B1").putValue("Days");
worksheet.getCells().get("B2").putValue(1);
worksheet.getCells().get("B3").putValue(2);
worksheet.getCells().get("B4").putValue(3);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("B6").putValue(5);

// Some values in string
const Sales = "100,150,130,160,150";
const Days = "1,2,3,4,5";

// Set Category Axis Data with string
chart.getNSeries().setCategoryData(`{${Days}}`);
// Or you can set Category Axis Data with data in cells
// chart.getNSeries().setCategoryData("B2:B6");

// Add Series to the chart
chart.getNSeries().add("Demand1", true);
// Set value axis with string 
chart.getNSeries().get(0).setValues(`{${Sales}}`);
chart.getNSeries().add("Demand2", true);
// Set value axis with data in cells
chart.getNSeries().get(1).setValues("A2:A6");

// Set some Category Axis properties
chart.getCategoryAxis().getTickLabels().setRotationAngle(45);
chart.getCategoryAxis().getTickLabels().getFont().setSize(8);
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

// Save the workbook to view the result file
workbook.save(path + "Output.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
