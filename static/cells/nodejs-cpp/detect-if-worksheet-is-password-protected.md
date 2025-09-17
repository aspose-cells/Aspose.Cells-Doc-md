##Detect if Worksheet is Password Protected with Node.js via C++
Learn how to detect if a worksheet is password protected using Aspose.Cells for Node.js via C++.
It is possible to protect the workbooks and worksheets separately. For instance, a spreadsheet may contain one or more worksheets that are password-protected, however, the spreadsheet itself may or may not be protected. Aspose.Cells APIs provide the means to detect if a given worksheet is password protected or not. This article demonstrates the usage of Aspose.Cells for Node.js via C++ API to achieve the same.
Aspose.Cells for Node.js via C++ has exposed the [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) property to detect if a worksheet is password protected or not. Boolean type [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) property returns **true** if [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) is password-protected and **false** if not.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook and load a spreadsheet
const book = new AsposeCells.Workbook(filePath);
// Access the protected Worksheet
const sheet = book.getWorksheets().get(0);
// Check if Worksheet is password protected
if (sheet.getProtection().isProtectedWithPassword()) {
console.log("Worksheet is password protected");
} else {
console.log("Worksheet is not password protected");
}
```
