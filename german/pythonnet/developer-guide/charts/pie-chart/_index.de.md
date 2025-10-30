---
title: Erstellung eines Tortendiagramms mit Führungslinien
description: Erfahren Sie, wie Sie mit Aspose.Cells für Python via .NET ein Kreisdiagramm mit Führungslinien in Microsoft Excel erstellen. Unser Leitfaden zeigt, wie Führungslinien hinzugefügt werden, die Datenpunkte mit der Legende verbinden und die Übersichtlichkeit Ihres Diagramms verbessern.
keywords: Aspose.Cells für Python via .NET, Kreisdiagramm, Führungslinien, Microsoft Excel, Datenvisualisierung, Diagrammanpassung.
linktitle: Tortendiagramm
type: docs
weight: 45
url: /de/python-net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Dieser Artikel erklärt, wie man ein Kreisdiagramm mit Führungslinien von Grund auf erstellt, während man die Aspose.Cells für Python via .NET API verwendet. In Excel ist die Option 'Führungslinien anzeigen' standardmäßig aktiviert, sodass beim Erstellen eines Kreisdiagramms in Excel die Führungslinien angezeigt werden. Bei der Erstellung eines ähnlichen Diagramms mit Aspose.Cells für Python via .NET-APIs müssen Sie jedoch die [**Series.has_leader_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/has_leader_lines)-Eigenschaft explizit setzen.

{{% /alert %}}

Um die Verwendung von Aspose.Cells für Python via .NET API zum Erstellen eines Kuchendiagramms mit Leitlinien zu demonstrieren, erstellen wir zunächst eine neue [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) und geben einige Daten ein, die als Datenquelle für die Serie dienen. Sobald die Daten vorhanden sind, fügen wir eine [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) vom Typ [**ChartType.PIE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype/) zur Sammlung der Diagramme hinzu und stellen ihre verschiedenen Aspekte ein, um die gewünschte Diagrammansicht zu erhalten.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateWorkbook.py" >}}

Bisher haben wir ein Tortendiagramm erstellt und seine verschiedenen Aspekte festgelegt. Jetzt werden wir die Führungslinien für das Diagramm einschalten. Bitte beachten Sie, dass wir die Datenbeschriftungen ein wenig verschieben müssen, um die Führungslinien anzuzeigen.

Der folgende Code aktiviert die Führungslinien, aktualisiert das Diagramm und berechnet dann die Positionen der Datenbeschriftungen, um sie entsprechend zu verschieben.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TurnOnLeaderLines.py" >}}

Abschließend speichert der folgende Code das Diagramm im Bildformat und die Arbeitsmappe im XLSX-Format.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SaveChartInImageAndWorkbookInXLSX.py" >}}

|**Ergebnis Tortendiagramm**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Erweiterte Themen**
- [Benutzerdefinierte Farben für Tortenstücke oder Sektoren in einem Tortendiagramm](/cells/de/python-net/custom-slice-or-sector-colors-in-pie-chart/)
- [Herausfinden, ob Datenpunkte in der zweiten Torte oder Balken in einem Tortendiagramm der Torten oder Balken sind](/cells/de/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Verwandte Artikel

- [Erstellen von Diagrammen](/cells/de/python-net/creating-charts/)
- [Diagramme anpassen](/cells/de/python-net/customizing-charts/)
- [Datenformatierung in Diagrammen](/cells/de/python-net/data-formatting-in-charts/)
- [Diagrammaussehen festlegen](/cells/de/python-net/setting-chart-appearance/)

{{< app/cells/assistant language="python-net" >}}
