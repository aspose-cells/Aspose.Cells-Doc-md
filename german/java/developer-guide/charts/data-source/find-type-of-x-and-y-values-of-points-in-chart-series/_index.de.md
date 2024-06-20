---
title: Suchen Sie nach dem Typ von X und Y Werten der Punkte in der Diagrammserie
type: docs
weight: 110
url: /de/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Mögliche Verwendungsszenarien**

Manchmal möchten Sie den Typ der X- und Y-Werte von Diagrammpunkten in einer Serie wissen. Aspose.Cells bietet die Eigenschaften [**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType) und [**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType), die zu diesem Zweck verwendet werden können. Bitte beachten Sie, dass Sie vor der effektiven Verwendung dieser Eigenschaften die Methode [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) aufrufen müssen.

## **Typen von X- und Y-Werten von Punkten in Diagrammserien herausfinden**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716920.xlsx) und greift auf das erste Diagramm im ersten Arbeitsblatt zu. Anschließend ruft es die Methode [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) auf und ermittelt den Typ der X- und Y-Werte des ersten Diagrammpunkts und gibt sie auf der Konsole aus. Bitte beachten Sie die unten gezeigte Konsolenausgabe als Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **Konsolenausgabe**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
