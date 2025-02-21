---  
title: Measure the Width and Height of the Cell Value in Unit of Pixels with Node.js via C++  
linktitle: Measure the Size  
type: docs  
weight: 260  
url: /nodejs-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/  
description: Learn how to Measure the Width and Height of the Cell Value in Unit of Pixels through the Aspose.Cells for Node.js via C++.  
keywords: Measure the Width of the Cell Value in Unit of Pixels Node.js via C++, Measure the Height of the Cell Value in Unit of Pixels Node.js via C++, Get the Width of the Cell Value in Unit of Pixels Node.js via C++, Get the Height of the Cell Value in Unit of Pixels Node.js via C++  
---  

{{% alert color="primary" %}}  

Sometimes you need to calculate the width and height of cell value to fit the cell value inside the cell. Aspose.Cells provides [**Cell.getWidthOfValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getWidthOfValue) and [**Cell.getHeightOfValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHeightOfValue) methods for this purpose. By using these methods you can calculate width and height of the cell value and then set the width of the column and height of the row of that cell respectively and this will then adjust or fit the cell value inside the cell.  

Alternatively, you can also [autofit rows and columns of your cell or range of cells](/cells/nodejs-cpp/autofit-rows-and-columns/) using Aspose.Cells APIs.  

{{% /alert %}}  

The following code explains the use of [**Cell.getWidthOfValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getWidthOfValue) and [**Cell.getHeightOfValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHeightOfValue) methods.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
let workbook = new AsposeCells.Workbook();

// Access first worksheet
let worksheet = workbook.getWorksheets().get(0);

// Access cell B2 and add some value inside it
let cell = worksheet.getCells().get("B2");
cell.putValue("Welcome to Aspose!");

// Enlarge its font to size 16
let style = cell.getStyle();
style.getFont().setSize(16);
cell.setStyle(style);

// Calculate the width and height of the cell value in unit of pixels
let widthOfValue = cell.getWidthOfValue();
let heightOfValue = cell.getHeightOfValue();

// Print both values
console.log("Width of Cell Value: " + widthOfValue);
console.log("Height of Cell Value: " + heightOfValue);

// Set the row height and column width to adjust/fit the cell value inside cell
worksheet.getCells().setColumnWidthPixel(1, widthOfValue);
worksheet.getCells().setRowHeightPixel(1, heightOfValue);

// Save the output excel file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Advance topics**  
- [Get Text Width of Cell Value](/cells/nodejs-cpp/get-text-width-of-cell-value/)  
  