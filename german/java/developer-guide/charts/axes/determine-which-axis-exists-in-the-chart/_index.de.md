---
title: Bestimmen Sie, welche Achse im Diagramm vorhanden ist
type: docs
weight: 130
url: /de/java/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Manchmal muss der Benutzer wissen, ob eine bestimmte Achse im Diagramm existiert. Zum Beispiel möchte er wissen, ob eine sekundäre Wertachse im Diagramm vorhanden ist oder nicht. Einige Diagramme wie Kuchen, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded usw. haben keine Achse.

Aspose.Cells stellt die Methode [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis-int-boolean-) bereit, um festzustellen, ob das Diagramm eine bestimmte Achse hat oder nicht.

{{% /alert %}}

## Bestimmen Sie, welche Achse im Diagramm existiert

Der folgende Screenshot zeigt ein Diagramm, das nur die primäre Kategorie- und Wertachse hat. Es hat keine sekundäre Kategorie- und Wertachse.

![todo:image_alt_text](determine-which-axis-exists-in-the-chart_1.png)

Der folgende Beispielcode zeigt die Verwendung von [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis-int-boolean-), um festzustellen, ob das Beispieldiagramm eine primäre und sekundäre Kategorie- und Wertachse hat. Die Konsolenausgabe des Codes wird unten angezeigt, die true für primäre Kategorie- und Wertachse und false für sekundäre Kategorie- und Wertachse anzeigt.

### Java-Code, um festzustellen, welche Achsen im Diagramm existieren

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### Von der Beispiellösung generierte Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
