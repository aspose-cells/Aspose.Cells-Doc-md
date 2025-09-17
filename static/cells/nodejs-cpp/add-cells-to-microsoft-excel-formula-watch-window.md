##Add Cells to Microsoft Excel Formula Watch Window with Node.js via C++
How to use Aspose.Cells library to add cells to the formula watch window in Excel using Node.js via C++. By loading an existing Excel file or creating a new one, we can manipulate the cells in it and set formulas. Finally, we save the modified Excel file to disk.
## **Possible Usage Scenarios**
Microsoft Excel Watch Window is a useful tool to watch the cell values and its formulas conveniently in a window. You can open the *Watch Window* using Microsoft Excel by clicking the *Formulas > Watch* *Window*. It has the *Add Watch* button that can be used to add the cells for inspection. Similarly, you can use [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cellwatchcollection/#add-number-number-) method to add cells into *Watch Window* using the Aspose.Cells API.
## **Add Cells to Microsoft Excel Formula Watch Window**
The following sample code sets the formula of cells C1 and E1 and adds both of them to the Watch Window. It then saves the workbook as [output Excel file](67338481.xlsx). If you open the output Excel file and view the *Watch Window*, you will see both cells as shown in this screenshot.
![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)
## **Sample Code**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();
// Access first worksheet.
const ws = wb.getWorksheets().get(0);
// Put some integer values in cell A1 and A2.
ws.getCells().get("A1").putValue(10);
ws.getCells().get("A2").putValue(30);
// Access cell C1 and set its formula.
const c1 = ws.getCells().get("C1");
c1.setFormula("=Sum(A1,A2)");
// Add cell C1 into cell watches by name.
ws.getCellWatches().add(c1.getName());
// Access cell E1 and set its formula.
const e1 = ws.getCells().get("E1");
e1.setFormula("=A2*A1");
// Add cell E1 into cell watches by its row and column indices.
ws.getCellWatches().add(e1.getRow(), e1.getColumn());
// Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", AsposeCells.SaveFormat.Xlsx);
```
