---
title: Convert CSV to JSON
type: docs
weight: 170
url: /java/convert-csv-to-json/
---

## **Convert CSV to JSON**

Aspose.Cells supports converting CSV to JSON. For this, the API provides [**ExportRangeToJsonOptions**](https://apireference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) and [**JsonUtility**](https://apireference.aspose.com/cells/java/com.aspose.cells/JsonUtility) classes. The [**ExportRangeToJsonOptions**](https://apireference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) class provides the options for exporting range to JSON. The [**ExportRangeToJsonOptions**](https://apireference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) class has the following properties.

- [**ExportAsString**](https://apireference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString): This exports the string value of the cells to JSON.
- [**HasHeaderRow**](https://apireference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): This indicates whether the range contains a header row.
- [**Indent**](https://apireference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): Indicates the indent.

The [**JsonUtility**](https://apireference.aspose.com/cells/java/com.aspose.cells/JsonUtility) class exports the JSON using the export options set with the [**ExportRangeToJsonOptions**](https://apireference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) class.

The following code sample demonstrates the use of [**ExportRangeToJsonOptions**](https://apireference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) and [**JsonUtility**](https://apireference.aspose.com/cells/java/com.aspose.cells/JsonUtility) classes to load the [source CSV file](SampleCsv.csv) and prints the [JSON](SampleJson_out.csv) output in the console.

### **Sample Code**

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **Console Output**

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
