---
title : "Convert CSV to JSON" 
description : "" 
weight : 12081 
toc : false
type: docs
url: /net/developerguide/ld-sv-cvt-mng/convert+csv+to+json/
---

# Aspose.Cells for .NET : Convert CSV to JSON


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Convert CSV to JSON](#convert-csv-to-json)
    *   1.1 [Sample Code](#sample-code)
    *   1.2 [Console Output](#console-output)
{{< /panel >}}
## Convert CSV to JSON

Aspose.Cells supports converting CSV to JSON. For this, the API provides [ExportRangeToJsonOptions](https://apireference.aspose.com/net/cells/aspose.cells.utility/exportrangetojsonoptions) and [JsonUtility](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonutility) classes. The [ExportRangeToJsonOptions](https://apireference.aspose.com/net/cells/aspose.cells.utility/exportrangetojsonoptions) class provides the options for exporting range to JSON. The [ExportRangeToJsonOptions](https://apireference.aspose.com/net/cells/aspose.cells.utility/exportrangetojsonoptions) class has the following properties.

*   [ExportAsString](https://apireference.aspose.com/net/cells/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring): This exports the string value of the cells to JSON.
*   [HasHeaderRow](https://apireference.aspose.com/net/cells/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow): This indicates whether the range contains a header row.
*   [Indent](https://apireference.aspose.com/net/cells/aspose.cells.utility/exportrangetojsonoptions/properties/indent): Indicates the indent.

The [JsonUtility](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonutility) class exports the JSON using the export options set with the [ExportRangeToJsonOptions](https://apireference.aspose.com/net/cells/aspose.cells.utility/exportrangetojsonoptions) class.

The following code sample demonstrates the use of [ExportRangeToJsonOptions](https://apireference.aspose.com/net/cells/aspose.cells.utility/exportrangetojsonoptions) and [JsonUtility](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonutility) classes to load the [source CSV file](https://docs2.aspose.com/cells/net/attachments/104267887/104398879.csv) and prints the [J](https://docs2.aspose.com/cells/net/attachments/104267887/104398871.csv)SON output in the console.

### Sample Code

### Console Output

\[  
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
\]

