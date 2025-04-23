---
title: Sammanfoga eller ogöra cellområde med Node.js via C++
linktitle: Slå samman eller dela upp cellintervall
type: docs
weight: 190
url: /sv/nodejs-cpp/merge-or-unmerge-range-of-cells/
description: Sammanfoga och ogöra celler i ett område i Excel med Node.js via C++ kod.
keywords: Node.js sammanfogar och ogör celler i ett område, Node.js sammanfogar och ogör celler i område, sammanfoga och ogöra celler i område med Node.js, sammanfoga och ogöra celler i område med Node.js, sammanfoga och ogöra celler i Excel med Node.js, sammanfoga och ogöra celler i Excel med Node.js, Node.js sammanfogar och ogör celler i Excel, Node.js sammanfoga celler i Excel, Node.js ogör celler i Excel, sammanfoga celler i område med Node.js
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att slå samman eller dela upp ett cellintervall. Aspose.Cells tillhandahåller [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) och [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--) metoder för detta ändamål. Denna artikel förklarar hur man slår samman ett cellintervall till en enda cell.

{{% /alert %}}

## **Exempel**

Följande exempel skapar först ett område - A1:D4 - och fusionerar sedan cellerna i området till en enda cell med hjälp av [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--)-metoden. På liknande sätt kan du dela upp celler genom att skapa ett område och använda [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--)-metoden.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range
const range = worksheet.getCells().createRange("A1:D4");

// Merge range into a single cell
range.merge();

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xlsx"));
```
