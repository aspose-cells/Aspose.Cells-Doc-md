---  
title: Créer une image transparente de la feuille Excel avec Node.js via C++  
linktitle: Create Transparent Image of Excel Worksheet  
type: docs  
weight: 170  
url: /fr/nodejs-cpp/create-transparent-image-of-excel-worksheet/  
description: Apprenez comment générer une image transparente d une feuille de calcul Excel en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Parfois, vous avez besoin de générer l'image de votre feuille de calcul en tant qu'image transparente. Vous souhaitez appliquer la transparence à toutes les cellules qui n'ont pas de couleur de remplissage. Aspose.Cells fournit la propriété [**ImageOrPrintOptions.getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--) pour appliquer la transparence à l'image de la feuille de calcul. Lorsque cette propriété est **fausse**, les cellules sans couleur de remplissage sont dessinées en blanc et lorsqu'elle est **true**, les cellules sans couleur de remplissage sont dessinées de manière transparente.  

{{% /alert %}}  

Dans l'image de la feuille de calcul suivante, la transparence n'a pas été appliquée. Les cellules sans couleur de remplissage sont dessinées en blanc.  

|**Sortie sans transparence : l'arrière-plan de la cellule est blanc**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|  

Alors que dans l'image de feuille de calcul suivante, la transparence a été appliquée. Les cellules sans couleur de remplissage sont transparentes.  

|**Sortie avec transparence activée**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|  

Le code d'exemple suivant génère une image transparente à partir d'une feuille de calcul Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook object from source file
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateTransparentImage.xlsx"));

// Apply different image or print options
const imgOption = new AsposeCells.ImageOrPrintOptions();
imgOption.setImageType(AsposeCells.ImageType.Png);
imgOption.setHorizontalResolution(200);
imgOption.setVerticalResolution(200);
imgOption.setOnePagePerSheet(true);

// Apply transparency to the output image
imgOption.setTransparent(true);

// Create image after applying image or print options
const sr = new AsposeCells.SheetRender(wb.getWorksheets().get(0), imgOption);
sr.toImage(0, path.join(outputDir, "outputCreateTransparentImage.png"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
