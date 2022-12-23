---
title: Optimieren der Speichernutzung beim Arbeiten mit großen Dateien mit großen Datensätzen
type: docs
weight: 110
url: /de/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

Beim Erstellen einer Arbeitsmappe mit großen Datensätzen oder beim Lesen einer großen Microsoft-Excel-Datei ist die Gesamtmenge an RAM, die der Prozess benötigt, immer ein Problem. Es gibt Maßnahmen, die an die Herausforderung angepasst werden können. Aspose.Cells bietet einige relevante Optionen und API fordert dazu auf, die Speichernutzung zu senken, zu reduzieren und zu optimieren. Außerdem kann es dazu beitragen, dass der Prozess effizienter arbeitet und schneller abläuft.

 Verwenden[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) Option zum Optimieren des Speichers, der für Zellendaten verwendet wird, um die Gesamtspeicherkosten zu senken. Beim Erstellen eines großen Datensatzes für Zellen kann im Vergleich zur Verwendung der Standardeinstellung eine gewisse Menge an Speicher eingespart werden[**Speichereinstellung.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **Speicher optimieren**

### **Große Excel-Dateien lesen**

Das folgende Beispiel zeigt, wie eine große Microsoft-Excel-Datei im optimierten Modus gelesen wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadLargeExcelFiles-ReadLargeExcelFiles.java" >}}

### **Schreiben großer Excel-Dateien**

Das folgende Beispiel zeigt, wie ein großes Dataset im optimierten Modus in ein Arbeitsblatt geschrieben wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-WritingLargeExcelFiles-WritingLargeExcelFiles.java" >}}

## **Vorsicht**

 Die Standardoption,[**Speichereinstellung.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)gilt für alle Versionen. In einigen Situationen, z. B. beim Erstellen einer Arbeitsmappe mit einem großen Datensatz für Zellen, ist die[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)Option kann die Speichernutzung optimieren und die Speicherkosten für die Anwendung senken. Diese Option kann jedoch in einigen Sonderfällen wie den folgenden die Leistung beeinträchtigen.

1. **Zufälliger und wiederholter Zugriff auf Cells** : Die effizienteste Reihenfolge für den Zugriff auf die Zellensammlung ist Zelle für Zelle in einer Zeile und dann Zeile für Zeile. Vor allem, wenn Sie auf Zeilen/Zellen zugreifen, die vom Enumerator stammen[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) und[**Reihe**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) , würde die Leistung mit maximiert werden[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE).
1. **Einfügen und Löschen von Cells und Zeilen** : Bitte beachten Sie, dass bei vielen Einfüge-/Löschvorgängen für Cells/Rows die Leistungseinbußen spürbar sind[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) Modus im Vergleich zum[**Speichereinstellung.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)Modus.
1. **Betrieb auf verschiedenen Cell-Typen** : Wenn die meisten Zellen Zeichenfolgenwerte oder Formeln enthalten, sind die Speicherkosten gleich[**Speichereinstellung.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)Modus, aber wenn es viele leere Zellen gibt oder Zellwerte numerisch, bool und so weiter sind, wird die[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)Option wird eine bessere Leistung geben.
