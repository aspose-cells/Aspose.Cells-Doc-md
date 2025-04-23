---
title: Imposta il codice di formattazione dei valori della serie del grafico con Node.js tramite C++
description: Impara come impostare il codice di formattazione dei valori della serie del grafico in Aspose.Cells for Node.js via C++. Questa guida ti aiuterà a capire come formattare i dati della serie del grafico usando il codice di formato appropriato, permettendoti di presentare i tuoi dati in modo preciso e professionale.
keywords: Aspose.Cells per Node.js, serie di grafici, codice di formattazione dei valori, formattazione, presentazione dei dati, precisione, professionalità.
linktitle: Formato numero
type: docs
weight: 100
url: /it/nodejs-cpp/set-the-values-format-code-of-chart-series/
---

## **Possibili Scenari di Utilizzo**
Puoi impostare il codice di formattazione dei valori della serie del grafico usando la proprietà [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--). Questa proprietà è utile non solo per la serie basata sull'intervallo all'interno del foglio di lavoro, ma funziona anche bene per la serie creata con un array di valori.

## **Impostare il codice di formato dei valori della serie del grafico**
Il seguente esempio di codice aggiunge una serie nel grafico vuoto che prima non aveva serie. Aggiunge la serie usando l'array di valori. Una volta aggiunta, la formatta con il codice $#,##0 usando la proprietà [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--) e il numero 10000 diventa $10,000. Lo screenshot mostra l'effetto del codice sul [file Excel di esempio](51740712.xlsx) e sul [file Excel di output](51740713.xlsx) dopo l'esecuzione.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Codice di Esempio**
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "51740712.xlsx");

// Load the source Excel file 
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Add series using an array of values
chart.getNSeries().add("{10000, 20000, 30000, 40000}", true);

// Access the series and set its values format code
const series = chart.getNSeries().get(0);
series.setValuesFormatCode("$#,##0");

// Save the output Excel file
workbook.save(path.join(dataDir, "51740713.xlsx"));
```
