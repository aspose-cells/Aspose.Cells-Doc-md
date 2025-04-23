---  
title: Exportera arbetsblad eller diagram till bild med önskad bredd och höjd via Node.js  
linktitle: Exportera arbetsbok eller diagram till bild med önskad bredd och höjd  
type: docs  
weight: 290  
url: /sv/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/  
description: Lär dig hur man exporterar ett arbetsblad eller diagram till en bild med specificerad bredd och höjd med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Du kan använda Aspose.Cells for Node.js via C++ för att exportera ditt arbetsblad eller diagram till en bild med önskad bredd och höjd. Det tillhandahåller [**ImageOrPrintOptions.setDesiredSize(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#setDesiredSize-number-number-boolean-) metod för att ställa in önskad bredd och höjd för den exporterade bilden. Bredden och höjden anges i pixlar.  
{{% /alert %}}  

Följande kod exporterar arbetsboken till en bild med storleken 400x400.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook object from source file
const filePath = path.join(sourceDir, "sampleWorksheetToImageDesiredSize.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set image or print options we want one page per sheet. The image format is in png and desired dimensions are 400x400
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);
opts.setDesiredSize(400, 400, false);

// Render sheet into image
const sr = new AsposeCells.SheetRender(worksheet, opts);
sr.toImage(0, path.join(outputDir, "outputWorksheetToImageDesiredSize.png"));
```  

