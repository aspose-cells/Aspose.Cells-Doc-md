---
title: Optimierung des Speicherverbrauchs beim Arbeiten mit großen Dateien und großen Datensätzen
type: docs
weight: 180
url: /de/python-net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Beim Erstellen eines Arbeitsbuchs mit großen Datenmengen oder beim Lesen einer großen Microsoft Excel-Datei ist die gesamte RAM-Menge, die der Prozess beansprucht, stets ein Thema. Es gibt Maßnahmen, die angepasst werden können, um die Herausforderung zu bewältigen. Aspose.Cells for Python via .NET bietet relevante Optionen und API-Aufrufe, um den Speicherverbrauch zu senken, zu reduzieren und zu optimieren. Dadurch kann der Prozess effizienter laufen und schneller sein.

Verwenden Sie die [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting)-Option, um den Speicherverbrauch für Zelleninhalte zu optimieren und die Gesamtspeicherkosten zu senken. Beim Erstellen eines großen Datensatzes für Zellen können Sie im Vergleich zur Verwendung der Standardeinstellung ([**MemorySetting.NORMAL**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting)) eine bestimmte Menge Speicher einsparen.

{{% /alert %}}

## **Speicheroptimierung**

### **Lesen großer Excel-Dateien**

Das folgende Beispiel zeigt, wie eine große Microsoft Excel-Datei im optimierten Modus gelesen wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.py" >}}

### **Schreiben großer Excel-Dateien**

Das folgende Beispiel zeigt, wie Sie ein großes Datenset im optimierten Modus in ein Arbeitsblatt schreiben.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OptimizingMemoryUsage-WritingLargeExcelFiles-1.py" >}}

## **Vorsicht**

Die Standardoption, [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) wird für alle Versionen angewendet. In einigen Situationen, wie dem Erstellen einer Arbeitsmappe mit einem großen Datensatz für Zellen, kann die Option [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) den Speicherverbrauch optimieren und die Speicherkosten für die Anwendung verringern. Diese Option kann jedoch in einigen speziellen Fällen die Leistung beeinträchtigen.

1. **Zufälliger und wiederholter Zugriff auf Zellen**: Die effizienteste Sequenz für den Zugriff auf die Zellensammlung ist Zelle für Zelle in einer Zeile und dann Zeile für Zeile. Insbesondere wenn Sie Zeilen/Zellen über den Enumerator, der von [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), [**RowCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/rowcollection) und [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) erworben wurde, abrufen, wird die Leistung mit [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) maximiert.
1. **Einfügen & Löschen von Zellen & Zeilen**: Bitte beachten Sie, dass bei vielen Einfüge/Löschvorgängen für Zellen/Zeilen die Leistungseinbuße im *MemoryPreference*-Modus im Vergleich zum *Normal*-Modus spürbar sein wird.
1. **Arbeiten mit verschiedenen Zelltypen**: Wenn die meisten Zellen Zeichenfolgen oder Formeln enthalten, wird der Speicherverbrauch wie im *Normal*-Modus sein, aber wenn es viele leere Zellen gibt oder Zellwerte numerisch, boolesch usw. sind, wird die Option [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) eine bessere Leistung bieten.

