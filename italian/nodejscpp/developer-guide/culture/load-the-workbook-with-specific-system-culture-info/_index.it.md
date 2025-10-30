---
title: Carica il Workbook con specifica cultura di sistema tramite Node.js e C++
linktitle: Carica il Workbook con informazioni specifiche sulle impostazioni regionali del sistema
type: docs
weight: 190
url: /it/nodejs-cpp/load-the-workbook-with-specific-system-culture-info/
---

## **Possibili Scenari di Utilizzo**
In precedenza, dovevi cambiare le info culturali dell'intero thread per gestire numeri e date in un formato culturale particolare, ma ora Aspose.Cells for Node.js via C++ offre la proprietà `LoadOptions.CultureInfo` che puoi usare per caricare il tuo workbook con informazioni sulla cultura specifica senza cambiare le info culturali dell'intero thread.

## **Carica il Workbook con informazioni specifiche sulle impostazioni regionali del sistema**
Il seguente esempio di codice mostra come caricare il workbook con informazioni sulla cultura di sistema specifica per gestire le date.

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const { Readable } = require('stream');

// Create a readable stream
const inputStream = new Readable();
inputStream._read = () => {}; // No-op

inputStream.push("<html><head><title>Test Culture</title></head><body><table><tr><td>10-01-2016</td></tr></table></body></html>");
inputStream.push(null); // Signal end of stream

const culture = new Intl.NumberFormat("en-GB", {
minimumFractionDigits: 2,
maximumFractionDigits: 2
```

Il seguente esempio di codice mostra come caricare il workbook con informazioni sulla cultura di sistema specifica per gestire i numeri.

```javascript
const AsposeCells = require("aspose.cells.node");
const { Readable } = require('stream');
const path = require("path");

const dataDir = path.join(__dirname, "data");
const inputStream = new Readable();
inputStream._read = () => {}; // No-op

inputStream.push("<html><head><title>Test Culture</title></head><body><table><tr><td>1234,56</td></tr></table></body></html>");
inputStream.push(null);

const options = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Html);        
options.setRegion(AsposeCells.CountryCode.UnitedKingdom);

(async () => {
const workbook = new AsposeCells.Workbook(inputStream, options);
const cell = workbook.getWorksheets().get(0).getCells().get("A1");
console.assert(cell.getType() === AsposeCells.CellValueType.IsNumeric);
console.assert(cell.getDoubleValue() === 1234.56);
})();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
