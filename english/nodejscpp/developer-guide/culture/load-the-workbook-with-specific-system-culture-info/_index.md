---
title: Load the Workbook with specific System Culture Info via Node.js and C++
linktitle: Load the Workbook with specific System Culture Info
type: docs
weight: 190
url: /nodejs-cpp/load-the-workbook-with-specific-system-culture-info/
---

## **Possible Usage Scenarios**
Earlier, you had to change the culture info of the entire thread to deal with numbers and dates in a particular culture format, but now Aspose.Cells for Node.js via C++ provides the `LoadOptions.CultureInfo` property which you can use to load your workbook with specific culture info without changing the culture info of the entire thread.

## **Load the Workbook with specific System Culture Info**
The following sample code shows how to load the workbook with specific system culture info to deal with dates.

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

The following sample code shows how to load the workbook with specific system culture info to deal with numbers.

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
