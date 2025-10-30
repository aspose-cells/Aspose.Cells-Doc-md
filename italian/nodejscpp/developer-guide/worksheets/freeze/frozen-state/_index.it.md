---
title: Come verificare lo stato di congelamento senza Excel usando Node.js tramite C++
linktitle: Stato congelato
type: docs
weight: 190
url: /it/nodejs-cpp/how-to-check-frozen-state-of-excel-worksheet
description: In questo articolo, imparerai come verificare lo stato di congelamento di un foglio Excel programmaticamente usando Node.js con libreria C++.

---

## **Introduzione**

 In questo articolo, impareremo come verificare lo stato di congelamento di un foglio Excel programmaticamente. Possiamo semplicemente scoprire se il foglio di lavoro è congelato o diviso in MS Excel. Ma c'è un modo per scoprire se è congelato o diviso con Node.js? Possiamo farlo semplicemente con Aspose.Cells for Node.js via C++.

## **Le riquadri della finestra sono congelati**
Con Aspose.Cells for Node.js via C++, possiamo verificare se la finestra è congelata e quante righe e colonne sono bloccate.

Usa la proprietà [**Worksheet.getPaneState()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPaneState--) per controllare lo stato delle ante di finestra e ottenere righe e colonne bloccate con il metodo [**Worksheet.getFreezedPanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFreezedPanes--).
1. Costruire il Workbook per aprire il file.
2. Verificare se il foglio di lavoro è congelato.
3. Ottieni le righe e le colonne bloccate.

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Frozen.xlsx");

// Loads the workbook which contains frozen panes
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Check whether worksheet is frozen.
if (sheet.getPaneState() === AsposeCells.PaneStateType.Frozen || sheet.getPaneState() === AsposeCells.PaneStateType.FrozenSplit) {
let row, column, rows, columns;
// Gets locked rows and columns.
sheet.getFreezedPanes().forEach((value) => {
row = value[0];
column = value[1];
rows = value[2];
columns = value[3];
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
