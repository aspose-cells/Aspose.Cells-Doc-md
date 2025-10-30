---
title: Konvertera CSV till JSON
type: docs
weight: 220
url: /sv/python-net/convert-csv-to-json/
description: Konvertera CSV till JSON genom att använda Aspose.Cells för Python via .NET API.
keywords: Konvertera CVS till JSON, Konvertera CSV till JSON i Python via NET, Python konvertera CSV till JSON, Spara CSV till JSON
---

## **Konvertera CSV till JSON**

Aspose.Cells för Python via .NET stöder konvertering av CSV till JSON. För detta tillhandahåller API:et [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) och [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) klasser. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) klassen tillhandahåller alternativen för att exportera område till JSON. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) klassen har följande egenskaper.

- [**export_as_string**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/): Detta exporterar cellernas strängvärde till JSON.
- [**has_header_row**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/): Detta indikerar om området innehåller en rubrikrad.
- [**indent**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/): Indikerar indrag.

 [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) klassen exporterar JSON med exportalternativen som anges med [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) klassen.

Följande kodexempel demonstrerar användningen av [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) och [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) klasser för att läsa in den [ursprungliga CSV-filen](104398879.csv) och skriva ut JSON-utdata i konsollen.

### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

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
{{< app/cells/assistant language="python-net" >}}
