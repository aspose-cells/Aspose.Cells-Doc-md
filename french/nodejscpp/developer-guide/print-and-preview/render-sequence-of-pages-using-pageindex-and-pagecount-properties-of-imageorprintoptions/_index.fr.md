---  
title: Rendre une séquence de pages en utilisant les propriétés PageIndex et PageCount d ImageOrPrintOptions avec Node.js via C++  
linktitle: Rendre une séquence de pages à l aide des propriétés PageIndex et PageCount de ImageOrPrintOptions  
type: docs  
weight: 110  
url: /fr/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/  
description: Apprenez comment rendre certaines pages spécifiques d un fichier Excel en images en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

 Vous pouvez rendre une séquence de pages de votre fichier Excel en images en utilisant Aspose.Cells avec les propriétés [**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--) et [**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--). Ces propriétés sont utiles lorsqu'il y a beaucoup de pages, par exemple des milliers de pages dans votre feuille de calcul, mais que vous souhaitez ne rendre que quelques-unes d'entre elles. Cela économisera non seulement le temps de traitement mais aussi la mémoire utilisée par le processus de rendu.  

## **Séquence de rendu des pages à l'aide des propriétés PageIndex et PageCount d'ImageOrPrintOptions**  

 Le code d'exemple ci-dessous charge le [fichier Excel d'exemple](55541781.xlsx) et ne rend que les pages 4, 5, 6 et 7 en utilisant les propriétés [**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--) et [**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--). Voici les pages rendues générées par le code.  

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|  
| :- | :- |  
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");
// Load the sample Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleImageOrPrintOptions_PageIndexPageCount.xlsx"));
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Specify image or print options
// We want to print pages 4, 5, 6, 7
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setPageIndex(3);
opts.setPageCount(4);
opts.setImageType(AsposeCells.ImageType.Png);
// Create sheet render object
const sheetRender = new AsposeCells.SheetRender(worksheet, opts);
// Print all the pages as images
for (let i = opts.getPageIndex(); i < sheetRender.getPageCount(); i++) {
sheetRender.toImage(i, path.join(outputDir, `outputImage-${i + 1}.png`));
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
