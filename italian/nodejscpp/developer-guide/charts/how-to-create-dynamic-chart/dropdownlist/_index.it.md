---
title: Come creare un Grafico Dinamico con Lista a Discesa usando Node.js tramite C++
linktitle: Come creare un grafico dinamico con elenco a discesa
description: Impara come creare un grafico dinamico che si aggiorna in base alla selezione di una lista a discesa usando Aspose.Cells for Node.js via C++. La nostra guida passo passo ti mostrerà come integrare una lista a discesa nel tuo grafico per una visualizzazione dei dati flessibile.
keywords: Aspose.Cells for Node.js via C++, Grafico Dinamico, Lista a Discesa, Visualizzazione dei Dati, Integrazione, Visualizzazione Flessibile.
type: docs
weight: 76
url: /it/nodejs-cpp/create-dynamic-chart-with-dropdownlist/
---

## **Possibili Scenari di Utilizzo**
Un grafico dinamico con elenco a discesa in Excel è uno strumento potente che consente agli utenti di creare grafici interattivi che possono aggiornarsi dinamicamente in base ai dati selezionati. Questa funzione è particolarmente utile in situazioni in cui è necessario analizzare più set di dati o confrontare vari scenari.

Una comune applicazione di un grafico dinamico con elenco a discesa è nell'analisi finanziaria. Ad esempio, un'azienda potrebbe avere dati finanziari per diversi anni o reparti. Utilizzando un elenco a discesa, gli utenti possono selezionare il set di dati specifico che desiderano analizzare e il grafico si aggiornerà automaticamente per visualizzare le informazioni corrispondenti. Questo consente un facile confronto e identificazione di tendenze o pattern.

Un'altra applicazione è nelle vendite e nel marketing. Un'azienda potrebbe avere dati di vendita per diversi prodotti o regioni. Con un grafico dinamico con elenco a discesa, gli utenti possono scegliere un prodotto o una regione specifica dall'elenco a discesa e il grafico si aggiornerà dinamicamente per mostrare le performance di vendita per l'opzione selezionata. Ciò aiuta a identificare le aree o i prodotti più performanti e a prendere decisioni basate sui dati.

In sintesi, un grafico dinamico con elenco a discesa in Excel fornisce un modo flessibile e interattivo per visualizzare e analizzare i dati. È prezioso in situazioni in cui è necessario confrontare più set di dati o esplorare diversi scenari, rendendolo uno strumento versatile per l'analisi finanziaria, le vendite e il marketing e molte altre applicazioni.

## **Usa Aspose Cells per creare un grafico dinamico con elenco a discesa**
 Nei paragrafi successivi, ti mostreremo come creare un Grafico Dinamico con Lista a Discesa usando Aspose.Cells for Node.js via C++. Mostreremo il codice dell'esempio, così come il file Excel creato con questo codice.

## **Codice di Esempio**
Il seguente codice di esempio genererà il [File del grafico dinamico con elenco a discesa](DynamicChartWithDropdownlist.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A3").putValue("Tea");
sheet.getCells().get("A4").putValue("Coffee");
sheet.getCells().get("A5").putValue("Sugar");

// In this example, we will add 12 months of data
sheet.getCells().get("B2").putValue("Jan");
sheet.getCells().get("C2").putValue("Feb");
sheet.getCells().get("D2").putValue("Mar");
sheet.getCells().get("E2").putValue("Apr");
sheet.getCells().get("F2").putValue("May");
sheet.getCells().get("G2").putValue("Jun");
sheet.getCells().get("H2").putValue("Jul");
sheet.getCells().get("I2").putValue("Aug");
sheet.getCells().get("J2").putValue("Sep");
sheet.getCells().get("K2").putValue("Oct");
sheet.getCells().get("L2").putValue("Nov");
sheet.getCells().get("M2").putValue("Dec");
const allMonths = 12;
const iCount = 3;
for (let i = 0; i < iCount; i++) {
for (let j = 0; j < allMonths; j++) {
const _row = i + 2;
const _column = j + 1; 
sheet.getCells().get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
}
}

// This is the Dropdownlist for Dynamic Data
const ca = AsposeCells.CellArea.createCellArea(9, 0, 9, 0);
const _index = sheet.getValidations().add(ca);
const _va = sheet.getValidations().get(_index);
_va.setType(AsposeCells.ValidationType.List);
_va.setInCellDropDown(true);
_va.setFormula1("=$B$2:$M$2");
sheet.getCells().get("A9").putValue("Current Month");
sheet.getCells().get("A10").putValue("Jan");
const _style = sheet.getCells().get("A10").getStyle();
_style.getFont().setIsBold(true);
_style.setPattern(AsposeCells.BackgroundType.Solid);
_style.setForegroundColor(AsposeCells.Color.Yellow);
sheet.getCells().get("A10").setStyle(_style);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtMonthData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtXLabels");
sheets.getNames().get(index).setRefersTo("=Sheet1!$A$3:$A$5");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 8, 2, 20, 8);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("month", true);
chart.getNSeries().get(0).setName("=Sheet1!$A$10");
chart.getNSeries().get(0).setValues("Sheet1!ChtMonthData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtXLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicChartWithDropdownlist.xlsx"));
```

## **Note**
Nel file generato, il grafico conterà dinamicamente i dati per il mese selezionato. Questo viene fatto utilizzando la formula "OFFSET" nel codice di esempio:

```
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

Puoi provare a cambiare il valore della lista a discesa nella cella "Foglio1!$A$10", e vedrai il cambiamento dinamico del grafico. Abbiamo creato con successo un grafico dinamico con lista a discesa utilizzando Aspose.Cells.
