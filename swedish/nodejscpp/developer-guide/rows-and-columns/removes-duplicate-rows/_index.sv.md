---
title: Ta bort dubblettrader i ett arbetsblad med Node.js via C++
linktitle: Ta bort dubblettrader i ett arbetsblad
type: docs
weight: 370
url: /sv/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/
description: Lär dig hur du tar bort dubblettrader i ett arbetsblad med Aspose.Cells for Node.js via C++ och väljer specifika kolumner för dupliceringskontroller.
---


Att ta bort dubblettrader är en av Microsoft Excels många användbara funktioner. Det låter användare ta bort dubblettrader i ett arbetsblad, och du kan välja vilka kolumner som ska kontrolleras för duplicerad information.

Aspose.Cells for Node.js via C++ tillhandahåller metoden `Cells.removeDuplicates()` för detta ändamål. Du kan också ställa in `startRow`, `startColumn`, `endRow`, och `endColumn` för att specificera intervallet av kolumner att kontrollera för dupliceringar.

Följande är provfiler som kan laddas ned för att testa denna funktion:

[removeduplicates.xlsx](removeduplicates.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "removeduplicates.xlsx");

// Create workbook
const book = new AsposeCells.Workbook(filePath);

// Remove Duplicate
book.getWorksheets().get(0).getCells().removeDuplicates(0, 0, 5, 3);

// Save result
book.save("removeduplicates-result.xlsx");
```
