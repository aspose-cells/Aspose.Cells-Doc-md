---  
title: Exporter une feuille de calcul ou un graphique en image avec une largeur et une hauteur désirées via Node.js  
linktitle: Exporter la feuille de calcul ou le graphique en image avec une largeur et une hauteur souhaitées  
type: docs  
weight: 290  
url: /fr/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/  
description: Apprenez comment exporter une feuille de calcul ou un graphique en une image avec une largeur et une hauteur spécifiées en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Vous pouvez utiliser Aspose.Cells for Node.js via C++ pour exporter votre feuille de calcul ou graphique en une image avec la largeur et la hauteur souhaitées. Il fournit la méthode [**ImageOrPrintOptions.setDesiredSize(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#setDesiredSize-number-number-boolean-) pour définir la largeur et la hauteur désirées de l'image exportée. La largeur et la hauteur sont en pixels.  
{{% /alert %}}  

Le code suivant exporte la feuille de calcul en une image de taille 400x400.  

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

