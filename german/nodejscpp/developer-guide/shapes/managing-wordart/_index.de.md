---
title: Fügen Sie eine WordArt Wasserzeichnungs in das Arbeitsblatt mit Node.js via C++ hinzu
linktitle: Verwalten von WordArt
type: docs
weight: 180
url: /de/nodejs-cpp/add-wordart-watermark-to-worksheet/
description: Lernen Sie, wie Sie WordArt als Hintergrund Wasserzeichen in ein Arbeitsblatt mit Aspose.Cells for Node.js via C++ hinzufügen.
---

{{% alert color="primary" %}} 

Verwenden Sie WordArt, um spezielle Texteffekte zu Tabellenkalkulationen hinzuzufügen. Zum Beispiel können Sie einen Titel über die Oberseite der Datei strecken, Text dekorieren und Text an eine Excel-Tabelle als Hintergrund-Wasserzeichen anwenden. Das WordArt wird zu einem Objekt, das Sie in Tabellenkalkulationen verschieben oder platzieren können, um Dekoration hinzuzufügen.

{{% /alert %}} 

Das folgende Beispiel zeigt, wie ein WordArt-Objekt hinzugefügt wird, um ein Hintergrundwasserzeichen für ein Arbeitsblatt festzulegen.

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

## **Erweiterte Themen**
- [Fügen Sie Word-Art-Text mit integrierten Stilen hinzu](/cells/de/nodejs-cpp/add-word-art-text-with-built-in-styles/)
- [Sperren des WordArt-Wasserzeichens](/cells/de/nodejs-cpp/locking-wordart-watermark/)
- [Voreingestellten WordArt-Stil auf den Text der Form setzen](/cells/de/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
