##Read and Write Table with Query Table Data Source via Node.js
Learn how to read and write a table with a QueryTable data source using Aspose.Cells for Node.js via C++.
## **Read and Write Table with Query Table Data Source**
With Aspose.Cells for Node.js via C++, you can read and write a table which has a QueryTable as a data source. The support for this feature also exists for XLS files. The following code snippet demonstrates reading and writing such a table by first reading the table and then modifying it to add the totals row.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the source directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
// Load workbook object
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTableWithQueryTable.xls"));
const worksheet = workbook.getWorksheets().get(0);
const table = worksheet.getListObjects().get(0);
// Check the data source type if it is query table
if (table.getDataSourceType() === AsposeCells.TableDataSourceType.QueryTable) {
table.setShowTotals(true);
}
// Save the file
workbook.save(path.join(outputDir, "SampleTableWithQueryTable_out.xls"));
```
The source and output excel files are attached for reference.
[Source File](96928091.xls)
[Output File](96928092.xls)
