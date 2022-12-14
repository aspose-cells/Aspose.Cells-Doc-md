---
title: Finden Sie den Typ von X- und Y-Werten von Punkten in Diagrammreihen
type: docs
weight: 150
url: /de/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **Mögliche Nutzungsszenarien**
Manchmal möchten Sie die Art der X- und Y-Werte von Diagrammpunkten in einer Reihe wissen. Aspose.Cells stellt ChartPoint.XValueType- und ChartPoint.YValueType-Eigenschaften bereit, die für diesen Zweck verwendet werden können. Bitte beachten Sie, dass Sie die Methode Chart.Calculate() aufrufen müssen, bevor Sie diese Eigenschaften effektiv nutzen können.
## **Finden Sie den Typ von X- und Y-Werten von Punkten in Diagrammreihen**
 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](64716905.xlsx) und greift auf das erste Diagramm im ersten Arbeitsblatt zu. Anschließend ruft es die Methode Chart.Calculate() auf und ermittelt den Typ der X- und Y-Werte des ersten Diagrammpunkts und gibt sie auf der Konsole aus. Bitte sehen Sie sich die unten gezeigte Konsolenausgabe als Referenz an.
## **Beispielcode**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
## **Konsolenausgabe**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
