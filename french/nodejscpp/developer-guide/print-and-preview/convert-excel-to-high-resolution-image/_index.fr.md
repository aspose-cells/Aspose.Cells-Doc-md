---  
title: Convertir Excel en image haute résolution avec Node.js via C++  
linktitle: Convertir Excel en image haute résolution  
type: docs  
weight: 100  
url: /fr/nodejs-cpp/convert-excel-to-high-resolution-image/  
description: Apprenez comment convertir des fichiers Excel en images haute résolution en utilisant Aspose.Cells for Node.js via C++.  
---  

Avec la prévalence croissante des écrans haute résolution, les images générées à la résolution par défaut de 96 DPI apparaissent souvent floues et peu nettes. Pour assurer la clarté sur les écrans haute résolution, il est essentiel de générer des images à une DPI plus élevée. Aspose.Cells for Node.js via C++ offre la fonctionnalité de définir [**ImageOrPrintOptions.getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--) et [**ImageOrPrintOptions.getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--), vous permettant de créer des images de haute qualité à partir de fichiers Excel qui semblent nets sur des écrans haute résolution.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of ImageOrPrintOptions
const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(300);
options.setVerticalResolution(300);
options.setImageType(AsposeCells.ImageType.Png);

// Get the worksheet
const sheet = workbook.getWorksheets().get(0);

// Create a SheetRender instance
const render = new AsposeCells.SheetRender(sheet, options);

// Generate and save the image
render.toImage(0, "output.png");
```  

