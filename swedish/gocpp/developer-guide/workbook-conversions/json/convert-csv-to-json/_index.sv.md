---
title: Konvertera CSV till JSON med Golang via C++
linktitle: Konvertera CSV till JSON
type: docs
weight: 220
url: /sv/go-cpp/convert-csv-to-json/
description: Konvertera CSV fil till JSON med den enkla API n Aspose.Cells for C++.
keywords: Konvertera, konvertera CSV till JSON, CSV till JSON, CSV, JSON, konvertera CSV till JSON C++, C++ kod för att konvertera CSV till JSON
---

## **Konvertera CSV till JSON**

Aspose.Cells stöder konvertering av CSV till JSON. För detta tillhandahåller API:n klasserna [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) och [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/). Klassen [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) ger valmöjligheter för att exportera intervall till JSON. Klassen [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) har följande egenskaper.

- [**GetExportAsString()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getexportasstring/): Detta exporterar cellernas strängvärde till JSON.
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/gethasheaderrow/): Detta indikerar om intervallet innehåller en rubrikrad.
- [**GetIndent()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getindent/): Indikerar indenteringen.

Klass [**JsonUtility**](https://reference.aspose.com/cells/go-cpp/jsonutility/) exporterar JSON med de exportalternativ som ställts in med klass [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/).

Följande kod exempel visar användningen av klasserna [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) och [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) för att ladda [kälcsv-fil](104398879.csv) och skriver ut JSON-resultatet i konsolen.

### **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertCsvToJson.go" >}}
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
