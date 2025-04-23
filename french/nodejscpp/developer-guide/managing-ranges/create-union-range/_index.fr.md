---  
title: Créez une plage d union avec Node.js via C++  
linktitle: Créer une plage union  
type: docs  
weight: 360  
url: /fr/nodejs-cpp/create-union-range/  
description: Apprenez comment créer une plage d union en utilisant Aspose.Cells for Node.js via C++.  
keywords: Créer une plage d union Node.js via C++, Plage d union Aspose.Cells Node.js, Collection de feuilles de calcul créer une plage d union Node.js  
---  

## **Créer l'union de la plage**  
Aspose.Cells offre la possibilité de créer une plage d'union en utilisant la méthode [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-). La méthode [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-) accepte deux paramètres, l'adresse pour créer la plage d'union et l'indice de la feuille de calcul. Elle retourne un objet [UnionRange](https://reference.aspose.com/cells/nodejs-cpp/unionrange).  

Le code ci-dessous illustre la création d'une plage d'union en utilisant la méthode [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-). Le fichier de sortie généré par le code est joint à titre de référence.  

- [Fichier de sortie](106364952.xlsx)  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create union range
const unionRange = workbook.getWorksheets().createUnionRange("sheet1!A1:A10,sheet1!C1:C10", 0);

// Put value "ABCD" in the range
unionRange.setValue("ABCD");

// Save the output workbook.
workbook.save("CreateUnionRange_out.xlsx");
```  

