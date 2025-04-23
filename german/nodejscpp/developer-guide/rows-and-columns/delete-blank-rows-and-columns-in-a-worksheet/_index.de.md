---
title: Leere Zeilen und Spalten in einem Arbeitsblatt mit Node.js via C++ löschen
linktitle: Löschen von leeren Zeilen und Spalten in einem Arbeitsblatt
type: docs
weight: 300
url: /de/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Erfahren Sie, wie Sie alle leeren Zeilen und Spalten aus einem Arbeitsblatt mit Aspose.Cells for Node.js via C++ löschen. 
---

{{% alert color="primary" %}}

Es ist möglich, alle leeren Zeilen und Spalten aus einem Arbeitsblatt zu löschen. Dies ist nützlich, wenn beispielsweise eine PDF-Datei aus einer Microsoft Excel-Datei generiert wird und nur Zeilen und Spalten mit Daten oder verwandten Objekten konvertiert werden sollen.

Verwenden Sie die folgenden Aspose.Cells-Methoden, um leere Zeilen und Spalten zu löschen:

1. Um leere Zeilen zu löschen, verwenden Sie die [**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankRows--)-Methode. Bitte beachten Sie, dass für die zu löschenden leeren Zeilen nicht nur erforderlich ist, dass [**Row.isBlank()**](https://reference.aspose.com/cells/nodejs-cpp/row/#isBlank--) wahr sein sollte, sondern es dürfen auch keine sichtbaren Kommentare für Zellen in diesen Zeilen definiert sein und kein Pivot-Table, dessen Bereich mit ihnen kollidiert.
2. Um leere Spalten zu löschen, verwenden Sie die [**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteBlankColumns--) Methode.

{{% /alert %}}

## Node.js Code zum Löschen leerer Zeilen

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

## Node.js Code zum Löschen leerer Spalten

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
