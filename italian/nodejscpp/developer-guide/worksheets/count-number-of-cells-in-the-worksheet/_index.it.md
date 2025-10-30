---
title: Conta il numero di celle nel Foglio di Lavoro con Node.js tramite C++
linktitle: Contare il numero di celle nel foglio di lavoro
type: docs
weight: 110
url: /it/nodejs-cpp/count-number-of-cells-in-the-worksheet/
description: Impara come contare programmaticamente il numero di celle in un foglio di Excel usando Aspose.Cells for Node.js via C++.
keywords: conta il numero di celle del foglio di lavoro Excel Node.js tramite C++, celle del foglio di lavoro Excel Node.js tramite C++
---

Puoi contare il numero di celle nel foglio di lavoro utilizzando le proprietà [**Cells.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCount--) o [**Cells.getCountLarge()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCountLarge--) come mostrato nell'esempio di codice riportato di seguito.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
