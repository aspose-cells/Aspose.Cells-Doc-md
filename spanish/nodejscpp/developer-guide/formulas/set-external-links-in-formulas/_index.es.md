---
title: Establecer enlaces externos en fórmulas con Node.js vía C++
linktitle: Establecer vínculos externos en fórmulas
type: docs
weight: 20
url: /es/nodejs-cpp/set-external-links-in-formulas/
description: Aprenda cómo establecer enlaces externos en fórmulas usando Aspose.Cells for Node.js via C++. 
keywords: Establecer enlaces externos en fórmulas Node.js vía C++, Incluir archivos externos en fórmulas Node.js vía C++ 
---

{{% alert color="primary" %}} 

A veces, es necesario incluir enlaces a archivos externos en fórmulas, por ejemplo, para evaluar un valor de celda o rango en relación a ellos. Aspose.Cells for Node.js via C++ proporciona esta función y este documento explica cómo usarla.

{{% /alert %}} 

El código de ejemplo a continuación muestra cómo incluir archivos externos en fórmulas.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get first Worksheet
const sheet = workbook.getWorksheets().get(0);

// Get Cells collection
const cells = sheet.getCells();

// Set formula with external links
cells.get("A1").setFormula(`=SUM('[${filePath}]Sheet1'!A2, '[${filePath}]Sheet1'!A4)`);

// Set formula with external links
cells.get("A2").setFormula(`='[${filePath}]Sheet1'!A8`);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
