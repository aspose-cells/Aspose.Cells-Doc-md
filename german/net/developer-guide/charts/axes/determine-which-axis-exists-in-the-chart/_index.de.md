---
title: Bestimmen Sie, welche Achse im Diagramm vorhanden ist
description: Erfahren Sie, wie Sie feststellen, welche Achse in einem mit Aspose.Cells for .NET erstellten Diagramm vorhanden ist. Unser Leitfaden hilft Ihnen zu verstehen, wie Sie die verschiedenen Achsen in einem Diagramm identifizieren und darauf zugreifen, einschließlich Kategorie-, Wert- und Sekundärachsen.
keywords: Aspose.Cells for .NET, chart, axis, existence, category, value, secondary.
type: docs
weight: 140
url: /de/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

Manchmal muss der Benutzer wissen, ob eine bestimmte Achse im Diagramm vorhanden ist. Er möchte beispielsweise wissen, ob im Diagramm eine sekundäre Wertachse vorhanden ist oder nicht. Einige Diagramme wie Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded usw. haben keine Achse.

 Aspose.Cells bietet[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) Methode, um zu bestimmen, ob das Diagramm eine bestimmte Achse hat oder nicht.

{{% /alert %}}

 Der folgende Beispielcode demonstriert die Verwendung von[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)um festzustellen, ob das Beispieldiagramm über eine primäre und sekundäre Kategorie und Werteachse verfügt.

##  C#-Code, um zu bestimmen, welche Achse im Diagramm vorhanden ist

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Durch den Beispielcode generierte Konsolenausgabe

Unten wird die Konsolenausgabe des Codes angezeigt, die für die primäre Kategorie und die Wertachse „true“ und für die sekundäre Kategorie und die Wertachse „false“ anzeigt.

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
