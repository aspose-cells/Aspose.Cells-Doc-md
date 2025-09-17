##Insert Ranges with Node.js via C++
Learn how to insert ranges in Excel and shift other data using Aspose.Cells for Node.js via C++.
## **Introduction**
In Excel, you can select a range, then insert a range and shift other data right or down.
## **Insert Ranges Using Aspose.Cells for Node.js via C++**
Aspose.Cells for Node.js via C++ provides [Cells.insertRange(CellArea, number, ShiftType, boolean)](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRange-cellarea-number-shifttype-boolean-) method to insert a range.
## **Insert Ranges And Shift Cells Right**
Insert a range and shift cells right as the following codes with Aspose.Cells:
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
// Create a range of cells.
const sourceRange = worksheet.getCells().createRange("A1", "A2");
// Input some data with some formattings into
// A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue("123");
const ca = AsposeCells.CellArea.createCellArea("A1", "A2");
worksheet.getCells().insertRange(ca, AsposeCells.ShiftType.Right);
console.log(worksheet.getCells().get("B1").getValue() === "Test");
```
## **Insert Ranges And Shift Cells Down**
Insert a range and shift cells down as the following codes with Aspose.Cells:
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
// Create a range of cells.
const sourceRange = worksheet.getCells().createRange("A1", "A2");
// Input some data with some formattings into
// A few cells in the range.
sourceRange.get(0, 0).putValue("Test");
sourceRange.get(1, 0).putValue(123);
const ca = AsposeCells.CellArea.createCellArea("A1", "A2");
worksheet.getCells().insertRange(ca, AsposeCells.ShiftType.Down);
console.log(worksheet.getCells().get("A3").getValue() === "Test");
```
