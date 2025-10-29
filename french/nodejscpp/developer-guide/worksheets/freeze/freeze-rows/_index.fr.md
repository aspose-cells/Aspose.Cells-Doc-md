---
title: Figer la ou les lignes supérieures de la feuille Excel avec Node.js via C++
linktitle: Geler les lignes
type: docs
weight: 190
url: /fr/nodejs-cpp/how-to-freeze-rows-of-excel-worksheet
description: Dans cet article, vous apprendrez comment figer les lignes supérieures des feuilles Excel de manière programmatique en utilisant la bibliothèque Node.js avec l’API C++.
keywords: Figer les lignes supérieures, Figer la ligne supérieure via Node.js avec C++.
---

## **Introduction**

Dans cet article, nous apprendrons comment figer la ou les lignes supérieures. Lorsque vous avez une grande quantité de données sous une en-tête commune, vous ne pouvez pas voir l'en-tête lorsque vous faites défiler la feuille vers le bas. Vous pouvez figer la ou les lignes supérieures pour voir cette partie figée même lorsque le reste des données est défilé. Vous pouvez facilement voir les en-têtes dans les lignes supérieures.

## **Figer les rangées dans Excel**

**![Figer la rangée(s) supérieure(s) dans Excel](Freeze-Rows.png)**

1. Si vous souhaitez figer la ou les premières lignes, sélectionnez d'abord la ligne sous celle qui doit être figée.
2. Cliquez sur Affichage > Fenêtres figées.
3. Dans le menu déroulant, cliquez sur Figer la rangée supérieure.
4. Si vous faites défiler vers le bas, la première ligne reste toujours en vue en haut.

**![Ligne figée](Frozen-Row.png)**

Comme vous pouvez le voir, la première ligne est figée ; la première ligne reste toujours en haut de la vue lorsque vous faites défiler vers le bas.

Figer les lignes vous permet de voir vos grandes données sans suivre l’étiquette de la ligne.

## **Figer les lignes avec Aspose.Cells for Node.js via C++**
Il est simple de figer la ou les lignes avec Aspose.Cells for Node.js via C++. 
Veuillez utiliser la méthode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) pour figer la ou les lignes à la ligne sélectionnée.
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.
2. Figer la première ligne avec la méthode Worksheet.freezePanes().
3. Enregistrez le fichier.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("A2", 1, 0);

// Saving the file
workbook.save("frozen.xlsx");
```

Fichier Excel source d'exemple joint [échantillon](../Freeze.xlsx).
{{< app/cells/assistant language="nodejs-cpp" >}}
