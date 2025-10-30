---
title: Läs och skrivfrågetabell i arbetsblad med Node.js via C++
linktitle: Läsning och skrivning av frågetabell i arbetsblad
type: docs
weight: 40
url: /sv/nodejs-cpp/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller Worksheet.QueryTables-samlingen som returnerar objektet av typ QueryTable efter index. Den har följande två egenskaper

- QueryTable.adjustColumnWidth
- QueryTable.preserveFormatting

Dessa är båda Boolean-värden. Du kan se dem i Microsoft Excel via Data > Connections > Properties.

{{% /alert %}}

## Läsning och skrivning av frågetabell i arbetsblad

Följande exempel läser det första QueryTable i det första arbetsbladet och skriver ut båda QueryTable-egenskaperna. Sedan sätter det QueryTable.preserveFormatting till true.

Du kan ladda ned den angivna källfilen Excel som används i koden och den genererade utdatafilen Excel med hjälp av följande länkar.

- [Käll-Excel-fil](5115533.xlsx)
- [Utdata-Excel-fil](5115537.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first Query Table
const qt = worksheet.getQueryTables().get(0);

// Print Query Table Data
console.log("Adjust Column Width: " + qt.getAdjustColumnWidth());
console.log("Preserve Formatting: " + qt.getPreserveFormatting());

// Now set Preserve Formatting to true
qt.setPreserveFormatting(true);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```

### Konsolutfall

Här är konsoloutputen av ovanstående kodexempel

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Hämta frågetabellens resultatintervall

Aspose.Cells ger möjlighet att läsa adressen dvs resultatintervallen av celler för en frågetabell. Följande kod visar denna funktion genom att läsa adressen för resultatintervallen för en frågetabell. Exempelfilen kan laddas ner [här](72417290.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");

// Create workbook from source excel file
const wb = new AsposeCells.Workbook(filePath);

// Display the address(range) of result range of query table
console.log(wb.getWorksheets().get(0).getQueryTables().get(0).getResultRange().getAddress());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
