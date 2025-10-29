---
title: عد خلايا ورقة العمل باستخدام Node.js عبر C++
linktitle: عدد خلايا ورقة العمل
type: docs
weight: 110
url: /ar/nodejs-cpp/count-number-of-cells-in-the-worksheet/
description: تعلم كيفية عد خلايا ورقة إكسل برمجياً باستخدام Aspose.Cells for Node.js via C++.
keywords: عد عدد خلايا ورقة العمل في إكسل باستخدام Node.js عبر C++، خلايا ورقة إكسل باستخدام Node.js عبر C++
---

يمكنك إحصاء عدد الخلايا في الورقة باستخدام الخصائص [**Cells.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCount--) أو [**Cells.getCountLarge()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCountLarge--) كما هو موضح في مثال الكود أدناه.

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
