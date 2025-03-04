---  
title: Worksheet to Image - Set Pixel Format for the Rendered Image with Node.js via C++  
linktitle: Worksheet to Image - Set Pixel Format for the Rendered Image  
type: docs  
weight: 200  
url: /nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/  
---  

{{% alert color="primary" %}}  
Sometimes you want to specify the pixel format when rendering a worksheet to image format. By default, Aspose.Cells uses 32 bits per pixel. Aspose.Cells allows you to customize the pixel format (bit depth) using options for the rendered image.  
{{% /alert %}}  

Please see the sample code below that demonstrates how to set the desired pixel format while rendering images of the sheets.  

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
  