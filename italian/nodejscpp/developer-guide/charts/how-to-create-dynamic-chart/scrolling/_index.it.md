---
title: Come creare un Grafico Scorrevole Dinamico con Node.js tramite C++
linktitle: Come creare un grafico dinamico a scorrimento
description: Impara come creare un grafico scorrevole dinamico usando Aspose.Cells for Node.js via C++. La nostra guida passo passo mostrerà come implementare transizioni di dati fluide e scorrimento automatico nel tuo grafico per una visualizzazione continua e aggiornata.
keywords: Aspose.Cells per Node.js, Grafico Scorrevole Dinamico, Transizioni di Dati, Scorrimento Fluido, Visualizzazione Continua, Aggiornamento Visualizzazione.
type: docs
weight: 75
url: /it/nodejs-cpp/create-dynamic-scrolling-chart/
---

## **Possibili Scenari di Utilizzo**
Un grafico dinamico a scorrimento è un tipo di rappresentazione grafica utilizzato per visualizzare dati che cambiano nel tempo. È progettato per fornire una visualizzazione in tempo reale dei dati, consentendo agli utenti di monitorare aggiornamenti e tendenze continui. Il grafico si aggiorna continuamente man mano che vengono aggiunti nuovi dati e scorre automaticamente per mostrare le informazioni più recenti.

I grafici dinamici a scorrimento sono comunemente utilizzati in vari settori, come finanza, analisi del mercato azionario, tracciamento del meteo e analisi dei social media. Consentono agli utenti di visualizzare e analizzare pattern di dati e prendere decisioni informate basate su informazioni in tempo reale.

Questi grafici sono tipicamente interattivi, consentendo all'utente di ingrandire o ridurre, scorrere attraverso dati storici e regolare gli intervalli temporali. Spesso supportano più serie di dati, fornendo una visione completa di diverse metriche e le loro correlazioni.

In generale, i grafici di scorrimento dinamici sono strumenti preziosi per monitorare e analizzare i dati a serie temporali, facilitando la presa delle decisioni in tempo reale e potenziando le capacità di visualizzazione dei dati.

## **Usa Aspose.Cells per creare un Grafico Scorrevole Dinamico**
 Nei paragrafi successivi, ti mostreremo come creare un Grafico Scorrevole Dinamico usando Aspose.Cells for Node.js via C++. Mostreremo il codice dell'esempio, così come il file Excel creato con questo codice.

## **Codice di Esempio**
Il codice di esempio seguente genererà il [File del grafico di scorrimento dinamico](DynamicScrollingChart.xlsx).

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
sheet.getCells().get("A1").putValue("Day");
sheet.getCells().get("B1").putValue("Sales");
// In this example, we will add 30 days of data
const allDays = 30;
const showDays = 10;
let currentDay = 1;

for (let i = 0; i < allDays; i++) {
const cellA = `A${i + 2}`;
const cellB = `B${i + 2}`;
sheet.getCells().get(cellA).putValue(i + 1);
sheet.getCells().get(cellB).putValue(50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3));
}

// This is the Dynamic Scrolling Control Data
sheet.getCells().get("G19").putValue("Start Day");
sheet.getCells().get("G20").putValue(currentDay);
sheet.getCells().get("H19").putValue("Show Days");
sheet.getCells().get("H20").putValue(showDays);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtScrollData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtScrollLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Add a ScrollBar for the Dynamic Scrolling Chart
const bar = sheet.getShapes().addScrollBar(2, 0, 3, 0, 200, 30);
bar.setMin(0);
bar.setMax(allDays - showDays);
bar.setCurrentValue(currentDay);
bar.setLinkedCell("$G$20");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 2, 4, 15, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtScrollData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtScrollLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicScrollingChart.xlsx"));
```

## **Note**
Nel file generato, è possibile operare sulla barra di scorrimento, mentre il grafico conta dinamicamente gli ultimi 10 set di dati. Ciò viene fatto utilizzando la formula "OFFSET" nel codice di esempio:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

Puoi provare a cambiare il numero "10" in "15" nella cella "Sheet1!$H$20", e il grafico dinamico conterà gli ultimi 15 set di dati. Ora abbiamo creato con successo un grafico scorrevole dinamico usando Aspose.Cells for Node.js via C++.
