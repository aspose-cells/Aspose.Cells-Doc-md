---
title: Bereichsdaten mit Format kopieren
type: docs
weight: 340
url: /de/java/copy-range-data-with-style/
---

{{% alert color="primary" %}} 

[Nur Bereichsdaten kopieren](/cells/de/java/copy-range-data-only/) erläutert, wie Sie die Daten von einem Zellenbereich in einen anderen kopieren können. Aspose.Cells kann auch einen Bereich komplett mit Formatierung kopieren. Dieser Artikel erläutert wie.

{{% /alert %}} 
## **Datenbereich mit Stil kopieren**
Aspose.Cells bietet eine Reihe von Klassen und Methoden zum Arbeiten mit Bereichen an, zum Beispiel [createRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), [StyleFlag](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [applyStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\)), usw.

Dieses Beispiel:

1. Erstellt ein Arbeitsblatt.
1. Füllt eine Anzahl von Zellen im ersten Arbeitsblatt mit Daten.
1. Erstellt einen Bereich.
1. Erstellt ein Style-Objekt mit angegebenen Formatierungseigenschaften.
1. Wendet den Stil auf den Datenbereich an.
1. Erstellt einen zweiten Zellenbereich.
1. Kopiert Daten mit Formatierung aus dem ersten Bereich in den zweiten Bereich.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

