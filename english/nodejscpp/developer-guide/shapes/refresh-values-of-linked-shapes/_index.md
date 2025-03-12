---  
title: Refresh Values of Linked Shapes with Node.js via C++  
linktitle: Refresh Values of Linked Shapes  
type: docs  
weight: 3200  
url: /nodejs-cpp/refresh-values-of-linked-shapes/  
description: Learn how to refresh the values of linked shapes in Excel using Aspose.Cells for Node.js via C++.  
---  
  
{{% alert color="primary" %}}  
  
Sometimes, you have a linked shape in your Excel file which is linked to some cell. In Microsoft Excel, changing the value of the linked cell also changes the value of the linked shape. This also works fine with Aspose.Cells for Node.js via C++ if you want to save your workbook in XLS or XLSX format. However, if you want to save your workbook in PDF or HTML format, then you will have to call [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--) method to refresh the value of the linked shape.  
  
{{% /alert %}}  
  
## Example  
  
The following screenshot shows the source Excel file used in the sample code below. It has a linked picture linked to cells A1 to E4. We will change the value of cell B4 with Aspose.Cells and then call [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--) method to refresh the value of the picture and save it in PDF format.  
  
![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)  
  
You can download the [source Excel file](95584291.xlsx) and the [output PDF](95584292.pdf) from the given links.  
  
### Node.js code to refresh the values of linked shapes  
  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleRefreshValueOfLinkedShapes.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Change the value of cell B4
const cell = worksheet.getCells().get("B4");
cell.putValue(100);

// Update the value of the Linked Picture which is linked to cell B4
worksheet.getShapes().updateSelectedValue();

// Save the workbook in PDF format
workbook.save(path.join(outputDir, "outputRefreshValueOfLinkedShapes.pdf"), AsposeCells.SaveFormat.Pdf);
```  
