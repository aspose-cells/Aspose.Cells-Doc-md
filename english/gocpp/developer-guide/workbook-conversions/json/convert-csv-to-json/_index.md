---
title: Convert CSV to JSON with Golang via C++
linktitle: Convert CSV to JSON
type: docs
weight: 220
url: /go-cpp/convert-csv-to-json/
description: Convert CSV file to JSON by using the simple-to-use Aspose.Cells for C++ API.
keywords: Convert, Convert CSV to JSON, CSV to JSON, CSV, JSON, Convert CSV to JSON C++, C++ code to convert CSV to JSON
---

## **Convert CSV to JSON**

Aspose.Cells supports converting CSV to JSON. For this, the API provides [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) and [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) classes. The [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) class provides options for exporting a range to JSON. The [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) class has the following properties.

- [**GetExportAsString()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getexportasstring/): Exports the string values of the cells to JSON.  
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/gethasheaderrow/): Indicates whether the range contains a header row.  
- [**GetIndent()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getindent/): Specifies the indentation.

The [**JsonUtility**](https://reference.aspose.com/cells/go-cpp/jsonutility/) class exports the JSON using the export options set with the [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) class.

The following code sample demonstrates the use of [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) and [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) classes to load the [source CSV file](104398879.csv) and print the JSON output to the console.

### **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertCsvToJson.go" >}}

### **Console Output**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jose",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jose",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".NET",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jose",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}