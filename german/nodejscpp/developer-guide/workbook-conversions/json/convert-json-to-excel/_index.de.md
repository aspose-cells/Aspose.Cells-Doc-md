---
title: Konvertieren von JSON nach Excel mit Node.js via C++
linktitle: Konvertieren Sie JSON nach Excel
type: docs
weight: 300
url: /de/nodejs-cpp/convert-json-to-excel/
description: Lernen Sie, wie Sie JSON mithilfe von Aspose.Cells for Node.js via C++ in eine Excel Datei konvertieren.
keywords: Importieren von JSON ohne Office 2013, Office 2016, Office 2019 und Office 365 mit Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Konvertierung einer JSON-(JavaScript-Objekt-Notation)-Datei in ein Excel-Arbeitsbuch.

{{% /alert %}}

## **Konvertieren Sie JSON in Excel-Arbeitsmappe**
Sie müssen sich keine Sorgen machen, wie man JSON in Excel konvertiert, denn Aspose.Cells for Node.js via C++ bietet die beste Lösung. Die Aspose.Cells-API unterstützt die Konvertierung des JSON-Formats in Tabellenkalkulationen. Sie können die [**JsonLoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonloadoptions)-Klasse verwenden, um zusätzliche Einstellungen für den Import von JSON in Arbeitsmappen festzulegen.

Das folgende Codebeispiel zeigt, wie man JSON in Excel-Arbeitsmappe importiert. Bitte sehen Sie sich den Code zur Konvertierung der [Quelldatei](sample.json) in die von dem Code generierte xlsx-Datei als Referenz an.

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

Das folgende Codebeispiel, das die JsonLoadOptions-Klasse verwendet, um zusätzliche Einstellungen festzulegen, zeigt den Import von JSON in ein Excel-Arbeitsbuch. Bitte beachten Sie den Code zur Konvertierung der [Quelldatei](sample.json) in die durch den Code generierte xlsx-Datei.

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

Das folgende Codebeispiel demonstriert das Importieren eines JSON-Strings in ein Excel-Arbeitsbuch. Sie können auch die Position des Layouts beim Importieren von JSON festlegen. Bitte beachten Sie den Code zur Konvertierung eines JSON-Strings in die durch den Code generierte xlsx-Datei.

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
