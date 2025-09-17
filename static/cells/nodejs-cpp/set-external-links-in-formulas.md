##Set External Links in Formulas with Node.js via C++
Learn how to set external links in formulas using Aspose.Cells for Node.js via C++.
Sometimes, it is necessary to include links to external files in formulas, for example, to evaluate a cell or range value against them. Aspose.Cells for Node.js via C++ provides this feature and this document explains how to use it.
The sample code below shows how to include external files in formulas.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();
// Get first Worksheet
const sheet = workbook.getWorksheets().get(0);
// Get Cells collection
const cells = sheet.getCells();
// Set formula with external links
cells.get("A1").setFormula(`=SUM('[${filePath}]Sheet1'!A2, '[${filePath}]Sheet1'!A4)`);
// Set formula with external links
cells.get("A2").setFormula(`='[${filePath}]Sheet1'!A8`);
// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
