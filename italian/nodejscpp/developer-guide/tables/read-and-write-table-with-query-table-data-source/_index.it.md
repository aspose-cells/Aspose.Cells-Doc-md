---
title: Leggi e Scrivi Tabella con Data Source Query Table via Node.js
linktitle: Leggi e Scrivi Tabella con Origine Dati Tabella Query
type: docs
weight: 30
url: /it/nodejs-cpp/read-and-write-table-with-query-table-data-source/
description: Impara come leggere e scrivere una tabella con una data source QueryTable usando Aspose.Cells for Node.js via C++. 
---

## **Leggere e scrivere una tabella con dati della tabella di query**
Con Aspose.Cells for Node.js via C++, puoi leggere e scrivere una tabella che ha un QueryTable come fonte dati. Il supporto per questa funzione esiste anche per i file XLS. Il seguente snippet di codice dimostra come leggere e scrivere una tale tabella prima leggendo la tabella e poi modificandola per aggiungere la riga dei totali.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the source directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load workbook object
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTableWithQueryTable.xls"));

const worksheet = workbook.getWorksheets().get(0);

const table = worksheet.getListObjects().get(0);

// Check the data source type if it is query table
if (table.getDataSourceType() === AsposeCells.TableDataSourceType.QueryTable) {
table.setShowTotals(true);
}

// Save the file
workbook.save(path.join(outputDir, "SampleTableWithQueryTable_out.xls"));
```

I file excel sorgente e di output sono allegati a scopo informativo.

[File di origine](96928091.xls)

[File di output](96928092.xls)
{{< app/cells/assistant language="nodejs-cpp" >}}
