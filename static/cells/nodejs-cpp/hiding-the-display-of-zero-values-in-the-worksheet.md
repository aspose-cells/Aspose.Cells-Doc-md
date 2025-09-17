##Hiding the Display of Zero Values in the Worksheet with Node.js via C++
This article will show you sample code explaining how to programmatically hide the zero values in an Excel spreadsheet using the Node.js library via C++.
Sometimes, you need to hide zero values in a spreadsheet. It might be a personal preference or a formatting standard.
To hide zero values in a worksheet in Microsoft Excel (for example Microsoft Excel 2003):
1. From the **Tools** menu, select **Options**, and then select the **View** tab.
1. Deselect the **Zero values** option.
1. Click **OK**.
Please see the following sample code that demonstrates hiding zeros using Aspose.Cells for Node.js via C++.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Create a new Workbook object
const workbook = new AsposeCells.Workbook(filePath);
// Get First worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);
// Hide the zero values in the sheet
sheet.setDisplayZeros(false);
// Save the workbook
workbook.save(path.join(dataDir, "outputfile.out.xlsx"));
```
