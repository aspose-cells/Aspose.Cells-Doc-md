---
title: Convert CSV to JSON with Node.js via C++
linktitle: Convert CSV to JSON
type: docs
weight: 220
url: /nodejs-cpp/convert-csv-to-json/
description: Convert CSV file to JSON using the easy-to-use Aspose.Cells for Node.js via C++ API.
keywords: Convert, Convert CSV to JSON, CSV to JSON, CSV, JSON, Convert CSV to JSON Node.js via C++, c++ code to convert CSV to JSON
---

## **Convert CSV to JSON**

Aspose.Cells supports converting CSV to JSON. For this, the API provides [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) and [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) classes. The [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) class provides the options for exporting range to JSON. The [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) class has the following properties.

- [**ExportRangeToJsonOptions.getExportAsString()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getExportAsString--): This exports the string value of the cells to JSON.
- [**ExportRangeToJsonOptions.getHasHeaderRow()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getHasHeaderRow--): This indicates whether the range contains a header row.
- [**ExportRangeToJsonOptions.getIndent()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getIndent--): Indicates the indent.

The [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) class exports the JSON using the export options set with the [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) class.

The following code sample demonstrates the use of [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) and [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) classes to load the [source CSV file](104398879.csv) and prints the JSON output in the console.

### **Sample Code**

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

### **Console Output**
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
