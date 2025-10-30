---
title: Rimuovere righe duplicate in un foglio di lavoro con Node.js tramite C++
linktitle: Rimuovere righe duplicate in un foglio di lavoro
type: docs
weight: 370
url: /it/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/
description: Impara come rimuovere righe duplicate in un foglio di lavoro usando Aspose.Cells for Node.js via C++ e selezionare colonne specifiche per i controlli di duplicazione.
---


Rimuovere righe duplicate è una delle molte funzionalità utili di Microsoft Excel. Consente agli utenti di rimuovere righe duplicate in un Foglio di lavoro, e puoi scegliere quali colonne devono essere controllate per informazioni duplicate.

Aspose.Cells for Node.js via C++ fornisce il metodo `Cells.removeDuplicates()` a questo scopo. Puoi anche impostare `startRow`, `startColumn`, `endRow` e `endColumn` per specificare l'intervallo di colonne da controllare per i duplicati.

Di seguito sono riportati i file di esempio che possono essere scaricati per testare questa funzionalità:

[removeduplicates.xlsx](removeduplicates.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "removeduplicates.xlsx");

// Create workbook
const book = new AsposeCells.Workbook(filePath);

// Remove Duplicate
book.getWorksheets().get(0).getCells().removeDuplicates(0, 0, 5, 3);

// Save result
book.save("removeduplicates-result.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
