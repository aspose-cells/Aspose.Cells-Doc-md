---
title: Detect if Worksheet is Password Protected with Node.js via C++
linktitle: Detect if Worksheet is Password Protected
type: docs
weight: 360
url: /nodejs-cpp/detect-if-worksheet-is-password-protected/
description: Learn how to detect if a worksheet is password protected using Aspose.Cells for Node.js via C++. 
keywords: Detect Worksheet Password Protection Node.js via C++, Check if Worksheet is Password Protected Node.js via C++, Aspose.Cells for Node.js via C++
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

It is possible to protect the workbooks and worksheets separately. For instance, a spreadsheet may contain one or more worksheets that are password‑protected; however, the spreadsheet itself may or may not be protected. Aspose.Cells APIs provide the means to detect whether a given worksheet is password protected. This article demonstrates the usage of Aspose.Cells for Node.js via C++ API to achieve the same.

{{% /alert %}}

Aspose.Cells for Node.js via C++ exposes the **Protection.isProtectedWithPassword()** property to detect if a worksheet is password protected. The Boolean property returns **true** if the worksheet is password‑protected and **false** otherwise.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook and load a spreadsheet
const book = new AsposeCells.Workbook(filePath);

// Access the protected worksheet
const sheet = book.getWorksheets().get(0);

// Check if worksheet is password protected
if (sheet.getProtection().isProtectedWithPassword()) {
    console.log("Worksheet is password protected");
} else {
    console.log("Worksheet is not password protected");
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
