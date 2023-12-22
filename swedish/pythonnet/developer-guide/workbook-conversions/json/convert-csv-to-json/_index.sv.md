---
title: Konvertera CSV till JSON
type: docs
weight: 220
url: /sv/python-net/convert-csv-to-json/
description: Konvertera CSV till JSON genom att använda Aspose.Cells for Python via .NET API.
keywords: Convert CVS to JSON, Convert CSV to JSON in Python via NET, Python convert CSV to JSON, Save CSV to JSON
---
##  **Konvertera CSV till JSON**

Aspose.Cells for Python via .NET stöder konvertering av CSV till JSON. För detta tillhandahåller API**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**och**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** klasser. De**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**klass ger alternativen för att exportera intervall till JSON. The**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**klass har följande egenskaper.

- *[export_as_string](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/)**: Detta exporterar strängvärdet för cellerna till JSON.
- *[has_header_row](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/)**: Detta indikerar om intervallet innehåller en rubrikrad.
- *[indrag](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/)**: Indikerar indraget.

De**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**klass exporterar JSON med hjälp av exportalternativen som ställts in med**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**klass.

Följande kodexempel visar användningen av**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**och**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** klasser för att ladda[källfil CSV](104398879.csv)och skriver ut JSON-utgången i konsolen.

###  **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

###  **Konsolutgång**
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