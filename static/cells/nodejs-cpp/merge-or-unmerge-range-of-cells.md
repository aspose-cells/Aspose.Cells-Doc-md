##Merge or Unmerge Range of Cells with Node.js via C++
Merge and Unmerge Cells in a Range in Excel with Node.js via C++ code.
You can use Aspose.Cells to merge or split a range of cells. Aspose.Cells provides the [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) and [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--) methods for this purpose. This article explains how to merge a range of cells into a single cell.
## **Example**
The following sample code first creates a range - A1:D4 - then merges the cells in the range into a single cell using the [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) method. Similarly, you can split cells by creating a range and calling the [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--) method.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Create a range
const range = worksheet.getCells().createRange("A1:D4");
// Merge range into a single cell
range.merge();
// Save the workbook
workbook.save(path.join(dataDir, "output.out.xlsx"));
```
