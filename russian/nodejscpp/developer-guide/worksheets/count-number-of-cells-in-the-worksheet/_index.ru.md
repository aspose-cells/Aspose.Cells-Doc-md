---
title: Подсчет количества ячеек в листе с помощью Node.js через C++
linktitle: Посчитать количество ячеек в листе
type: docs
weight: 110
url: /ru/nodejs-cpp/count-number-of-cells-in-the-worksheet/
description: Научитесь программно подсчитывать количество ячеек в Excel листе с помощью Aspose.Cells for Node.js via C++.
keywords: подсчет количества ячеек Excel листа с помощью Node.js через C++, ячейки Excel листа Node.js через C++
---

Вы можете подсчитать количество ячеек в листе, используя свойства [**Cells.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCount--) или [**Cells.getCountLarge()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCountLarge--), как показано в приведенном ниже примере кода.

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
