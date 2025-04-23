---  
title: 通过 C++ 使用 Node.js 获取形状的连接点  
linktitle: 获取连接点  
type: docs  
weight: 3500  
url: /zh/nodejs-cpp/get-connection-points-from-shape/  
description: 学习如何使用Aspose.Cells for Node.js via C++在Excel中检索形状的连接点。  
---  

Aspose.Cells 提供丰富的功能来管理电子表格中的形状。有时需要获取形状的连接点，以便对齐或将形状放置在合适的位置。为此，需要所有连接点。可以使用以下代码，通过 [Shape.getConnectionPoints()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getConnectionPoints--) 属性获取形状的连接点列表。

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

