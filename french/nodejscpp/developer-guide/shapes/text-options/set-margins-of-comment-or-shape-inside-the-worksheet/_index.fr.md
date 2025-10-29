---  
title: Définir les marges des commentaires ou formes à l intérieur de la feuille de calcul avec Node.js via C++  
linktitle: Définir les marges du commentaire ou de la forme à l intérieur de la feuille de calcul  
type: docs  
weight: 1500  
url: /fr/nodejs-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Apprenez à définir les marges des commentaires ou des formes dans une feuille Excel en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Aspose.Cells vous permet de définir les marges de n'importe quelle forme ou commentaire en utilisant la propriété [**Shape.textBody.textAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/). Cette propriété retourne l'objet de la classe [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment) qui possède différentes propriétés, par exemple [**ShapeTextAlignment.getTopMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getTopMarginPt--), [**ShapeTextAlignment.getLeftMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getLeftMarginPt--), [**ShapeTextAlignment.getBottomMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getBottomMarginPt--), [**ShapeTextAlignment.getRightMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRightMarginPt--), etc., pouvant être utilisées pour définir les marges du haut, de la gauche, du bas et de la droite.  

## **Définir les marges du commentaire ou de la forme à l'intérieur de la feuille de calcul**  

Veuillez consulter le code d'échantillon suivant. Il charge le [fichier Excel d'échantillon](61767851.xlsx) qui contient deux formes. Le code accède aux formes une par une et définit leurs marges supérieure, gauche, inférieure et droite. Veuillez consulter le [fichier Excel de sortie](61767852.xlsx) généré par le code et la capture d'écran montrant l'effet du code sur le fichier Excel de sortie.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

const shapes = ws.getShapes();
for (let i = 0; i < shapes.getCount(); i++) {
const sh = shapes.get(i);
// Access the text alignment
const txtAlign = sh.getTextBody().getTextAlignment();

// Set auto margin false
txtAlign.setIsAutoMargin(false);

// Set the top, left, bottom and right margins
txtAlign.setTopMarginPt(10);
txtAlign.setLeftMarginPt(10);
txtAlign.setBottomMarginPt(10);
txtAlign.setRightMarginPt(10);
}

// Save the output Excel file
workbook.save("outputSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
