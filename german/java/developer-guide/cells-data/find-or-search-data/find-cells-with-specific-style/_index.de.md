---
title: Zellen mit bestimmten Stil finden
type: docs
weight: 80
url: /de/java/find-cells-with-specific-style/
description: Dieser Artikel zeigt, wie man Zellen mit einem bestimmten Stil unter Verwendung von MS Excel und Aspose.Cells for Java API finden kann.
keywords: Zellen mit bestimmtem Stil finden, Zellen mit bestimmtem Stil in Excel finden, Zellen mit bestimmtem Stil in Excel Java finden, Zellen mit bestimmtem Stil suchen, in Excel nach Zellen mit bestimmtem Stil suchen, in Excel mit bestimmtem Stil in Excel Java suchen, wie man Zellen mit bestimmtem Stil findet, wie man Zellen mit bestimmtem Stil in Excel findet, wie man Zellen mit bestimmtem Stil in Excel Java findet
---

{{% alert color="primary" %}}

Manchmal müssen Sie die Zellen mit einem bestimmten Stil finden. Dieser Artikel zeigt, wie Sie dies unter Verwendung von Microsoft Excel sowie der Aspose.Cells for Java API erreichen können.

{{% /alert %}}

## Verwendung von Microsoft Excel

Dies sind die Schritte, die erforderlich sind, um Zellen mit bestimmten Stilen in MS Excel zu suchen.

1. Wählen Sie **Suchen & Auswählen** im **Start-Tab** aus.
1. Wählen Sie **Suchen** aus.
1. Klicken Sie auf **Optionen**, wenn erweiterte Optionen nicht sichtbar sind.
1. Wählen Sie **Format aus Zelle übernehmen...** aus dem **Format**-Dropdown.
1. Wählen Sie die Zelle mit dem gewünschten Stil zum Suchen aus.
1. Klicken Sie auf **Alle finden**, um alle Zellen mit einem ähnlichen Stil wie Ihre ausgewählte Zelle zu finden.

## Verwendung von Aspose.Cells for Java

Aspose.Cells for Java bietet die Funktion, Zellen im Arbeitsblatt mit einem bestimmten Stil zu finden. Hierfür stellt die API die Eigenschaft [**FindOptions.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style) bereit.

### Beispielcode

Der folgende Codeausschnitt findet alle Zellen, die denselben Stil wie die Zelle **A1** haben, und ändert den Text in diesen Zellen. Bitte beachten Sie das Screenshot der Quell- und Ausgabedateien, um das Ergebnis des Beispielscodes zu analysieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

Nach der Ausführung des Codes werden alle Zellen, die denselben Stil wie die Zelle A1 haben, den Text "Gefunden" enthalten.

### Bildschirmfotos

![todo:image_alt_text](find-cells-with-specific-style_1.png)

**Abbildung:** Quelldatei mit Zellen, die Stile haben

Dies ist die Ausgabedatei, die durch den folgenden Code generiert wurde. Sie können alle Zellen sehen, die den gleichen Stil wie die Zelle **A1** haben, haben einen Text "Gefunden".

![todo:image_alt_text](find-cells-with-specific-style_2.png)

**Abbildung:** Ausgabedatei mit gefundenen Zellen nach der Suche nach dem Stil **A1**
{{< app/cells/assistant language="java" >}}
