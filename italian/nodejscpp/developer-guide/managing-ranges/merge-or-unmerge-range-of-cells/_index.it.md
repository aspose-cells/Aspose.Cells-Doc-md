---
title: Unisci o disunisci un intervallo di celle con Node.js tramite C++
linktitle: Unisci o separa un intervallo di celle
type: docs
weight: 190
url: /it/nodejs-cpp/merge-or-unmerge-range-of-cells/
description: Unisci e disunisci celle in un intervallo in Excel con Node.js tramite codice C++.
keywords: Unione e disunione di celle in un intervallo in Excel con Node.js, unisci e disunisci celle in intervallo con Node.js, unisci e disunisci celle con Node.js, unisci e disunisci celle in Excel usando Node.js, unisci e disunisci celle in Excel con Node.js, unisci e disunisci celle in Excel con Node.js, unisci e disunisci celle in Excel con Node.js, unisci celle in Excel con Node.js, disunisci celle in Excel con Node.js, unisci celle in intervallo con Node.js
---

{{% alert color="primary" %}}

Puoi utilizzare Aspose.Cells per unire o dividere un intervallo di celle. Aspose.Cells fornisce i metodi [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) e [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--) a questo scopo. Questo articolo spiega come unire un intervallo di celle in una singola cella.

{{% /alert %}}

## **Esempio**

Il seguente esempio di codice crea prima un intervallo - A1:D4 - quindi unisce le celle dell'intervallo in una singola cella usando il metodo [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--). Analogamente, puoi suddividere le celle creando un intervallo e chiamando il metodo [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range
const range = worksheet.getCells().createRange("A1:D4");

// Merge range into a single cell
range.merge();

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
