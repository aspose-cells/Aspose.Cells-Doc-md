---
title: Node.js ile C++ kullanarak İş Sayfasındaki hücre sayısını sayma
linktitle: Çalışma Sayfasındaki Hücrelerin Sayısını Say
type: docs
weight: 110
url: /tr/nodejs-cpp/count-number-of-cells-in-the-worksheet/
description: Aspose.Cells for Node.js via C++ kullanarak Excel iş sayfasında hücre sayısını programlı olarak saymayı öğrenin.
keywords: Node.js ile C++ kullanarak Excel iş sayfası hücre sayısı, C++ ile Node.js kullanarak hücre sayısı
---

Aşağıdaki örnekte verilen kod örneğinde gösterildiği gibi, çalışma sayfasındaki hücre sayısını [**Cells.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCount--) veya [**Cells.getCountLarge()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCountLarge--) özelliklerini kullanarak sayabilirsiniz.

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
