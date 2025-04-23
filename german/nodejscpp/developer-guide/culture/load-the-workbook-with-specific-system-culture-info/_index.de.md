---
title: Laden Sie die Arbeitsmappe mit spezifischen Systemkulturinformationen mittels Node.js und C++
linktitle: Laden Sie die Arbeitsmappe mit bestimmten Systemkulturinformationen
type: docs
weight: 190
url: /de/nodejs-cpp/load-the-workbook-with-specific-system-culture-info/
---

## **Mögliche Verwendungsszenarien**
Früher mussten Sie die Kulturinformationen des gesamten Threads ändern, um Zahlen und Daten in einem bestimmten Kulturformat zu behandeln. Jetzt bietet Aspose.Cells for Node.js via C++ die Eigenschaft `LoadOptions.CultureInfo`, mit der Sie Ihre Arbeitsmappe mit spezifischen Kulturinformationen laden können, ohne die Kulturinformationen des gesamten Threads zu ändern.

## **Laden Sie die Arbeitsmappe mit bestimmten Systemkulturinformationen**
Das folgende Beispiel zeigt, wie die Arbeitsmappe mit spezifischen Systemkulturinformationen geladen wird, um mit Daten umzugehen.

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

Das folgende Beispiel zeigt, wie die Arbeitsmappe mit spezifischen Systemkulturinformationen geladen wird, um mit Zahlen umzugehen.

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
