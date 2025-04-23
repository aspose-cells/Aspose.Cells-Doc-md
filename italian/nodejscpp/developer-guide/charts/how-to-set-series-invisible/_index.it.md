---
title: Come impostare la serie invisibile con Node.js tramite C++
linktitle: Come impostare la serie come invisibile
description: Impara come impostare le serie come invisibili nel grafico Excel usando Aspose.Cells for Node.js via C++. 
keywords: Grafico Excel, Serie, Invisibile, IsFiltered Node.js tramite C++.
type: docs
weight: 74
url: /it/nodejs-cpp/how-to-set-series-invisible/
---

## Come impostare le serie come invisibili nel grafico Excel

In Excel, puoi cliccare con il tasto destro su un grafico, cliccare su "Seleziona dati", e nella finestra popup puoi impostare se una serie è visibile spuntando o deselezionando l'opzione. Puoi scaricare il seguente [file di esempio](SeriesFiltered.xlsx) e operarlo in Excel come mostrato nella figura per ottenere questa funzione. Successivamente, ti spiegheremo come farlo usando la libreria Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## Come impostare le serie come invisibili usando Aspose.Cells 

Usiamo il seguente codice per impostare le serie come invisibili usando Aspose.Cells:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SeriesFiltered.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const charts = workbook.getWorksheets().get(0).getCharts();
const chart = charts.get("Chart 1");
const nSeriesFiltered = chart.getFilteredNSeries();
const nSeries = chart.getNSeries();
nSeries.get(1).setIsColorVaried(true);
nSeries.get(0).setIsColorVaried(true);
workbook.save(path.join(dataDir, "output.xlsx"));
```

Puoi ottenere il seguente [File di input](SeriesFiltered.xlsx) e [file di output](output.xlsx).

Come mostrato nella figura sotto, le prime due serie, che erano visibili originariamente, sono diventate invisibili nel file di output.
![todo:image_alt_text](output.png)
