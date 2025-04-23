---  
title: Node.js kullanarak Şekilden Bağlantı Noktalarını Alma ve C++  
linktitle: Şekilden Bağlantı Noktalarını Al  
type: docs  
weight: 3500  
url: /tr/nodejs-cpp/get-connection-points-from-shape/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel de şekillerden bağlantı noktalarını nasıl alacağınızı öğrenin.  
---  

Aspose.Cells, çalışma sayfasındaki şekilleri yönetmek için zengin özellikler sunar. Bazen, şeklin hizalanması veya uygun yere yerleştirilmesi için bağlantı noktalarının alınması gerekebilir. Bu amaçla, tüm bağlantı noktalarının listesi gereklidir. Aşağıdaki kod, [Shape.getConnectionPoints()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getConnectionPoints--) özelliği kullanılarak bir şeklin bağlantı noktalarını alabilir.

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

