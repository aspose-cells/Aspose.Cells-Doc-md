---
title: Prüfen, ob Datenpunkte im zweiten Kreis oder Balken eines Kreis oder Balkendiagramms mit Golang über C++ liegen
linktitle: Feststellen, ob Datenauswahl in der zweiten Torte oder Balken in einem Tortendiagramm oder Balkendiagramm aufgeführt ist
description: Lernen Sie, wie man Aspose.Cells for C++ benutzt, um zu finden, ob Datenpunkte in der zweiten Torte oder Bar eines Pie of Pie oder Bar of Pie Diagramms sind. Unser Leitfaden zeigt, wie man den sekundären Tortendiagramm oder Balken in einer zusammengesetzten Grafik erkennt und darauf zugreift, um die Daten effektiv zu analysieren und zu manipulieren.
keywords: Aspose.Cells for C++, Pie of Pie Diagramm, Bar of Pie Diagramm, Sekundäre Torte, Sekundäre Bar, Datenanalyse, Datenmanipulation.
type: docs
weight: 180
url: /de/go-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Mögliche Verwendungsszenarien**
Sie können mit Aspose.Cells feststellen, ob die Datenpunkte einer Serie im zweiten Kreis eines *Pie of Pie* Diagramms oder im Balken eines *Bar of Pie* Diagramms liegen. Bitte verwenden Sie die Eigenschaft [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/go-cpp/chartpoint/isinsecondaryplot/), um dies zu bestimmen.

Bitte laden Sie die [Beispiel-Excel-Datei](5115193.xlsx) herunter, die im folgenden Beispielcode verwendet wird, und sehen Sie sich dessen Konsolenausgabe an. Wenn Sie die [Beispiel-Excel-Datei](5115193.xlsx) öffnen, finden Sie alle Datenpunkte, die kleiner als 10 sind, innerhalb der Leiste des *Balken aus Kuchen*, wie auch von der Konsolenausgabe angezeigt.

## **Herausfinden, ob Datenpunkte in der zweiten Torte oder Balken in einem Tortendiagramm der Torten oder Balken sind**
Der folgende Beispielcode zeigt, wie Sie herausfinden können, ob Datenpunkte im zweiten Kuchen oder Balken auf einem *Kuchen aus Kuchen* oder *Balken aus Kuchen* vorhanden sind.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfDataPointsAreInTheSecondPieOrBarOnAPieOfPieOrBarOfPieChart.go" >}}
## **Konsolenausgabe**
 Siehe die folgende Konsolenausgabe, die nach der Ausführung des obigen Beispielcodes mit der [Beispieldatei Excel](5115193.xlsx) erstellt wurde. Wenn [IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) **falsch** ist, befindet sich der Datenpunkt innerhalb der Torte, wenn **wahr**, dann ist der Datenpunkt innerhalb der Bar.

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
