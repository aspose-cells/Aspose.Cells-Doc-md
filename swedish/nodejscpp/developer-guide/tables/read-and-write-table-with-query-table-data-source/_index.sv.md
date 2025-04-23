---
title: Läs och skriv tabell med Query Table data källa via Node.js
linktitle: Läs och skriv tabell med datakälla för frågetabell
type: docs
weight: 30
url: /sv/nodejs-cpp/read-and-write-table-with-query-table-data-source/
description: Lär dig hur du läser och skriver en tabell med en QueryTable data källa med Aspose.Cells for Node.js via C++. 
---

## **Läs och skriv tabell med datakälla för frågetabell**
Med Aspose.Cells for Node.js via C++ kan du läsa och skriva en tabell som har en QueryTable som datakälla. Stödet för denna funktion finns också för XLS-filer. Följande kod exempel demonstrerar att läsa och skriva en sådan tabell genom att först läsa tabellen och sedan ändra den för att lägga till totalsraden.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the source directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load workbook object
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTableWithQueryTable.xls"));

const worksheet = workbook.getWorksheets().get(0);

const table = worksheet.getListObjects().get(0);

// Check the data source type if it is query table
if (table.getDataSourceType() === AsposeCells.TableDataSourceType.QueryTable) {
table.setShowTotals(true);
}

// Save the file
workbook.save(path.join(outputDir, "SampleTableWithQueryTable_out.xls"));
```

Käll- och utdataexcelfilerna är bilagda som referens.

[Källfil](96928091.xls)

[Resultatfil](96928092.xls)
