---  
title: Bloquear marca de agua WordArt con Node.js mediante C++  
linktitle: Bloqueo de marca de agua de WordArt  
type: docs  
weight: 170  
url: /es/nodejs-cpp/locking-wordart-watermark/  
description: Aprende cómo bloquear marcas de agua WordArt en Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Las APIs de Aspose.Cells permiten agregar marcas de agua WordArt en la hoja de cálculo de forma que el WordArt se convierte en un objeto que puedes mover y posicionar en la hoja de cálculo. También es posible bloquear el objeto WordArt para cualquier interacción como editar, mover y seleccionar. Este artículo explica el uso del método [**Shape.setLockedProperty(ShapeLockType, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/shape/#setLockedProperty-shapelocktype-boolean-) para bloquear algunos aspectos de la marca de agua.

{{% /alert %}}  

Las APIs de Aspose.Cells permiten bloquear ciertos aspectos de la marca de agua para que la interacción del usuario pueda ser limitada o completamente bloqueada. El siguiente fragmento de código demuestra el uso de Aspose.Cells for Node.js via C++ para bloquear la selección, movimiento, edición y redimensionamiento de la marca de agua creando una hoja de cálculo desde cero.  

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

