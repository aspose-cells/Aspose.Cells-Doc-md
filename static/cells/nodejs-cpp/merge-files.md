##Merge Files with Node.js via C++
## **Introduction**
Aspose.Cells provides different ways for merging files. For simple files with data, formatting, and formulas, the [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) method can be used to combine several workbooks, and the [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-) method can be used to copy worksheets into a new workbook. These methods are easy to use and effective, but if you have a lot of files to merge, you might find that they take a lot of system resources. To avoid this, use the [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) static method, a more efficient way to merge several files.
## **Merge Files Using Aspose.Cells for Node.js via C++**
The following sample code illustrates how to merge large files using the [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) method. It takes two simple but large files, Book1.xls and Book2.xls. The files contain formatted data and formulas only.
The [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) method only supports merging data, styles, formatting, and formulas. Objects like charts, pictures, comments or other objects might not be merged using this method. Moreover, a cached file is used to store temporary data for the process.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create an Array (length=2)
const files = new Array(2);
// Specify files with their paths to be merged
files[0] = path.join(dataDir, "book1.xls");
files[1] = path.join(dataDir, "Book2.xlsx");
// Create a cachedFile for the process
const cacheFile = path.join(dataDir, "test.txt");
// Output File to be created
const dest = path.join(dataDir, "output.xlsx");
// Merge the files in the output file. Supports only .xls files
AsposeCells.CellsHelper.mergeFiles(files, cacheFile, dest);
console.log(cacheFile);
// Now if you need to rename your sheets, you may load the output file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "output.xlsx"));
let i = 1;
// Browse all the sheets to rename them accordingly
const worksheets = workbook.getWorksheets();
for (let j = 0; j < worksheets.getCount(); j++) {
worksheets.get(j).setName(`Sheet1${i}`);
i++;
}
// Re-save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```
