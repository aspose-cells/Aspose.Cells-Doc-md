---
title: Feststellen, ob Datenauswahl in der zweiten Torte oder Balken in einem Tortendiagramm oder Balkendiagramm aufgeführt ist
description: Erfahren Sie, wie Sie Aspose.Cells for .NET verwenden, um festzustellen, ob Datenauswahlen in der zweiten Torte oder Balken in einem Tortendiagramm oder Balkendiagramm enthalten sind. Unser Leitfaden wird zeigen, wie Sie die sekundäre Torte oder den Balken in einem zusammengesetzten Diagramm identifizieren und darauf zugreifen können, um die Daten effektiv zu analysieren und zu manipulieren.
keywords: Aspose.Cells for .NET, Pie of Pie Chart, Bar of Pie Chart, Sekundäre Pie, Sekundäre Bar, Datenanalyse, Datenmanipulation.
type: docs
weight: 180
url: /de/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Mögliche Verwendungsszenarien**
Sie können mit Aspose.Cells herausfinden, ob Datenpunkte einer Serie im zweiten Kuchen auf einem *Kuchen aus Kuchen* oder in der Leiste des *Balken aus Kuchen* mit der Eigenschaft [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) sind.

Bitte laden Sie die [Beispiel-Excel-Datei](5115193.xlsx) herunter, die im folgenden Beispielcode verwendet wird, und sehen Sie sich dessen Konsolenausgabe an. Wenn Sie die [Beispiel-Excel-Datei](5115193.xlsx) öffnen, finden Sie alle Datenpunkte, die kleiner als 10 sind, innerhalb der Leiste des *Balken aus Kuchen*, wie auch von der Konsolenausgabe angezeigt.
## **Herausfinden, ob Datenpunkte in der zweiten Torte oder Balken in einem Tortendiagramm der Torten oder Balken sind**
Der folgende Beispielcode zeigt, wie Sie herausfinden können, ob Datenpunkte im zweiten Kuchen oder Balken auf einem *Kuchen aus Kuchen* oder *Balken aus Kuchen* vorhanden sind.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **Konsolenausgabe**
Bitte beachten Sie die folgende Konsolenausgabe, die nach der Ausführung des obigen Beispielcodes mit der [Beispiel-Excel-Datei](5115193.xlsx) generiert wurde. Wenn [IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) **false** ist, befindet sich der Datenpunkt im Kuchen, und wenn **true**, dann befindet sich der Datenpunkt im Balken.



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
{{< app/cells/assistant language="csharp" >}}
