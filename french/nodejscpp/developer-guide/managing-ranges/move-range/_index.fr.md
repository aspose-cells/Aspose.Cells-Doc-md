---  
title: Déplacer une plage de cellules dans une feuille de calcul avec Node.js via C++  
linktitle: Déplacer une plage de cellules dans une feuille de calcul  
type: docs  
weight: 370  
url: /fr/nodejs-cpp/move-range-of-cells-in-a-worksheet/  
description: Découvrez comment déplacer une plage de cellules dans une feuille de calcul en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Cet article montre comment déplacer une plage de cellules dans une feuille de calcul.  
{{% /alert %}}  

## **Déplacer une plage de cellules dans une feuille de calcul**  
Le code d'exemple utilise un fichier modèle pour démontrer la tâche.  

**Le fichier d'entrée**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)  

Veuillez consulter le fichier généré suivant avec la plage A1:B5 déplacée en C1:D5.  

**Le fichier de sortie**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Instantiate the workbook object. Open the Excel file
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells();

const range = cells.createRange("A1", "B5");
//move the range to right.
range.moveTo(0, 2);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
