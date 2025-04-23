---  
title: Ottieni punti di connessione da forma con Node.js tramite C++  
linktitle: Ottenere i punti di connessione da una Forma  
type: docs  
weight: 3500  
url: /it/nodejs-cpp/get-connection-points-from-shape/  
description: Scopri come recuperare i punti di connessione dalle forme in Excel usando Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells offre funzioni ricche per gestire le forme nel foglio di calcolo. A volte, è necessario ottenere i punti di connessione di una forma per allineare o posizionare le forme correttamente. A questo scopo, sono necessari tutti i punti di connessione. Il codice seguente può essere usato per ottenere l'elenco dei punti di connessione di una forma usando la proprietà [Shape.getConnectionPoints()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getConnectionPoints--).

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

