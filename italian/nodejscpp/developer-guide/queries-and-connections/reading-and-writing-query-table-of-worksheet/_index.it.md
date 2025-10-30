---
title: Leggi e scrivi la tabella di query di un worksheet con Node.js tramite C++
linktitle: Lettura e Scrittura Tabelle Query del Foglio di lavoro di Aspose.Cells
type: docs
weight: 40
url: /it/nodejs-cpp/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells fornisce la collezione Worksheet.QueryTables che restituisce l'oggetto di tipo QueryTable per indice. Ha le seguenti due proprietà

- QueryTable.adjustColumnWidth
- QueryTable.preserveFormatting

Questi sono entrambi valori booleani. È possibile visualizzarli in Microsoft Excel tramite Dati > Connessioni > Proprietà.

{{% /alert %}}

## Lettura e Scrittura della Tabella di Query del Foglio di Lavoro

Il seguente esempio di codice legge la prima QueryTable del primo worksheet e quindi stampa entrambe le proprietà della QueryTable. Poi imposta QueryTable.preserveFormatting su true.

È possibile scaricare il file Excel di origine utilizzato in questo codice e il file Excel di output generato dal codice dai seguenti link.

- [File Excel di Origine](5115533.xlsx)
- [File Excel di Output](5115537.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first Query Table
const qt = worksheet.getQueryTables().get(0);

// Print Query Table Data
console.log("Adjust Column Width: " + qt.getAdjustColumnWidth());
console.log("Preserve Formatting: " + qt.getPreserveFormatting());

// Now set Preserve Formatting to true
qt.setPreserveFormatting(true);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```

### Output della console

Ecco l'output console del codice di esempio sopra

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Recupero dell'intervallo di risultati della tabella di query

Aspose.Cells fornisce l'opzione di leggere l'indirizzo ossia l'intervallo di risultati delle celle per una tabella di query. Il codice seguente dimostra questa funzionalità leggendo l'indirizzo dell'intervallo di risultati per una tabella di query. È possibile scaricare il file di esempio [qui](72417290.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");

// Create workbook from source excel file
const wb = new AsposeCells.Workbook(filePath);

// Display the address(range) of result range of query table
console.log(wb.getWorksheets().get(0).getQueryTables().get(0).getResultRange().getAddress());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
