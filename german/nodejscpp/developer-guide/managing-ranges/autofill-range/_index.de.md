---
title: AutoAusfüllbereich einer Excel Datei mit Node.js über C++
linktitle: Autoausfüllbereich
type: docs
weight: 105
url: /de/nodejs-cpp/autofill-ranges/
description: Lernen Sie, wie Sie mit Aspose.Cells for Node.js via C++ eine Autofüllung in einem bestimmten Bereich einer Excel Datei durchführen.
---

## **Führen Sie eine automatische Ausfüllung im angegebenen Bereich in Excel durch**

Wählen Sie in Excel einen Bereich aus, bewegen Sie die Maus nach rechts unten und ziehen Sie das "Plus"-Symbol, um Daten automatisch auszufüllen.

## **Auto-Füllbereiche mit Aspose.Cells for Node.js via C++**

Das folgende Beispiel zeigt, wie man eine AutoFill-Operation auf einen Bereich durchführt, und hier ist die Beispiel-Datei, die zum Testen dieser Funktion heruntergeladen werden kann:

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

