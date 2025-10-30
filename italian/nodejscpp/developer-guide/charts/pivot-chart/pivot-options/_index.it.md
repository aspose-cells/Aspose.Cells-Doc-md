---
title: Come Gestire PivotChart con PivotOptions in Node.js tramite C++
linktitle: Opzioni Pivot
type: docs
weight: 10
url: /it/nodejs-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Come gestire PivotChart con PivotOptions in Node.js via C++.
keywords: PivotChart Node.js tramite C++
---
## Cosa è un PivotChart

Un PivotChart in Excel è una rappresentazione grafica dei dati creata da una tabella pivot. Consente agli utenti di visualizzare e analizzare dinamicamente i dati riassumendo e visualizzando le informazioni in forma di grafico. I PivotCharts sono interattivi e possono essere facilmente modificati per mostrare diverse prospettive dei dati, rendendoli uno strumento potente per l'analisi e la presentazione dei dati in Excel.

## Come gestire PivotChart con PivotOptions

Utilizzando Aspose.Cells for Node.js via C++, puoi usare [**PivotOptions**](https://reference.aspose.com/cells/nodejs-cpp/pivotoptions/) per gestire PivotChart.

File di esempio e codice:
[File di esempio](Sample.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const chart = workbook.getWorksheets().get(0).getCharts().get(0);
const opt = chart.getPivotOptions();

// Hide ZoneFilter in PivotChart
opt.setDropZoneFilter(false); // HideZoneFilter

// You can set more properties, try them!
// opt.setDropZoneCategories(false); // HideZoneCategories
// opt.setDropZoneData(false); // HideZoneData
// opt.setDropZoneSeries(false); // HideZoneSeries
// opt.setDropZonesVisible(false); // Hide All

// Save the file and see the effect.
workbook.save(path.join(dataDir, "HideZoneFilter.xlsx"));
```

Con il codice di esempio sopra, è possibile controllare il file di risultato con l'effetto seguente, come mostrato nella figura:

**![Output](Output.png)**
{{< app/cells/assistant language="nodejs-cpp" >}}
