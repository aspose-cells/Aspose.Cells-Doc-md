---
title: Finden Sie den Typ von X- und Y-Werten von Punkten in Diagrammreihen
type: docs
weight: 110
url: /de/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **Mögliche Nutzungsszenarien**

Manchmal möchten Sie die Art der X- und Y-Werte von Diagrammpunkten in einer Reihe wissen. Aspose.Cells bietet[**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType)und[**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType)Eigenschaften, die für diesen Zweck verwendet werden können. Bitte beachten Sie, dass Sie anrufen müssen[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate())-Methode, bevor Sie diese Eigenschaften effektiv nutzen konnten.

## **Finden Sie den Typ von X- und Y-Werten von Punkten in Diagrammreihen**

Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](64716920.xlsx)und greift auf das erste Diagramm im ersten Arbeitsblatt zu. Es ruft dann die[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate())-Methode und findet den Typ der X- und Y-Werte des ersten Diagrammpunkts und gibt sie auf der Konsole aus. Bitte sehen Sie sich die unten gezeigte Konsolenausgabe als Referenz an.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
