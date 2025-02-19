---
title: Find if the cell value starts with single quote mark with Node.js via C++
type: docs
weight: 270
url: /nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Learn how to find if the cell value starts with a single quote mark through the Aspose.Cells for Node.js via C++ API.
keywords: Find cell value starts with a single quote mark Node.js via C++, Search cell value starts with a single quote mark Node.js via C++
---

{{% alert color="primary" %}}

Aspose.Cells now provides the [**Style.quotePrefix**](https://reference.aspose.com/cells/nodejs-cpp/style/#quotePrefix) property to find if the cell value starts with a single quote mark. Before this property, there was no way to distinguish between strings like sample and 'sample etc.

{{% /alert %}}

The following sample code explains that the strings like sample and 'sample cannot be differentiated with [**Cell.stringValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#stringValue) property. Therefore we must use [**Style.quotePrefix**](https://reference.aspose.com/cells/nodejs-cpp/style/#quotePrefix) property to distinguish them.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const wb = new AsposeCells.Workbook();

// Create worksheet
const sheet = wb.getWorksheets().get(0);

// Access cell A1 and A2
const a1 = sheet.getCells().get("A1");
const a2 = sheet.getCells().get("A2");

// Add sample in A1 and sample with quote prefix in A2
a1.putValue("sample");
a2.putValue("'sample");

// Print their string values, A1 and A2 both are same
console.log("String value of A1: " + a1.getStringValue());
console.log("String value of A2: " + a2.getStringValue());

// Access styles of A1 and A2
const s1 = a1.getStyle();
const s2 = a2.getStyle();

console.log();

// Check if A1 and A2 has a quote prefix
console.log("A1 has a quote prefix: " + s1.getQuotePrefix());
console.log("A2 has a quote prefix: " + s2.getQuotePrefix());
```
