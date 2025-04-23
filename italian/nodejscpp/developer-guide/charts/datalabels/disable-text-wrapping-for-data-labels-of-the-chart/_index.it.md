---
title: Disabilita l inviluppo del testo per le etichette dei dati del grafico con Node.js via C++
description: Impara come disabilitare l inviluppo del testo per le etichette dei dati nei grafici usando Aspose.Cells for Node.js via C++. La nostra guida mostrerà come evitare che le etichette lunghe si sovrappongano e come fornire visualizzazioni più chiare e leggibili del grafico.
keywords: Aspose.Cells for Node.js via C++, creazione grafici, etichette dei dati, inviluppo testo, sovrapposizione, leggibilità, visualizzazioni.
type: docs
weight: 70
url: /it/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 consente agli utenti di abilitare o disabilitare il testo all'interno delle etichette dati del grafico. Per impostazione predefinita, il testo all'interno delle etichette dati del grafico è nello stato di testo a capo.

Aspose.Cells fornisce la proprietà [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#isTextWrapped--) che puoi impostare su true o false per abilitare o disabilitare rispettivamente l'inviluppo del testo delle etichette dei dati.

{{% /alert %}}

Il campione di codice sottostante mostra come disabilitare il testo a capo per le etichette dati del grafico.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_wrap_label.xlsx");
// Load the sample Excel file inside the workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Disable the Text Wrapping of Data Labels in all Series
chart.getNSeries().get(0).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(1).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(2).getDataLabels().setIsTextWrapped(false);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```
