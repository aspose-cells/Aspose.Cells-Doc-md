---
title: Radera tomma rader och kolumner i ett kalkylblad med Node.js via C++
linktitle: Radera tomma rader och kolumner i ett kalkylblad
type: docs
weight: 300
url: /sv/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Lär dig hur man tar bort alla tomma rader och kolumner från ett kalkylblad med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Det är möjligt att ta bort alla tomma rader och kolumner från ett kalkylblad. Detta är användbart när man, till exempel, genererar en PDF-fil från en Microsoft Excel-fil och vill konvertera endast rader och kolumner som innehåller data eller relaterade objekt.

Använd följande Aspose.Cells-metoder för att ta bort tomma rader och kolumner:

1. För att ta bort tomma rader, använd metoden [**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankRows--). Observera, för tomma rader som kommer att tas bort, krävs det inte bara att [**Row.isBlank()**](https://reference.aspose.com/cells/nodejs-cpp/row/#isBlank--) ska vara sant, utan det får inte heller finnas någon synlig kommentar definierad för någon cell i dessa rader, och ingen pivottabell vars omfång korsar dem.
2. För att ta bort tomma kolumner, använd [**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankColumns--)-metoden.

{{% /alert %}}

## Node.js-kod för att radera tomma rader

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(filePath);

// Create a Worksheets object with reference to
// The sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Rows from the worksheet
sheet.getCells().deleteBlankRows();

// Save the excel file.
wb.save(path.join(dataDir, "mybook.out.xlsx"));
```

## Node.js-kod för att radera tomma kolumner

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an existing excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleInput.xlsx"));

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = workbook.getWorksheets();

// Get first Worksheet from WorksheetCollection
const sheet = sheets.get(0);

// Delete the Blank Columns from the worksheet
sheet.getCells().deleteBlankColumns();

// Save the excel file.
workbook.save(path.join(dataDir, "mybook.out.xlsx"));
```
