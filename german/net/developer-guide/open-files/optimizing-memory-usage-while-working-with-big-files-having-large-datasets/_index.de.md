---
title: Optimieren der Speichernutzung beim Arbeiten mit großen Dateien mit großen Datensätzen
type: docs
weight: 180
url: /de/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

Beim Erstellen einer Arbeitsmappe mit großen Datensätzen oder beim Lesen einer großen Microsoft-Excel-Datei ist die Gesamtmenge an RAM, die der Prozess benötigt, immer ein Problem. Es gibt Maßnahmen, die angepasst werden können, um mit der Herausforderung fertig zu werden. Aspose.Cells bietet einige relevante Optionen und API fordert dazu auf, die Speichernutzung zu senken, zu reduzieren und zu optimieren. Außerdem kann es dazu beitragen, dass der Prozess effizienter arbeitet und schneller abläuft.

 Verwenden Sie die[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) Option zum Optimieren der Speichernutzung für Zelldaten und zum Senken der Gesamtspeicherkosten. Beim Erstellen eines großen Datensatzes für Zellen kann im Vergleich zur Verwendung der Standardeinstellung ([**Speichereinstellung.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)).

{{% /alert %}}

## **Speicher optimieren**

### **Große Excel-Dateien lesen**

Das folgende Beispiel zeigt, wie eine große Microsoft-Excel-Datei im optimierten Modus gelesen wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **Schreiben großer Excel-Dateien**

Das folgende Beispiel zeigt, wie ein großes Dataset in einem optimierten Modus in ein Arbeitsblatt geschrieben wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **Vorsicht**

 Die Standardoption,[**Speichereinstellung.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)gilt für alle Versionen. In einigen Situationen, z. B. beim Erstellen einer Arbeitsmappe mit einem großen Datensatz für Zellen, ist die[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)Option kann die Speichernutzung optimieren und die Speicherkosten für die Anwendung senken. Diese Option kann jedoch in einigen Sonderfällen wie den folgenden die Leistung beeinträchtigen.

1. **Zufälliger und wiederholter Zugriff auf Cells** : Die effizienteste Reihenfolge für den Zugriff auf die Zellensammlung ist Zelle für Zelle in einer Zeile und dann Zeile für Zeile. Vor allem, wenn Sie auf Zeilen/Zellen zugreifen, die vom Enumerator stammen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection) und[**Die Zeile**](https://reference.aspose.com/cells/net/aspose.cells/row) , würde die Leistung mit maximiert werden[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting).
1. **Einfügen und Löschen von Cells und Zeilen** : Bitte beachten Sie, dass bei vielen Einfüge-/Löschvorgängen für Cells/Rows die Leistungseinbußen spürbar sind*Speicherpräferenz* Modus im Vergleich zum*Normal*Modus.
1. **Betrieb auf verschiedenen Cell-Typen** : Wenn die meisten Zellen Zeichenfolgenwerte oder Formeln enthalten, sind die Speicherkosten gleich*Normal* Modus, aber wenn es viele leere Zellen gibt oder Zellwerte numerisch, bool und so weiter sind, wird die[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)Option wird eine bessere Leistung geben.
