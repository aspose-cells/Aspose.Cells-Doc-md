---
title: Convert CSV to JSON
type: docs
weight: 220
url: /python-net/convert-csv-to-json/
description: Convert CSV to JSON by using Aspose.Cells for Python via .NET API.
keywords: Convert CVS to JSON, Convert CSV to JSON in Python via NET, Python convert CSV to JSON, Save CSV to JSON
---

## **Convert CSV to JSON**

Aspose.Cells for Python via .NET supports converting CSV to JSON. For this, the API provides **[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)** and **[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** classes. The **[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)** class provides the options for exporting range to JSON. The **[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)** class has the following properties.

- **[export_as_string](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/)**: This exports the string value of the cells to JSON.
- **[has_header_row](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/)**: This indicates whether the range contains a header row.
- **[indent](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/)**: Indicates the indent.

The **[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** class exports the JSON using the export options set with the **[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)** class.

The following code sample demonstrates the use of **[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)** and **[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** classes to load the [source CSV file](104398879.csv) and prints the JSON output in the console.

### **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

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