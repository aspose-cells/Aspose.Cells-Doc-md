---  
title: Locking WordArt Watermark with Node.js via C++  
linktitle: Locking WordArt Watermark  
type: docs  
weight: 170  
url: /nodejs-cpp/locking-wordart-watermark/  
description: Learn how to lock WordArt watermarks in Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells APIs allow adding WordArt watermarks on the worksheet in a way that the WordArt becomes an object that you can move and position on the worksheet. It is also possible to lock the WordArt object for any interaction such as editing, movement & selection. This article explains the usage of [**Shape.setLockedProperty(ShapeLockType, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/shape/#setLockedProperty-shapelocktype-boolean-) method to lock a few aspects of the watermark.

{{% /alert %}}  

Aspose.Cells APIs allow locking certain aspects of the watermark so that user interaction could be limited or completely blocked. The following code snippet demonstrates the usage of Aspose.Cells for Node.js via C++ to lock selection, movement, editing, and resizing of the watermark by creating a spreadsheet from scratch.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();

// Get the first default sheet
const sheet = workbook.getWorksheets().get(0);

// Add Watermark
const wordart = sheet.getShapes().addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
"CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

// Lock Shape Aspects
wordart.setIsLocked(true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Selection, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.ShapeType, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Move, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Resize, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Text, true);

// Get the fill format of the word art
const wordArtFormat = wordart.getFill();

// Set the color
wordArtFormat.setOneColorGradient(AsposeCells.Color.Red, 0.2, AsposeCells.GradientStyleType.Horizontal, 2);

// Set the transparency
wordArtFormat.setTransparency(0.9);

// Make the line invisible
wordart.setHasLine(false);

// Save the file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}