##Delete Ranges with Node.js via C++
Learn how to delete ranges in Excel and shift cells left or up using Aspose.Cells for Node.js via C++.
## **Introduction**
In Excel, you can select a range, then delete it and shift other data left or up.
## **Delete Ranges Using Aspose.Cells for Node.js via C++**
Aspose.Cells provides [Cells.deleteRange(number, number, number, number, ShiftType)](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRange-number-number-number-number-shifttype-) method to delete a range.
## **Delete Ranges And Shift Cells Left**
Delete a range and shift cells left as the following codes with Aspose.Cells for Node.js via C++:
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Instantiate a new Workbook.
const newWorkbook = new AsposeCells.Workbook();
// Get all the worksheets in the book.
const worksheets = newWorkbook.getWorksheets();
// Get the first worksheet in the worksheets collection.
const worksheet = newWorkbook.getWorksheets().get(0);
// Gets cells.
const cells = worksheet.getCells();
// Input some data with some formattings into
// A few cells in the range.
cells.get("C2").putValue("C2");
cells.get("C3").putValue("C3");
const ca = AsposeCells.CellArea.createCellArea("B2", "B3");
cells.deleteRange(ca.startRow, ca.startColumn, ca.endRow, ca.endColumn, AsposeCells.ShiftType.Left);
console.log(worksheet.getCells().get("B2").getStringValue() === "C2");
```
## **Delete Ranges And Shift Cells Up**
Delete a range and shift cells up as the following codes with Aspose.Cells for Node.js via C++:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Instantiate a new Workbook.
const newWorkbook = new AsposeCells.Workbook();
// Get all the worksheets in the book.
const worksheets = newWorkbook.getWorksheets();
// Get the first worksheet in the worksheets collection.
const worksheet = newWorkbook.getWorksheets().get(0);
// Gets cells.
const cells = worksheet.getCells();
// Input some data with some formattings into
// A few cells in the range.
cells.get("B4").putValue("B4");
cells.get("B5").putValue("B5");
const ca = AsposeCells.CellArea.createCellArea("B2", "B3");
cells.deleteRange(ca.startRow, ca.startColumn, ca.endRow, ca.endColumn, AsposeCells.ShiftType.Up);
console.log(cells.get("B2").stringValue === "B4");
```
