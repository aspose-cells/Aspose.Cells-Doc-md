---
title: Konvertera CSV till JSON
type: docs
weight: 170
url: /sv/java/convert-csv-to-json/
---

## **Konvertera CSV till JSON**

Aspose.Cells stöder konvertering av CSV till JSON. För detta tillhandahåller API:et [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) och [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) klasser. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) klassen tillhandahåller alternativen för att exportera område till JSON. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) klassen har följande egenskaper.

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString): Detta exporterar cellernas strängvärde till JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): Detta indikerar om området innehåller en rubrikrad.
- [**Indent**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): Indikerar indrag.

 [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) klassen exporterar JSON med exportalternativen som anges med [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) klassen.

Följande kodprov demonstrerar användningen av [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) och [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) klasser för att ladda [inledande CSV-fil](SampleCsv.csv) och skriva ut [JSON](SampleJson_out.csv) utdata i konsolen.

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

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
{{< app/cells/assistant language="java" >}}
