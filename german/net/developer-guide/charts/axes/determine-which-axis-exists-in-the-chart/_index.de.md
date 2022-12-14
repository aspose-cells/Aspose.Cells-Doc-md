---
title: Bestimmen Sie, welche Achse im Diagramm vorhanden ist
type: docs
weight: 140
url: /de/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

Manchmal muss der Benutzer wissen, ob eine bestimmte Achse im Diagramm vorhanden ist. Beispielsweise möchte er wissen, ob eine sekundäre Wertachse im Diagramm vorhanden ist oder nicht. Einige Diagramme wie Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded usw. haben keine Achse.

 Aspose.Cells bietet[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) Methode, um festzustellen, ob das Diagramm eine bestimmte Achse hat oder nicht.

{{% /alert %}}

 Der folgende Beispielcode demonstriert die Verwendung von[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)um festzustellen, ob das Beispieldiagramm eine primäre und sekundäre Kategorie und Wertachse hat.

## C#-Code, um zu bestimmen, welche Achse im Diagramm vorhanden ist

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Vom Beispielcode generierte Konsolenausgabe

Die Konsolenausgabe des Codes wurde unten gezeigt, die wahr für die primäre Kategorie und die Wertachse und falsch für die sekundäre Kategorie und die Wertachse anzeigt.

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
