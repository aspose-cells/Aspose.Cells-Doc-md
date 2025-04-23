---
title: Laden der Quelldatei ohne Diagramme mit Node.js über C++
linktitle: Quell Excel Datei ohne Diagramme laden
type: docs
weight: 420
url: /de/nodejs-cpp/load-source-excel-file-without-charts/
description: Erfahren Sie, wie Sie eine Excel Datei ohne Diagramme mit Aspose.Cells for Node.js via C++ laden. 
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, Ihre Excel-Datei ohne Diagramme zu laden. Bitte verwenden Sie die Eigenschaft [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) dafür.

{{% /alert %}}

## **Laden von Tabellenkalkulationen ohne Diagramme**

Der folgende Beispielcode lädt die Beispiel-Excel-Datei ohne Diagramme und speichert sie im PDF-Format.

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
