---
title: Speicherverbrauch beim Arbeiten mit großen Dateien mit umfangreichen Datensätzen mit Golang via C++ optimieren
linktitle: Speicher optimieren
type: docs
weight: 180
url: /de/go-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
description: Lernen Sie, wie man den Speicherverbrauch beim Arbeiten mit großen Excel Dateien mit Aspose.Cells in Golang via C++ optimiert.
---

{{% alert color="primary" %}}

Beim Erstellen eines Arbeitsblatts mit großen Datensätzen oder beim Lesen einer großen Microsoft Excel-Datei ist die Gesamtmenge des RAMs, die der Prozess benötigt, immer ein Anliegen. Es gibt Maßnahmen, die ergriffen werden können, um mit der Herausforderung umzugehen. Aspose.Cells bietet einige relevante Optionen und API-Aufrufe, um den Speicherverbrauch zu verringern, zu reduzieren und zu optimieren. Außerdem kann dies helfen, den Prozess effizienter und schneller zu machen.

Verwenden Sie die [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/)-Option, um den Speicherverbrauch für Zelleninhalte zu optimieren und die Gesamtspeicherkosten zu senken. Beim Erstellen eines großen Datensatzes für Zellen können Sie im Vergleich zur Verwendung der Standardeinstellung ([**MemorySetting.Normal**](https://reference.aspose.com/cells/go-cpp/memorysetting/)) eine bestimmte Menge Speicher einsparen.

{{% /alert %}}

## **Speicheroptimierung**

### **Lesen großer Excel-Dateien**

Das folgende Beispiel zeigt, wie eine große Microsoft Excel-Datei im optimierten Modus gelesen wird.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OptimizingMemoryUsageWhileWorkingWithBigFilesHavingLargeDatasets.go" >}}
### **Schreiben großer Excel-Dateien**

Das folgende Beispiel zeigt, wie Sie ein großes Datenset im optimierten Modus in ein Arbeitsblatt schreiben.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OptimizingMemoryUsageWhileWorkingWithBigFilesHavingLargeDatasets-1.go" >}}
## **Vorsicht**

Die Standardoption, [**MemorySetting.Normal**](https://reference.aspose.com/cells/go-cpp/memorysetting/) wird für alle Versionen angewendet. In einigen Situationen, wie dem Erstellen einer Arbeitsmappe mit einem großen Datensatz für Zellen, kann die Option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) den Speicherverbrauch optimieren und die Speicherkosten für die Anwendung verringern. Diese Option kann jedoch in einigen speziellen Fällen die Leistung beeinträchtigen.

1. **Zufälliger und wiederholter Zugriff auf Zellen**: Die effizienteste Sequenz für den Zugriff auf die Zellensammlung ist Zelle für Zelle in einer Zeile und dann Zeile für Zeile. Insbesondere wenn Sie Zeilen/Zellen über den Enumerator, der von [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) und [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) erworben wurde, abrufen, wird die Leistung mit [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) maximiert.
1. **Einfügen & Löschen von Zellen & Zeilen**: Bitte beachten Sie, dass bei vielen Einfüge/Löschvorgängen für Zellen/Zeilen die Leistungseinbuße im *MemoryPreference*-Modus im Vergleich zum *Normal*-Modus spürbar sein wird.
1. **Arbeiten mit verschiedenen Zelltypen**: Wenn die meisten Zellen Zeichenfolgen oder Formeln enthalten, wird der Speicherverbrauch wie im *Normal*-Modus sein, aber wenn es viele leere Zellen gibt oder Zellwerte numerisch, boolesch usw. sind, wird die Option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) eine bessere Leistung bieten.
