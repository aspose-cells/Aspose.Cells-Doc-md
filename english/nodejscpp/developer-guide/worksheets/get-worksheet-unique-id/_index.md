---
title: Get worksheet unique ID with Node.js via C++
linktitle: Get worksheet unique ID
type: docs
weight: 190
url: /nodejs-cpp/get-worksheet-unique-id/
description: This article shows how to get an Excel worksheet's unique ID using the Node.js library and C++ API programmatically.
keywords: unique ID Excel worksheet Node.js via C++, unique ID worksheet Node.js via C++
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Get worksheet unique ID**

Aspose.Cells for Node.js via C++ provides the ability to get the unique ID of a worksheet by using the [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--) property. The following code snippet demonstrates the use of the [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--) property to print the unique ID of a worksheet. The following code snippet uses this [sample Excel file](105480213.xlsx).

### Source Code

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Print Unique Id
console.log("Unique Id: " + worksheet.getUniqueId());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
