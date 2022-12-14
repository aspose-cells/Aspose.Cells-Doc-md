---
title: Finden Sie Zellen mit einem bestimmten Stil
type: docs
weight: 80
url: /de/java/find-cells-with-specific-style/
description: Dieser Artikel zeigt, wie Sie Zellen mit einem bestimmten Stil mit MS Excel und Aspose.Cells for Java API finden.
keywords: find cells with specific style, find cells with specific style excel, find cells with specific style excel java, search cells with specific style, search cells with specific style excel, search cells with specific style excel java, how to find cells with specific style, how to find cells with specific style excel, how to find cells with specific style excel java
---
{{% alert color="primary" %}}

Manchmal müssen Sie die Zellen mit einem bestimmten Stil finden. Dieser Artikel zeigt, wie Sie dies erreichen, indem Sie Microsoft Excel sowie Aspose.Cells for Java API verwenden.

{{% /alert %}}

## Mit Microsoft Excel

Dies sind die Schritte, die zum Suchen von Zellen mit bestimmten Stilen in MS Excel erforderlich sind.

1.  Auswählen**Suchen & auswählen** in dem**Startseite**.
1.  Auswählen**Finden**.
1.  Klicken**Optionen**wenn erweiterte Optionen nicht sichtbar sind.
1.  Auswählen**Wählen Sie das Format aus Cell...** von dem**Format** Dropdown-Liste.
1. Wählen Sie die Zelle mit dem Stil aus, den Sie durchsuchen möchten.
1.  Klicken**Finde alle** , um alle Zellen mit ähnlichem Stil wie die ausgewählte Zelle zu finden.

## Mit Aspose.Cells for Java

 Aspose.Cells for Java bietet die Funktion, Zellen in Arbeitsblättern mit einem bestimmten Stil zu finden. Dafür sorgt die API[**FindOptions.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style) Eigentum.

### Beispielcode

 Das folgende Code-Snippet findet alle Zellen, die denselben Stil wie cell haben**A1** und ändert den Text in diesen Zellen. Bitte sehen Sie sich den Screenshot der Quell- und Ausgabedateien an, um die Ausgabe des Beispielcodes zu analysieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

Nach der Ausführung des Codes haben alle Zellen, die denselben Stil wie Zelle A1 haben, einen Text "Gefunden".

### Screenshots

![todo: Bild_alt_Text](find-cells-with-specific-style_1.png)

**Figur:** Quelldatei mit Zellen mit Stilen

 Hier ist die Ausgabedatei, die durch den folgenden Code generiert wird. Sie können alle Zellen sehen, die denselben Stil wie Zelle haben**A1** hat einen Text "Gefunden"

![todo: Bild_alt_Text](find-cells-with-specific-style_2.png)

**Figur:**Ausgabedatei mit gefundenen Zellen nach Suche nach**A1** Stil
