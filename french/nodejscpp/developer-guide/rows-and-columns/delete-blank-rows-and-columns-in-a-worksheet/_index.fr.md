---
title: Supprimer les lignes et colonnes vides dans une feuille de calcul avec Node.js via C++
linktitle: Supprimer les lignes et colonnes vides dans une feuille de calcul
type: docs
weight: 300
url: /fr/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Apprenez comment supprimer toutes les lignes et colonnes vides d’une feuille de calcul en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Il est possible de supprimer toutes les lignes et colonnes vides d'une feuille de calcul. Cela est utile, par exemple, lors de la génération d'un fichier PDF à partir d'un fichier Microsoft Excel et que vous souhaitez ne convertir que les lignes et colonnes contenant des données ou des objets liés.

Utilisez les méthodes Aspose.Cells suivantes pour supprimer les lignes et colonnes vides :

1. Pour supprimer les lignes vides, utilisez la méthode [**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankRows--). Veuillez noter que, pour les lignes vides qui seront supprimées, il est non seulement nécessaire que [**Row.isBlank()**](https://reference.aspose.com/cells/nodejs-cpp/row/#isBlank--) soit vrai, mais il ne doit également y avoir aucun commentaire visible défini pour une quelconque cellule de ces lignes, et aucun tableau croisé dynamique dont la plage intersecte avec elles.
2. Pour supprimer des colonnes vides, utilisez la méthode [**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankColumns--).

{{% /alert %}}

## Code Node.js pour supprimer les lignes vides

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(filePath);

// Create a Worksheets object with reference to
// The sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Rows from the worksheet
sheet.getCells().deleteBlankRows();

// Save the excel file.
wb.save(path.join(dataDir, "mybook.out.xlsx"));
```

## Code Node.js pour supprimer les colonnes vides

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an existing excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleInput.xlsx"));

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = workbook.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Columns from the worksheet
sheet.getCells().deleteBlankColumns();

// Save the excel file.
workbook.save(path.join(dataDir, "mybook.out.xlsx"));
```
