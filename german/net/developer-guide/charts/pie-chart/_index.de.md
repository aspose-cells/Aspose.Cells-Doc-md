---
title: Kreisdiagramm mit Führungslinien erstellen
linktitle: Kuchendiagramm
type: docs
weight: 45
url: /de/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

 In diesem Artikel wird erläutert, wie Sie ein Kreisdiagramm mit Führungslinien von Grund auf neu erstellen, während Sie Aspose.Cells for .NET API verwenden. In Excel ist die Option „Führungslinien anzeigen“ standardmäßig aktiviert, sodass beim Erstellen eines Kreisdiagramms in Excel die Führungslinien angezeigt werden. Beim Erstellen eines ähnlichen Diagramms mit Aspose.Cells-APIs müssen Sie jedoch explizit festlegen[**Serie.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) Eigentum.

{{% /alert %}}

Um die Verwendung von Aspose.Cells for .NET API zum Erstellen eines Kreisdiagramms mit Führungslinien zu demonstrieren, erstellen wir zunächst ein neues[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) und geben Sie einige Daten ein, die als Datenquelle für die Serie dienen. Sobald die Daten vorhanden sind, werden wir a hinzufügen[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) des Typs[**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)zur Sammlung von Diagrammen und stellen Sie die verschiedenen Aspekte ein, um die gewünschte Diagrammansicht zu erhalten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Bisher haben wir ein Tortendiagramm erstellt und seine verschiedenen Aspekte festgelegt. Jetzt werden wir die Führungslinien für das Diagramm einschalten. Bitte beachten Sie, dass wir die Datenbeschriftungen ein wenig verschieben müssen, um die Führungslinien anzuzeigen.

Der folgende Codeabschnitt aktiviert die Führungslinien, aktualisiert das Diagramm und berechnet dann die Positionen der Datenbeschriftungen, um sie entsprechend zu verschieben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Schließlich speichert der folgende Code das Diagramm im Bildformat und die Arbeitsmappe im XLSX-Format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Resultierendes Kreisdiagramm**|
|:- |
|![todo: Bild_alt_Text](creating-pie-chart-with-leader-lines_1.png)|

## **Themen vorantreiben**
- [Benutzerdefinierte Segment- oder Sektorfarben im Kreisdiagramm](/cells/de/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Finden Sie heraus, ob sich Datenpunkte im zweiten Kreis oder Balken auf einem Kreisdiagramm oder Balkendiagramm befinden](/cells/de/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Zum Thema passende Artikel

- [Erstellen von Diagrammen](/cells/de/net/creating-charts/)
- [Anpassen von Diagrammen](/cells/de/net/customizing-charts/)
- [Datenformatierung in Diagrammen](/cells/de/net/data-formatting-in-charts/)
- [Darstellung des Diagramms einstellen](/cells/de/net/setting-chart-appearance/)

