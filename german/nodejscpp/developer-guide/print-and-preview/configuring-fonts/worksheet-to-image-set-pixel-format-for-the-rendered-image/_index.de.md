---  
title: Arbeitsblatt zu Bild  Setzen des Pixel Formats für das gerenderte Bild mit Node.js über C++  
linktitle: Arbeitsblatt zu Bild  Festlegen des Pixelformats für das gerenderte Bild  
type: docs  
weight: 200  
url: /de/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/  
---  

{{% alert color="primary" %}}  
Manchmal möchten Sie das Pixelformat beim Rendern eines Arbeitsblatts im Bildformat angeben. Standardmäßig verwendet Aspose.Cells 32 Bits pro Pixel. Aspose.Cells ermöglicht es Ihnen, das Pixelformat (Bit-Tiefe) mit Optionen für das gerenderte Bild anzupassen.  
{{% /alert %}}  

Bitte beachten Sie den unten stehenden Beispielcode, der zeigt, wie das gewünschte Pixelformat beim Rendern von Blättern festgelegt wird.  

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
