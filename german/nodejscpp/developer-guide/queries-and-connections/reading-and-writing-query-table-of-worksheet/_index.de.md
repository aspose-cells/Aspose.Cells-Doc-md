---
title: Lesen und Schreiben von Abfrage Tabellen eines Arbeitsblatts mit Node.js über C++
linktitle: Lesen und Schreiben von Abfrage Tabellen des Arbeitsblatts
type: docs
weight: 40
url: /de/nodejs-cpp/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Worksheet.QueryTables-Sammlung, die ein Objekt des Typs QueryTable nach Index zurückgibt. Sie hat die folgenden zwei Eigenschaften

- QueryTable.adjustColumnWidth
- QueryTable.preserveFormatting

Diese sind beide boolesche Werte. Sie können sie in Microsoft Excel unter Daten > Verbindungen > Eigenschaften anzeigen.

{{% /alert %}}

## Lesen und Schreiben von Abfrage-Tabellen im Arbeitsblatt

Das folgende Beispiel liest die erste QueryTable des ersten Arbeitsblatts und gibt dann beide Eigenschaften der QueryTable aus. Anschließend wird die Eigenschaft QueryTable.preserveFormatting auf true gesetzt.

Sie können die Quelldatei von Excel, die in diesem Code verwendet wird, und die Ausgabedatei, die von dem Code generiert wird, von den folgenden Links herunterladen.

- [Quelldatei](5115533.xlsx)
- [Ausgabedatei](5115537.xlsx)

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

### Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielscodes

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Abrufen des Ergebnisbereichs der Abfrage-Tabelle

Aspose.Cells bietet die Möglichkeit, die Adresse, d.h. den Ergebnisbereich der Zellen für eine Abfrage-Tabelle, zu lesen. Der folgende Code demonstriert diese Funktion, indem er die Adresse des Ergebnisbereichs für eine Abfrage-Tabelle liest. Die Beispieldatei kann [hier heruntergeladen werden](72417290.xlsx).

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
