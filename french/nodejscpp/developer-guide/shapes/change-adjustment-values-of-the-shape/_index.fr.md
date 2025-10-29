---  
title: Modifier les valeurs d ajustement de la forme avec Node.js via C++  
linktitle: Modifier les valeurs d ajustement de la forme.  
type: docs  
weight: 2000  
url: /fr/nodejs-cpp/change-adjustment-values-of-the-shape/  
description: Apprenez comment changer les valeurs d ajustement des formes dans Excel en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells fournit la propriété [**Shape.getGeometry()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGeometry--) pour apporter des modifications aux points d'ajustement avec les formes. Dans l'interface utilisateur Microsoft Excel, les ajustements s'affichent sous forme de nœuds de diamant jaune. Par exemple :  

- Le rectangle arrondi possède un ajustement pour changer l'arc.  
- Le triangle a un ajustement pour changer l'emplacement du point.  
- Le trapèze a un ajustement pour changer la largeur du haut  
- Les flèches ont deux ajustements pour changer la forme de la tête et de la queue.  

Cet article expliquera l'utilisation de la propriété [**Shape.getGeometry()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGeometry--) pour changer la valeur d'ajustement des formes différentes.  
{{% /alert %}}  

## **Changer les valeurs d'ajustement**  

L'exemple de code ci-dessous montre comment changer les valeurs d'ajustement de la forme.  

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

## **Comment définir ou changer le point de pointe du callout rectangulaire arrondi dans Excel**  

Le code exemple ci-dessous montre comment définir ou changer la position du point de pointe d'un callout rectangulaire arrondi dans Excel.  

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
