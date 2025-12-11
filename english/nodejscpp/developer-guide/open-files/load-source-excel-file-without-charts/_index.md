---
title: Load Source Excel File Without Charts with Node.js via C++
linktitle: Load Source Excel File Without Charts
type: docs
weight: 420
url: /nodejs-cpp/load-source-excel-file-without-charts/
description: Learn how to load an Excel file without charts using Aspose.Cells for Node.js via C++. 
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells allows you to load your Excel file without charts. Please use [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) property for this purpose.

{{% /alert %}}

## **Load Spreadsheet Without Charts**

The following sample code loads the sample Excel file without charts and saves it as a PDF.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the load options and filter the data
const options = new AsposeCells.LoadOptions();

// Include everything except charts
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Load the workbook with specified load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xlsx"), options);

// Save the workbook in PDF format
workbook.save(path.join(dataDir, "ResultWithoutChart.pdf"), AsposeCells.SaveFormat.Pdf);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
