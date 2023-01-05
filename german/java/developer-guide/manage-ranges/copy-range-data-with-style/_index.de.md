---
title: Bereichsdaten mit Stil kopieren
type: docs
weight: 340
url: /de/java/copy-range-data-with-style/
---
{{% alert color="primary" %}} 

[Nur Bereichsdaten kopieren](/cells/de/java/copy-range-data-only/) erklärt, wie man die Daten aus einem Zellbereich in einen anderen Bereich kopiert. Aspose.Cells kann auch einen Bereich komplett mit Formatierung kopieren. Dieser Artikel erklärt, wie.

{{% /alert %}} 
## **Bereichsdaten mit Stil kopieren**
Aspose.Cells bietet eine Reihe von Klassen und Methoden für die Arbeit mit Bereichen, z. B.[createRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), [StyleFlag](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [applyStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\)), etc.

Dieses Beispiel:

1. Erstellt eine Arbeitsmappe.
1. Füllt eine Reihe von Zellen im ersten Arbeitsblatt mit Daten.
1. Erstellt einen Bereich.
1. Erstellt ein Stilobjekt mit angegebenen Formatierungsattributen.
1. Wendet den Stil auf den Datenbereich an.
1. Erstellt einen zweiten Zellbereich.
1. Kopiert Daten mit der Formatierung aus dem ersten Bereich in den zweiten Bereich.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

