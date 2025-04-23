---
title: Konvertera CSV till JSON
type: docs
weight: 220
url: /sv/net/convert-csv-to-json/
description: Konvertera CSF fil till JSON genom att använda den enkla att använda Aspose.Cells for .NET API.
keywords: Konvertera, Konvertera CSV till JSON, CSV till JSON, CSV, JSON, Konvertera CSV till JSON CSharp, c# kod för att konvertera CSV till JSON
---

## **Konvertera CSV till JSON**

Aspose.Cells stödjer konvertering av CSV till JSON. För detta tillhandahåller API:et [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) och [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)-klasser. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)-klassen ger alternativ för att exportera området till JSON. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)-klassen har följande egenskaper.

- [**ExportAsString**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring): Detta exporterar cellernas strängvärde till JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow): Detta indikerar om området innehåller en rubrikrad.
- [**Indent**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent): Indikerar indrag.

 [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) klassen exporterar JSON med exportalternativen som anges med [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) klassen.

Följande kodexempel demonstrerar användningen av [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) och [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) klasser för att läsa in den [ursprungliga CSV-filen](104398879.csv) och skriva ut JSON-utdata i konsollen.

### **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
