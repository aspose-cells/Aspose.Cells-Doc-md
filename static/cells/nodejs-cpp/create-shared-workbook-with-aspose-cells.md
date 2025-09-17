##Create Shared Workbook with Aspose.Cells for Node.js via C++
Learn how to create a shared workbook using Aspose.Cells for Node.js via C++.
## **Possible Usage Scenarios**
Microsoft Excel allows you to share the workbook as shown in the following screenshot. When you share the workbook, more than one user can edit the workbook on the network. Aspose.Cells for Node.js via C++ enables you to create a shared workbook with the [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--) property.
![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)
## **Create Shared Workbook with Aspose.Cells**
The following sample code creates a shared workbook by setting the [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--) property as **true**. When you open the [output Excel file](55541786.xlsx) in Microsoft Excel, you will see **Shared** with the output workbook name as shown in this screenshot.
![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)
## **Sample Code**
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create Workbook object
const wb = new AsposeCells.Workbook();
// Share the Workbook
wb.getSettings().setShared(true);
// Save the Shared Workbook
wb.save("outputSharedWorkbook.xlsx");
```
