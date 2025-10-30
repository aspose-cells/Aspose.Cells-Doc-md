---  
title: Angiv hur du korsar strängar i utdata PDF och bild med Node.js via C++  
linktitle: Ange hur du ska korsa strängen i utdata PDF och bild  
type: docs  
weight: 120  
url: /sv/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/  
description: Lär dig att kontrollera textöverflöd i utdata PDF/Bild genom att ange korsningstyp med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**

När en cell innehåller text eller en sträng men är större än cellens bredd, flödar strängen ut om nästa cell i nästa kolumn är null eller tom. När du sparar din Excel-fil till PDF/Bild kan du kontrollera detta överflöd genom att ange korsningstypen med [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype). Den har följande värden:

- **TextCrossType.Default**: Visar text som MS Excel, vilket beror på nästa cell. Om nästa cell är null kommer strängen att korsas eller så kommer den att skäras av.

- **TextCrossType.CrossKeep**: Visa strängen som MS Excel-exporterar till PDF/Bild.

- **TextCrossType.CrossOverride**: Visa all text genom att korsar andra celler och åsidosätter texten i korsade celler.

- **TextCrossType.StrictInCell**: Visar endast strängen inom cellens bredd.

## **Ange hur du ska korsa strängen i utdata PDF/Bild med hjälp av TextCrossType**

Följande kod laddar standadexempel fil och sparar den i PDF/Bild-format genom att specificera olika [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype). Standadexempel fil och utdatafiler kan laddas ner från följande länkar:

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### Exempelkod

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCrosssType.xlsx"));

// Initialize PDF save options
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set text cross type
pdfSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Save PDF file
workbook.save(outputDir + "outputCrosssType.pdf", pdfSaveOptions);

// Initialize image or print options
const imageSaveOptions = new AsposeCells.ImageOrPrintOptions();

// Set text cross type
imageSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Initialize sheet renderer object
const sheetRenderer = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imageSaveOptions);

sheetRenderer.toImage(0, outputDir + "outputCrosssType.png");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
