##Insert or Delete Rows in an Excel Worksheet with Node.js via C++
This article provides Node.js code using C++ to insert and delete rows in an Excel worksheet.
When creating a new worksheet or working with an existing worksheet, you might need to add extra rows or columns to accommodate data. At other times, you might need to delete rows or columns from specified positions in the worksheet.
Aspose.Cells for Node.js via C++ offers two methods for inserting and deleting rows: [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) and [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-). These methods are optimized for performance and do the job very quickly.
To insert or remove a number of rows, we recommend that you always use the [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) and [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) methods instead of using the [**Cells.insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) or [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRow-number-) methods in a loop.
Aspose.Cells works in the same way as Microsoft Excel does. When rows or columns are added, the worksheet content is shifted down and to the right. When rows or columns are removed, the worksheet content is shifted up or to the left. Any references in other worksheets and cells are updated when rows are added or removed.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object.
// Load a template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));
// Get the first worksheet in the book.
const sheet = workbook.getWorksheets().get(0);
// Insert 10 rows at row index 2 (insertion starts at 3rd row)
sheet.getCells().insertRows(2, 10);
// Delete 5 rows now. (8th row - 12th row)
sheet.getCells().deleteRows(7, 5);
// Save the excel file.
workbook.save(path.join(dataDir, "out_book1.out.xlsx"));
```
