---  
title: Node.js経由でC++を使用してシェイプの調整値を変更する  
linktitle: シェイプの調整値の変更  
type: docs  
weight: 2000  
url: /ja/nodejs-cpp/change-adjustment-values-of-the-shape/  
description: Aspose.Cells for Node.js via C++を使用してExcelのシェイプの調整値を変更する方法を学びます。  
---  

{{% alert color="primary" %}}  
Aspose.Cells は、シェイプの調整ポイントを変更するための [**Shape.getGeometry()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGeometry--) プロパティを提供します。Microsoft Excel の UI では、調整は黄色のダイヤモンドノードとして表示されます。例:  

- 角丸四角形は、円弧を変更するための調整があります  
- 三角形は、ポイントの位置を変更するための調整があります  
- 台形は、上部の幅を変更するための調整があります  
- 矢印には、頭部と末尾の形状を変更するための2つの調整があります  

この記事では、異なるシェイプの調整値を変更するための [**Shape.getGeometry()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGeometry--) プロパティの使用方法について説明します。  
{{% /alert %}}  

## **調整値の変更**  

以下のコードサンプルは、シェイプの調整値を変更する方法を示しています。  

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

## **ExcelでRoundedRectangularCalloutの先端点を設定または変更する方法**  

以下のコード例は、Excelでラウンド長方形のコールアウトの先端点位置を設定または変更する方法を示しています。  

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


