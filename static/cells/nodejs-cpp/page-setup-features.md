##Page Setup Features with Node.js via C++
Explore page setup features using Aspose.Cells for Node.js via C++. Learn how to configure page dimensions, orientations, and settings.
## **Introduction**
With Aspose.Cells for Node.js via C++, you can manipulate various page setup features of an Excel workbook. These features include setting page size, orientation, margins, and more. Proper configuration of these features allows for a better printing and viewing experience.
## **Setting Page Size and Orientation**
You can specify the page size and orientation of a worksheet by using the `PageSetup` class. It provides various properties to manage page dimensions and layout.
### **Example Code**
Here’s an example code snippet demonstrating how to set the page size and orientation.
```javascript
const { Workbook } = require("aspose.cells");
// Create a new workbook
let workbook = new Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Set the page size
worksheet.getPageSetup().setPaperSize(0); // A4 size
// Set the page orientation
worksheet.getPageSetup().setOrientation(1); // Landscape orientation
// Save the workbook
workbook.save("PageSetupExample.xlsx");
```
## **Setting Margins**
You can also set the margins for the page using the same `PageSetup` class. The margins can be adjusted for left, right, top, and bottom sides.
### **Example Code**
Here’s how you can set the margins of a worksheet.
```javascript
// Set the margins
worksheet.getPageSetup().setLeftMargin(0.5);
worksheet.getPageSetup().setRightMargin(0.5);
worksheet.getPageSetup().setTopMargin(1.0);
worksheet.getPageSetup().setBottomMargin(1.0);
// Save the workbook
workbook.save("PageMarginsExample.xlsx");
```
## **Conclusion**
In this document, you have learned how to manipulate page setup features in Excel using Aspose.Cells for Node.js via C++. By effectively using the `PageSetup` class, you can control how your worksheets are printed and displayed, enhancing the overall presentation of information.
