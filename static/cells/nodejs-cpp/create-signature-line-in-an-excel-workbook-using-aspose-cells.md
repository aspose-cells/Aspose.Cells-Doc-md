##Create Signature Line in an Excel Workbook using Aspose.Cells for Node.js via C++
This article describes how to create a Signature Line in an Excel Workbook using Node.js code with Aspose.Cells for Node.js via C++.
## **Introduction**
Microsoft Excel provides a feature to add **Signature Line** in Excel workbooks. You can add a Signature Line by clicking the **Insert** Tab and then selecting **Signature Line** from the **Text** group.
## **How to Create Signature Line for Excel**
Aspose.Cells for Node.js via C++ also provides this feature and has exposed the [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) property for this purpose. This article will explain how to use this property to add a Signature Line using Aspose.Cells.
The following sample code adds a Signature Line using [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) property and saves the workbook.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object
const workbook = new AsposeCells.Workbook();
// Create signature line object
const signatureLine = new AsposeCells.SignatureLine();
signatureLine.setSigner("John Doe");
signatureLine.setTitle("Development Lead");
signatureLine.setEmail("john.doe@aspose.com");
// Adds a Signature Line to the worksheet.
workbook.getWorksheets().get(0).getShapes().addSignatureLine(1, 1, signatureLine);
// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
