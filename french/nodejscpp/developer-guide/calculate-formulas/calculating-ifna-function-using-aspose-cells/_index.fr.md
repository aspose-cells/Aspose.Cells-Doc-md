---
title: Calcul de la fonction IFNA en utilisant Aspose.Cells for Node.js via C++
description: Comment calculer les fonctions IFNA en utilisant la bibliothèque Aspose.Cells pour Node.js via C++. Chargez un fichier Excel existant ou créez en un nouveau, et calculez la fonction IFNA pour obtenir le résultat. Enfin, enregistrez le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, fonctions IFNA, calculs Node.js via C++
type: docs
weight: 40
url: /fr/nodejs-cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells prend en charge le calcul de la fonction Excel IFNA. La fonction IFNA retourne la valeur que vous spécifiez si la formule renvoie l’erreur #N/A ; sinon, elle retourne le résultat de la formule.

{{% /alert %}} 
## **Calcul de la fonction IFNA en utilisant Aspose.Cells for Node.js via C++**
Le code d'exemple suivant illustre le calcul de la fonction IFNA en utilisant Aspose.Cells for Node.js via C++.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create new workbook
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add data for VLOOKUP
worksheet.getCells().get("A1").putValue("Apple");
worksheet.getCells().get("A2").putValue("Orange");
worksheet.getCells().get("A3").putValue("Banana");

// Access cell A5 and A6
const cellA5 = worksheet.getCells().get("A5");
const cellA6 = worksheet.getCells().get("A6");

// Assign IFNA formula to A5 and A6
cellA5.setFormula('=IFNA(VLOOKUP("Pear",$A$1:$A$3,1,0),"Not found")');
cellA6.setFormula('=IFNA(VLOOKUP("Orange",$A$1:$A$3,1,0),"Not found")');

// Calculate the formula of workbook
workbook.calculateFormula();

// Print the values of A5 and A6
console.log(cellA5.getStringValue());
console.log(cellA6.getStringValue());
```
## **Sortie console**
Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight javascript >}}
 Not found

Orange
{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
