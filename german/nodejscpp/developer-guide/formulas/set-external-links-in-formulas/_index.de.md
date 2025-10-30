---
title: Externe Links in Formeln mit Node.js über C++ festlegen
linktitle: Externe Links in Formeln setzen
type: docs
weight: 20
url: /de/nodejs-cpp/set-external-links-in-formulas/
description: Lernen Sie, wie man externe Links in Formeln mit Aspose.Cells for Node.js via C++ festlegt. 
keywords: Externe Links in Formeln mit Node.js über C++ festlegen, Externe Dateien in Formeln mit Node.js über C++ einbinden 
---

{{% alert color="primary" %}} 

 Manchmal ist es notwendig, Links zu externen Dateien in Formeln einzufügen, beispielsweise um einen Zellwert oder einen Bereich gegen sie zu bewerten. Aspose.Cells for Node.js via C++ bietet diese Funktion, und dieses Dokument erklärt, wie man sie verwendet.

{{% /alert %}} 

Der nachfolgende Beispielcode zeigt, wie externe Dateien in Formeln eingebunden werden.



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
