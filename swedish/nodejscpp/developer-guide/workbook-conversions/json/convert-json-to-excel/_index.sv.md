---
title: Konvertera JSON till Excel med Node.js via C++
linktitle: Konvertera JSON till Excel
type: docs
weight: 300
url: /sv/nodejs-cpp/convert-json-to-excel/
description: Lär dig hur du konverterar JSON till Excel fil med Aspose.Cells for Node.js via C++.
keywords: Importera JSON utan Office 2013, Office 2016, Office 2019 och Office 365 med Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells stöder konvertering av en JSON (JavaScript-objektnotation) fil till en Excel-arbetsbok.

{{% /alert %}}

## **Konvertera JSON till Excel-arbetsbok**
Inga problem att undra hur man konverterar JSON till Excel-fil, eftersom Aspose.Cells for Node.js via C++ tillhandahåller den bästa lösningen. Aspose.Cells API ger stöd för att konvertera JSON-format till kalkylblad. Du kan använda [**JsonLoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonloadoptions)-klassen för att specificera ytterligare inställningar för att importera JSON till arbetsbok.

Följande kodexempel visar import av JSON till Excel-arbetsbok. Se koden för att konvertera [källfilen](sample.json) till den xlsx-fil som genereras av koden som referens.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");
// create a Workbook object
const wb = new AsposeCells.Workbook(filePath);

// save file to xlsx format
wb.save("sample_out.xlsx");
```

Följande kodexempel, som använder JsonLoadOptions-klassen för att specificera ytterligare inställningar, demonstrerar import av JSON till Excel-arbetsbok. Se koden för att konvertera [källfil](sample.json) till xlsx-filen som genereras av koden för referens.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");

// Create an options of loading the file.
const options = new AsposeCells.JsonLoadOptions();
options.setMultipleWorksheets(true);

// Loads the workbook from JSON file
const book = new AsposeCells.Workbook(filePath, options);

// Save file to xlsx format
book.save("sample_out.xlsx");
```

Följande kodexempel visar import av en JSON-sträng till Excel-arbetsbok. Du kan också specificera platsen för layouten vid import av JSON. Se koden för att konvertera en JSON-sträng till xlsx-filen som genereras av koden för referens.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputJson = JSON.stringify([
{ BEFORE: 'before cell', TEST: 'asd1', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd2', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd3', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd4', AFTER: 'after cell' }
]);
const sheetName = "Sheet1";
const row = 3;
const column = 2;

// create a Workbook object
const book = new AsposeCells.Workbook();
const worksheet = book.getWorksheets().get(sheetName);

// set JsonLayoutOptions to treat Arrays as Table
const jsonLayoutOptions = new AsposeCells.JsonLayoutOptions();
jsonLayoutOptions.setArrayAsTable(true);

AsposeCells.JsonUtility.importData(inputJson, worksheet.getCells(), row, column, jsonLayoutOptions);

// save file to xlsx format
book.save("out.xlsx");
```
