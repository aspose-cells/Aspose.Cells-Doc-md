---
title: Feststellen, ob Datenauswahl in der zweiten Torte oder Balken in einem Tortendiagramm oder Balkendiagramm aufgeführt ist
type: docs
weight: 910
url: /de/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Mögliche Verwendungsszenarien**
Mit Aspose.Cells können Sie feststellen, ob Datenpunkte einer Serie im zweiten Tortendiagramm auf dem *Pie of Pie*-Diagramm oder in der Säule des *Bar of Pie*-Diagramms sind. Verwenden Sie die Eigenschaft [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot), um dies zu bestimmen.

Bitte laden Sie die [Beispiel-Excel-Datei](5473373.xlsx) herunter, die im folgenden Beispielcode verwendet wird, und sehen Sie sich ihre Konsolenausgabe an. Wenn Sie die [Beispiel-Excel-Datei](5473373.xlsx) öffnen, finden Sie alle Datenpunkte, die kleiner als 10 sind, sind innerhalb der Säule des *Bar of Pie*-Diagramms, wie auch von der Konsolenausgabe angezeigt.
## **Herausfinden, ob Datenpunkte in der zweiten Torte oder Balken in einem Tortendiagramm der Torten oder Balken sind**
Der folgende Beispielcode zeigt, wie Sie herausfinden können, ob Datenpunkte im zweiten Kuchen oder Balken auf einem *Kuchen aus Kuchen* oder *Balken aus Kuchen* vorhanden sind.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **Konsolenausgabe**
Bitte sehen Sie sich die folgende Konsolenausgabe an, die nach der Ausführung des obigen Beispielcodes mit der [Beispiel-Excel-Datei](5473373.xlsx) generiert wird. Wenn [IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) **false** ist, befindet sich der Datenpunkt innerhalb des Kreises oder wenn er **true** ist, befindet sich der Datenpunkt innerhalb der Säule.

{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: false

Value: 9

IsInSecondaryPlot: true

Value: 2

IsInSecondaryPlot: true

Value: 40

IsInSecondaryPlot: false

Value: 5

IsInSecondaryPlot: true

Value: 4

IsInSecondaryPlot: true

Value: 25

IsInSecondaryPlot: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
