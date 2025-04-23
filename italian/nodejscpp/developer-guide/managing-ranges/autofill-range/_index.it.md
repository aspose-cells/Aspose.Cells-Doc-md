---
title: Auto inserimento di una gamma di celle di Excel con Node.js tramite C++
linktitle: Intervallo di riempimento automatico
type: docs
weight: 105
url: /it/nodejs-cpp/autofill-ranges/
description: Scopri come eseguire un operazione di auto inserimento in un intervallo specificato di un file Excel usando Aspose.Cells for Node.js via C++.
---

Esegui un'autocompletamento nell'intervallo specificato in Excel

In Excel, seleziona un intervallo, sposta il mouse in basso a destra e trascina la "più" per riempire automaticamente i dati.

## **Intervalli di riempimento automatico con Aspose.Cells for Node.js via C++**

Il seguente esempio mostra come eseguire un'operazione di riempimento automatico su un intervallo, e qui il file di esempio che puoi scaricare per testare questa funzione:

[range_autofill.xlsx](range_autofill.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "range_autofill.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("C3:C4");
const dest = cells.createRange("C5:C10");
// AutoFill
src.autoFill(dest, AsposeCells.AutoFillType.Series);
// Save the Workbook
workbook.save("range_autofill_result.xlsx");
```

