##Remove Pivot Connection with Node.js via C++
Learn how to remove pivot connection using Aspose.Cells for Node.js via C++.
## **Possible Usage Scenarios**
If you want to disassociate a slicer and pivot table in Excel, you need to right-click the slicer and select "Report Connections..." item. In the option list, you can operate on the checkbox. Similarly, if you want to disassociate a slicer and pivot table using the Aspose.Cells API programmatically, please use the [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#removePivotConnection-pivottable-) method. It will disassociate the slicer and pivot table.
## **Disassociate slicer and pivot table**
The following sample code loads the [sample Excel file](remove-pivot-connection.xlsx) that contains an existing slicer. It accesses the slicers and then disassociates the slicer and pivot table. Finally, it saves the workbook as [output Excel file](remove-pivot-connection-out.xlsx).
## **Sample Code**
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "remove-pivot-connection.xlsx");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Remove PivotTable connection.
slicer.removePivotConnection(pivotTable);
// Save the workbook in output XLSX format.
workbook.save(path.join(dataDir, "remove-pivot-connection-out.xlsx"));
```
