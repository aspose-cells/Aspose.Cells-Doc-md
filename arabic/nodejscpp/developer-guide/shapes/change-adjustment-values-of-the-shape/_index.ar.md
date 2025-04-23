---  
title: تغيير قيم الضبط للشكل باستخدام Node.js عبر C++  
linktitle: تغيير قيم التعديل للشكل  
type: docs  
weight: 2000  
url: /ar/nodejs-cpp/change-adjustment-values-of-the-shape/  
description: تعلم كيفية تغيير قيم ضبط الأشكال في Excel باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
توفر Aspose.Cells خاصية [**Shape.getGeometry()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGeometry--) لإجراء تغييرات على نقاط التعديل مع الأشكال. في واجهة مستخدم Microsoft Excel، تعرض عمليات التعديل على شكل نقاط ماسية صفراء. على سبيل المثال:  

- المستطيل المستدير له تعديل لتغيير القوس  
- المثلث له تعديل لتغيير موقع النقطة  
- المنظر له تعديل لتغيير عرض الجزء العلوي  
- السهام لها تعديلين لتغيير شكل الرأس والذيل  

سيشرح هذا المقال استخدام خاصية [**Shape.getGeometry()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGeometry--) لتغيير قيمة التعديل لأشكال مختلفة.  
{{% /alert %}}  

## **تغيير قيم التعديل**  

يُظهر الكود العيني أدناه كيفية تغيير قيم التعديل للشكل.  

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

## **كيفية ضبط أو تغيير نقطة طرف Callout المستديرة في Excel**  

يظهر المثال التالي لكيفية ضبط أو تغيير موضع نقطة طرف Callout المستديرة في Excel.  

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


