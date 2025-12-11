---  
title: Tile Picture as a Texture inside the Shape with Node.js via C++  
linktitle: Tile Picture as a Texture inside the Shape  
type: docs  
weight: 1700  
url: /nodejs-cpp/tile-picture-as-a-texture-inside-the-shape/  
description: Learn how to tile a small picture as a texture inside a shape using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

## **Possible Usage Scenarios**  

When the picture is small and does not cover the entire surface of the shape without losing its quality, you have the option to tile it. Tiling fills the shape surface with a small image by repeating it as tiles.  

## **Tile Picture as a Texture inside the Shape**  

You can fill the shape surface with an image and tile it by using the [**Shape.isTiling()**](https://reference.aspose.com/cells/nodejs-cpp/texturefill/#isTiling--) property and setting it to **true**. Please see the following sample code, its [sample Excel file](46465050.xlsx), and the screenshot for reference.  

## **Screenshot**  

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)  

## **Sample Code**  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
