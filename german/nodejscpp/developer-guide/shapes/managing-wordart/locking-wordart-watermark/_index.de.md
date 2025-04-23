---  
title: Locken Sie WordArt Wasserzeichen mit Node.js via C++  
linktitle: Sperren des WordArt Wasserzeichens  
type: docs  
weight: 170  
url: /de/nodejs-cpp/locking-wordart-watermark/  
description: Erfahren Sie, wie Sie WordArt Wasserzeichen in Aspose.Cells for Node.js via C++ sperren.  
---  

{{% alert color="primary" %}}  

Aspose.Cells APIs ermöglichen das Hinzufügen von WordArt-Wasserzeichen auf dem Arbeitsblatt, sodass WordArt zu einem Objekt wird, das bewegt und positioniert werden kann. Es ist auch möglich, das WordArt-Objekt für Interaktionen wie Bearbeitung, Bewegung & Auswahl zu sperren. Dieser Artikel erklärt die Verwendung der [**Shape.setLockedProperty(ShapeLockType, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/shape/#setLockedProperty-shapelocktype-boolean-)-Methode, um bestimmte Aspekte des Wasserzeichens zu sperren.

{{% /alert %}}  

Aspose.Cells APIs erlauben es, bestimmte Aspekte des Wasserzeichens zu sperren, sodass die Benutzerinteraktion eingeschränkt oder vollständig blockiert wird. Der folgende Codeausschnitt demonstriert die Verwendung von Aspose.Cells for Node.js via C++, um die Auswahl, Bewegung, Bearbeitung und Größenänderung des Wasserzeichens durch das Erstellen einer Tabelle von Grund auf zu sperren.  

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

