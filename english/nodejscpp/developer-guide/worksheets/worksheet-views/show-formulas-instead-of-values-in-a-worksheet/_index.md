---
title: Show Formulas Instead of Values in a Worksheet with Node.js via C++
linktitle: Show Formulas Instead of Values in a Worksheet
type: docs
weight: 20
url: /nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: This article provides sample code for using the Node.js API via C++ to programmatically display formulas rather than values in an Excel worksheet or spreadsheet.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

It is possible to show formulas instead of calculated values in Microsoft Excel using the **Show Formulas** option from the **Formulas** ribbon. When formulas are shown, Microsoft Excel displays formulas in the worksheet. You can achieve the same thing using Aspose.Cells for Node.js via C++.

{{% /alert %}}

Aspose.Cells provides a [**Worksheet.getShowFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getShowFormulas--) property. Set this to **true** to cause Microsoft Excel to display formulas.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Load the source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Show formulas for the worksheet
worksheet.setShowFormulas(true);

// Save the workbook
workbook.save(path.join(dataDir, ".out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
