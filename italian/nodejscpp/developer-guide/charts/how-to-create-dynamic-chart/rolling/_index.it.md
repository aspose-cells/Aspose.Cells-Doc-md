---
title: Come creare un Grafico a Ribaltamento Dinamico con Node.js tramite C++
linktitle: Come creare un grafico dinamico a scorrimento
description: Impara come creare un grafico a ribaltamento dinamico usando Aspose.Cells for Node.js via C++. La nostra guida dimostrerà come implementare transizioni di dati fluide e medie mobili nel tuo grafico per una visualizzazione continua e aggiornata.
keywords: Aspose.Cells per Node.js, Grafico Dinamico a Ribaltamento, Transizioni di Dati, Medie Mobili Fluide, Visualizzazione Continua, Aggiornamento Visualizzazione.
type: docs
weight: 74
url: /it/nodejs-cpp/create-dynamic-rolling-chart/
---

## **Possibili Scenari di Utilizzo**
Un grafico dinamico a scorrimento si riferisce a una rappresentazione grafica che visualizza costantemente punti dati in continuo spostamento e aggiornamento nel tempo. È un tipo di grafico che si aggiorna continuamente, mostrando una finestra mobile dei punti dati più recenti mentre scarta i punti dati più vecchi man mano che ne arrivano di nuovi.

I grafici dinamici a scorrimento sono comunemente utilizzati per visualizzare tendenze e pattern in dati in tempo reale o in streaming. Sono particolarmente utili in scenari in cui gli aspetti temporali e i cambiamenti nel tempo sono fondamentali, come l'analisi di mercato azionario, il monitoraggio meteorologico o il tracciamento delle performance in tempo reale.

Questi grafici di solito impiegano meccanismi di animazione o autoscrolling per assicurare che le informazioni più aggiornate siano sempre presentate. La lunghezza della finestra mobile può essere personalizzata per mostrare un periodo temporale specifico, come l'ultima ora, giorno o settimana.

In sintesi, un grafico dinamico a scorrimento è una rappresentazione grafica continuamente aggiornata che visualizza gli ultimi punti dati mentre scarta quelli più vecchi, consentendo agli utenti di osservare tendenze e pattern in tempo reale.

## **Usa Aspose Cells per creare un grafico dinamico a scorrimento**
Nei paragrafi successivi, ti mostreremo come creare un grafico dinamico a scorrimento utilizzando Aspose.Cells. Ti mostreremo il codice dell'esempio, nonché il file Excel creato con questo codice.

## **Codice di Esempio**
Il seguente codice di esempio genererà il [File del Grafico Dinamico a Scorrimento](DynamicRollingChart.xlsx).

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
sheet.getCells().get("A1").putValue("Month");
sheet.getCells().get("A2").putValue(1);
sheet.getCells().get("A3").putValue(2);
sheet.getCells().get("A4").putValue(3);
sheet.getCells().get("A5").putValue(4);
sheet.getCells().get("A6").putValue(5);
sheet.getCells().get("A7").putValue(6);
sheet.getCells().get("A8").putValue(7);

sheet.getCells().get("B1").putValue("Sales");
sheet.getCells().get("B2").putValue(50);
sheet.getCells().get("B3").putValue(45);
sheet.getCells().get("B4").putValue(55);
sheet.getCells().get("B5").putValue(60);
sheet.getCells().get("B6").putValue(55);
sheet.getCells().get("B7").putValue(65);
sheet.getCells().get("B8").putValue(70);

// Set the dynamic range for the chart's data source.
let index = sheets.getNames().add("Sheet1!ChtData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

// Set the dynamic range for the chart's data labels.
index = sheets.getNames().add("Sheet1!ChtLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 10, 3, 25, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicRollingChart.xlsx"));
```

## **Note**
Nel file generato, puoi continuare ad aggiungere dati nelle colonne A e B, mentre il grafico conta dinamicamente gli ultimi 5 set di dati. Ciò viene fatto utilizzando la formula "SCARTO" nel codice di esempio:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Puoi provare a cambiare il numero "-5" in "-10" nella formula, e il grafico dinamico conterà gli ultimi 10 set di dati. Ora abbiamo creato con successo un grafico dinamico a scorrimento utilizzando Aspose.Cells.
{{< app/cells/assistant language="nodejs-cpp" >}}
