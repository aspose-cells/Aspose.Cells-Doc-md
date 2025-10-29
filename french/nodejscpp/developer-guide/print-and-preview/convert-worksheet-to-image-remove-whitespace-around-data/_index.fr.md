---
title: Convertir feuille de calcul en image  Supprimer l espace blanc autour des données avec Node.js via C++
linktitle: Convertir la feuille de calcul en image  Supprimer les espaces blancs autour des données
type: docs
weight: 40
url: /fr/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Apprenez comment convertir des feuilles Microsoft Excel en images et supprimer l espace blanc autour des données en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Parfois, vous devez présenter des images de feuille de calcul dans des applications ou des pages web. Par exemple, vous pourriez avoir besoin d'insérer des images dans un document Word, un fichier PDF, une présentation PowerPoint ou un autre document. Fondamentalement, vous souhaitez afficher une feuille de calcul sous forme d'image afin de pouvoir la coller dans d'autres applications. Aspose.Cells vous permet de convertir des feuilles de calcul Microsoft Excel en images.

{{% /alert %}}

## **Supprimer les espaces vides autour des données**

L'API [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) convertit une feuille de calcul en un fichier image avec les attributs spécifiés, par exemple, le format de l'image, les feuilles paginées, etc. Plusieurs formats d'image sont pris en charge, notamment BMP, GIF, JPG, TIFF et EMF.

Lorsque vous utilisez la fonction de feuille à image, l'image de sortie comporte par défaut des espaces vides, c'est-à-dire une bordure. Vous pouvez supprimer cela en définissant les marges de mise en page supérieure, inférieure, gauche et droite pour la feuille source sur 0 et en spécifiant les attributs [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions) en conséquence.

Le code suivant supprime les espaces vides autour des données dans l'image de sortie.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
const options = new AsposeCells.LoadOptions();
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All));
// Specify your print area if you want
// sheet.getPageSetup().setPrintArea("A1:H8");

// To remove the white border around the image.
sheet.getPageSetup().setLeftMargin(0);
sheet.getPageSetup().setRightMargin(0);
sheet.getPageSetup().setBottomMargin(0);
sheet.getPageSetup().setTopMargin(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Emf);

// Set only one page would be rendered for the image
imgOptions.setOnePagePerSheet(true);
imgOptions.setPrintingPage(AsposeCells.PrintingPageType.IgnoreBlank);

// Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Convert the image
sr.toImage(0, path.join(outputDir, "outputRemoveWhitespaceAroundData.emf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
