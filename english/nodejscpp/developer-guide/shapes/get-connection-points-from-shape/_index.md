---  
title: Get Connection Points from Shape with Node.js via C++  
linktitle: Get Connection Points from Shape  
type: docs  
weight: 3500  
url: /nodejs-cpp/get-connection-points-from-shape/  
description: Learn how to retrieve connection points from shapes in Excel using Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells provides rich features to manage shapes in the spreadsheet. Sometimes there is a need to get the connection points of a shape for aligning or placing the shapes at the appropriate place. For this purpose, all the connection points are required. The following code can be used to get the list of connection points of a shape by using the [Shape.getConnectionPoints()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getConnectionPoints--) property.

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Instantiate a new Workbook.
const newWorkbook = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const worksheet = newWorkbook.getWorksheets().get(0);

// Add a new textbox to the collection.
const textboxIndex = worksheet.getTextBoxes().add(2, 1, 160, 200);

// Access your text box which is also a shape object from shapes collection
const shape = newWorkbook.getWorksheets().get(0).getShapes().get(0);

// Get all the connection points in this shape
const connectionPoints = shape.getConnectionPoints();

// Display all the shape points
connectionPoints.forEach(pt => {
console.log(`X = ${pt[0]}, Y = ${pt[1]}`);
```  
  