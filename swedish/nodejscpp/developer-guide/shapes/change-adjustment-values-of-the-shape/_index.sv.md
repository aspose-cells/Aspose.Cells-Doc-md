---  
title: Ändra justeringsvärden på formen med Node.js via C++  
linktitle: Ändra justeringsvärden för formen  
type: docs  
weight: 2000  
url: /sv/nodejs-cpp/change-adjustment-values-of-the-shape/  
description: Lär dig hur du ändrar justeringsvärden för former i Excel med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells tillhandahåller egenskapen [**Shape.getGeometry()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGeometry--) för att göra ändringar av justeringspunkter med former. I Microsoft Excel-gränssnittet visas justeringar som gula diamantnoder. Till exempel:  

- Avrundad rektangel har en justering för att ändra buen  
- Triangel har en justering för att ändra platsen för punkten  
- Trapets har en justering för att ändra bredden på toppen  
- Pilar har två justeringar för att ändra formen på huvudet och svansen  

Den här artikeln förklarar användningen av [**Shape.getGeometry()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGeometry--) egenskapen för att ändra justeringsvärdet för olika former.  
{{% /alert %}}  

## **Ändra justeringsvärden**  

Nedan visas ett kodexempel på hur man ändrar justeringsvärden för formen.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source_shapes.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first three shapes of the worksheet
const shape1 = worksheet.getShapes().get(0);
const shape2 = worksheet.getShapes().get(1);
const shape3 = worksheet.getShapes().get(2);

// Change the adjustment values of the shapes
shape1.getGeometry().getShapeAdjustValues().get(0).setValue(0.5);
shape2.getGeometry().getShapeAdjustValues().get(0).setValue(0.8);
shape3.getGeometry().getShapeAdjustValues().get(0).setValue(0.5);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Hur man ställer in eller ändrar RoundedRectangularCallout-tippunkt i Excel**  

Följande kodexempel visar hur man ställer in eller ändrar positionen för ett rundat rektangulärt callout-tippunkt i Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = dataDir + "/"; // Ensure you define filePath

// Create a new workbook
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Add a RoundedRectangularCallout to the worksheet
let polygonShape = sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.RoundedRectangularCallout, 0, 0, 0, 0, 0, 0);

polygonShape.setTop(200); // Shape Top properties
polygonShape.setLeft(500); // Shape Left properties
polygonShape.setWidth(200); // Shape Width
polygonShape.setHeight(100); // Shape Height

let shapeGuides = polygonShape.getGeometry().getShapeAdjustValues();
shapeGuides.add("adj1", 1.02167); // The distance between the tip point and the center point
shapeGuides.add("adj2", -0.295);  // The distance between the tip point and the center point
shapeGuides.add("adj3", 0.16667); // Usually the default value

// Save the workbook
workbook.save(path.join(filePath, "res.xlsx"), AsposeCells.SaveFormat.Xlsx);

// Read a new workbook
workbook = new AsposeCells.Workbook(path.join(filePath, "res.xlsx"));
sheet = workbook.getWorksheets().get(0);

// Get a RoundedRectangularCallout from the worksheet
polygonShape = sheet.getShapes().get(0);
shapeGuides = polygonShape.getGeometry().getShapeAdjustValues();
shapeGuides.get(0).setValue(0.7);

// Save the workbook
workbook.save(path.join(filePath, "res-resave.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
