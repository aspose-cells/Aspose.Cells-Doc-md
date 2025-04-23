---
title: Sätt externa länkar i formler med Node.js via C++
linktitle: Ange externa länkar i formler
type: docs
weight: 20
url: /sv/nodejs-cpp/set-external-links-in-formulas/
description: Lär dig hur du ställer in externa länkar i formler med Aspose.Cells for Node.js via C++. 
keywords: Sätt externa länkar i formler Node.js via C++, Inkludera externa filer i formler Node.js via C++ 
---

{{% alert color="primary" %}} 

Ibland är det nödvändigt att inkludera länkar till externa filer i formler, till exempel för att utvärdera ett cell- eller områdevärde mot dem. Aspose.Cells for Node.js via C++ tillhandahåller denna funktion och detta dokument förklarar hur man använder den.

{{% /alert %}} 

Det exempelkod nedan visar hur du inkluderar externa filer i formler.



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
