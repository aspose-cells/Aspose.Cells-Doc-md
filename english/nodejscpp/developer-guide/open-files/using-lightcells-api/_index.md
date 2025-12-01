---  
title: Using LightCells API with Node.js via C++  
linktitle: Using LightCells API  
type: docs  
weight: 160  
url: /nodejs-cpp/using-lightcells-api/  
description: Learn how to read and write large Excel files using the LightCells API in Node.js via C++. Improve performance and efficiency with less memory consumption.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

Sometimes you need to read and write large Microsoft Excel files with a huge list of data or content in the worksheet. The LightCells API is useful for creating huge Excel spreadsheets: with it, you need less memory and get better performance and efficiency.  

{{% /alert %}}  
# Event Driven Architecture  
Aspose.Cells provides the LightCells API, mainly designed to manipulate cell data one by one without building a complete data model block (using the Cell collection etc.) into memory. It works in an event-driven mode.  

To save workbooks, provide the cell content cell by cell when saving, and the component saves it to the output file directly.  

When reading template files, the component parses every cell and provides their value one by one.  

In both procedures, one Cell object is processed and then discarded; the Workbook object does not hold the collection. In this mode, therefore, memory is saved when importing and exporting Microsoft Excel files that have a large data set which would otherwise use a lot of memory.  

Even though the LightCells API processes the cells in the same way for XLSX and XLS files (it does not actually load all cells in memory but processes one cell and then discards it), it saves memory more effectively for XLSX files than XLS files because of the different data models and structures of the two formats.  

However, **for XLS files**, to save more memory, developers can specify a temporary location for saving temporary data generated during the Save process. Commonly, **using LightCells API to save XLSX files may save 50% or more memory** than using the common way; **saving XLS may save about 20-40% memory**.  

## Writing a Large Excel File  
Aspose.Cells provides an interface, `LightCellsDataProvider`, that needs to be implemented in your program. The interface represents the data provider for saving large spreadsheet files in light-weight mode.  

When saving a workbook by this mode, `StartSheet(int)` is checked when saving every worksheet in the workbook. For one sheet, if `StartSheet(int)` is true, then all the data and properties of rows and cells of this sheet to be saved are provided by this implementation. In the first place, `NextRow()` is called to get the next row index to be saved. If a valid row index is returned (the row index must be in ascending order for the rows to be saved), then a Row object representing this row is provided for implementation to set its properties by `StartRow(Row)`.  

For one row, `NextCell()` is checked first. If a valid column index is returned (the column index must be in ascending order for all cells of one row to be saved), then a Cell object representing that cell is provided for implementation to set its data and properties by `StartCell(Cell)`. After the data of the cell is set, the cell is saved directly to the generated spreadsheet file and the next cell is checked and processed.  
### Writing a Large Excel File: Example  
Please see the following sample code to see the working of the LightCells API. Add and remove, or update the code segments according to your needs.  

The program creates a huge file with **10,000 (10000x30 matrix) records** in a worksheet and fills them with dummy data. You can specify your own matrix by changing the `rowsCount` and `colsCount` variables in the `Main()` method.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class TestDataProvider {
constructor(workbook, maxRows, maxColumns) {
this._workbook = workbook;
this.maxRows = maxRows;
this.maxColumns = maxColumns;
this._row = -1;
this._column = -1;
}

isGatherString() {
return false;
}

nextCell() {
this._column++;
if (this._column < this.maxColumns) {
return this._column;
} else {
this._column = -1;
return -1;
}
}

nextRow() {
this._row++;
if (this._row < this.maxRows) {
this._column = -1;
return this._row;
} else {
return -1;
}
}

startCell(cell) {
cell.putValue(this._row + this._column);
if (this._row !== 1) {
cell.setFormula("=Rand() + A2");
}
}

startRow(row) {
}

startSheet(sheetIndex) {
return sheetIndex === 0;
}
}

const run = async () => {
const dataDir = path.join(__dirname, "data");

const rowsCount = 10000;
const colsCount = 30;

const workbook = new AsposeCells.Workbook();
const ooxmlSaveOptions = new AsposeCells.OoxmlSaveOptions();

ooxmlSaveOptions.setLightCellsDataProvider(new TestDataProvider(workbook, rowsCount, colsCount));

await workbook.saveAsync(path.join(dataDir, "output.out.xlsx"), ooxmlSaveOptions);
};

run();
```  

## Reading Large Excel Files  
Aspose.Cells provides an interface, `LightCellsDataHandler`, that needs to be implemented in your program. The interface represents the data provider for reading large spreadsheet files in light-weight mode.  

When reading a workbook in this mode, `StartSheet` is checked when reading every worksheet in the workbook. For a sheet, if `StartSheet` returns true, then all the data and properties of the cells in rows and columns of the sheet are checked and processed by the implementation of this interface. For every row, `StartRow` is called to check whether it needs to be processed. If a row needs to be processed, its properties are read first, and the developer can access its properties with `ProcessRow`. If the row's cells also need to be processed, then `ProcessRow` should return true, and then `StartCell` is called for every existing cell in the row to check whether one cell needs to be processed. If one cell needs to be processed, then `ProcessCell` is called to process the cell by the implementation of this interface.  
### Reading Large Excel Files: Example  
Please see the following sample code to see the working of the LightCells API. Add and remove, or update the code segments according to your needs.  

The program reads a huge file with millions of records in a worksheet. It takes a little time to read each sheet in the workbook. The sample code reads the file and retrieves the total number of cells, the string count, and formula count in each worksheet.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class LightCellsDataHandlerVisitCells {
constructor() {
this.cellCount = 0;
this.formulaCount = 0;
this.stringCount = 0;
}

get CellCount() {
return this.cellCount;
}

get FormulaCount() {
return this.formulaCount;
}

get StringCount() {
return this.stringCount;
}

StartSheet(sheet) {
console.log("Processing sheet[" + sheet.getName() + "]");
return true;
}

StartRow(rowIndex) {
return true;
}

ProcessRow(row) {
return true;
}

StartCell(column) {
return true;
}

ProcessCell(cell) {
this.cellCount++;
if (cell.isFormula()) {
this.formulaCount++;
} else if (cell.getType() === AsposeCells.CellValueType.IsString) {
this.stringCount++;
}
return false;
}
}

async function run() {
const dataDir = path.join(__dirname, "data");
const opts = new AsposeCells.LoadOptions();
const v = new LightCellsDataHandlerVisitCells();
opts.setLightCellsDataHandler(v);
const wb = new AsposeCells.Workbook(path.join(dataDir, "LargeBook1.xlsx"), opts);
const sheetCount = wb.getWorksheets().getCount();
console.log("Total sheets: " + sheetCount + ", cells: " + v.CellCount
+ ", strings: " + v.StringCount + ", formulas: " + v.FormulaCount);
}

run();
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
