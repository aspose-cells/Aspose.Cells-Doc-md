---
title: Elimina righe e colonne vuote in un foglio di lavoro con Node.js tramite C++
linktitle: Eliminare Righe e Colonne Vuote in un Foglio di Lavoro
type: docs
weight: 300
url: /it/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Impara come eliminare tutte le righe e le colonne vuote da un foglio di lavoro usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

È possibile eliminare tutte le righe e colonne vuote da un foglio di lavoro. Questo è utile quando, ad esempio, si genera un file PDF da un file Microsoft Excel e si desidera convertire solo le righe e colonne che contengono dati o oggetti correlati.

Utilizzare i seguenti metodi Aspose.Cells per eliminare le righe e le colonne vuote:

1. Per eliminare le righe vuote, utilizzare il metodo [**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankRows--). Si prega di notare che, per le righe vuote che verranno eliminate, non è solo richiesto che [**Row.isBlank()**](https://reference.aspose.com/cells/nodejs-cpp/row/#isBlank--) sia vero, ma non deve essere definito alcun commento visibile per qualsiasi cella in quelle righe e non deve esserci alcuna tabella pivot il cui intervallo si sovrapponga con esse.
2. Per eliminare colonne vuote, utilizza il metodo [**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankColumns--).

{{% /alert %}}

## Codice Node.js per eliminare righe vuote

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(filePath);

// Create a Worksheets object with reference to
// The sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Rows from the worksheet
sheet.getCells().deleteBlankRows();

// Save the excel file.
wb.save(path.join(dataDir, "mybook.out.xlsx"));
```

## Codice Node.js per Eliminare colonne vuote

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an existing excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleInput.xlsx"));

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = workbook.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Columns from the worksheet
sheet.getCells().deleteBlankColumns();

// Save the excel file.
workbook.save(path.join(dataDir, "mybook.out.xlsx"));
```
