---
title: Cambia la direzione delle etichette dei tick con Node.js tramite C++
linktitle: Cambiare la direzione delle etichette degli intervalli
description: Impara come cambiare la direzione delle etichette dei tick in Aspose.Cells per Node.js. La nostra guida ti aiuterà a capire come regolare l orientamento delle etichette dei tick sugli assi, inclusi orientamenti orizzontali, verticali e angolati.
keywords: Aspose.Cells per Node.js, etichette dei tick, direzione, orientamento, assi, orizzontale, verticale, angolato.
type: docs
weight: 170
url: /it/nodejs-cpp/change-tick-label-direction/
---

## **Cambia la direzione delle etichette di graduazione**

Aspose.Cells ti permette di cambiare la direzione delle etichette dei tick dell'asse utilizzando la proprietà [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--). La proprietà [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--) accetta il valore dell'enumerazione [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype). L'enumerazione [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype) include i seguenti membri:

- Orizzontale
- Verticale
- Ruota90
- Ruota270
- Impilato

L'immagine seguente confronta i file sorgente e di output

### **Immagine del file sorgente**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Immagine del file di output**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Il seguente frammento di codice cambia la direzione dell'etichetta dell'asse da Rotate90 a Orizzontale.

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const filePath = path.join(sourceDir, "SampleChangeTickLabelDirection.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Horizontal);

// Output the file
workbook.save(path.join(outputDir, "outputChangeChartDataLableDirection.xlsx"));
```

I file sorgente e di output possono essere scaricati dai seguenti link.

[File sorgente](105480221.xlsx)

[File di output](105480223.xlsx)
