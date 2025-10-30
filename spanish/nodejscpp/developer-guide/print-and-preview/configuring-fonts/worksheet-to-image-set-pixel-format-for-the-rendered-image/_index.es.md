---  
title: Hoja de trabajo a imagen  Establecer formato de píxel para la imagen renderizada con Node.js a través de C++  
linktitle: Hoja de Cálculo a Imagen  Establecer Formato de Píxel para la Imagen Renderizada  
type: docs  
weight: 200  
url: /es/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/  
---  

{{% alert color="primary" %}}  
A veces deseas especificar el formato de píxel al renderizar una hoja de cálculo a formato de imagen. Por defecto, Aspose.Cells utiliza 32 bits por píxel. Aspose.Cells te permite personalizar el formato de píxel (profundidad de bits) usando opciones para la imagen renderizada.  
{{% /alert %}}  

Por favor, consulta el código de ejemplo a continuación que demuestra cómo establecer el formato de píxel deseado al renderizar imágenes de las hojas.  

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
