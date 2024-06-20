---
title: Converti CSV in JSON
type: docs
weight: 170
url: /it/java/convert-csv-to-json/
---

## **Convertire CSV in JSON**

Aspose.Cells supporta la conversione da CSV a JSON. A tal fine, l'API fornisce le classi [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) e [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility). La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) fornisce le opzioni per esportare l'intervallo in JSON. La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) ha le seguenti proprietà.

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString): Questo esporta il valore stringa delle celle in JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): Questo indica se l'intervallo contiene una riga di intestazione.
- [**Indent**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): Indica l'indentazione.

La classe [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) esporta il JSON utilizzando le opzioni di esportazione impostate con la classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions).

Il seguente codice di esempio dimostra l'uso delle classi [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) e [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) per caricare il [file CSV di origine](SampleCsv.csv) e stampa l'output [JSON](SampleJson_out.csv) nella console.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **Output della console**

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
