---
title: Añadir texto WordArt con estilos integrados usando Node.js mediante C++
linktitle: Añadir texto de Word Art con estilos integrados
type: docs
weight: 270
url: /es/nodejs-cpp/add-word-art-text-with-built-in-styles/
description: Aprende a agregar texto WordArt con estilos integrados usando Aspose.Cells for Node.js via C++. Crea texto visualmente atractivo en Excel usando estilos integrados.
---

## **Escenarios de uso posibles**
Puedes agregar texto WordArt con estilos integrados usando Aspose.Cells for Node.js via C++. Usa el método [ShapeCollection.addWordArt()](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addWordArt-presetwordartstyle-string-number-number-number-number-number-number-) para ello.

## **Añadir texto de Word Art con estilos integrados**
El siguiente código de muestra añade textos de Word Art con diferentes estilos integrados. Por favor, revise el [archivo de excel de salida](5115470.xlsx) generado con este código. Así es como se ve el [archivo de excel de salida](5115470.xlsx) en Microsoft Excel

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Add Word Art Text with Built-in Styles
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle1, "Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```
