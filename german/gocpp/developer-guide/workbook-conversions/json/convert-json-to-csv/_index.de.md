---
title: JSON in CSV mit Golang über C++ umwandeln
linktitle: Konvertieren Sie JSON in CSV
type: docs
weight: 210
url: /de/go-cpp/convert-json-to-csv/
description: Erfahren Sie, wie Sie JSON mit einfachen und verschachtelten JSON Beispielen mit Aspose.Cells for C++ in CSV konvertieren.
---

## **JSON in CSV konvertieren**

Aspose.Cells unterstützt die Konvertierung von einfachem sowie verschachteltem JSON in CSV. Hierfür stellt die API die Klassen [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) und [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) bereit. Die Klasse [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) bietet Optionen für das JSON-Layout wie [**SetIgnoreTitle**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/setignoretitle/) (ignoriert den Titel, wenn das Array eine Eigenschaft eines Objekts ist) oder [**GetArrayAsTable()**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/getarrayastable/) (verarbeitet das Array als Tabelle). Die Klasse [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) verarbeitet JSON unter Verwendung der mit [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) festgelegten Layout-Optionen.

Das folgende Codebeispiel demonstriert die Verwendung der Klassen [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) und [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/), um die [Quelldatei JSON](104398869.json) zu laden und die [Ausgabedatei CSV](104398870.csv) zu generieren.

### **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertJsonToCsv.go" >}}
