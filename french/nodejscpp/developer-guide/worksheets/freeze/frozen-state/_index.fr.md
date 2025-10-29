---
title: Comment vérifier l’état figé sans Excel en utilisant Node.js via C++
linktitle: État figé
type: docs
weight: 190
url: /fr/nodejs-cpp/how-to-check-frozen-state-of-excel-worksheet
description: Dans cet article, vous apprendrez comment vérifier l’état figé d’une feuille Excel de manière programmatique en utilisant Node.js avec la bibliothèque C++.

---

## **Introduction**

Dans cet article, nous apprendrons comment vérifier l’état figé d’une feuille Excel de manière programmatique. Nous pouvons simplement déterminer si la feuille est figée ou fractionnée dans MS Excel. Mais existe-t-il une méthode pour savoir si elle est figée ou fractionnée avec Node.js ? Nous pouvons le faire simplement avec Aspose.Cells for Node.js via C++.

## **Les volets de fenêtre sont-ils gelés**
Avec Aspose.Cells for Node.js via C++, nous pouvons vérifier si la fenêtre est figée et combien de lignes et colonnes sont verrouillées.

Veuillez utiliser la propriété [**Worksheet.getPaneState()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPaneState--) pour vérifier l’état des volets de la fenêtre et obtenir les lignes et colonnes verrouillées avec la méthode [**Worksheet.getFreezedPanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFreezedPanes--).
1. Construisez un classeur pour ouvrir le fichier.
2. Vérifiez si la feuille de calcul est gelée.
3. Obtenez les lignes et colonnes verrouillées.

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Frozen.xlsx");

// Loads the workbook which contains frozen panes
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Check whether worksheet is frozen.
if (sheet.getPaneState() === AsposeCells.PaneStateType.Frozen || sheet.getPaneState() === AsposeCells.PaneStateType.FrozenSplit) {
let row, column, rows, columns;
// Gets locked rows and columns.
sheet.getFreezedPanes().forEach((value) => {
row = value[0];
column = value[1];
rows = value[2];
columns = value[3];
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
