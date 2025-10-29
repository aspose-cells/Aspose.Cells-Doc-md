---  
title: Geler la(les) première(s) colonne(s) de la feuille de calcul Excel avec Node.js via C++  
linktitle: Geler les colonnes  
type: docs  
weight: 190  
url: /fr/nodejs-cpp/how-to-freeze-columns-of-excel-worksheet  
description: Apprenez comment geler les colonnes de gauche des feuilles Excel de manière programmatique en utilisant Aspose.Cells for Node.js via C++.  
keywords: Fixer les colonnes de gauche, Fixer la ou les premières colonnes, Verrouiller la ou les colonnes  
---  

## **Introduction**  

Dans cet article, nous apprendrons comment geler la(les) colonne(s) de gauche. Lorsqu'une ligne contient une grande quantité de données, vous pourriez ne pas voir les colonnes de gauche lorsque vous faites défiler horizontalement la feuille. Vous pouvez geler et verrouiller la(les) première(s) colonne(s) afin de voir cette partie figée même lorsque le reste des données défile. Il est facile de voir les en-têtes dans les colonnes de gauche.  

## **Geler les colonnes dans Excel**  

**![Geler la ou les premières colonnes dans Excel](freeze-columns.png)**  

1. Si vous souhaitez fixer la ou les colonnes de gauche, sélectionnez d'abord la colonne sous la colonne qui doit être figée.
2. Cliquez sur Affichage > Fenêtres figées.
3. Dans le menu déroulant, cliquez sur Geler la première colonne.
4. Si vous faites défiler vers le bas, la première colonne reste toujours visible à gauche.

**![Colonne figée](frozen-columns.png)**  

Comme vous pouvez le voir, la première colonne est gelée, et cette colonne reste toujours verrouillée en haut de la vue lorsque vous faites défiler horizontalement.

Figer les colonnes vous permet de voir vos longues données sans aucune difficulté à suivre la première colonne.

## **Figer les colonnes avec Aspose.Cells for Node.js via C++**  
Il est simple de figer la ou les premières colonnes avec Aspose.Cells for Node.js via C++.  
Veuillez utiliser la méthode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) pour figer la ou les colonnes à la colonne sélectionnée.  
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Figez la première colonne avec la méthode Worksheet.freezePanes().
3. Enregistrez le fichier.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Freezing panes at the second column
workbook.getWorksheets().get(0).freezePanes("B1", 0, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

Fichier Excel source [exemple joint](Freeze.xlsx).  

{{< app/cells/assistant language="nodejs-cpp" >}}
