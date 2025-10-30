---  
title: Ändern der Anpassungswerte der Form mit Node.js via C++  
linktitle: Anpassung von Formwerten ändern  
type: docs  
weight: 2000  
url: /de/nodejs-cpp/change-adjustment-values-of-the-shape/  
description: Erfahren Sie, wie Sie die Anpassungswerte von Formen in Excel mit Aspose.Cells for Node.js via C++ ändern.  
---  

{{% alert color="primary" %}}  
Aspose.Cells stellt die Eigenschaft [**Shape.getGeometry()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGeometry--) bereit, um Änderungen an den Anpassungspunkten mit Formen vorzunehmen. In der Microsoft Excel-Benutzeroberfläche werden Anpassungen als gelbe Diamantknoten angezeigt. Zum Beispiel:  

- Das abgerundete Rechteck hat eine Anpassung, um den Bogen zu ändern  
- Das Dreieck hat eine Anpassung, um die Position des Punktes zu ändern  
- Das Trapezoid hat eine Anpassung, um die Breite des oberen Teils zu ändern  
- Pfeile haben zwei Anpassungen, um die Form des Kopfes und des Endes zu ändern  

In diesem Artikel wird die Verwendung der Eigenschaft [**Shape.getGeometry()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGeometry--) erklärt, um den Anpassungswert der verschiedenen Formen zu ändern.  
{{% /alert %}}  

## **Änderung der Anpassungswerte**  

Im folgenden Codebeispiel wird gezeigt, wie Anpassungswerte der Form geändert werden.  

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

## **So setzen oder ändern Sie den Tip-Punkt eines RoundedRectangularCallout in Excel**  

Das folgende Code-Beispiel zeigt, wie man einen abgerundeten Rechteck-Ausrufpunkt in Excel festlegt oder ändert.  

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
