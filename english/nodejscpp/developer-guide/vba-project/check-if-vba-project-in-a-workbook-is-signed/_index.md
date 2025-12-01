---
title: Check if VBA project in a Workbook is Signed with Node.js via C++
linktitle: Check if VBA project in a Workbook is Signed
type: docs
weight: 70
url: /nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Learn how to check if a VBA project in a workbook is signed using Aspose.Cells for Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

You can check if your VBA project is signed or not using Microsoft Excel via **Tools > Digital Signatures...** menu command. Similarly, you can check it programmatically using Aspose.Cells [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--) property.

{{% /alert %}}

## **Check if VBA project in a Workbook is Signed in Node.js**

The following code loads the workbook and checks if its VBA project is signed using [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--) property. The property will return **true** if the project is signed otherwise it will return **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
console.log("VBA Project is Signed: " + workbook.getVbaProject().isSigned());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
