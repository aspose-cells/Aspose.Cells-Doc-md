---
title: Konvertera CSV till JSON med Node.js via C++
linktitle: Konvertera CSV till JSON
type: docs
weight: 220
url: /sv/nodejs-cpp/convert-csv-to-json/
description: Konvertera CSV fil till JSON med den lättanvända Aspose.Cells for Node.js via C++ API n.
keywords: Konvertera, Konvertera CSV till JSON, CSV till JSON, CSV, JSON, Konvertera CSV till JSON Node.js via C++, c++ kod för att konvertera CSV till JSON
---

## **Konvertera CSV till JSON**

Aspose.Cells stödjer konvertering av CSV till JSON. För detta tillhandahåller API:et [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) och [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/)-klasser. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/)-klassen ger alternativ för att exportera området till JSON. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/)-klassen har följande egenskaper.

- [**ExportRangeToJsonOptions.getExportAsString()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getExportAsString--): Detta exporterar cellernas strängvärde till JSON.
- [**ExportRangeToJsonOptions.getHasHeaderRow()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getHasHeaderRow--): Detta indikerar om området innehåller en rubrikrad.
- [**ExportRangeToJsonOptions.getIndent()**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/#getIndent--): Indikerar indrag.

 [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) klassen exporterar JSON med exportalternativen som anges med [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) klassen.

Följande kodexempel demonstrerar användningen av [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/nodejs-cpp/exportrangetojsonoptions/) och [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility/) klasser för att läsa in den [ursprungliga CSV-filen](104398879.csv) och skriva ut JSON-utdata i konsollen.

### **Exempelkod**

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

### **Konsoloutput**
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
