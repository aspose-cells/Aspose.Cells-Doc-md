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

## **Adding Custom Labels**  
### **Introduction**  
While working with Smart Markers' grouping data feature, sometimes you need to add your own custom labels to the summary row. You also want to concatenate the Column's name with that Label, e.g "Sub Total of Orders". Aspose.Cells provides you Label and LabelPosition attributes, so you may place your custom labels in the Smart Markers while concatenating with the Subtotal rows in grouping data.  

### **Adding custom Labels to concatenate with the Subtotal rows in Smart Markers**  
This example uses a [data file](96927971.xlsx) and a [template file](96927972.xlsx) with a few markers in the cells. When executing the code, Aspose.Cells adds some custom labels to the summary rows for the grouped data.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
const designer = new AsposeCells.Workbook(path.join(dataDir, "SmartMarker_Designer.xlsx"));

// Export data from the first worksheet to fill a data table
const dt = workbook.getWorksheets().get(0).getCells().exportDataTable(0, 0, 11, 5, true);

// Set the table name
dt.setTableName("Report");

// Instantiate a new WorkbookDesigner
const d = new AsposeCells.WorkbookDesigner();

// Specify the workbook to the designer book
d.setWorkbook(designer);

// Set the data source
d.setDataSource(dt);

// Process the smart markers
d.process();

// Save the Excel file
designer.save(path.join(dataDir, "output.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  
  