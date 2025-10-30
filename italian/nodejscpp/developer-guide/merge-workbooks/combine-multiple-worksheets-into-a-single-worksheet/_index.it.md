---
title: Combina più fogli di lavoro in un singolo foglio di lavoro con Node.js tramite C++
linktitle: Combina più fogli di lavoro in un unico foglio di lavoro
type: docs
weight: 160
url: /it/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: Impara come combinare più fogli di lavoro in un singolo foglio usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

A volte è necessario combinare più fogli di lavoro in un unico foglio di lavoro. Questo può essere facilmente ottenuto utilizzando l'API Aspose.Cells. Questo articolo ti mostrerà un esempio di codice che legge un libro di lavoro di origine e combina i dati di tutti i fogli di lavoro di origine in un unico foglio di lavoro all'interno di un libro di lavoro di destinazione.

{{% /alert %}} 

Il seguente esempio di codice mostra come combinare più fogli di lavoro in un unico foglio di lavoro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const destWorkbook = new AsposeCells.Workbook();
const destSheet = destWorkbook.getWorksheets().get(0);

let TotalRowCount = 0;

for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
const sourceSheet = workbook.getWorksheets().get(i);

const sourceRange = sourceSheet.getCells().getMaxDisplayRange();
const destRange = destSheet.getCells().createRange(
sourceRange.getFirstRow() + TotalRowCount,
sourceRange.getFirstColumn(),
sourceRange.getRowCount(),
sourceRange.getColumnCount()
);

destRange.copy(sourceRange);
TotalRowCount += sourceRange.getRowCount();
}

const outputFilePath = path.join(dataDir, "Output.out.xlsx");
destWorkbook.save(outputFilePath);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
