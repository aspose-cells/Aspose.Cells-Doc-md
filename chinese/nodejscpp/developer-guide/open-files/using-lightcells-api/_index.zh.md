---  
title: 在 Node.js 中使用 C++ 的 LightCells API  
linktitle: 使用 LightCells API  
type: docs  
weight: 160  
url: /zh/nodejs-cpp/using-lightcells-api/  
description: 学习如何在 Node.js 中使用 LightCells API 读写大型 Excel 文件，以提升性能和效率，并减少内存消耗。  
---  

{{% alert color="primary" %}}  

有时您需要读写大量数据或工作表中的大量内容的大型Microsoft Excel文件。LightCells API 用于创建巨大的Excel电子表格非常有用：使用它，您需要更少的内存，并获得更好的性能和效率。  

{{% /alert %}}  
# 事件驱动架构  
Aspose.Cells 提供 LightCells API，主要设计用于逐个处理单元格数据，而无需将完整的数据模型块（使用 Cell 集合等）构建到内存中。它以事件驱动模式工作。  

在保存工作簿时，保存组件会直接提供逐个单元格的单元格内容，然后将其保存到输出文件。  

在读取模板文件时，组件会解析每个单元格，并逐个提供它们的值。  

在两个过程中，处理和丢弃一个单元格对象；工作簿对象不持有集合。在此模式下，导入和导出拥有大量数据集的 Microsoft Excel 文件时，可以节省内存。  

即使 LightCells API 在 XLSX 和 XLS 文件上以相同的方式处理单元格（它实际上并不将所有单元格加载到内存中，而是处理一个单元格然后丢弃它），但它对于 XLSX 文件比 XLS 文件更有效地节省内存，因为这两种格式的数据模型和结构不同。  

然而，**对于 XLS 文件**，为了节省更多内存，开发者可以指定保存临时数据的临时位置。通常，**使用 LightCells API 保存 XLSX 文件可能比常规方式节省 50% 或以上的内存；保存 XLS 文件则大约节省 20-40% 内存。**  

## 写一个大型的Excel文件  
Aspose.Cells 提供接口 `LightCellsDataProvider`，需要在程序中实现该接口。该接口代表用于以轻量级模式保存大型电子表格文件的数据提供者。  

采用此模式保存工作簿时，每次保存工作表都调用 `StartSheet(int)` 进行检查。对于某个工作表，如果 `StartSheet(int)` 返回真，则此工作表的所有数据和属性（行和单元格）由此实现提供。首先调用 `NextRow()` 获取下一个要保存的行索引。如果返回有效行索引（行索引必须递增），则提供一个代表该行的 `Row` 对象，供 `StartRow(Row)` 设置其属性。  

对于一行，先调用 `NextCell()` 检查。如果返回有效列索引（列索引必须递增），则提供一个代表该单元格的 `Cell` 对象，供 `StartCell(Cell)` 设置其数据和属性。单元格数据设置完毕后，直接保存到生成的电子表格文件中，然后继续检查和处理下一个单元格。  
### 写入大型Excel文件示例  
请查看以下示例代码，了解LightCells API的工作方式。根据您的需求添加和删除或更新代码段。  

程序在工作表中创建一个包含10,000（10000x30矩阵）记录的大文件，并用虚拟数据填充。您可以通过修改 `Main()` 方法中的 `rowsCount` 和 `colsCount` 变量来指定不同的矩阵大小。  

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

## 读取大型Excel文件  
Aspose.Cells 提供了接口 `LightCellsDataHandler`，需要在您的程序中实现。该接口代表在轻量级模式下读取大型电子表格文件的数据提供者。  

在这种模式下读取工作簿时，`StartSheet` 在读取每个工作表时进行检查。对于某个工作表，如果 `StartSheet` 返回 true，则该工作表中所有行列的单元格数据和属性将由此接口的实现进行检查和处理。对于每一行，会调用 `StartRow` 来检查是否需要处理该行。如果需要处理该行，则首先读取其属性，开发者可以通过 `ProcessRow` 访问其属性。如果该行的单元格也需要处理，则 `ProcessRow` 应返回 true，然后对该行中的每个存在的单元格调用 `StartCell` 以检查是否需要处理该单元格。如果需要处理某个单元格，则调用 `ProcessCell` 由该接口的实现处理该单元格。  
### 读取大型Excel文件示例  
请查看以下示例代码，了解LightCells API的工作方式。根据您的需求添加和删除或更新代码段。  

程序读取具有数百万记录的工作表非常耗时。每个工作表的读取时间很短。示例代码读取文件，并检索每个工作表中的总单元格数、字符串数和公式数。  

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

