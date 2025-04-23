---
title: Konvertieren von CSV in JSON
type: docs
weight: 170
url: /de/java/convert-csv-to-json/
---

## **Konvertieren von CSV in JSON**

Aspose.Cells unterstützt die Konvertierung von CSV in JSON. Dafür bietet die API die Klassen [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) und [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility). Die Klasse [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) bietet Optionen für den Export des Bereichs in JSON. Die Klasse [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) hat die folgenden Eigenschaften.

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString): Exportiert den Zeichenfolgenwert der Zellen in JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): Gibt an, ob der Bereich eine Kopfzeile enthält.
- [**Indent**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): Gibt die Einrückung an.

Die Klasse [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) exportiert das JSON unter Verwendung der Exportoptionen, die mit der Klasse [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) festgelegt sind.

Der folgende Codeausschnitt zeigt die Verwendung der Klassen [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) und [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) zum Laden der [Quell-CSV-Datei](SampleCsv.csv) und zum Ausgeben des [JSONs](SampleJson_out.csv) in die Konsole.

### **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **Konsolenausgabe**

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
