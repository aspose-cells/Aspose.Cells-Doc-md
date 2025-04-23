---
title: Insérer un Sparkline avec Node.js via C++
linktitle: Minigraphiques
type: docs
weight: 160
url: /fr/nodejs-cpp/creating-sparklines/
description: Créer un sparkline pour Excel en utilisant Aspose.Cells for Node.js via C++.
---

## **Insérer un sparkline**
{{% alert color="primary" %}} 

Un Sparkline est un petit graphique dans une cellule de feuille de calcul qui offre une représentation visuelle des données. Utilisez les sparklines pour montrer les tendances dans une série de valeurs, telles que des augmentations ou diminutions saisonnières, des cycles économiques, ou pour mettre en évidence les valeurs maximales et minimales. Positionnez un sparkline près de ses données pour un impact optimal. Il existe trois types de Sparkline : Ligne, Colonne et Empilé.

{{% /alert %}} 

Il est simple de créer un sparkline avec Aspose.Cells for Node.js via C++ avec les codes d'exemple suivants :



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);
const sheet = book.getWorksheets().get(0);

sheet.getCells().get("A1").putValue(5);
sheet.getCells().get("B1").putValue(2);
sheet.getCells().get("C1").putValue(1);
sheet.getCells().get("D1").putValue(3);

// Define the CellArea
const ca = AsposeCells.CellArea.createCellArea(0, 4, 0, 4);

const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, `${sheet.getName()}!A1:D1`, false, ca);

const group = sheet.getSparklineGroups().get(idx);
group.getSparklines().add(`${sheet.getName()}!A1:D1`, 0, 4);

// Customize Sparklines

// Create CellsColor
const clr = book.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Set the high points are colored green and the low points are colored red
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.getHighPointColor().setColor(AsposeCells.Color.Green);
group.getLowPointColor().setColor(AsposeCells.Color.Red);
// Set line weight 
group.setLineWeight(1.0);

// Saving the Excel file
book.save(path.join(dataDir, "output.xlsx"));
```

## **Sujets avancés**
- [Utiliser les sparklines et les paramètres de format 3D](/cells/fr/nodejs-cpp/using-sparklines-and-settings-3d-format/)
