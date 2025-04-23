---
title: AutoAnpassa Kolumner och Rader när du laddar HTML i Workbook med Node.js via C++
linktitle: Justera kolumner och rader automatiskt vid inläsning av HTML i arbetsboken
type: docs
weight: 120
url: /sv/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Lär dig hur du autofixar kolumner och rader när du laddar HTML filer i en Workbook med Aspose.Cells for Node.js via C++.
---

## **Möjliga användningsscenario**

Du kan autofixa kolumner och rader när du laddar HTML-filen inuti Workbook-objektet. Sätt [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) egenskapen till **true** för detta ändamål.

## **Justera kolumner och rader automatiskt vid inläsning av HTML i arbetsboken**

Följande exempel laddar först HTML-testfilen i en Workbook utan någon laddningsalternativ och sparar den i XLSX-format. Sedan laddar den om HTML-filen men den här gången, laddar HTML efter att ha satt [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) egenskapen till **true** och sparar den i XLSX-format. Ladda ner båda utdata Excel-filerna dvs. [Utdatak Excel-fil Utan AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) och [Utdatak Excel-fil Med AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). Följande skärmbild visar effekten av [**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--) egenskapen på båda utdata Excel-filer.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Sample HTML.
const sampleHtml = "<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>";

// Load HTML string into memory stream.
const ms = Uint8Array.from(sampleHtml, c => c.charCodeAt(0));

// Load memory stream into workbook.
let wb = new AsposeCells.Workbook(ms);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWithout_AutoFitColsAndRows.xlsx"));

// Specify the HTMLLoadOptions and set AutoFitColsAndRows = true.
const opts = new AsposeCells.HtmlLoadOptions();
opts.setAutoFitColsAndRows(true);

// Load memory stream into workbook with the above HTMLLoadOptions.
wb = new AsposeCells.Workbook(ms, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWith_AutoFitColsAndRows.xlsx"));
```

