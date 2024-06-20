---
title: Konvertieren Sie JSON in CSV
type: docs
weight: 210
url: /de/net/convert-json-to-csv/
---

## **JSON in CSV konvertieren**

Aspose.Cells unterstützt die Konvertierung von einfachen sowie verschachtelten JSONs in CSV. Hierfür bietet die API die [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)- und [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)-Klassen. Die [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)-Klasse bietet Optionen für das JSON-Layout wie [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle) (ignoriert den Titel, wenn das Array eine Eigenschaft eines Objekts ist) oder [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable) (verarbeitet das Array als Tabelle). Die [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)-Klasse verarbeitet das JSON unter Verwendung der mit der [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)-Klasse festgelegten Layoutoptionen.

Der folgende Beispielcode zeigt die Verwendung der [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)- und [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)-Klassen zum Laden der [Quell-JSON-Datei](104398869.json) und erzeugt die [Ausgabe-CSV-Datei](104398870.csv).

### **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
