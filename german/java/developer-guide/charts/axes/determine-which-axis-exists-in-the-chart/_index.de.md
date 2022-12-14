---
title: Bestimmen Sie, welche Achse im Diagramm vorhanden ist
type: docs
weight: 130
url: /de/java/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

Manchmal muss der Benutzer wissen, ob eine bestimmte Achse im Diagramm vorhanden ist. Beispielsweise möchte er wissen, ob eine sekundäre Wertachse im Diagramm vorhanden ist oder nicht. Einige Diagramme wie Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded usw. haben keine Achse.

 Aspose.Cells bietet[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean))-Methode, um festzustellen, ob das Diagramm eine bestimmte Achse hat oder nicht.

{{% /alert %}}

## Bestimmen Sie, welche Achse im Diagramm vorhanden ist

Der folgende Screenshot zeigt ein Diagramm, das nur die primäre Kategorie und die Wertachse enthält. Es hat keine sekundäre Kategorie und Wertachse.

![todo: Bild_alt_Text](determine-which-axis-exists-in-the-chart_1.png)

 Der folgende Beispielcode demonstriert die Verwendung von[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)), um zu bestimmen, ob das Beispieldiagramm eine primäre und sekundäre Kategorie und Wertachse hat. Die Konsolenausgabe des Codes wurde unten gezeigt, die wahr für die primäre Kategorie und die Wertachse und falsch für die sekundäre Kategorie und die Wertachse anzeigt.

### Java-Code, um zu bestimmen, welche Achse im Diagramm vorhanden ist

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### Vom Beispielcode generierte Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
