---
title: Tre metodi per filtrare i dati del grafico con Node.js tramite C++
linktitle: Tre metodi per filtrare i dati del grafico
description: Impara come filtrare i grafici in Excel utilizzando Aspose.Cells for Node.js via C++. La nostra guida completa mostrerà come applicare filtri ai grafici, personalizzare gli elementi del grafico e usare strumenti di analisi dei dati per migliori approfondimenti e decisioni informate.
keywords: Aspose.Cells for Node.js via C++, Filtrare i grafici in Excel, Analisi dei dati, Decisioni, Visualizzazione.
type: docs
weight: 2210
url: /it/nodejs-cpp/filtering-charts-in-excel/
---


## **1. Filtrare le serie per visualizzare un grafico**

### **Passaggi per filtrare le serie da un grafico in Excel**
In Excel, possiamo filtrare specifiche serie da un grafico, facendo sì che quelle serie filtrate non siano visualizzate nel grafico. Il grafico originale è mostrato in **Figura 1**. Tuttavia, quando filtriamo **Testseries2** e **Testseries4**, il grafico apparirà come mostrato in **Figura 2**.

In Aspose.Cells for Node.js via C++, possiamo eseguire un'operazione simile. Per un file di esempio (sample) come questo, se vogliamo filtrare **Testseries2** e **Testseries4**, possiamo eseguire il seguente codice. Inoltre, manterremo due liste: una ([Chart.getNSeries()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getNSeries--)) per memorizzare tutte le serie selezionate.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Codice di Esempio**
Il seguente codice di esempio carica il [file Excel di esempio](seriesFiltered.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "seriesFiltered.xlsx");
// Create an instance of existing Workbook
let workbook = new AsposeCells.Workbook(filePath);
// Get filtered series list
let nSeriesFiltered = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getFilteredNSeries();
// Get selected series list
let nSeries = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getNSeries();
// Should be 0
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 6
console.log("Visible Series count: " + nSeries.getCount());
// Process from the end to the beginning
nSeries.get(1).setIsFiltered(true);
nSeries.get(0).setIsFiltered(true);
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
workbook.save("seriesFiltered-out.xlsx");
workbook = new AsposeCells.Workbook("seriesFiltered-out.xlsx");
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
```

## **2. Filtrare i dati e far cambiare il grafico**

Filtrare i propri dati è un ottimo modo per gestire i filtri del grafico con molti dati. Quando filtri i dati, il grafico cambierà. Un problema che dovremo affrontare è assicurarsi che il grafico rimanga visibile a schermo. Quando si applicano filtri, vengono nastrate righe e occasionalmente il grafico sarà in quelle righe nascoste.

![todo:image_alt_text](Figure3.png)

### **Passaggi per utilizzare i filtri dei dati per modificare il grafico in Excel**

1. Fare clic all'interno del proprio intervallo di dati.
2. Fare clic sulla scheda **Dati**, e attivare i filtri cliccando su Filtri. La riga di intestazione avrà frecce a discesa.
3. Creare un grafico andando alla scheda **Inserisci** e selezionando un grafico a colonne.
4. Ora filtra i tuoi dati utilizzando le frecce a discesa nei dati. Non utilizzare i filtri del grafico.

### **Codice di Esempio**
Il seguente esempio di codice mostra la stessa funzione usando Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of Worksheet
const sheet = workbook.getWorksheets().get("Sheet1");
// Add data into details cells.
sheet.getCells().get(0, 0).putValue("Fruits Name");
sheet.getCells().get(0, 1).putValue("Fruits Price");
sheet.getCells().get(1, 0).putValue("Apples");
sheet.getCells().get(2, 0).putValue("Bananas");
sheet.getCells().get(3, 0).putValue("Grapes");
sheet.getCells().get(4, 0).putValue("Oranges");
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(2, 1).putValue(2);
sheet.getCells().get(3, 1).putValue(1);
sheet.getCells().get(4, 1).putValue(4);

// Add a chart to the worksheet
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
// Access the instance of the newly added chart
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B5", true);
// Set AutoFilter range
sheet.getAutoFilter().setRange("A1:B5");
// Add filters for a filter column.
sheet.getAutoFilter().addFilter(0, "Bananas");
sheet.getAutoFilter().addFilter(0, "Oranges");
// Apply the filters
sheet.getAutoFilter().refresh();
chart.toImage("Autofilter.png");
workbook.save("Autofilter.xlsx");
```

## **3. Filtra i dati utilizzando una Tabella e fai cambiare il grafico**

Utilizzare una Tabella è simile al Metodo 2, utilizzando un intervallo, ma hai vantaggi con le tabelle rispetto agli intervalli. Quando cambia il tuo intervallo in una Tabella e aggiungi dati, il grafico si aggiorna automaticamente. Con un intervallo, dovrai modificare la fonte dati.

### **Formatta come tabella in Excel**

Fare clic all'interno dei dati e utilizzare **CTRL + T** oppure utilizzare la scheda Home, **Formatta come Tabella**

![todo:image_alt_text](Figure4.png)

### **Codice di Esempio**
Il seguente esempio di codice carica il [file di esempio Excel](TableFilters.xlsx) e mostra la stessa funzionalità usando Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "TableFilters.xlsx");
// Create a workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet
const sheet = workbook.getWorksheets().get(0);
// Access the instance of the newly added chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B7", true);
// Convert the chart to image
chart.toImage("TableFilters.before.png");
// Add a new List Object to the worksheet
const listObject = sheet.getListObjects().get(sheet.getListObjects().add("A1", "B7", true));
// Add default style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);
// Show Total
listObject.setShowTotals(false);
// Add filters for a filter column.
listObject.getAutoFilter().addFilter(0, "James");
// Apply the filters
listObject.getAutoFilter().refresh();
// After adding new value the chart will change
listObject.putCellValue(7, 0, "Me");
listObject.putCellValue(7, 1, 1000);
// Check the changed images
chart.toImage("TableFilters.after.png");
// Saving the Excel file
workbook.save("TableFilter.out.xlsx");
```
