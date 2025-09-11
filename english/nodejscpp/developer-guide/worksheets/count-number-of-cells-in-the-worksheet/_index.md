---
title: Count number of cells in the Worksheet with Node.js via C++
linktitle: Count number of cells in the Worksheet
type: docs
weight: 110
url: /nodejs-cpp/count-number-of-cells-in-the-worksheet/
description: Learn how to programmatically count the number of cells in an Excel worksheet using Aspose.Cells for Node.js via C++.
keywords: count number of excel worksheet cells Node.js via C++, excel worksheet cells Node.js via C++
---

You may count the number of cells in the worksheet by using the [**Cells.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCount--) or [**Cells.getCountLarge()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCountLarge--) properties as shown in the code example given below.

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