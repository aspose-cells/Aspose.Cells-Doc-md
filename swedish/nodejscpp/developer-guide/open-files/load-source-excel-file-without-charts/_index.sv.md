---
title: Ladda käll Excel fil utan diagram med Node.js via C++
linktitle: Ladda käll Excel fil utan diagram
type: docs
weight: 420
url: /sv/nodejs-cpp/load-source-excel-file-without-charts/
description: Lär dig hur du laddar en Excel fil utan diagram med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells låter dig ladda din Excel-fil utan diagram. Vänligen använd [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) för detta ändamål.

{{% /alert %}}

## **Ladda kalkylblad utan diagram**

Följande exempel laddar exempel-Excel-filen utan diagram och sparar den i PDF-format.

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
