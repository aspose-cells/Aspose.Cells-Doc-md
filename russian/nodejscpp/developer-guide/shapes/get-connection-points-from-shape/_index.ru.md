---  
title: Получить точки соединения фигуры с помощью Node.js через C++  
linktitle: Получить точки подключения фигуры  
type: docs  
weight: 3500  
url: /ru/nodejs-cpp/get-connection-points-from-shape/  
description: Узнайте, как получать точки соединения фигуры в Excel с помощью Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells предоставляет богатые возможности для управления фигурами в таблице. Иногда необходимо получить точки соединения фигуры для выравнивания или размещения фигур в нужном месте. Для этого нужны все точки соединения. Следующий код можно использовать для получения списка точек соединения фигуры с помощью свойства [Shape.getConnectionPoints()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getConnectionPoints--).

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

{{< app/cells/assistant language="nodejs-cpp" >}}
