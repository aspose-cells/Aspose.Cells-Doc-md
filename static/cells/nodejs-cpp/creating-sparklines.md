##Insert Sparkline with Node.js via C++
Create sparkline for Excel using Aspose.Cells for Node.js via C++.
## **Insert a sparkline**
Sparkline is a tiny chart in a worksheet cell that provides a visual representation of data. Use sparklines to show trends in a series of values, such as seasonal increases or decreases, economic cycles, or to highlight maximum and minimum values. Position a sparkline near its data for greatest impact. There are three types of Sparkline: Line, Column and Stacked.
It’s simple to create a sparkline with Aspose.Cells for Node.js via C++ with the following example codes:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);
const sheet = book.getWorksheets().get(0);
sheet.getCells().get("A1").putValue(5);
sheet.getCells().get("B1").putValue(2);
sheet.getCells().get("C1").putValue(1);
sheet.getCells().get("D1").putValue(3);
// Define the CellArea
const ca = AsposeCells.CellArea.createCellArea(0, 4, 0, 4);
const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, `${sheet.getName()}!A1:D1`, false, ca);
const group = sheet.getSparklineGroups().get(idx);
group.getSparklines().add(`${sheet.getName()}!A1:D1`, 0, 4);
// Customize Sparklines
// Create CellsColor
const clr = book.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);
// Set the high points are colored green and the low points are colored red
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.getHighPointColor().setColor(AsposeCells.Color.Green);
group.getLowPointColor().setColor(AsposeCells.Color.Red);
// Set line weight
group.setLineWeight(1.0);
// Saving the Excel file
book.save(path.join(dataDir, "output.xlsx"));
```
## **Advance topics**
- [Using Sparklines and Settings 3D Format](https://docs.aspose.com/cells/nodejs-cpp/using-sparklines-and-settings-3d-format/)
