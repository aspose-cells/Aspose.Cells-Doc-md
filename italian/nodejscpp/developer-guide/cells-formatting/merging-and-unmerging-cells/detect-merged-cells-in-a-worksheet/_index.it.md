---
title: Rileva le celle unite in un foglio con Node.js tramite C++
linktitle: Rilevare celle unite in un foglio di lavoro
description: Impara come rilevare le celle unite in un foglio usando Aspose.Cells for Node.js via C++. Questo articolo mostrerà come usare la libreria per identificare e manipolare le celle unite.
keywords: Aspose.Cells, Foglio di lavoro, Unisci celle, Rileva, Identifica, Opera Node.js tramite C++
type: docs
weight: 80
url: /it/nodejs-cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Questo articolo fornisce informazioni su come ottenere le aree di celle unite in un foglio di lavoro.

Aspose.Cells for Node.js via C++ permette di ottenere le aree di celle unite in un foglio di lavoro. Puoi anche disunirle. Questo articolo mostra il codice più semplice usando l'API **Aspose.Cells** per eseguire il compito.

{{% /alert %}}

Il componente fornisce il metodo [**Cells.getMergedAreas()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMergedAreas--) che può ottenere tutte le celle unite. Il seguente esempio di codice mostra come rilevare le celle unite in un foglio di lavoro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Instantiate a new Workbook
// Open an existing excel file
const wkBook = new AsposeCells.Workbook(filePath);
// Get a worksheet in the workbook
const wkSheet = wkBook.getWorksheets().get("Sheet2");
// Clear its contents
wkSheet.getCells().clear();

// Get merged areas
const areas = wkSheet.getCells().getMergedAreas();

// Check if areas is null or not
if (!areas || areas.length === 0) {
console.warn("No merged areas to unmerge.");
return;
}

// Define some variables
let frow, fcol, erow, ecol, trows, tcols;
// Loop through the arraylist and get each cellarea
// To unmerge it
for (let i = 0; i < areas.length; i++) {
frow = areas[i].startRow;
fcol = areas[i].startColumn;
erow = areas[i].endRow;
ecol = areas[i].endColumn;

trows = erow - frow + 1;
tcols = ecol - fcol + 1;
wkSheet.getCells().unMerge(frow, fcol, trows, tcols);
}

const outputFilePath = path.join(dataDir, "MergeTrial.out.xlsx");
// Save the excel file
wkBook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
