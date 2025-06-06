---  
title: Obtener puntos de conexión de forma con Node.js vía C++  
linktitle: Obtener puntos de conexión de forma  
type: docs  
weight: 3500  
url: /es/nodejs-cpp/get-connection-points-from-shape/  
description: Aprenda cómo recuperar los puntos de conexión de formas en Excel usando Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells proporciona funciones ricas para gestionar formas en la hoja de cálculo. A veces se necesita obtener los puntos de conexión de una forma para alinearlas o colocarlas en el lugar adecuado. Para ello, se requieren todos los puntos de conexión. El siguiente código puede usarse para obtener la lista de puntos de conexión de una forma usando la propiedad [Shape.getConnectionPoints()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getConnectionPoints--).

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

