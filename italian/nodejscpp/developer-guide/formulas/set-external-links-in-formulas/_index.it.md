---
title: Imposta Link Esterni nelle Formule con Node.js via C++
linktitle: Imposta collegamenti esterni nelle formule
type: docs
weight: 20
url: /it/nodejs-cpp/set-external-links-in-formulas/
description: Impara come impostare link esterni nelle formule usando Aspose.Cells for Node.js via C++. 
keywords: Imposta link esterni nelle formule Node.js via C++, Includi file esterni nelle formule Node.js via C++ 
---

{{% alert color="primary" %}} 

A volte è necessario includere link a file esterni nelle formule, ad esempio, per valutare un valore di una cella o intervallo rispetto a questi. Aspose.Cells for Node.js via C++ offre questa funzionalità e questo documento spiega come utilizzarla.

{{% /alert %}} 

Il codice di esempio qui sotto mostra come includere file esterni nelle formule.



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
{{< app/cells/assistant language="nodejs-cpp" >}}
