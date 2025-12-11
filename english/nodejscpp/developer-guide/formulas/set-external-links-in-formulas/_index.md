---
title: Set External Links in Formulas with Node.js via C++
linktitle: Set External Links in Formulas
type: docs
weight: 20
url: /nodejs-cpp/set-external-links-in-formulas/
description: Learn how to set external links in formulas using Aspose.Cells for Node.js via C++. 
keywords: Set external links in formulas Node.js via C++, Include external files in formulas Node.js via C++ 
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Sometimes, it is necessary to include links to external files in formulas, for example, to evaluate a cell or range value against them. Aspose.Cells for Node.js via C++ provides this feature, and this document explains how to use it.

{{% /alert %}} 

The sample code below shows how to include external files in formulas.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Get the Cells collection.
const cells = sheet.getCells();

// Set formula with external links.
cells.get("A1").setFormula(`=SUM('[${filePath}]Sheet1'!A2, '[${filePath}]Sheet1'!A4)`);

// Set formula with external links.
cells.get("A2").setFormula(`='[${filePath}]Sheet1'!A8`);

// Save the workbook.
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
