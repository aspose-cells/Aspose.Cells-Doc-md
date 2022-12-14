---
title: Konvertieren Sie JSON in CSV
type: docs
weight: 210
url: /de/net/convert-json-to-csv/
---
## **Konvertieren Sie JSON in CSV**

Aspose.Cells unterstützt die Konvertierung von einfachem sowie verschachteltem JSON in CSV. Dafür sorgt die API**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)** und**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** Klassen. Das**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**Die Klasse bietet die Optionen für das JSON-Layout wie z**[IgnoreArrayTitle](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)**(ignoriert den Titel, wenn das Array eine Eigenschaft eines Objekts ist) oder**[ArrayAsTable](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arraystable)**(verarbeitet das Array als Tabelle). Das**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**-Klasse verarbeitet den JSON-Code mithilfe der Layoutoptionen, die mit der festgelegt wurden**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**Klasse.

Das folgende Codebeispiel veranschaulicht die Verwendung von**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**und**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**Klassen zum Laden der[Quell-JSON-Datei](104398869.json) und generiert die[CSV-Datei ausgeben](104398870.csv).

### **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
