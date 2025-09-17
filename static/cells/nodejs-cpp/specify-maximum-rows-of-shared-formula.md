##Specify Maximum Rows of Shared Formula with Node.js via C++
Learn how to specify the maximum rows for shared formulas using Aspose.Cells for Node.js via C++.
## **Possible Usage Scenarios**
The default maximum rows of the shared formula are 64. It could be any number e.g. it could be 1000. The performance of shared formula changes with a different number of rows. Therefore, Aspose.Cells provides the [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--) property that can be used to specify the maximum rows of the shared formula. The shared formula will be split into several shared formulae if the total rows of the shared formula are greater than it as shown in the following screenshot.
![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)
## **Specify Maximum Rows of Shared Formula**
The following sample code explains the usage of the [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--) property. It sets the maximum rows of the shared formula to 5 and adds the shared formula in cell D1 for 100 rows and saves to [output Excel file](61767856.xlsx). If you extract the contents of the output Excel file and check the *sheet1.xml*, you will see the shared formula splits after every 5 rows as highlighted in the above screenshot.
## **Sample Code**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create a new workbook
const wb = new AsposeCells.Workbook();
// Set the max rows of shared formula to 5
wb.getSettings().setMaxRowsOfSharedFormula(5);
// Access first worksheet
const ws = wb.getWorksheets().get(0);
// Access cell D1
const cell = ws.getCells().get("D1");
// Set the shared formula in 100 rows
cell.setSharedFormula("=Sum(A1:A2)", 100, 1);
// Save the output Excel file
wb.save("outputSpecifyMaximumRowsOfSharedFormula.xlsx");
```
