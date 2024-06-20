---
title: Bestimmen Sie, welche Achse im Diagramm vorhanden ist
description: Erfahren Sie, wie Sie bestimmen können, welche Achse in einem mit Aspose.Cells for .NET erstellten Diagramm existiert. Unser Leitfaden hilft Ihnen zu verstehen, wie Sie auf die verschiedenen Achsen in einem Diagramm, einschließlich Kategorie , Wert und sekundäre Achsen, zugreifen und diese identifizieren können.
keywords: Aspose.Cells for .NET, Diagramm, Achse, Existenz, Kategorie, Wert, Sekundär.
type: docs
weight: 140
url: /de/net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Manchmal muss der Benutzer wissen, ob eine bestimmte Achse im Diagramm vorhanden ist. Zum Beispiel möchte er wissen, ob eine sekundäre Wertachse im Diagramm existiert oder nicht. Einige Diagramme wie Kuchen, explodierender Kuchen, KuchenKuchen, Kuchenspalte, 3D-Kuchen, 3D-explosierter Kuchen, Donut, explodierender Donut usw. haben keine Achse.

Aspose.Cells stellt die Methode [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) bereit, um festzustellen, ob das Diagramm eine bestimmte Achse hat oder nicht.

{{% /alert %}}

Der folgende Beispielcode zeigt die Verwendung von [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) zur Bestimmung, ob das Beispieldiagramm primäre und sekundäre Kategorie- und Wertachsen hat.

## C#-Code, um festzustellen, welche Achse im Diagramm existiert

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Von dem Beispielcode generierte Konsolenausgabe

Die Konsolenausgabe des Codes zeigt unten, dass für die primäre Kategorie- und Wertachse true und für die sekundäre Kategorie- und Wertachse false angezeigt wird.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
