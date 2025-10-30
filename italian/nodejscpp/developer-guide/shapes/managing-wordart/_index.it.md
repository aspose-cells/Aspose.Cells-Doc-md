---
title: Aggiungi filigrana WordArt al foglio di lavoro con Node.js tramite C++
linktitle: Gestire WordArt
type: docs
weight: 180
url: /it/nodejs-cpp/add-wordart-watermark-to-worksheet/
description: Impara come aggiungere WordArt come filigrana di sfondo in un foglio di lavoro usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Usa WordArt per aggiungere effetti speciali al testo nei fogli di calcolo. Ad esempio, distendi un titolo sulla parte superiore del file, decora il testo e fai adattare il testo a una forma preimpostata, o applica il testo a un foglio di Excel come un watermark di sfondo. Il WordArt diventa un oggetto che puoi spostare o posizionare nei fogli di calcolo per aggiungere decorazioni.

{{% /alert %}} 

L'esempio seguente mostra come aggiungere una forma WordArt per impostare un watermark di sfondo per un foglio di lavoro.

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

## **Argomenti avanzati**
- [Aggiungi testo Word Art con stili incorporati](/cells/it/nodejs-cpp/add-word-art-text-with-built-in-styles/)
- [Bloccare WordArt Come Filigrana](/cells/it/nodejs-cpp/locking-wordart-watermark/)
- [Imposta lo stile predefinito di WordArt al testo della forma](/cells/it/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
{{< app/cells/assistant language="nodejs-cpp" >}}
