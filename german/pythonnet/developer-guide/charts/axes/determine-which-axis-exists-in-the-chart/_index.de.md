---
title: Bestimmen Sie, welche Achse im Diagramm vorhanden ist
description: Erfahren Sie, wie Sie feststellen können, welche Achse in einem mit Aspose.Cells für Python via .NET erstellten Diagramm existiert. Unser Leitfaden hilft Ihnen, die verschiedenen Achsen in einem Diagramm zu identifizieren und darauf zuzugreifen, einschließlich Kategorie , Wert und Sekundärachsen.
keywords: Aspose.Cells für Python via .NET, Diagramm, Achse, Existenz, Kategorie, Wert, Sekundär.
type: docs
weight: 140
url: /de/python-net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Manchmal muss der Benutzer wissen, ob eine bestimmte Achse im Diagramm vorhanden ist. Zum Beispiel möchte er wissen, ob eine sekundäre Wertachse im Diagramm existiert oder nicht. Einige Diagramme wie Kuchen, explodierender Kuchen, KuchenKuchen, Kuchenspalte, 3D-Kuchen, 3D-explosierter Kuchen, Donut, explodierender Donut usw. haben keine Achse.

Aspose.Cells für Python via .NET bietet die Methode [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis), um festzustellen, ob das Diagramm eine bestimmte Achse hat oder nicht.

{{% /alert %}}

Der folgende Beispielcode zeigt die Verwendung von [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis) zur Bestimmung, ob das Beispieldiagramm primäre und sekundäre Kategorie- und Wertachsen hat.

## C#-Code, um festzustellen, welche Achse im Diagramm existiert

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DetermineAxisInChart.py" >}}

## Von dem Beispielcode generierte Konsolenausgabe

Die Konsolenausgabe des Codes zeigt unten, dass für die primäre Kategorie- und Wertachse true und für die sekundäre Kategorie- und Wertachse false angezeigt wird.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
