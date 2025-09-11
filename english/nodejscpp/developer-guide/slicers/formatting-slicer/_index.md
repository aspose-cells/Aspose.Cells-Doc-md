---  
title: Formatting Slicer with Node.js via C++  
linktitle: Formatting Slicer  
type: docs  
weight: 20  
url: /nodejs-cpp/formatting-slicer/  
---  
  
## **Possible Usage Scenarios**  
  
You can format the slicer in Microsoft Excel by setting its number of columns or by setting its style etc. Aspose.Cells for Node.js via C++ also allows you to do this using the [**Slicer.getNumberOfColumns()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getNumberOfColumns--) and [**Slicer.getStyleType()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getStyleType--) properties.  
  
## **Formatting Slicer**  
  
Please see the following code, it loads the [sample Excel file](67338473.xlsx) that contains a slicer. It accesses the slicer and sets its number of columns and style type and saves it as [output Excel file](67338474.xlsx). The screenshot shows how the slicer looks after the execution of the sample code.  
  
![todo:image_alt_text](formatting-slicer_1.png)  
  
## **Sample Code**  
  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFormattingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Set the number of columns of the slicer.
slicer.setNumberOfColumns(2);

// Set the type of slicer style.
slicer.setStyleType(AsposeCells.SlicerStyleType.SlicerStyleLight6);

// Save the workbook in output XLSX format.
wb.save("outputFormattingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}