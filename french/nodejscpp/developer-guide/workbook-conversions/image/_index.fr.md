---  
title: Image avec Node.js via C++  
linktitle: Image  
type: docs  
weight: 300  
url: /fr/nodejs-cpp/convert-excel-to-image/  
---  

{{% alert color="primary" %}}  
Aspose.Cells vous permet d'exporter une feuille de calcul du classeur et de la convertir en différents formats. Cet article explique comment convertir une feuille de calcul en différents formats.  
{{% /alert %}}  

## Conversion du classeur en TIFF  

Un fichier Excel peut contenir plusieurs feuilles avec plusieurs pages. [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender) vous permet de convertir Excel en TIFF avec plusieurs pages. Vous pouvez également contrôler plusieurs options pour le TIFF, comme [ImageOrPrintOptions.getTiffCompression()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffCompression--), [ImageOrPrintOptions.getTiffColorDepth()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffColorDepth--), Résolution([ImageOrPrintOptions.getHorizontalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--), [ImageOrPrintOptions.getVerticalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--)).  

Le code ci-dessous montre comment convertir Excel en TIFF avec plusieurs pages. Les [fichier Excel source](workbook-to-tiff-with-mulitiple-pages.xlsx) et [image TIFF générée](workbook-to-tiff-with-mulitiple-pages.tiff) sont joints à titre de référence.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "workbook-to-tiff-with-mulitiple-pages.xlsx");

// Load the workbook
const wb = new AsposeCells.Workbook(filePath);

const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Tiff);

// Set resolution to 200
imgOptions.setHorizontalResolution(200);
imgOptions.setVerticalResolution(200);

// Set TIFF compression to LZW
imgOptions.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

const workbookRender = new AsposeCells.WorkbookRender(wb, imgOptions);
workbookRender.toImage("workbook-to-tiff-with-mulitiple-pages.tiff");
```  

## **Conversion de la feuille de calcul en image**  

Les feuilles de calcul contiennent des données que vous souhaitez analyser. Par exemple, une feuille de calcul peut contenir des paramètres, des totaux, des pourcentages, des exceptions et des calculs.  

En tant que développeur, vous pourriez avoir besoin de présenter des feuilles de calcul sous forme d'images. Par exemple, vous pourriez avoir besoin d'utiliser une image d'une feuille de calcul dans une application ou une page Web. Vous pourriez vouloir insérer une image dans un document Microsoft Word, un fichier PDF, une présentation PowerPoint ou tout autre type de document. En bref, vous voulez qu'une feuille de calcul soit rendue sous forme d'image afin de pouvoir l'utiliser ailleurs.  

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender)
[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions)
[**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender)

La classe [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) représente une feuille de calcul à rendre en images. Elle possède une méthode surcharge, [**SheetRender.toImage(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-string-), qui peut convertir une feuille de calcul en fichier(s) image avec différents attributs ou options. Elle retourne un objet Buffer et vous pouvez enregistrer une image sur le disque ou en flux. Plusieurs formats d'image sont supportés, par exemple BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.  

Le code suivant montre comment convertir une feuille de calcul dans un fichier Excel en fichier image.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) 
{
let path = "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif";
sr.toImage(j, path);
}
```  

{{% alert color="primary" %}}  
Actuellement, l'API de conversion des feuilles de calcul en images ne prend pas en charge les graphiques à bulles en 3D.  
{{% /alert %}}  

## **Conversion de feuille de calcul en SVG**  

SVG signifie Scalable Vector Graphics. SVG est une spécification basée sur les normes XML pour les graphiques vectoriels bidimensionnels. Il s'agit d'une norme ouverte qui est en cours de développement par le World Wide Web Consortium (W3C) depuis 1999.  

Aspose.Cells for Node.js via C++ a pu convertir des feuilles de calcul en images SVG depuis la version 7.1.0. Le code suivant montre comment convertir une feuille de calcul dans un fichier Excel en fichier image SVG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Put sample text in the first cell of the first worksheet in the newly created workbook
workbook.getWorksheets().get(0).getCells().get("A1").putValue("DEMO TEXT ON SHEET1");

// Add second worksheet in the workbook
workbook.getWorksheets().add(AsposeCells.SheetType.Worksheet);

// Set text in the first cell of the second sheet
workbook.getWorksheets().get(1).getCells().get("A1").putValue("DEMO TEXT ON SHEET2");

// Set currently active sheet index to 1 i.e. Sheet2
workbook.getWorksheets().setActiveSheetIndex(1);

// Save workbook to SVG. It shall render the active sheet only to SVG
workbook.save(path.join(outputDir, "ConvertWorksheetToSVG_out.svg"));
```  

## **Sujets avancés**  
- [Convertir un graphique Excel en image](/cells/fr/nodejs-cpp/convert-an-excel-chart-to-image/)  
- [Conversion de graphique en image au format SVG](/cells/fr/nodejs-cpp/converting-chart-to-image-in-svg-format/)  
- [Exportation du graphique en SVG avec l'attribut viewBox](/cells/fr/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/)  
- [Suivre la progression de la conversion d'Excel en TIFF](/cells/fr/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
