---
title: Lägg till WordArt vattenmärke i blad med Node.js via C++
linktitle: Hantera WordArt
type: docs
weight: 180
url: /sv/nodejs-cpp/add-wordart-watermark-to-worksheet/
description: Lär dig hur du lägger till WordArt som ett bakgrundsvattenmärke till ett blad med Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

 Använd WordArt för att lägga till speciella texteffekter till kalkylblad. Till exempel, sträck en rubrik överst på filen, dekorera text och få texten att passa en förinställd form eller applicera text på ett Excel-ark som en bakgrundsvattenstämpel. WordArt blir ett objekt som du kan flytta eller placera i kalkylblad för att lägga till dekoration.

{{% /alert %}} 

Följande exempel visar hur man lägger till en WordArt-form för att ställa in en bakgrundsvattenstämpel för ett arbetsblad.

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

## **Fortsatta ämnen**
- [Lägg till Word Art Text med Inbyggda Stilar](/cells/sv/nodejs-cpp/add-word-art-text-with-built-in-styles/)
- [Låsa WordArt vattenstämpel](/cells/sv/nodejs-cpp/locking-wordart-watermark/)
- [Ange förvald WordArt-stil för texten på formen](/cells/sv/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
