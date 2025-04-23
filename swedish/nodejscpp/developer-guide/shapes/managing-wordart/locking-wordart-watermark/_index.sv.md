---  
title: Lås WordArt vattenmärke med Node.js via C++  
linktitle: Låsa WordArt vattenstämpel  
type: docs  
weight: 170  
url: /sv/nodejs-cpp/locking-wordart-watermark/  
description: Lär dig att låsa WordArt vattenmärken i Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells API:er tillåter att lägga till WordArt-vattenmärken på arbetsbladet på ett sätt som gör att WordArt blir ett objekt du kan flytta och positionera på arbetsbladet. Det är också möjligt att låsa WordArt-objektet för interaktion som redigering, flyttning och urval. Den här artikeln förklarar användningen av [**Shape.setLockedProperty(ShapeLockType, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/shape/#setLockedProperty-shapelocktype-boolean-)-metoden för att låsa några aspekter av vattenmärket.

{{% /alert %}}  

Aspose.Cells API:er tillåter att låsa vissa aspekter av vattenmärket så att användarens interaktion kan begränsas eller helt blockeras. Följande kodexempel demonstrerar användningen av Aspose.Cells for Node.js via C++ för att låsa val av område, flyttning, redigering och storleksändring av vattenmärket genom att skapa ett kalkylblad från början.  

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

