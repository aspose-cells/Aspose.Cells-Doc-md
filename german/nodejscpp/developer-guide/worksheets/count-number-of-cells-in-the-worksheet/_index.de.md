---
title: Anzahl der Zellen im Arbeitsblatt mit Node.js über C++ zählen
linktitle: Anzahl der Zellen im Arbeitsblatt zählen
type: docs
weight: 110
url: /de/nodejs-cpp/count-number-of-cells-in-the-worksheet/
description: Lernen Sie, wie Sie programmatisch die Anzahl der Zellen in einem Excel Arbeitsblatt mit Aspose.Cells for Node.js via C++ zählen.
keywords: Anzahl der Zellen im Excel Arbeitsblatt Node.js über C++, Excel Arbeitszellencount Node.js über C++
---

Sie können die Anzahl der Zellen im Arbeitsblatt mithilfe der [**Cells.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCount--) oder [**Cells.getCountLarge()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getCountLarge--) Eigenschaften wie im folgenden Codebeispiel gezeigt zählen.

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
