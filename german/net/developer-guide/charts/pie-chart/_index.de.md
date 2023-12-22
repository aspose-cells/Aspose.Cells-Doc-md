---
title: Kreisdiagramm mit Führungslinien erstellen
description: Erfahren Sie, wie Sie mit Aspose.Cells for .NET ein Kreisdiagramm mit Führungslinien in Microsoft Excel erstellen. Unser Leitfaden zeigt, wie Sie Führungslinien hinzufügen, die Datenpunkte mit der Legende verbinden und die Gesamtklarheit Ihres Diagramms verbessern.
keywords: Aspose.Cells for .NET, Pie Chart, Leader Lines, Microsoft Excel, Data Visualization, Chart Customization.
linktitle: Kuchendiagramm
type: docs
weight: 45
url: /de/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie Sie unter Verwendung von Aspose.Cells for .NET API ein Kreisdiagramm mit Führungslinien von Grund auf erstellen. In Excel ist die Option „Führungslinien anzeigen“ standardmäßig eingestellt, sodass beim Erstellen eines Kreisdiagramms in Excel die Führungslinien angezeigt werden. Beim Erstellen eines ähnlichen Diagramms mit Aspose.Cells-APIs müssen Sie jedoch explizit festlegen[**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) Eigentum.

{{% /alert %}}

 Um die Verwendung von Aspose.Cells for .NET API zum Erstellen eines Kreisdiagramms mit Führungslinien zu demonstrieren, erstellen wir zunächst ein neues[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) und geben Sie einige Daten ein, die als Seriendatenquelle dienen. Sobald die Daten vorhanden sind, fügen wir eine hinzu[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) vom Typ[**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)Klicken Sie auf die Sammlung von Diagrammen und legen Sie die verschiedenen Aspekte fest, um die gewünschte Diagrammansicht zu erhalten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Bisher haben wir ein Kreisdiagramm erstellt und seine verschiedenen Aspekte festgelegt. Jetzt werden wir die Führungslinien für das Diagramm aktivieren. Bitte beachten Sie, dass wir die Datenbeschriftungen ein wenig verschieben müssen, um die Führungslinien anzuzeigen.

Der folgende Codeteil aktiviert die Führungslinien, aktualisiert das Diagramm und berechnet dann die Positionen der Datenbeschriftungen, um sie entsprechend zu verschieben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Abschließend speichert der folgende Code das Diagramm im Bildformat und die Arbeitsmappe im Format XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Resultierendes Kreisdiagramm**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

##  **Vorabthemen**
- [Benutzerdefinierte Segment- oder Sektorfarben im Kreisdiagramm](/cells/de/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Finden Sie heraus, ob sich Datenpunkte im zweiten Kreis oder Balken eines Kreisdiagramms oder Balkendiagramms befinden](/cells/de/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

##  In Verbindung stehende Artikel

- [Diagramme erstellen](/cells/de/net/creating-charts/)
- [Anpassen von Diagrammen](/cells/de/net/customizing-charts/)
- [Datenformatierung in Diagrammen](/cells/de/net/data-formatting-in-charts/)
- [Festlegen der Darstellung des Diagramms](/cells/de/net/setting-chart-appearance/)

