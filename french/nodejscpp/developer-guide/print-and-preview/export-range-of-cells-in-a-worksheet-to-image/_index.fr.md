---  
title: Exporter une plage de cellules d une feuille de calcul vers une image avec Node.js via C++  
linktitle: Exporter la plage de cellules dans une feuille de calcul en tant qu image  
type: docs  
weight: 60  
url: /fr/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/  
---  

## **Scénarios d'utilisation possibles**  

Vous pouvez créer une image d'une feuille de calcul à l'aide de Aspose.Cells for Node.js via C++. Cependant, parfois, il est nécessaire d'exporter uniquement une plage de cellules d'une feuille de calcul vers une image. Cet article explique comment procéder.  

## **Exporter une plage de cellules d'une feuille de calcul vers une image**  

Pour prendre une image d'une plage, définissez la zone d'impression sur la plage souhaitée, puis réglez toutes les marges à 0. Configurez également [**ImageOrPrintOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOnePagePerSheet--) sur **true**. Le code suivant capture une image de la plage D8:G16. Ci-dessous, une capture d'écran du [fichier Excel d'exemple](47153160.xlsx) utilisé dans le code. Vous pouvez essayer le code avec n'importe quel fichier Excel.  

## **Capture d'écran du fichier Excel d'exemple et de son image exportée**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

L'exécution du code crée une image de la plage D8:G16 seulement.  

**![todo:image_alt_text](Output-Image.png)**  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportRangeOfCellsInWorksheetToImage.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area with your desired range
worksheet.getPageSetup().setPrintArea("D8:G16");

// Set all margins as 0
worksheet.getPageSetup().setLeftMargin(0);
worksheet.getPageSetup().setRightMargin(0);
worksheet.getPageSetup().setTopMargin(0);
worksheet.getPageSetup().setBottomMargin(0);

// Set OnePagePerSheet option as true
const options = new AsposeCells.ImageOrPrintOptions();
options.setOnePagePerSheet(true);
options.setImageType(AsposeCells.ImageType.Jpeg);
options.setHorizontalResolution(200);
options.setVerticalResolution(200);

// Take the image of your worksheet
const sr = new AsposeCells.SheetRender(worksheet, options);
sr.toImage(0, path.join(outputDir, "outputExportRangeOfCellsInWorksheetToImage.jpg"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
