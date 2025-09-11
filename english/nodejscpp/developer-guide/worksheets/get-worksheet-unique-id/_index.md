---
title: Get worksheet unique id with Node.js via C++
linktitle: Get worksheet unique id
type: docs
weight: 190
url: /nodejs-cpp/get-worksheet-unique-id/
description: This article shows how to get Excel worksheet unique id using Node.js library and C++ API programmatically.
keywords: unique id excel worksheet Node.js via C++, unique id worksheet Node.js via C++
---

## **Get worksheet unique id**

Aspose.Cells for Node.js via C++ provides the ability to get the unique id of a worksheet by using the [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--) property. The following code snippet demonstrates the use of the [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--) property to print the unique id of a worksheet. The following code snippet uses this [sample excel file](105480213.xlsx).

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