---
title: Lägg till Word Art Text med inbyggda stilar med Node.js via C++
linktitle: Lägg till Word Art Text med Inbyggda Stilar
type: docs
weight: 270
url: /sv/nodejs-cpp/add-word-art-text-with-built-in-styles/
description: Lär dig att lägga till Word Art Text med inbyggda stilar med Aspose.Cells for Node.js via C++. Skapa visuellt tilltalande text i Excel med inbyggda stilar.
---

## **Möjliga användningsscenario**
Du kan lägga till Word Art Text med inbyggda stilar med Aspose.Cells for Node.js via C++. Använd [ShapeCollection.addWordArt()](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addWordArt-presetwordartstyle-string-number-number-number-number-number-number-) metoden för detta ändamål.

## **Lägg till Word Art Text med Inbyggda Stilar**
Följande kodexempel lägger till Word Art-texter med olika inbyggda stilar. Vänligen kontrollera [output excel-filen](5115470.xlsx) som genererats med denna kod. Så här ser [output excel-filen](5115470.xlsx) ut i Microsoft Excel.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
