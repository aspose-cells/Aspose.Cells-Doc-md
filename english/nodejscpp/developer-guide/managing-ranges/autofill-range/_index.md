---
title: AutoFill range of Excel file with Node.js via C++
linktitle: AutoFill Range
type: docs
weight: 105
url: /nodejs-cpp/autofill-ranges/
description: Learn how to perform an autofill operation in a specified range of an Excel file using Aspose.Cells for Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Perform an autofill in the specified range in Excel**

In Excel, select a range, move the mouse to the bottom‑right, and drag the “plus” to autofill data.

## **Auto Fill Ranges with Aspose.Cells for Node.js via C++**

The following example shows how to perform an AutoFill operation on a range, and here is the sample file that can be downloaded for testing this feature:

[range_autofill.xlsx](range_autofill.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "range_autofill.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("C3:C4");
const dest = cells.createRange("C5:C10");
// AutoFill
src.autoFill(dest, AsposeCells.AutoFillType.Series);
// Save the Workbook
workbook.save("range_autofill_result.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}
