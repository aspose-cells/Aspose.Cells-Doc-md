---
title: Définir la propriété DefaultFont des options PdfSaveOptions et ImageOrPrintOptions pour avoir priorité avec Node.js via C++
linktitle: Définir la propriété DefaultFont de PdfSaveOptions et ImageOrPrintOptions afin de lui donner la priorité
type: docs
weight: 30
url: /fr/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Découvrez comment définir la propriété DefaultFont de PdfSaveOptions et ImageOrPrintOptions en utilisant Aspose.Cells for Node.js via C++. Assurez un rendu correct des polices lorsqu elles sont manquantes.
---

## **Scénarios d'utilisation possibles**

En définissant la propriété **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/), vous pourriez vous attendre à ce que l'enregistrement en PDF ou en image définit cette police par défaut pour tout le texte dans un classeur qui a une police manquante (non installée).

Généralement, lors de l'enregistrement en PDF ou en image, Aspose.Cells for Node.js via C++ tentera d'abord de définir la police par défaut du classeur (c'est-à-dire `Workbook.DefaultStyle.Font`). Si la police par défaut du classeur ne peut toujours pas afficher/rendre le texte correctement, Aspose.Cells essaiera de rendre avec la police mentionnée dans l'attribut DefaultFont dans [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/).

Pour répondre à votre attente, nous avons une propriété booléenne nommée "**CheckWorkbookDefaultFont**" dans [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/). Vous pouvez la définir sur **false** pour désactiver l'essai de la police par défaut du classeur ou laisser la définition de **DefaultFont** dans [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) avoir la priorité.

## **Définir la propriété DefaultFont de PdfSaveOptions/ImageOrPrintOptions**

Le code d'exemple suivant ouvre un fichier Excel. La cellule A1 (dans la première feuille) a un texte défini sur "Christmas Time Font text". Le nom de la police est "Christmas Time Personal Use" qui n'est pas installée sur la machine. Nous définissons l'attribut **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) à "Times New Roman". Nous configurons également la propriété booléenne **CheckWorkbookDefaultFont** à **"false"** pour garantir que le texte de la cellule A1 est rendu avec la police "Times New Roman" et ne doit pas utiliser la police par défaut du classeur ("Calibri" dans ce cas). Le code rend la première feuille en formats PNG et TIFF. Finalement, il la rend en format PDF.

{{% alert color="primary" %}}

La valeur par défaut de l'attribut **CheckWorkbookDefaultFont** est **true**.

{{% /alert %}}

Il s'agit de la capture d'écran du [fichier modèle](49446913.xlsx) utilisé dans le code exemple.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Voici l’image PNG de sortie après avoir réglé la propriété [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) à "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Voir l’image [TIFF](48496672.tiff) de sortie après avoir réglé la propriété [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) à "Times New Roman".

Voir le fichier [PDF](48496673.pdf) après avoir réglé la propriété [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) à "Times New Roman".

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open an Excel file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx"));

// Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const imgOpt = new AsposeCells.ImageOrPrintOptions();
imgOpt.setImageType(AsposeCells.ImageType.Png);
imgOpt.setCheckWorkbookDefaultFont(false);
imgOpt.setDefaultFont("Times New Roman");
const sr = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imgOpt);
sr.toImage(0, path.join(outputDir, "out1_imagePNG.png"));

// Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
imgOpt.setImageType(AsposeCells.ImageType.Tiff);
const wr = new AsposeCells.WorkbookRender(workbook, imgOpt);
wr.toImage(path.join(outputDir, "out1_imageTIFF.tiff"));

// Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setDefaultFont("Times New Roman");
saveOptions.setCheckWorkbookDefaultFont(false);
workbook.save(path.join(outputDir, "out1_pdf.pdf"), saveOptions);
```
