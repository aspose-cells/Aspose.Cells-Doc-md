---
title: Come aggiungere un PivotChart usando Aspose.Cells for Node.js via C++
linktitle: Grafico pivot
type: docs
weight: 100
url: /it/nodejs-cpp/how-to-add-pivot-chart/
description: Come aggiungere un PivotChart usando Aspose.Cells for Node.js via C++.
keywords: PivotChart Node.js tramite C++
---
## Cosa è un PivotChart

Un grafico pivot è una rappresentazione visiva dei dati in una tabella pivot. I grafici pivot offrono un modo per riassumere, analizzare, esplorare e presentare dati riassuntivi. Ecco alcune caratteristiche e aspetti chiave dei grafici pivot:

1. Rappresentazione Dinamica dei Dati: I grafici pivot si aggiornano automaticamente per riflettere le modifiche nella tabella pivot. Se aggiungi o rimuovi campi nella tabella pivot, il grafico pivot si aggiorna di conseguenza.

1. Interattivo: I grafici pivot sono interattivi, permettendo agli utenti di filtrare, ordinare e approfondire i dati. Questo rende facile esplorare diversi aspetti del set di dati.

1. Layout flessibile: gli utenti possono modificare il layout del grafico pivot trascinando e rilasciando i campi, offrendo flessibilità nella visualizzazione dei dati.

1. Tipi di grafico vari: i grafici pivot possono essere creati utilizzando vari tipi di grafico come grafici a barre, a linee, a torta e altri, a seconda della natura dei dati e delle intuizioni desiderate.

1. Sintesi: i grafici pivot riassumono grandi quantità di dati e possono mostrare totali, medie, conteggi o altre statistiche di sintesi.

1. Filtraggio: offrono capacità di filtraggio, consentendo di visualizzare solo i dati che soddisfano determinati criteri.

<br>
I grafici pivot sono comunemente usati nelle strategie di business intelligence e analisi dei dati per fornire un riassunto visivo chiaro e conciso di insiemi di dati complessi. Sono uno strumento potente per prendere decisioni basate sui dati.

## Come aggiungere un PivotChart usando Aspose.Cells for Node.js via C++

### **Aggiunta di una tabella pivot**

Per creare una tabella pivot usando Aspose.Cells for Node.js via C++:

1. Aggiungi alcuni dati a un foglio di lavoro usando il metodo `putValue` di un oggetto Cell. Puoi anche usare un file modello già riempito con i dati. I dati verranno usati come sorgente dei dati per la tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo `add` della raccolta `PivotTables`.
1. Accedi al nuovo oggetto PivotTable dalla raccolta `PivotTables` passando il suo indice. Usa uno qualsiasi degli oggetti pivot table incapsulati nell'oggetto PivotTable per gestire la tabella.

Di seguito sono riportati esempi di codice.

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Obtaining the reference of the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Name the sheet
sheet.setName("Data");
const cells = sheet.getCells();

// Setting the values to the cells
cells.get("A1").putValue("Employee");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Product");
cells.get("D1").putValue("Continent");
cells.get("E1").putValue("Country");
cells.get("F1").putValue("Sale");

const namesAndValues = [
["David", 1, "Maxilaku", "Asia", "China", 2000],
["David", 2, "Maxilaku", "Asia", "India", 500],
["David", 3, "Chai", "Asia", "Korea", 1200],
["David", 4, "Maxilaku", "Asia", "India", 1500],
["James", 1, "Chang", "Europe", "France", 500],
["James", 2, "Chang", "Europe", "France", 1500],
["James", 3, "Chang", "Europe", "Germany", 800],
["James", 4, "Chang", "Europe", "Italy", 900],
["James", 4, "Chang", "Europe", "France", 500],
["Miya", 1, "Geitost", "America", "U.S.", 1600],
["Miya", 2, "Chai", "America", "U.S.", 600],
["Miya", 3, "Geitost", "America", "Brazil", 2000],
["Miya", 2, "Geitost", "America", "U.S.", 500],
["Miya", 3, "Maxilaku", "America", "Canada", 900],
["Miya", 4, "Geitost", "America", "U.S.", 700],
["Miya", 5, "Geitost", "America", "U.S.", 1400],
["Miya", 6, "Ikuru", "Europe", "Italy", 1350],
["Miya", 7, "Ikuru", "Europe", "France", 300],
["Miya", 8, "Ikuru", "Europe", "Italy", 500],
["Miya", 9, "Ikuru", "America", "New Zealand", 1000],
["Miya", 10, "Ipoh Coffee", "Oceania", "Australia", 1500],
["Miya", 11, "Chocolade", "Oceania", "Australia", 500],
["Miya", 12, "Chocolade", "Oceania", "New Zealand", 1500],
["Miya", 13, "Chocolade", "Oceania", "S.Africa", 1600],
["Miya", 14, "Chocolade", "Africa", "Egypt", 1000],
["Miya", 15, "Chocolade", "Africa", "Egypt", 1200],
["Miya", 16, "Chocolade", "Africa", "Egypt", 1300],
];

namesAndValues.forEach((item, index) => {
const rowIndex = index + 2;
cells.get(`A${rowIndex}`).putValue(item[0]);
cells.get(`B${rowIndex}`).putValue(item[1]);
cells.get(`C${rowIndex}`).putValue(item[2]);
cells.get(`D${rowIndex}`).putValue(item[3]);
cells.get(`E${rowIndex}`).putValue(item[4]);
cells.get(`F${rowIndex}`).putValue(item[5]);
```

### **Aggiunta di un grafico pivot**

Per creare un PivotChart usando Aspose.Cells for Node.js via C++:

1. Aggiungi un grafico.
1. Imposta il `PivotSource` del grafico per fare riferimento a una tabella pivot esistente nel foglio di calcolo.
1. Imposta altri attributi.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating an Workbook object
// Opening the excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "pivotTable_test.xlsx"));
// Adding a new sheet
const sheetIndex = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);
const sheet3 = workbook.getWorksheets().get(sheetIndex);
sheet3.setName("PivotChart");
// Adding a column chart
const index = sheet3.getCharts().add(AsposeCells.ChartType.Column, 0, 5, 28, 16);
// Setting the pivot chart data source
sheet3.getCharts().get(index).setPivotSource("PivotTable!PivotTable1");
sheet3.getCharts().get(index).setHidePivotFieldButtons(false);
// Saving the Excel file
workbook.save(path.join(dataDir, "pivotChart_test_out.xlsx"));
```

