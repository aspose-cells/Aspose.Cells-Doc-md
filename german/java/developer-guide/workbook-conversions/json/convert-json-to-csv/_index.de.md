---
title: Konvertieren Sie JSON in CSV
type: docs
weight: 160
url: /de/java/convert-json-to-csv/
---

Aspose.Cells unterstützt die Konvertierung von einfachen sowie verschachtelten JSON-Dateien in CSV. Dafür stellt die API die Klassen [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) und [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) zur Verfügung. Die Klasse [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) bietet die Optionen für das Layout des JSON wie [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle) (ignoriert den Titel, wenn das Array eine Eigenschaft eines Objekts ist) oder [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable) (verarbeitet das Array als Tabelle). Die Klasse [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) verarbeitet das JSON mit den mit der Klasse [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) festgelegten Layoutoptionen.

Das folgende Codebeispiel zeigt die Verwendung der Klassen [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) und [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) zum Laden der [Quell-JSON-Datei](SampleJson.json) und erzeugt die [Ausgabedatei im CSV-Format](SampleJson_out.csv).

## Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
