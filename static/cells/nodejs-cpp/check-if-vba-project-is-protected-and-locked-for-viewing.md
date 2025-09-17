##Check if VBA Project is Protected and Locked for Viewing with Node.js via C++
Learn how to check if a VBA project in an Excel file is protected and locked for viewing using Aspose.Cells for Node.js via C++.
## Check if VBA Project is Protected and Locked for Viewing in Node.js
Aspose.Cells allows you to check if the VBA (Visual Basic for Applications) Project of an Excel file is protected and locked for viewing. For this, the API provides the [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--) property. If it is locked for viewing, then the [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--) property returns **true**.
## **Sample Code**
The following sample code loads the [sample Excel file](43352065.xlsm) and checks if the VBA (Visual Basic for Applications) Project of the Excel file is protected and locked for viewing. Please also see its Console Output for reference.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source Excel file.
const filePath = path.join(dataDir, "sampleCheckifVBAProjectisProtected.xlsm");
const workbook = new AsposeCells.Workbook(filePath);
// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();
// Whether "Lock project for viewing" is true or not.
console.log("Is VBA Project Locked for Viewing: " + vbaProject.getIslockedForViewing());
```
## **Console Output**
This is the console output of the above sample code when executed with the provided [sample Excel file](43352065.xlsm).
Is VBA Project Locked for Viewing: True
