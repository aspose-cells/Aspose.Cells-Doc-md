---
title: Ladda arbetsboken med specifik systemkulturinfo via Node.js och C++
linktitle: Ladda arbetsboken med specifik systemkulturinformation
type: docs
weight: 190
url: /sv/nodejs-cpp/load-the-workbook-with-specific-system-culture-info/
---

## **Möjliga användningsscenario**
Tidigare var du tvungen att ändra kulturinformationen för hela tråden för att hantera nummer och datum i ett visst kulturformat, men nu ger Aspose.Cells for Node.js via C++ egenskapen `LoadOptions.CultureInfo` för att ladda din arbetsbok med specifik kulturinfo utan att ändra kulturinformationen för hela tråden.

## **Ladda arbetsboken med specifik systemkulturinformation**
Följande kodexempel visar hur man laddar arbetsboken med specifik systemkulturinfo för att hantera datum.

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

Följande kodexempel visar hur man laddar arbetsboken med specifik systemkulturinfo för att hantera nummer.

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
