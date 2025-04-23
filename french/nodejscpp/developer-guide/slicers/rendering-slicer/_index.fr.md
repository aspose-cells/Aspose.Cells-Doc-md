---  
title: Rendu de segment avec Node.js via C++  
linktitle: Rendu de la trancheuse  
type: docs  
weight: 40  
url: /fr/nodejs-cpp/rendering-slicer/  
---  

## **Scénarios d'utilisation possibles**  
Aspose.Cells for Node.js via C++ supporte le rendu des formes de segments. Si vous convertissez votre feuille de calcul en image ou enregistrez votre classeur au format PDF ou HTML, vous verrez que les segments sont rendus correctement.  

## **Rendu du tronçonneur**  
Le code d'exemple suivant charge le [fichier Excel d'exemple](67338479.xlsx) contenant un segment existant. Il convertit la feuille de calcul en une image en définissant la zone d'impression qui ne couvre que le segment. L'image résultante est [l'image de sortie](67338480.png) montrant le segment rendu. Comme vous pouvez le voir, le segment a été rendu correctement et ressemble à celui du fichier Excel d'exemple.  

![todo:image_alt_text](rendering-slicer_1)  
## **Code d'exemple**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderingSlicer.xlsx");

// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Set the print area because we want to render slicer only.
ws.getPageSetup().setPrintArea("B15:E25");

// Specify image or print options, set one page per sheet and only area to true.
const imgOpts = new AsposeCells.ImageOrPrintOptions();
imgOpts.setHorizontalResolution(200);
imgOpts.setVerticalResolution(200);
imgOpts.setImageType(AsposeCells.ImageType.Png);
imgOpts.setOnePagePerSheet(true);
imgOpts.setOnlyArea(true);

// Create sheet render object and render worksheet to image.
const sr = new AsposeCells.SheetRender(ws, imgOpts);
sr.toImage(0, "outputRenderingSlicer.png");
```  

