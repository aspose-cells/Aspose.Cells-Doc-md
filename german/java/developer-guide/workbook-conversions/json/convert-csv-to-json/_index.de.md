---
title: Konvertieren Sie CSV in JSON
type: docs
weight: 170
url: /de/java/convert-csv-to-json/
---
## **Konvertieren Sie CSV in JSON**

Aspose.Cells unterstützt die Konvertierung von CSV in JSON. Dafür sorgt die API[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)und[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)Klassen. Das[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)-Klasse bietet die Optionen zum Exportieren des Bereichs nach JSON. Das[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)Klasse hat die folgenden Eigenschaften.

- [**AlsString exportieren**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString)Dies exportiert den Zeichenfolgenwert der Zellen in JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): Gibt an, ob der Bereich eine Kopfzeile enthält.
- [**Einzug**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): Gibt den Einzug an.

Das[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)-Klasse exportiert die JSON-Datei mithilfe der mit der festgelegten Exportoptionen[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)Klasse.

Das folgende Codebeispiel veranschaulicht die Verwendung von[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)und[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)Klassen zum Laden der[Quell-CSV-Datei](SampleCsv.csv)und druckt die[JSON](SampleJson_out.csv) Ausgabe in der Konsole.

### **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **Konsolenausgabe**

[ { "id": 1, "language": "Java", "edition": "dritte", "author": "Herbert Schildt", "streetAddress": 126, "city": "San Jone", "state": "CA", "postalCode": 394221 }, { "id": 2, "language": "C++", "edition": "second", "Autor": "EAAAA", "streetAddress": 126, "city": "San Jone", "state": "CA", "postalCode": 394221 }, { "id": 3 , "Sprache": ".Net", "Ausgabe": "Sekunde", "Autor": "E.Balagurusamy", "StraßeAdresse": 126, "Stadt": "San Jone", " state": "CA", "postalCode": 394221 } ]