---
title: Générer une miniature de la feuille de calcul avec Node.js via C++
linktitle: Générer une miniature de la feuille de calcul
type: docs
weight: 110
url: /fr/nodejs-cpp/generate-thumbnail-of-the-worksheet/
description: Apprenez comment générer une image miniature à partir d une feuille en utilisant Aspose.Cells for Node.js via C++. Créez de petites images pour les aperçus dans les documents et présentations.
---

{{% alert color="primary" %}} 

Il peut être utile de générer des miniatures à partir de feuilles de calcul. Une miniature est une petite image qui peut être collée dans un document Word ou une présentation PowerPoint pour donner un aperçu de ce qui se trouve sur la feuille de calcul. Elle peut être ajoutée à une page web avec un lien pour télécharger le document original et avoir une multitude d'autres utilisations.

{{% /alert %}} 

Aspose.Cells for Node.js via C++ vous permet de produire des fichiers image à partir de feuilles de calcul, ce qui facilite la création de miniatures. Le code exemple ci-dessous montre comment exporter des feuilles de calcul en fichiers image.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiate and open an Excel file
const filePath = path.join(sourceDir, "sampleGenerateThumbnailOfWorksheet.xlsx");
const book = new AsposeCells.Workbook(filePath);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Set the vertical and horizontal resolution
imgOptions.setVerticalResolution(200);
imgOptions.setHorizontalResolution(200);

// One page per sheet is enabled
imgOptions.setOnePagePerSheet(true);

// Set desired thumbnail dimensions
imgOptions.setDesiredSize(600, 600, true);

// Get the first worksheet
const sheet = book.getWorksheets().get(0);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the thumbnail directly
sr.toImage(0, path.join(outputDir, "outputGenerateThumbnailOfWorksheet.jpg"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
