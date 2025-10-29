---  
title: 通过 C++ 使用 Node.js 更改 Shape 的调整值  
linktitle: 更改形状的调整值  
type: docs  
weight: 2000  
url: /zh/nodejs-cpp/change-adjustment-values-of-the-shape/  
description: 了解如何使用 Aspose.Cells for Node.js via C++ 更改 Excel 中形状的调整值。  
---  

{{% alert color="primary" %}}  
Aspose.Cells 提供 [**Shape.getGeometry()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGeometry--) 属性以更改形状的调整点。在微软Excel用户界面中，调整显示为黄色菱形节点。例如：  

- 圆角矩形有一个调整来改变拱形  
- 三角形有一个调整来改变顶点的位置  
- 梯形具有一个调整以更改顶部的宽度  
- 箭头有两个调整，可改变箭头头部和尾部的形状  

本文将解释如何使用 [**Shape.getGeometry()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGeometry--) 属性来更改不同形状的调整值。  
{{% /alert %}}  

## ** 更改调整值**  

以下代码示例显示如何更改形状的调整值。  

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

## **在Excel中设置或更改圆角矩形文本框的尖端点**  

以下示例演示如何在Excel中设置或更改圆角矩形文本框的尖端点位置。  

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
