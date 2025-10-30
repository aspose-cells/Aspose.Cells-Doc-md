---  
title: Arbetsblad till bild  Ange pixelformat för den renderade bilden med Node.js via C++  
linktitle: Kalkylblad till bild  Ställ in bildpunktsformat för den renderade bilden  
type: docs  
weight: 200  
url: /sv/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/  
---  

{{% alert color="primary" %}}  
Ibland vill du ange bildpunktsformatet vid rendering av ett kalkylblad till bildformat. Som standard använder Aspose.Cells 32 bitar per pixel. Aspose.Cells tillåter dig att anpassa bildpunktsformatet (bitdjup) med hjälp av alternativ för den renderade bilden.  
{{% /alert %}}  

Se den nedanstående exempelkoden som visar hur man ställer in önskat bildpunktsformat vid rendering av arkens bilder.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleSetPixelFormatRenderedImage.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the ImageOrPrintOptions with desired color depth (24 bits per pixel) and image format type
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setTiffColorDepth(AsposeCells.ColorDepth.Format24bpp);
opts.setImageType(AsposeCells.ImageType.Tiff);

// Instantiate SheetRender object based on the first worksheet
const sheetRender = new AsposeCells.SheetRender(worksheet, opts);

// Save the image (first page of the sheet) with the specified options
sheetRender.toImage(0, path.join(outputDir, "outputSetPixelFormatRenderedImage.tiff"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
