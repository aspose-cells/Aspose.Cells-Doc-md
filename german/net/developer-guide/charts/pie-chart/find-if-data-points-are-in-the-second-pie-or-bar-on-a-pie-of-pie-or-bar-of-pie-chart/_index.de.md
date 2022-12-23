---
title: Finden Sie heraus, ob sich Datenpunkte im zweiten Kreis oder Balken auf einem Kreisdiagramm oder Balkendiagramm befinden
type: docs
weight: 180
url: /de/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
## **Mögliche Nutzungsszenarien**
 Sie können sehen, ob sich Datenpunkte der Reihe im zweiten Kreis befinden*Torte von Torte* Diagramm oder in der Leiste von*Kuchenriegel* Diagramm mit Aspose.Cells. Bitte verwenden Sie die[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)Eigentum, um es zu bestimmen.

 Bitte laden Sie die herunter[Excel-Beispieldatei](5115193.xlsx) im folgenden Beispielcode verwendet und sehen Sie sich die Konsolenausgabe an. Wenn Sie die öffnen[Excel-Beispieldatei](5115193.xlsx) , werden Sie feststellen, dass sich alle Datenpunkte, die kleiner als 10 sind, innerhalb des Balkens von befinden*Kuchenriegel*Diagramm, wie es auch durch die Konsolenausgabe gezeigt wird.
## **Finden Sie heraus, ob sich Datenpunkte im zweiten Kreis oder Balken auf einem Kreisdiagramm oder Balkendiagramm befinden**
 Der folgende Beispielcode zeigt, wie Sie herausfinden, ob sich Datenpunkte im zweiten Kreis oder Balken auf a befinden*Torte von Torte* oder*Kuchenriegel*Diagramm.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **Konsolenausgabe**
 Bitte sehen Sie sich die folgende Konsolenausgabe an, die nach der Ausführung des obigen Beispielcodes mit der generiert wird[Excel-Beispieldatei](5115193.xlsx) . Wenn[IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) ist**FALSCH** , der Datenpunkt befindet sich innerhalb des Kuchens oder wenn ja**wahr**, dann befindet sich der Datenpunkt innerhalb des Balkens.



{{< highlight "java" >}}

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
