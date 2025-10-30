---
title: Skapa miniatyrbild av arbetsblad med Node.js via C++
linktitle: Generera miniatyrbild av arbetsboken
type: docs
weight: 110
url: /sv/nodejs-cpp/generate-thumbnail-of-the-worksheet/
description: Lär dig hur man genererar en miniatyrbild från ett arbetsblad med Aspose.Cells for Node.js via C++. Skapa små bilder för förhandsgranskningar i dokument och presentationer.
---

{{% alert color="primary" %}} 

Det kan vara användbart att generera miniatyrbilder från arbetsböcker. En miniatyrbild är en liten bild som kan klistras in i ett Word-dokument eller en PowerPoint-presentation för att ge en förhandsgranskning av innehållet i arbetsboken. Den kan läggas till på en webbsida med en länk för att ladda ner den ursprungliga filen och har en mängd andra användningsområden.

{{% /alert %}} 

Aspose.Cells for Node.js via C++ tillåter dig att utdata arbetsblad till bildfiler, så att skapa en miniatyrbild är enkelt. Koden nedan visar hur du utdata arbetsblad till bildfiler.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiate and open an Excel file
const filePath = path.join(sourceDir, "sampleGenerateThumbnailOfWorksheet.xlsx");
const book = new AsposeCells.Workbook(filePath);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Set the vertical and horizontal resolution
imgOptions.setVerticalResolution(200);
imgOptions.setHorizontalResolution(200);

// One page per sheet is enabled
imgOptions.setOnePagePerSheet(true);

// Set desired thumbnail dimensions
imgOptions.setDesiredSize(600, 600, true);

// Get the first worksheet
const sheet = book.getWorksheets().get(0);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the thumbnail directly
sr.toImage(0, path.join(outputDir, "outputGenerateThumbnailOfWorksheet.jpg"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
