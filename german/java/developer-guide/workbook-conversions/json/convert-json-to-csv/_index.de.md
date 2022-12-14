---
title: Konvertieren Sie JSON in CSV
type: docs
weight: 160
url: /de/java/convert-json-to-csv/
---
Aspose.Cells unterstützt die Konvertierung von einfachem sowie verschachteltem JSON in CSV. Dafür sorgt die API[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)und[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)Klassen. Das[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)Die Klasse bietet die Optionen für das JSON-Layout wie z[**ArrayTitle ignorieren**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)(ignoriert den Titel, wenn das Array eine Eigenschaft eines Objekts ist) oder[**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)(verarbeitet das Array als Tabelle). Das[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)-Klasse verarbeitet den JSON-Code mithilfe der Layoutoptionen, die mit der festgelegt wurden[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)Klasse.

Das folgende Codebeispiel veranschaulicht die Verwendung von[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)und[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)Klassen zum Laden der[Quell-JSON-Datei](SampleJson.json)und generiert die[CSV-Datei ausgeben](SampleJson_out.csv).

## Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
