---
title: Remove Duplicate Rows in a Worksheet with Node.js via C++
linktitle: Remove duplicate rows in a Worksheet
type: docs
weight: 370
url: /nodejs-cpp/remove-duplicate-rows-in-a-worksheet/
description: Learn how to remove duplicate rows in a worksheet using Aspose.Cells for Node.js via C++ and select specific columns for duplication checks.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


Remove duplicate rows is one of Microsoft Excel's many useful features. It allows users to remove duplicate rows in a Worksheet, and you can pick which columns should be checked for duplicate information.

Aspose.Cells for Node.js via C++ provides the `Cells.removeDuplicates()` method for this purpose. You can also set `startRow`, `startColumn`, `endRow`, and `endColumn` to specify the range of columns to check for duplicates.

Following are the sample files which can be downloaded for testing this feature:

[removeduplicates.xlsx](removeduplicates.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "removeduplicates.xlsx");

// Create workbook
const book = new AsposeCells.Workbook(filePath);

// Remove Duplicate
book.getWorksheets().get(0).getCells().removeDuplicates(0, 0, 5, 3);

// Save result
book.save("removeduplicates-result.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
