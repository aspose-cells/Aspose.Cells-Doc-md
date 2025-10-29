---
title: Ajouter des cellules à la fenêtre de surveillance des formules de Microsoft Excel avec Node.js via C++
linktitle: Ajouter des cellules à la fenêtre de surveillance des formules Microsoft Excel
description: Comment utiliser la bibliothèque Aspose.Cells pour ajouter des cellules à la fenêtre de surveillance des formules dans Excel en utilisant Node.js via C++. En chargeant un fichier Excel existant ou en créant un nouveau, nous pouvons manipuler ses cellules et définir des formules. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, fenêtre de surveillance des formules, cellules, ajout, Node.js via C++
type: docs
weight: 60
url: /fr/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Scénarios d'utilisation possibles**

La fenêtre de surveillance dans Microsoft Excel est un outil pratique pour suivre les valeurs des cellules et leurs formules dans une fenêtre. Vous pouvez ouvrir la *Fenêtre de surveillance* en utilisant Microsoft Excel en cliquant sur *Formules > Surveillance > Fenêtre*. Elle comporte un bouton *Ajouter une surveillance* qui permet d'ajouter des cellules pour inspection. De même, vous pouvez utiliser la méthode [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cellwatchcollection/#add-number-number-) pour ajouter des cellules à la *Fenêtre de surveillance* via l'API Aspose.Cells.

## **Ajouter des cellules à la fenêtre de surveillance des formules Microsoft Excel**

Le code d'exemple suivant définit la formule des cellules C1 et E1 et les ajoute toutes deux à la Fenêtre de surveillance. Ensuite, il enregistre le classeur en tant que [fichier Excel de sortie](67338481.xlsx). Si vous ouvrez le fichier Excel de sortie et visualisez la *Fenêtre de surveillance*, vous verrez les deux cellules comme illustré dans cette capture d'écran.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Put some integer values in cell A1 and A2.
ws.getCells().get("A1").putValue(10);
ws.getCells().get("A2").putValue(30);

// Access cell C1 and set its formula.
const c1 = ws.getCells().get("C1");
c1.setFormula("=Sum(A1,A2)");

// Add cell C1 into cell watches by name.
ws.getCellWatches().add(c1.getName());

// Access cell E1 and set its formula.
const e1 = ws.getCells().get("E1");
e1.setFormula("=A2*A1");

// Add cell E1 into cell watches by its row and column indices.
ws.getCellWatches().add(e1.getRow(), e1.getColumn());

// Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
