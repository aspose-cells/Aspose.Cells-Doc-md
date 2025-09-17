##Search and Replace Data in a Range with Node.js via C++
This article shows how to search and replace data in a range in Excel using Node.js via C++ code.
Sometimes you need to search for and replace specific data in a range ignoring any cell values outside the desired range. Aspose.Cells for Node.js via C++ allows you to limit a search to a specific range. This article explains how.
Aspose.Cells for Node.js via C++ provides the [**FindOptions.setRange(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setRange-cellarea-) method for specifying a range when searching for data. Below code sample searches and replaces data in a range.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const area = AsposeCells.CellArea.createCellArea("E9", "H15");
const opts = new AsposeCells.FindOptions();
opts.setLookInType(AsposeCells.LookInType.Values);
opts.setLookAtType(AsposeCells.LookAtType.EntireContent);
opts.setRange(area);
let cell = null;
do {
cell = worksheet.getCells().find("search", cell, opts);
if (cell === null || cell.isNull()) {
break;
}
cell.putValue("replace");
} while (true);
workbook.save(path.join(dataDir, "output.out.xlsx"));
```
