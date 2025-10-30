---
title: Räkna antalet celler i kalkylbladet med Node.js via C++
linktitle: Räkna antalet celler i kalkylbladet
type: docs
weight: 110
url: /sv/nodejs-cpp/count-number-of-cells-in-the-worksheet/
description: Lär dig hur man programmässigt räknar antalet celler i ett Excel kalkylblad med Aspose.Cells for Node.js via C++.
keywords: räknar antal celler i Excel kalkylblad Node.js via C++, excelkalkylbladceller Node.js via C++
---

Du kan räkna antalet celler i kalkylbladet genom att använda [**Cells.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCount--) eller [**Cells.getCountLarge()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCountLarge--) egenskaper som visas i kodexemplet nedan.

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
