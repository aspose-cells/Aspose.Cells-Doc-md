---
title: Aggiungi testo Word Art con stili incorporati usando Node.js tramite C++
linktitle: Aggiungi testo Word Art con stili incorporati
type: docs
weight: 270
url: /it/nodejs-cpp/add-word-art-text-with-built-in-styles/
description: Impara ad aggiungere testo WordArt con stili incorporati usando Aspose.Cells for Node.js via C++. Crea testo visivamente attraente in Excel usando stili incorporati.
---

## **Possibili Scenari di Utilizzo**
Puoi aggiungere testo WordArt con stili incorporati usando Aspose.Cells for Node.js via C++. Si prega di usare il metodo [ShapeCollection.addWordArt()](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addWordArt-presetwordartstyle-string-number-number-number-number-number-number-) per questa funzione.

## **Aggiungi testo Word Art con stili incorporati**
Il seguente codice di esempio aggiunge testi Word Art con differenti stili incorporati. Si prega di controllare il [file excel di output](5115470.xlsx) generato con questo codice. Ecco come appare il [file excel di output](5115470.xlsx) in Microsoft Excel.

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
