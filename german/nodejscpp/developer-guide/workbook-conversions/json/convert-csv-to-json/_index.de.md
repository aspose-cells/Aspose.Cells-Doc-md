---
title: Konvertieren Sie CSV nach JSON mit Node.js via C++
linktitle: Konvertieren von CSV in JSON
type: docs
weight: 220
url: /de/nodejs-cpp/convert-csv-to-json/
description: Konvertieren Sie CSV Dateien in JSON mithilfe der benutzerfreundlichen Aspose.Cells for Node.js via C++ API.
keywords: Konvertieren, CSV nach JSON, CSV zu JSON, CSV, JSON, CSV nach JSON mit Node.js via C++, C++ Code zur Konvertierung von CSV in JSON
---

## **Konvertieren von CSV in JSON**

Aspose.Cells unterstützt die Umwandlung von CSV in JSON. Hierfür bietet die API die [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/)- und [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/)-Klassen. Die [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/)-Klasse bietet Optionen zum Exportieren des Bereichs als JSON. Die [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/)-Klasse hat folgende Eigenschaften.

- [**ExportRangeToJsonOptions.getExportAsString()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getExportAsString--): Exportiert den Zeichenfolgenwert der Zellen in JSON.
- [**ExportRangeToJsonOptions.getHasHeaderRow()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getHasHeaderRow--): Gibt an, ob der Bereich eine Kopfzeile enthält.
- [**ExportRangeToJsonOptions.getIndent()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getIndent--): Gibt die Einrückung an.

Die Klasse [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) exportiert das JSON unter Verwendung der Exportoptionen, die mit der Klasse [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) festgelegt sind.

Der folgende Beispielcode zeigt die Verwendung der [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/)- und [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/)-Klassen zum Laden der [Quell-CSV-Datei](104398879.csv) und gibt die JSON-Ausgabe in der Konsole aus.

### **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);
// Load CSV file
const filePath = path.join(sourceDir, "SampleCsv.csv");
const workbook = new AsposeCells.Workbook(filePath, loadOptions);
const lastCell = workbook.getWorksheets().get(0).getCells().getLastCell();

// Set JsonSaveOptions
const jsonSaveOptions = new AsposeCells.JsonSaveOptions();
const range = workbook.getWorksheets().get(0).getCells().createRange(0, 0, lastCell.getRow() + 1, lastCell.getColumn() + 1);
const data = AsposeCells.JsonUtility.exportRangeToJson(range, jsonSaveOptions);

// Print JSON
console.log(data);
```

### **Konsolenausgabe**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
