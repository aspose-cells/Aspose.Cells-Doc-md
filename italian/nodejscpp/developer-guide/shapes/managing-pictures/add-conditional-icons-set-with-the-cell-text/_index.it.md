---
title: Aggiungi Icone Condizionali con il testo della cella usando Node.js tramite C++
linktitle: Aggiungi un insieme di icone condizionali con il testo della cella
type: docs
weight: 160
url: /it/nodejs-cpp/add-conditional-icons-set-with-the-cell-text/
description: Impara come aggiungere icone condizionali accanto al testo della cella usando Aspose.Cells for Node.js via C++. Migliora il significato dei dati tramite icone.
---

{{% alert color="primary" %}} 

A volte, vuoi aggiungere icone condizionali accanto al testo in una cella per rendere i dati più significativi per i lettori. Vuoi usare alcuni dei tipi di icone di formattazione condizionale senza applicare la formattazione condizionale alle celle. Aspose.Cells for Node.js via C++ supporta questa funzione.

{{% /alert %}} 

Il seguente esempio di codice mostra come aggiungere un insieme di icone condizionali con il testo della cella.



```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet (default worksheet) in the workbook
const worksheet = workbook.getWorksheets().get(0);
// Get the cells
const cells = worksheet.getCells();
// Set the columns widths (A, B and C)
worksheet.getCells().setColumnWidth(0, 24);
worksheet.getCells().setColumnWidth(1, 24);
worksheet.getCells().setColumnWidth(2, 24);

// Input date into the cells
cells.get("A1").putValue("KPIs");
cells.get("A2").putValue(19551794);
cells.get("A3").putValue(11.8070745566204);
cells.get("A4").putValue(11.858589818569);
cells.get("B1").putValue("UA Contract Size Group 4");
cells.get("B2").putValue(19551794);
cells.get("B3").putValue(11.8070745566204);
cells.get("B4").putValue(11.858589818569);
cells.get("C1").putValue("UA Contract Size Group 3");
cells.get("C2").putValue(8150131.66666667);
cells.get("C3").putValue(10.3168384396244);
cells.get("C4").putValue(11.3326931937091);

// Get the conditional icon's image data and add pictures
const iconTypes = [
{ type: AsposeCells.IconSetType.TrafficLights31, row: 1, column: 1 },
{ type: AsposeCells.IconSetType.Arrows3, row: 1, column: 2 },
{ type: AsposeCells.IconSetType.Symbols3, row: 2, column: 1 },
{ type: AsposeCells.IconSetType.Stars3, row: 2, column: 2 },
{ type: AsposeCells.IconSetType.Boxes5, row: 3, column: 1 },
{ type: AsposeCells.IconSetType.Flags3, row: 3, column: 2 }
];

iconTypes.forEach(icon => {
const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(icon.type, icon.type === AsposeCells.IconSetType.Flags3 ? 1 : 0);
const stream = new Uint8Array(imagedata);
worksheet.getPictures().add(icon.row, icon.column, stream);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
