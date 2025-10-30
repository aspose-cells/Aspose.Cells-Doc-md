---
title: Agregar marca de agua WordArt al worksheet con Node.js a través de C++
linktitle: Gestionar WordArt
type: docs
weight: 180
url: /es/nodejs-cpp/add-wordart-watermark-to-worksheet/
description: Aprende a agregar WordArt como marca de agua de fondo en una hoja de cálculo usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Utilice WordArt para agregar efectos especiales de texto a las hojas de cálculo. Por ejemplo, estire un título en la parte superior del archivo, decore texto y ajuste texto a una forma predefinida, o aplique texto a una hoja de Excel como marca de agua de fondo. El WordArt se convierte en un objeto que puede mover o posicionar en las hojas de cálculo para agregar decoración.

{{% /alert %}} 

El siguiente ejemplo muestra cómo agregar una forma WordArt para establecer una marca de agua de fondo para una hoja de cálculo.

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

// Get the fill format of the word art
const wordArtFormat = wordart.getFill();            

// Set the transparency
wordArtFormat.setTransparency(0.9);

// Make the line invisible
const lineFormat = wordart.getLine();          

const outputFilePath = path.join(dataDir, "Watermark_Test.out.xls");
// Save the file
workbook.save(outputFilePath);
```

## **Temas avanzados**
- [Añadir texto de Word Art con estilos integrados](/cells/es/nodejs-cpp/add-word-art-text-with-built-in-styles/)
- [Bloquear marca de agua WordArt](/cells/es/nodejs-cpp/locking-wordart-watermark/)
- [Establecer un estilo de WordArt preestablecido al texto de la forma](/cells/es/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
{{< app/cells/assistant language="nodejs-cpp" >}}
