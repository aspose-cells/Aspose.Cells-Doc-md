---
title: Carica File Excel di Origine Senza Grafici con Node.js tramite C++
linktitle: Carica file Excel di origine senza grafici
type: docs
weight: 420
url: /it/nodejs-cpp/load-source-excel-file-without-charts/
description: Impara come caricare un file Excel senza grafici usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells consente di caricare il file Excel senza grafici. Si usi la proprietà [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) a questo scopo.

{{% /alert %}}

## **Carica foglio di calcolo senza grafici**

Il seguente esempio carica il file Excel di esempio senza grafici e lo salva in formato PDF in output.

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
