---  
title: Angiv enskilda eller privata teckensnittssatser för arbetsboksrendering med Node.js via C++  
linktitle: Ange individuella eller privata uppsättningar typsnitt för arbetsbokpresentation  
type: docs  
weight: 40  
url: /sv/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/  
description: Lär dig hur man specificerar enskilda eller privata teckensnittssatser för arbetsboksrendering med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Vanligtvis specificerar du teckensnittmappen eller listan av teckensnitt för alla arbetsböcker, men ibland måste du specificera enskilda eller privata teckensnittssatser för dina arbetsböcker. Aspose.Cells for Node.js via C++ tillhandahåller klassen [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs) som kan användas för att specificera enskilda eller privata teckensnittssatser för din arbetsbok.  

## **Ange individuella eller privata uppsättningar typsnitt för arbetsbokpresentation**  

Följande exempelkod laddar [exempel Excel-fil](67338268.xlsx) med dess enskilda eller privata teckensnittssatser som specificeras med klassen [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs). Se även den [exempel teckensnitt](67338271.zip) som används i koden samt den [genererade PDF-filen](67338269.pdf). Denna skärmdump visar hur den färdiga PDF:en ser ut om tecknet hittas framgångsrikt.  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Path of your custom font directory.
const customFontsDir = "C:\\TempDir\\CustomFonts";

// Specify individual font configs custom font directory.
const fontConfigs = new AsposeCells.IndividualFontConfigs();

// If you comment this line or if custom font directory is wrong or 
// if it does not contain required font then output pdf will not be rendered correctly.
fontConfigs.setFontFolder(customFontsDir, false);

// Specify load options with font configs.
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setFontConfigs(fontConfigs);

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx");
// Output directory
const outputDir = path.join(__dirname, "output");
// Load the sample Excel file with individual font configs. 
const wb = new AsposeCells.Workbook(filePath, opts);

// Save to PDF format.
wb.save(outputDir + "outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", AsposeCells.SaveFormat.Pdf);
```  

