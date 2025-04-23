---
title: Compter le nombre de cellules dans la feuille de calcul avec Node.js via C++
linktitle: Compter le nombre de cellules dans la feuille de calcul
type: docs
weight: 110
url: /fr/nodejs-cpp/count-number-of-cells-in-the-worksheet/
description: Apprenez à compter de manière programmatique le nombre de cellules dans une feuille Excel en utilisant Aspose.Cells for Node.js via C++.
keywords: compter le nombre de cellules de feuilles Excel Node.js via C++, cellules de feuilles Excel Node.js via C++
---

Vous pouvez compter le nombre de cellules dans la feuille de calcul en utilisant les propriétés [**Cells.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCount--) ou [**Cells.getCountLarge()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCountLarge--) comme indiqué dans l'exemple de code ci-dessous.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const filePath = path.join(sourceDir, "BookWithSomeData.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Print number of cells in the Worksheet
console.log("Number of Cells: " + worksheet.getCells().getCount());

// If the number of cells is greater than 2147483647, use CountLarge
console.log("Number of Cells (CountLarge): " + worksheet.getCells().getCountLarge());
```
