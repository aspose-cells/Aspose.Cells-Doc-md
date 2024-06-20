---
title: Optimierung des Speicherverbrauchs beim Arbeiten mit großen Dateien und großen Datensätzen
type: docs
weight: 110
url: /de/nodejs-java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Beim Erstellen eines Arbeitsmappen mit großen Datensätzen oder beim Lesen einer großen Microsoft Excel-Datei ist die Gesamtmenge an RAM, die der Prozess benötigt, immer ein Anliegen. Es gibt Maßnahmen, die zur Bewältigung der Herausforderung angepasst werden können. Aspose.Cells bietet einige relevante Optionen und API-Aufrufe, um den Speicherverbrauch zu verringern, zu reduzieren und zu optimieren. Außerdem kann es dem Prozess helfen, effizienter zu arbeiten und schneller zu laufen.

Verwenden Sie die [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)-Option, um den Speicherplatz für Zellendaten zu optimieren und die Gesamtspeicherkosten zu senken. Beim Erstellen großer Datensätze für Zellen kann dies im Vergleich zur Verwendung der Standardeinstellung [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) eine bestimmte Menge an Speicherplatz sparen.

{{% /alert %}}

## **Speicheroptimierung**

Das folgende Beispiel zeigt, wie der Speicherverbrauch beim Arbeiten mit großen Daten in Aspose.Cells für Node.js via Java optimiert werden kann.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-nodejs-optimize-memory-usage-while-working-with-large-data.java" >}}

## **Vorsicht**

Die Standardeinstellung [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) wird für alle Versionen angewendet. Für einige Situationen, wie das Erstellen einer Arbeitsmappe mit einem großen Datensatz für Zellen, kann die Option [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) den Speicherplatz optimieren und die Speicherkosten für die Anwendung senken. Diese Option kann jedoch die Leistung in einigen speziellen Fällen wie folgt beeinträchtigen.

1. **Zufälliger und wiederholter Zugriff auf Zellen**: Die effizienteste Sequenz für den Zugriff auf die Zellensammlung ist Zelle für Zelle in einer Zeile und dann Zeile für Zeile. Insbesondere wenn Sie Zeilen/Zellen über den Enumerator, der von [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) und [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) erworben wurde, abrufen, wird die Leistung mit [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) maximiert.
1. **Einfügen & Löschen von Zellen & Zeilen**: Bitte beachten Sie, dass bei vielen Einfüge-/Löschvorgängen für Zellen/Zeilen die Leistungseinbußen für den [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)-Modus im Vergleich zum [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)-Modus spürbar sein werden.
1. **Arbeiten mit verschiedenen Zellentypen**: Wenn die meisten Zellen Zeichenfolgenwerte oder Formeln enthalten, wird der Speicherverbrauch dem des [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)-Modus entsprechen. Wenn jedoch viele leere Zellen vorhanden sind oder Zellwerte numerisch, boolesch usw. sind, wird die Option [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) eine bessere Leistung bieten.

