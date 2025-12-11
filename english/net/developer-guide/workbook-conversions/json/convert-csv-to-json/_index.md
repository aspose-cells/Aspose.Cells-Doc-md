---
title: Convert CSV to JSON
type: docs
weight: 220
url: /net/convert-csv-to-json/
description: Convert CSV file to JSON by using the simple-to-use Aspose.Cells for .NET API.
keywords: Convert, Convert CSV to JSON, CSV to JSON, CSV, JSON, Convert CSV to JSON C#, c# code to convert CSV to JSON
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Convert CSV to JSON**

Aspose.Cells supports converting CSV to JSON. For this, the API provides **[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)** and **[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** classes. The **ExportRangeToJsonOptions** class provides the options for exporting a range to JSON. The **ExportRangeToJsonOptions** class has the following properties.

- **[ExportAsString](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring)**: Exports the string values of the cells to JSON.  
- **[HasHeaderRow](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow)**: Indicates whether the range contains a header row.  
- **[Indent](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent)**: Indicates the indentation.

The **JsonUtility** class exports the JSON using the export options set with the **ExportRangeToJsonOptions** class.

The following code sample demonstrates the use of **ExportRangeToJsonOptions** and **JsonUtility** classes to load the [source CSV file](104398879.csv) and print the JSON output in the console.

### **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

### **Console Output**
{{< highlight json >}}
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
    "language": ".NET",
    "edition": "second",
    "author": "E.Balagurusamy",
    "streetAddress": 126,
    "city": "San Jone",
    "state": "CA",
    "postalCode": 394221
  }
]
{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
