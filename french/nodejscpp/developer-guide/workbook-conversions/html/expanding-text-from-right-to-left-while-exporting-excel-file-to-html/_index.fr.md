---  
title: Extension du texte de droite à gauche lors de l exportation d un fichier Excel en HTML avec Node.js via C++  
linktitle: Expansion du texte de droite à gauche lors de l exportation d un fichier Excel vers HTML  
type: docs  
weight: 60  
url: /fr/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/  
---  

{{% alert color="primary" %}}  

Aspose.Cells prend désormais en charge l'expansion du texte de droite à gauche lors de l'exportation d'un fichier Excel vers HTML. Cette fonctionnalité a été implémentée depuis la version 8.9.0.0. Désormais, si votre fichier excel source contient un texte qui s'étend de droite à gauche, Aspose.Cells l'exportera correctement vers HTML.  

{{% /alert %}}  
## **Expansion du texte de droite à gauche lors de l'exportation d'un fichier Excel vers HTML**  
Le code d'exemple suivant convertit le [fichier excel d'exemple](5115502.xlsx) en HTML. Cette capture d'écran montre à quoi ressemble le fichier excel d'exemple dans Microsoft Excel 2013.  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)  

Cette capture d'écran montre la [sortie HTML générée avec une ancienne version](5115509).  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)  

Cette capture d'écran montre la [sortie HTML générée avec une nouvelle version](5115508).  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)  

Comme vous pouvez le voir dans les captures d'écran, la nouvelle version expand le texte aligné à droite vers la gauche correctement, tout comme Microsoft Excel.  


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load source excel file inside the workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save workbook in html format
wb.save(path.join(dataDir, `ExpandTextFromRightToLeft_out_${AsposeCells.CellsHelper.getVersion()}.html`), AsposeCells.SaveFormat.Html);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
