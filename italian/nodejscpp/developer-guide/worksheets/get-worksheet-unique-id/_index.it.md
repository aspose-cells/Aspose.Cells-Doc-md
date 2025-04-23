---
title: Ottieni l’ID univoco del foglio di lavoro con Node.js tramite C++
linktitle: Ottieni l ID univoco del foglio di lavoro
type: docs
weight: 190
url: /it/nodejs-cpp/get-worksheet-unique-id/
description: Questo articolo mostra come ottenere l’ID univoco di un foglio di lavoro Excel usando la libreria Node.js e API C++ in modo programmatico.
keywords: ID univoco del foglio di lavoro Excel Node.js tramite C++, ID univoco del foglio di lavoro Node.js tramite C++
---

## **Ottieni l'ID univoco del foglio di lavoro**

Aspose.Cells for Node.js via C++ fornisce la capacità di ottenere l’ID univoco di un foglio di lavoro usando la proprietà [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--). Il seguente frammento di codice dimostra l’uso della proprietà [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--) per stampare l’ID univoco di un foglio di lavoro. Il frammento di codice seguente utilizza questo [file Excel di esempio](105480213.xlsx).

### Codice Sorgente

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
