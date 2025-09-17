##Add Pivot Connection with Node.js via C++
Learn how to add pivot connection using Aspose.Cells for Node.js via C++.
## **Possible Usage Scenarios**
If you want to associate a slicer and pivot table in Excel, you need to right-click the slicer and select "Report Connections..." item. In the option list, you can operate on the check box. Similarly, if you want to associate a slicer and pivot table using Aspose.Cells API programmatically, please use the [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#addPivotConnection-PivotTable-) method. It will associate the slicer and pivot table.
## **Associate Slicer and PivotTable**
The following sample code loads the [sample Excel file](add-pivot-connection.xlsx) that contains an existing slicer. It accesses the slicer and then associates the slicer and pivot table. Finally, it saves the workbook as [output Excel file](add-pivot-connection-out.xlsx).
## **Sample Code**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "add-pivot-connection.xlsx");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Adds PivotTable connection.
slicer.addPivotConnection(pivotTable);
workbook.save(path.join(dataDir, "add-pivot-connection-out.xlsx"));
```
