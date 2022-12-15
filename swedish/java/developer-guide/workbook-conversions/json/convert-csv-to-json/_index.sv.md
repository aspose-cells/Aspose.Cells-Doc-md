---
title: Konvertera CSV till JSON
type: docs
weight: 170
url: /sv/java/convert-csv-to-json/
---
## **Konvertera CSV till JSON**

Aspose.Cells stöder konvertering av CSV till JSON. För detta tillhandahåller API[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)och[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)klasser. De[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)klass ger alternativen för att exportera intervall till JSON. De[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)klass har följande egenskaper.

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString)Detta exporterar strängvärdet för cellerna till JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): Detta indikerar om intervallet innehåller en rubrikrad.
- [**Indrag**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): Indikerar indraget.

De[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)class exporterar JSON med hjälp av exportalternativen som ställts in med[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)klass.

Följande kodexempel visar användningen av[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)och[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)klasser för att ladda[käll-CSV-fil](SampleCsv.csv)och skriver ut[JSON](SampleJson_out.csv) utgång i konsolen.

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **Konsolutgång**

[ { "id": 1, "language": "Java", "edition": "third", "author": "Herbert Schildt",x "streetAddress"_: "streetAddress"_ "San Jone", "state": "CA", "postalCode": 394221 }, { "id": 2, "language": "C+d" "0", _x000,_x000: "C+d" "author": "EAAAA", "streetAddress": 126, "city": "San Jone", "state": "CA", "postalkod": 394221 }, __x00d: _d_x00d: , "language": ".Net", "edition": "second", "author": "E.Balagurusamy", "streetAddress": 126, "city": "San Jone",_x00 state": "CA", "postalCode": 394221 } ]