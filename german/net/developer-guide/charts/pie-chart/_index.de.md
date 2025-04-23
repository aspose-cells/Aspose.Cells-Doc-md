---
title: Erstellung eines Tortendiagramms mit Führungslinien
description: Erfahren Sie, wie Sie Aspose.Cells for .NET verwenden, um ein Tortendiagramm mit Führungslinien in Microsoft Excel zu erstellen. Unser Leitfaden wird zeigen, wie Sie Führungslinien hinzufügen, die Datenpunkte mit der Legende verbinden und die Gesamtübersicht Ihres Diagramms verbessern.
keywords: Aspose.Cells for .NET, Tortendiagramm, Führungslinien, Microsoft Excel, Datenvisualisierung, Diagrammanpassung.
linktitle: Tortendiagramm
type: docs
weight: 45
url: /de/net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Dieser Artikel erklärt, wie man ein Tortendiagramm mit Führungslinien von Grund auf mit der Aspose.Cells for .NET-API erstellt. In Excel ist die Option 'Führungslinien anzeigen' standardmäßig eingestellt, sodass beim Erstellen eines Tortendiagramms in Excel die Führungslinien angezeigt werden. Wenn Sie jedoch ein ähnliches Diagramm mit Aspose.Cells-APIs erstellen, müssen Sie die [**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines)-Eigenschaft explizit festlegen.

{{% /alert %}}

Um die Verwendung der Aspose.Cells for .NET-API zum Erstellen eines Tortendiagramms mit Führungslinien zu demonstrieren, werden wir zuerst ein neues [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) erstellen und einige Daten eingeben, die als Datenquelle für die Serie dienen. Sobald die Daten bereit sind, fügen wir ein [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) vom Typ [**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) zur Sammlung von Diagrammen hinzu und setzen dessen verschiedene Aspekte, um die gewünschte Diagrammansicht zu erhalten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Bisher haben wir ein Tortendiagramm erstellt und seine verschiedenen Aspekte festgelegt. Jetzt werden wir die Führungslinien für das Diagramm einschalten. Bitte beachten Sie, dass wir die Datenbeschriftungen ein wenig verschieben müssen, um die Führungslinien anzuzeigen.

Der folgende Code aktiviert die Führungslinien, aktualisiert das Diagramm und berechnet dann die Positionen der Datenbeschriftungen, um sie entsprechend zu verschieben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Abschließend speichert der folgende Code das Diagramm im Bildformat und die Arbeitsmappe im XLSX-Format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Ergebnis Tortendiagramm**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Erweiterte Themen**
- [Benutzerdefinierte Farben für Tortenstücke oder Sektoren in einem Tortendiagramm](/cells/de/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Herausfinden, ob Datenpunkte in der zweiten Torte oder Balken in einem Tortendiagramm der Torten oder Balken sind](/cells/de/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Verwandte Artikel

- [Erstellen von Diagrammen](/cells/de/net/creating-charts/)
- [Diagramme anpassen](/cells/de/net/customizing-charts/)
- [Datenformatierung in Diagrammen](/cells/de/net/data-formatting-in-charts/)
- [Diagrammaussehen festlegen](/cells/de/net/setting-chart-appearance/)

{{< app/cells/assistant language="csharp" >}}
