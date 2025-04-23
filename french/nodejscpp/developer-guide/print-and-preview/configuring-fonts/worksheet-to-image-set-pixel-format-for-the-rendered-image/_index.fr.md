---  
title: Feuille de calcul en image  Définir le format pixel pour l’image rendue avec Node.js via C++  
linktitle: Feuille de calcul vers l image  Définir le format de pixel pour l image rendue  
type: docs  
weight: 200  
url: /fr/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/  
---  

{{% alert color="primary" %}}  
Parfois, vous souhaitez spécifier le format de pixel lors du rendu d'une feuille de calcul au format image. Par défaut, Aspose.Cells utilise 32 bits par pixel. Aspose.Cells vous permet de personnaliser le format de pixel (profondeur de bits) en utilisant des options pour l'image rendue.  
{{% /alert %}}  

Veuillez consulter le code exemple ci-dessous qui montre comment définir le format de pixel souhaité lors du rendu des images des feuilles.  

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

