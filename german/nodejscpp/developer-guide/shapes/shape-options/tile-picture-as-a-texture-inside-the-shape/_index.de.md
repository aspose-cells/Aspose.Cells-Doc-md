---  
title: Kachelbild als Textur innerhalb des Shapes mit Node.js via C++  
linktitle: Kachelbild als Textur in der Form  
type: docs  
weight: 1700  
url: /de/nodejs-cpp/tile-picture-as-a-texture-inside-the-shape/  
description: Erfahren Sie, wie Sie ein kleines Bild als Textur innerhalb eines Shapes mit Aspose.Cells for Node.js via C++ kacheln.  
---  

## **Mögliche Verwendungsszenarien**  

Wenn das Bild klein ist und nicht die gesamte Oberfläche der Form abdeckt, ohne an Qualität zu verlieren, haben Sie die Möglichkeit, es zu kacheln. Kacheln füllt die Oberfläche der Form mit einem kleinen Bild, indem es diese wiederholt, als wären es Fliesen.  

## **Kachelbild als Textur in der Form**  

Sie können die Fläche des Shapes mit einem Bild füllen und es mit der Eigenschaft [**Shape.isTiling()**](https://reference.aspose.com/cells/nodejs-cpp/texturefill/#isTiling--) und dem Wert **true** kacheln. Bitte sehen Sie sich den folgenden Beispielcode, die [Beispieldatei Excel](46465050.xlsx) sowie den Screenshot als Referenz an.  

## **Screenshot**  

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleTextureFill_IsTiling.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape inside the worksheet
const shape = worksheet.getShapes().get(0);

// Tile Picture as a Texture inside the Shape 
shape.getFill().getTextureFill().setIsTiling(true);

// Save the output Excel file
workbook.save(path.join(outputDir, "outputTextureFill_IsTiling.xlsx"));
```  

