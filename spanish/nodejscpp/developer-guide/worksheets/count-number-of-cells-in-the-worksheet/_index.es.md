---
title: Contar el número de celdas en la hoja de cálculo con Node.js a través de C++
linktitle: Contar el número de celdas en la hoja de cálculo
type: docs
weight: 110
url: /es/nodejs-cpp/count-number-of-cells-in-the-worksheet/
description: Aprende a contar programáticamente el número de celdas en una hoja de cálculo de Excel usando Aspose.Cells for Node.js via C++.
keywords: contar número de celdas en hoja de cálculo de Excel Node.js a través de C++, contar celdas en hoja de cálculo de Excel Node.js a través de C++
---

Puede contar el número de celdas en la hoja de cálculo utilizando las propiedades [**Cells.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCount--) o [**Cells.getCountLarge()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCountLarge--) como se muestra en el ejemplo de código a continuación.

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
