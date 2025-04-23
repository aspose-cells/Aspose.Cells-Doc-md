---
title: Leggi il sottotitolo del grafico dal file ODS usando Node.js tramite C++
linktitle: Leggi il sottotitolo del grafico dal file ODS
description: Impara a usare Aspose.Cells for Node.js via C++ per leggere il sottotitolo del grafico da un file di Foglio di Calcolo OpenDocument (ODS). La nostra guida dimostrerà come estrarre e accedere al sottotitolo di un grafico per ulteriori analisi o visualizzazione.
keywords: Aspose.Cells for Node.js via C++, Leggi sottotitolo del grafico, Foglio di Calcolo OpenDocument, File ODS, Estrazione del grafico, Analisi dei dati.
type: docs
weight: 160
url: /it/nodejs-cpp/read-chart-subtitle-from-ods-file/
---

## **Leggi il sottotitolo del grafico dal file ODS**

Aspose.Cells consente di leggere i sottotitoli dei grafici nei file ODS utilizzando la proprietà [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--). Il seguente esempio di codice carica il [file ODS di esempio](89620481.ods) e legge il sottotitolo del grafico usando la proprietà [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--), stampandolo nella Console. Consulta l'output di esempio del codice riportato di seguito come riferimento.

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Load excel file containing charts
const filePath = path.join(sourceDir, "SampleChart.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

console.log("Chart Subtitle: " + chart.getSubTitle().getText());
```

## **Output della console**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
