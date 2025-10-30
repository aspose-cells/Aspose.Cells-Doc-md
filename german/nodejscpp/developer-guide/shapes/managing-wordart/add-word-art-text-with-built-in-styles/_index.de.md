---
title: WortArt Text mit integrierten Stilen mit Node.js via C++ hinzufügen
linktitle: Fügen Sie Word Art Text mit integrierten Stilen hinzu
type: docs
weight: 270
url: /de/nodejs-cpp/add-word-art-text-with-built-in-styles/
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ WordArt Text mit integrierten Stilen hinzufügen. Erstellen Sie visuell ansprechenden Text in Excel mit integrierten Stilen.
---

## **Mögliche Verwendungsszenarien**
Sie können WordArt-Text mit integrierten Stilen mit Aspose.Cells for Node.js via C++ hinzufügen. Verwenden Sie dafür die Methode [ShapeCollection.addWordArt()](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addWordArt-presetwordartstyle-string-number-number-number-number-number-number-)

## **Fügen Sie Word-Art-Text mit integrierten Stilen hinzu**
Der folgende Beispielcode fügt Wortkunsttexte mit unterschiedlichen integrierten Stilen hinzu. Überprüfen Sie die mit diesem Code generierte [Ausgabedatei](5115470.xlsx) in Microsoft Excel. So sieht die [Ausgabedatei](5115470.xlsx) in Microsoft Excel aus.

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
