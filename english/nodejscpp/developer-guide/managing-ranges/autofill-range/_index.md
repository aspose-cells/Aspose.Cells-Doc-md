---
title: AutoFill range of Excel file with Node.js via C++
linktitle: AutoFill Range
type: docs
weight: 105
url: /nodejs-cpp/autofill-ranges/
description: Learn how to perform an autofill operation in a specified range of an Excel file using Aspose.Cells for Node.js via C++.
---

##  **Perform an autofill in the specified range in Excel**

In Excel, select a range, move the mouse to the right-bottom, and drag "plus" to autofill data.

## **Auto Fill Ranges with Aspose.Cells for Node.js via C++**

The following example shows how to perform an AutoFill operation on a Range, and here is the sample file which can be downloaded for testing this feature:

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

