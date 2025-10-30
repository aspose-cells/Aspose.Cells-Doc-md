---
title: Extrahera bilder från arbetsblad med ImageOrPrintOptions med Node.js via C++
linktitle: Extrahera bilder från arbetsböcker med hjälp av ImageOrPrintOptions
type: docs
weight: 140
url: /sv/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Lär dig hur man extraherar bilder från Excel arbetsblad och sparar dem med Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Microsoft Excel-användare kan lägga till bilder i kalkylblad. Med Aspose.Cells for Node.js via C++ är det möjligt att läsa bilder från Microsoft Excel-filer och spara dem till en lokal enhet. Denna artikel visar hur.

{{% /alert %}} 

Den exempelkod nedan visar hur man extraherar bilder från en Excel-fil och sparar dem.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExtractImagesFromWorksheets.xlsx"));

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the first Picture in the first worksheet
const pic = worksheet.getPictures().get(0);

// Set the output image file path
const picformat = pic.getImageType().toString();

// Note: you may evaluate the image format before specifying the image path
// Define ImageOrPrintOptions
const printoption = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
printoption.setImageType(AsposeCells.ImageType.Jpeg);

// Save the image
pic.toImage(path.join(outputDir, "outputExtractImagesFromWorksheets.jpg"), printoption);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
