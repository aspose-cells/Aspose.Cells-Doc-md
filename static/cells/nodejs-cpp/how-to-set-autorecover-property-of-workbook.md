##How to set AutoRecover property of Workbook with Node.js via C++
Learn how to set the AutoRecover property of a workbook using Aspose.Cells for Node.js via C++.
You can use Aspose.Cells to set the AutoRecover property of the workbook. The default value of this property is **true**. When you set it **false** on a workbook, Microsoft Excel disables AutoRecover (Autosave) on that Excel file.
Aspose.Cells provides [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) property to enable or disable this option.
The following code explains how to use [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) property of the workbook. The code first reads the default value of this property which is **true**, then it sets it as **false** and saves the workbook. Then it reads the workbook again and reads the value of this property which is **false** at this time.
## Node.js code to set the AutoRecover property of Workbook
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object
const workbook = new AsposeCells.Workbook();
// Read AutoRecover property
console.log("AutoRecover: " + workbook.getSettings().getAutoRecover());
// Set AutoRecover property to false
workbook.getSettings().setAutoRecover(false);
// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
// Read the saved workbook again
const workbook2 = new AsposeCells.Workbook(path.join(dataDir, "output_out.xlsx"));
// Read AutoRecover property
console.log("AutoRecover: " + workbook2.getSettings().getAutoRecover());
```
## **Output**
Here is the console output of the above sample code.
AutoRecover: True
AutoRecover: False
