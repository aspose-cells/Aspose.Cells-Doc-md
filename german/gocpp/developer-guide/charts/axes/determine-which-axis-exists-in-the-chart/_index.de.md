---
title: Bestimmen Sie, welche Achse im Diagramm mit Golang über C++ vorhanden ist
description: Lernen Sie, wie man erkennt, welche Achse in einem mit Aspose.Cells for C++ erstellten Diagramm vorhanden ist. Unser Leitfaden hilft Ihnen zu verstehen, wie man die verschiedenen Achsen in einem Diagramm identifiziert und zugänglich macht, einschließlich Kategorie , Wert und Sekundärachsen.
keywords: Aspose.Cells for C++, Diagramm, Achse, Existenz, Kategorie, Wert, Sekundärachse.
type: docs
weight: 140
url: /de/go-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Manchmal muss der Benutzer wissen, ob eine bestimmte Achse im Diagramm vorhanden ist. Zum Beispiel möchte er wissen, ob eine sekundäre Wertachse im Diagramm existiert oder nicht. Einige Diagramme wie Kuchen, explodierender Kuchen, KuchenKuchen, Kuchenspalte, 3D-Kuchen, 3D-explosierter Kuchen, Donut, explodierender Donut usw. haben keine Achse.

Aspose.Cells stellt die Methode [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) bereit, um festzustellen, ob das Diagramm eine bestimmte Achse hat oder nicht.

{{% /alert %}}

Das folgende Beispiel zeigt, wie [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) verwendet wird, um zu bestimmen, ob das Beispiel-Diagramm primäre und sekundäre Kategorie- und Wertachsen hat.

## C++-Code zur Bestimmung, welche Achse im Diagramm vorhanden ist

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetermineWhichAxisExistsInTheChart.go" >}}
## Von dem Beispielcode generierte Konsolenausgabe

Die Konsolenausgabe des Codes zeigt unten, dass für die primäre Kategorie- und Wertachse true und für die sekundäre Kategorie- und Wertachse false angezeigt wird.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
