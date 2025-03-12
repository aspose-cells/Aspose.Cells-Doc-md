---  
title: Formatting Smart Markers with Node.js via C++  
linktitle: Formatting Smart Markers  
type: docs  
weight: 20  
url: /nodejs-cpp/formatting-smart-markers/  
---  

## **Copy Style Attribute**  
Sometimes, when using smart markers, you want to copy the style of the cell that contains the smart marker tags. You can use the CopyStyle attribute of the smart marker's tags for this purpose.  

### **Copying Styles from Cells with Smart Markers**  
This example uses a simple template Microsoft Excel file with two markers in the A2 and B2 cells. The marker pasted in cell B2 uses the CopyStyle attribute, whereas the marker in cell A2 does not. Apply simple formatting (for example, set the font color to **red** and set the cell fill color to **yellow**).  

When executing the code, Aspose.Cells copies the formatting to all the records in column B but does not keep the formatting in column A.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
const { WorkbookDesigner } = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "TestSmartMarkers.xlsx");
// Create Students DataTable
const dtStudent = [];

// Add three rows to it
dtStudent.push({ Name: "John" });
dtStudent.push({ Name: "Jack" });
dtStudent.push({ Name: "James" });

// Create a workbook from Smart Markers template file
const workbook = new AsposeCells.Workbook(filePath);

// Instantiate a new WorkbookDesigner
const designer = new WorkbookDesigner();

// Specify the Workbook
designer.setWorkbook(workbook);

// Set the Data Source
designer.setDataSource(dtStudent);

// Process the smart markers
designer.process();

// Save the Excel file
workbook.save(path.join(dataDir, "output.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

  