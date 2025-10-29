---  
title: Obtenir les points de connexion d une forme avec Node.js via C++  
linktitle: Obtenir les points de connexion d une forme  
type: docs  
weight: 3500  
url: /fr/nodejs-cpp/get-connection-points-from-shape/  
description: Apprenez comment récupérer les points de connexion des formes dans Excel en utilisant Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells offre de riches fonctionnalités pour gérer les formes dans la feuille de calcul. Parfois, il est nécessaire d'obtenir les points de connexion d'une forme pour l'aligner ou la placer au bon endroit. À cette fin, tous les points de connexion sont requis. Le code suivant peut être utilisé pour obtenir la liste des points de connexion d'une forme en utilisant la propriété [Shape.getConnectionPoints()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getConnectionPoints--).

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
