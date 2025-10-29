---  
title: Insérer ou supprimer des lignes dans une feuille Excel avec Node.js via C++  
linktitle: Insérer ou supprimer des lignes dans une feuille de calcul Excel  
type: docs  
weight: 20  
url: /fr/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/  
description: Cet article fournit du code Node.js utilisant C++ pour insérer et supprimer des lignes dans une feuille Excel.  
keywords: node.js insérer ou supprimer des lignes dans une feuille Excel, node.js insérer ou supprimer des lignes dans Excel, node.js insérer des lignes dans Excel, node.js supprimer des lignes dans Excel, insérer ou supprimer des lignes dans une feuille Excel avec node.js, insérer ou supprimer des lignes dans Excel avec node.js, insérer des lignes dans Excel avec node.js, supprimer des lignes dans Excel avec node.js  
---  

{{% alert color="primary" %}}  

Lors de la création d'une nouvelle feuille ou de la manipulation d'une feuille existante, vous pourriez avoir besoin d'ajouter des lignes ou des colonnes supplémentaires pour accueillir les données. D'autres fois, vous pourriez avoir besoin de supprimer des lignes ou colonnes aux positions spécifiées dans la feuille.  

{{% /alert %}}  

Aspose.Cells for Node.js via C++ offre deux méthodes pour insérer et supprimer des lignes : [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) et [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-). Ces méthodes sont optimisées pour la performance et exécutent la tâche très rapidement.  

Pour insérer ou retirer un nombre de lignes, il est recommandé d'utiliser toujours les méthodes [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) et [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) au lieu des méthodes [**Cells.insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) ou [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRow-number-) dans une boucle.  

Aspose.Cells fonctionne de la même manière que Microsoft Excel. Lorsque des lignes ou des colonnes sont ajoutées, le contenu de la feuille de calcul est déplacé vers le bas et vers la droite. Lorsque des lignes ou des colonnes sont supprimées, le contenu de la feuille de calcul est déplacé vers le haut ou vers la gauche. Toutes les références dans les autres feuilles de calcul et cellules sont mises à jour lorsque des lignes sont ajoutées ou supprimées.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object.
// Load a template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));

// Get the first worksheet in the book.
const sheet = workbook.getWorksheets().get(0);

// Insert 10 rows at row index 2 (insertion starts at 3rd row)
sheet.getCells().insertRows(2, 10);

// Delete 5 rows now. (8th row - 12th row)
sheet.getCells().deleteRows(7, 5);

// Save the excel file.
workbook.save(path.join(dataDir, "out_book1.out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
