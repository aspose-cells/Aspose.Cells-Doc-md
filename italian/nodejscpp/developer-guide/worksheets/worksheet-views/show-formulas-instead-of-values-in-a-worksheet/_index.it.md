---
title: Mostra Formule invece di Valori in un Foglio di Lavoro con Node.js tramite C++
linktitle: Mostrare le Formule invece dei Valori in un Foglio di Lavoro
type: docs
weight: 20
url: /it/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Questo articolo fornisce codice di esempio per usare l API Node.js via C++ per mostrare programmaticamente formule anziché valori in un foglio di lavoro o foglio di calcolo Excel.
---

{{% alert color="primary" %}}

È possibile mostrare formule invece di valori calcolati in Microsoft Excel usando l'opzione **Mostra Formule** dalla scheda **Formule**. Quando vengono mostrate le formule, Microsoft Excel visualizza le formule nel foglio di lavoro. Puoi ottenere lo stesso risultato usando Aspose.Cells for Node.js via C++.

{{% /alert %}}

Aspose.Cells fornisce una proprietà [**Worksheet.getShowFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getShowFormulas--). Impostala a **true** per far sì che Microsoft Excel visualizzi le formule.

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

// Show formulas of the worksheet
worksheet.setShowFormulas(true);

// Save the workbook
workbook.save(path.join(dataDir, ".out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
