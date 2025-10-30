---  
title: Verbindungspunkte von Formen mit Node.js via C++ erhalten  
linktitle: Verbindungspunkte der Form abrufen  
type: docs  
weight: 3500  
url: /de/nodejs-cpp/get-connection-points-from-shape/  
description: Lernen Sie, wie Sie Verbindungspunkte aus Formen in Excel mit Aspose.Cells for Node.js via C++ abrufen.  
---  

Aspose.Cells bietet umfangreiche Funktionen zur Verwaltung von Formen in Tabellenkalkulationen. Manchmal ist es notwendig, die Verbindungspunkte einer Form zum Ausrichten oder Platzieren der Formen an der geeigneten Stelle zu erhalten. Dafür sind alle Verbindungspunkte erforderlich. Der folgende Code kann verwendet werden, um die Liste der Verbindungspunkte einer Form mit der Eigenschaft [Shape.getConnectionPoints()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getConnectionPoints--) zu erhalten.

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
