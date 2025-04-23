---
title: Tabelle mit Abfrage Tabellen Datenquelle in Node.js lesen und schreiben
linktitle: Tabelle mit Abfrage Tabellendatenquelle lesen und schreiben
type: docs
weight: 30
url: /de/nodejs-cpp/read-and-write-table-with-query-table-data-source/
description: Lernen Sie, wie Sie eine Tabelle mit einer QueryTable Datenquelle mit Aspose.Cells for Node.js via C++ lesen und schreiben. 
---

## **Tabelle mit Abfrage-Tabellendatenquelle lesen und schreiben**
 Mit Aspose.Cells for Node.js via C++ können Sie eine Tabelle lesen und schreiben, die eine QueryTable als Datenquelle hat. Diese Unterstützung besteht auch für XLS-Dateien. Der folgende Code zeigt, wie man eine solche Tabelle liest und schreibt, indem man zuerst die Tabelle liest und dann modifiziert, um die Summezeile hinzuzufügen.

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

Die Quell- und Ausgabedateien sind als Referenz angehängt.

[Quelldatei](96928091.xls)

[Ausgabedatei](96928092.xls)
