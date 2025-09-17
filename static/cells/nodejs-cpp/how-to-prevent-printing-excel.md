##How to Prevent Users from Printing Excel File with Node.js via C++
Learn how to prevent users from printing Excel files using Aspose.Cells for Node.js via C++.
## **Possible Usage Scenarios**
In our daily work, there may be some important information in the Excel file; in order to protect the internal data from spreading, the company will not allow us to print them. This document will tell you how to prevent others from printing Excel files.
## **How to Prevent Users from Printing File in MS-Excel**
You can apply the following VBA code to protect your specific file from being printed.
1. Open your workbook which you don’t allow others to print.
1. Select the "Developer" tab in the Excel ribbon and click on the "View Code" button in the "Controls" section. Alternatively, you can hold down the ALT + F11 keys to open the Microsoft Visual Basic for Applications window.
1. And then in the left Project Explorer, double click ThisWorkbook to open the module, and add some VBA codes.
1. Then save and close this code, go back to the workbook, and now when you print the sample file, it will not be allowed to be printed, and you will get the following warning box:
## **How to Prevent Users from Printing Excel File using Aspose.Cells for Node.js via C++**
The following sample code illustrates how to prevent users from printing an Excel file:
1. Load the [sample file](sample.xlsx).
1. Get the VbaModuleCollection object from the VbaProject property of Workbook.
1. Get the VbaModule object via the "ThisWorkbook" name.
1. Set the codes property of VbaModule.
1. Save the sample file to [xlsm format](out.xlsm).
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);
const modules = wb.getVbaProject().getModules();
modules.get("ThisWorkbook").setCodes("Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n");
wb.save("out.xlsm");
```
