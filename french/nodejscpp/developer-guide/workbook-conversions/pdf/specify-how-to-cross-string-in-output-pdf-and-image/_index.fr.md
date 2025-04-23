---  
title: Spécifier comment traiter les chaînes dans le PDF et l image générés avec Node.js via C++  
linktitle: Spécifiez comment croiser une chaîne dans le PDF de sortie et l image  
type: docs  
weight: 120  
url: /fr/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/  
description: Apprenez à contrôler le débordement du texte dans le PDF/Image de sortie en spécifiant le type de croisement à l aide de Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**

Lorsqu'une cellule contient du texte ou une chaîne mais est plus large que la largeur de la cellule, la chaîne déborde si la cellule suivante dans la colonne suivante est nulle ou vide. Lors de la sauvegarde de votre fichier Excel en PDF/Image, vous pouvez contrôler ce débordement en spécifiant le type de croisement avec le [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype). Il a les valeurs suivantes :

- **TextCrossType.Default** : Affiche le texte comme MS Excel, dépendant de la cellule suivante. Si la cellule suivante est nulle, la chaîne débordera ou sera tronquée.

- **TextCrossType.CrossKeep** : Affiche la chaîne comme l'exportation PDF/Image de MS Excel.

- **TextCrossType.CrossOverride** : Affiche tout le texte en croisant d'autres cellules et en écrasant le texte des cellules croisées.

- **TextCrossType.StrictInCell**: Affiche uniquement la chaîne dans la largeur de la cellule.

## **Spécifiez comment croiser une chaîne dans le PDF de sortie/une image en utilisant TextCrossType**

Le code d'exemple suivant charge le fichier Excel d'exemple et le sauvegarde au format PDF/Image en spécifiant différents [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype). Le fichier Excel d'exemple et les fichiers de sortie peuvent être téléchargés depuis les liens suivants :

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### Code d'exemple

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCrosssType.xlsx"));

// Initialize PDF save options
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set text cross type
pdfSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Save PDF file
workbook.save(outputDir + "outputCrosssType.pdf", pdfSaveOptions);

// Initialize image or print options
const imageSaveOptions = new AsposeCells.ImageOrPrintOptions();

// Set text cross type
imageSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Initialize sheet renderer object
const sheetRenderer = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imageSaveOptions);

sheetRenderer.toImage(0, outputDir + "outputCrosssType.png");
```  

