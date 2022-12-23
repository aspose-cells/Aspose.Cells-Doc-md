---
title: Converti CSV in JSON
type: docs
weight: 170
url: /it/java/convert-csv-to-json/
---
## **Converti CSV in JSON**

Aspose.Cells supporta la conversione da CSV a JSON. Per questo, API fornisce[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)e[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)classi. Il[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)class fornisce le opzioni per l'esportazione dell'intervallo a JSON. Il[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)class ha le seguenti proprietà.

- [**Esporta come stringa**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString): Questo esporta il valore stringa delle celle in JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): Indica se l'intervallo contiene una riga di intestazione.
- [**Rientro**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): Indica il rientro.

Il[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)class esporta lo JSON utilizzando le opzioni di esportazione impostate con il file[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)classe.

L'esempio di codice seguente illustra l'utilizzo di[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)e[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)classi per caricare il file[fonte CSV file](SampleCsv.csv)e stampa il[JSON](SampleJson_out.csv) uscita nella console.

### **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **Uscita console**

[ { "id": 1, "language": "Java", "edition": "three", "author": "Herbert Schildt", "streetAddress": 126, "city": "San Jone", "state": "CA", "postalCode": 394221 }, { "id": 2, "language": "C++", "edition": "second", "author": "EAAAA", "streetAddress": 126, "city": "San Jone", "state": "CA", "postalCode": 394221 }, { "id": 3 , "language": ".Net", "edition": "second", "author": "E.Balagurusamy", "streetAddress": 126, "city": "San Jone", " stato": "CA", "codicepostale": 394221 } ]