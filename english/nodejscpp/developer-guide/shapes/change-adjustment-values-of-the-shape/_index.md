---  
title: Change Adjustment Values of the Shape with Node.js via C++  
linktitle: Change Adjustment Values of the Shape  
type: docs  
weight: 2000  
url: /nodejs-cpp/change-adjustment-values-of-the-shape/  
description: Learn how to change adjustment values of shapes in Excel using Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells provides [**Shape.geometry.shapeAdjustValues**](https://reference.aspose.com/cells/nodejs-cpp/shape/geometry/#shapeAdjustValues) property to make changes to the adjustment points with shapes. In the Microsoft Excel UI, adjustments display as yellow diamond nodes. For example:  

- Rounded Rectangle has an adjustment to change the arc  
- Triangle has an adjustment to change the location of the point  
- Trapezoid has an adjustment to change the width of the top  
- Arrows have two adjustments to change the shape of the head and tail  

This article will explain the use of [**Shape.geometry.shapeAdjustValues**](https://reference.aspose.com/cells/nodejs-cpp/shape/geometry/#shapeAdjustValues) property to change the adjustment value of the different shapes.  
{{% /alert %}}  

## **Change Adjustment Values**  

The below code sample shows how to change adjustment values of the shape.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

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

## **How to set or change the RoundedRectangularCallout tip point in excel**  

The following code example shows how to set or change a rounded rectangle callout tip point position in Excel.  

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
await workbook.saveAsync(path.join(filePath, "res.xlsx"), AsposeCells.SaveFormat.Xlsx);

// Read a new workbook
workbook = await AsposeCells.Workbook.openAsync(path.join(filePath, "res.xlsx"));
sheet = workbook.getWorksheets().get(0);

// Get a RoundedRectangularCallout from the worksheet
polygonShape = sheet.getShapes().get(0);
shapeGuides = polygonShape.getGeometry().getShapeAdjustValues();
shapeGuides.get(0).setValue(0.7);

// Save the workbook
await workbook.saveAsync(path.join(filePath, "res-resave.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

  