---
title: Feststellen, ob Datenauswahl in der zweiten Torte oder Balken in einem Tortendiagramm oder Balkendiagramm aufgeführt ist
description: Erfahren Sie, wie Sie Aspose.Cells für Python via .NET verwenden, um zu ermitteln, ob Datenpunkte im zweiten Kreis oder Balken eines Kreis oder Balkendiagramms liegen. Unser Leitfaden zeigt, wie Sie sekundäre Kreise oder Balken in einer komplexen Darstellung identifizieren und zugreifen, um die Daten effektiv zu analysieren und zu manipulieren.
keywords: Aspose.Cells für Python via .NET, Kreis von Kreis Diagramm, Balken von Kreis Diagramm, Sekundärer Kreis, Sekundärer Balken, Datenanalyse, Datenmanipulation.
type: docs
weight: 180
url: /de/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Mögliche Verwendungsszenarien**
Sie können mit Aspose.Cells für Python via .NET überprüfen, ob Datenpunkte einer Serie im zweiten Kreis bei *Kreis von Kreis*-Diagrammen oder im Balken bei *Balken von Kreis*-Diagrammen liegen. Bitte verwenden Sie die Eigenschaft [ChartPoint.is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot), um dies zu bestimmen.

Bitte laden Sie die [Beispiel-Excel-Datei](5115193.xlsx) herunter, die im folgenden Beispielcode verwendet wird, und sehen Sie sich dessen Konsolenausgabe an. Wenn Sie die [Beispiel-Excel-Datei](5115193.xlsx) öffnen, finden Sie alle Datenpunkte, die kleiner als 10 sind, innerhalb der Leiste des *Balken aus Kuchen*, wie auch von der Konsolenausgabe angezeigt.

## **Herausfinden, ob Datenpunkte in der zweiten Torte oder Balken in einem Tortendiagramm der Torten oder Balken sind**
Der folgende Beispielcode zeigt, wie Sie herausfinden können, ob Datenpunkte im zweiten Kuchen oder Balken auf einem *Kuchen aus Kuchen* oder *Balken aus Kuchen* vorhanden sind.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindDataPointsInPieBar.py" >}}
## **Konsolenausgabe**
Siehe die folgende Konsolenausgabe, die nach Ausführung des obigen Beispielcodes mit der [Beispieldatei](5115193.xlsx) generiert wird. Wenn [is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot/) **falsch** ist, befindet sich der Datenpunkt im Kreis, wenn **wahr** dann im Balken.



{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
