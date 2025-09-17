##Disable Compatibility Checker in Excel with Node.js via C++
Learn how to disable the compatibility checker through the Aspose.Cells for Node.js via C++ API.
## Disable Compatibility Checker in Excel Worksheets in Node.js
Microsoft Excel's Compatibility Checker flags when saving a file in an earlier file format might cause functionality issues or loss of fidelity. The Compatibility Checker is a feature of Microsoft Office Excel 2007 and Microsoft Excel 2010.
When you save a workbook in a previous version, Excel 97 through Excel 2003, from Excel 2007 or Excel 2010, the Compatibility Checker scans the workbook to see if it contains features that are not supported by the earlier version. To help you make decisions about how to handle compatibility issues, the Compatibility Checker displays dialog boxes with options. It can also be used to create a report on any issues in the workbook, or disable the feature.
Sometimes, you need to disable the Compatibility Checker for a particular spreadsheet. With Aspose.Cells' APIs, you can do this programmatically so that users don't get frustrated or confused by the Compatibility Checker dialog box popping up when they re-save the file in Microsoft Excel manually.
## **How to Disable Compatibility Checker using Microsoft Excel**
To disable the Compatibility Checker in Microsoft Excel (for example Microsoft Excel 2007/2010):
- (Excel 2007) On the Office button, click **Prepare**, then **Run Compatibility Checker**, and then clear the **Check compatibility when you save this workbook** option.
- (Excel 2010) On the File tab, click **Info**, then **Check for issues**, click **Check Compatibility**, and, finally, clear the **Check compatibility when you save this workbook** option.
## **How to Disable Compatibility Checker using Aspose.Cells APIs**
Set the [**Workbook.getCheckCompatibility()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCheckCompatibility--) property to **false** to disable Microsoft Excel's Compatibility Checker.
### **Code Examples**
The code examples that follow show how to disable the Compatibility Checker with Aspose.Cells for Node.js via C++.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));
// Disable the compatibility checker
workbook.getSettings().setCheckCompatibility(false);
const outputFilePath = path.join(dataDir, "Output_BK_CompCheck.out.xlsx");
// Saving the Excel file
workbook.save(outputFilePath);
```
