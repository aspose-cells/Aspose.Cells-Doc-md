---  
title: Mise en forme du segment avec Node.js via C++  
linktitle: Formatage de la trancheuse  
type: docs  
weight: 20  
url: /fr/nodejs-cpp/formatting-slicer/  
---  

## **Scénarios d'utilisation possibles**  

Vous pouvez formater le segment dans Microsoft Excel en réglant son nombre de colonnes ou en choisissant son style, etc. Aspose.Cells for Node.js via C++ permet également de faire cela en utilisant les propriétés [**Slicer.getNumberOfColumns()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getNumberOfColumns--) et [**Slicer.getStyleType()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getStyleType--).  

## **Formatage d'un tronçonneur**  

Veuillez voir le code suivant, il charge le [fichier Excel d'exemple](67338473.xlsx) contenant une trancheuse. Il accède à la trancheuse et définit son nombre de colonnes et son type de style, puis l'enregistre en tant que [fichier Excel de sortie](67338474.xlsx). La capture d'écran montre à quoi ressemble la trancheuse après l'exécution du code d'exemple.  

![todo:image_alt_text](formatting-slicer_1.png)  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFormattingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Set the number of columns of the slicer.
slicer.setNumberOfColumns(2);

// Set the type of slicer style.
slicer.setStyleType(AsposeCells.SlicerStyleType.SlicerStyleLight6);

// Save the workbook in output XLSX format.
wb.save("outputFormattingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

