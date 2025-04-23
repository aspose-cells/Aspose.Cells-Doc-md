---
title: AutoFyll område av Excel fil med Node.js via C++
linktitle: Autofyllningsområde
type: docs
weight: 105
url: /sv/nodejs-cpp/autofill-ranges/
description: Lär dig hur du gör en autofylloperation i ett angivet område av en Excel fil med Aspose.Cells for Node.js via C++.
---

## **Utför en autofyllning i det angivna området i Excel**

I Excel, välj ett område, flytta musen till högra nederkanten, och dra "plus" för att autofyll data.

## **AutoFyll områden med Aspose.Cells for Node.js via C++**

Nedan visas hur man utför en AutoFill-operation på ett område, och här är exempel-filen som kan laddas ner för att testa denna funktion:

[range_autofill.xlsx](range_autofill.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "range_autofill.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("C3:C4");
const dest = cells.createRange("C5:C10");
// AutoFill
src.autoFill(dest, AsposeCells.AutoFillType.Series);
// Save the Workbook
workbook.save("range_autofill_result.xlsx");
```

