---
title: Konvertera CSV till JSON
type: docs
weight: 220
url: /sv/net/convert-csv-to-json/
description: Konvertera CSF-filen till JSON genom att använda den enkla att använda Aspose.Cells for .NET API.
keywords: Convert, Convert CVS to JSON, CSV to JSON, CSV, JSON, Convert CSV to JSON CSharp, c# code to convert CSV to JSON
---
## **Konvertera CSV till JSON**

Aspose.Cells stöder konvertering av CSV till JSON. För detta tillhandahåller API**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**och**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** klasser. De**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**klass ger alternativen för att exportera intervall till JSON. The**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**klass har följande egenskaper.

- **[ExportAsString](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring)**: Detta exporterar strängvärdet för cellerna till JSON.
- **[HasHeaderRow](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow)**: Detta indikerar om intervallet innehåller en rubrikrad.
- **[Indrag](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent)**: Indikerar indraget.

De**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**klass exporterar JSON med hjälp av exportalternativen som ställts in med**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**klass.

Följande kodexempel visar användningen av**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**och**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** klasser för att ladda[källfil CSV](104398879.csv)och skriver ut JSON-utgången i konsolen.

### **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

### **Konsolutgång**
```json
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
```