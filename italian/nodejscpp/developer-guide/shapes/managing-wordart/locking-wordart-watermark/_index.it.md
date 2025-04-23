---  
title: Blocca WordArt Watermark con Node.js tramite C++  
linktitle: Bloccare WordArt Come Filigrana  
type: docs  
weight: 170  
url: /it/nodejs-cpp/locking-wordart-watermark/  
description: Impara come bloccare i filigrane WordArt in Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Le API di Aspose.Cells consentono di aggiungere filigrane WordArt sul foglio di lavoro in modo che il WordArt diventi un oggetto che puoi spostare e posizionare sul foglio di lavoro. È anche possibile bloccare l’oggetto WordArt per qualsiasi interazione come modifica, spostamento e selezione. Questo articolo spiega l’uso del metodo [**Shape.setLockedProperty(ShapeLockType, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/shape/#setLockedProperty-shapelocktype-boolean-) per bloccare alcuni aspetti della filigrana.

{{% /alert %}}  

Le API di Aspose.Cells consentono di bloccare alcuni aspetti della filigrana in modo che l’interazione dell’utente possa essere limitata o completamente bloccata. Il seguente frammento di codice dimostra l’uso di Aspose.Cells for Node.js via C++ per bloccare la selezione, il movimento, la modifica e le dimensioni della filigrana creando un foglio di calcolo da zero.  

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

