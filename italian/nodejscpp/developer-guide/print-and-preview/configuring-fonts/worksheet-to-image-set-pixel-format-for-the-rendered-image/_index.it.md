---  
title: Worksheet to Image  Imposta il formato pixel per l immagine renderizzata con Node.js tramite C++  
linktitle: Foglio di lavoro in immagine  Imposta il formato del pixel per l immagine renderizzata  
type: docs  
weight: 200  
url: /it/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/  
---  

{{% alert color="primary" %}}  
A volte è necessario specificare il formato del pixel durante la renderizzazione di un foglio di lavoro in formato immagine. Per impostazione predefinita, Aspose.Cells utilizza 32 bit per pixel. Aspose.Cells consente di personalizzare il formato del pixel (profondità dei bit) utilizzando opzioni per l'immagine renderizzata.  
{{% /alert %}}  

Si prega di consultare il codice di esempio di seguito che dimostra come impostare il formato del pixel desiderato durante la renderizzazione delle immagini dei fogli.  

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

