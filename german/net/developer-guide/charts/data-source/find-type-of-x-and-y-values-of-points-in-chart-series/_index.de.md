---
title: Finden Sie die Art der X- und Y-Werte von Punkten in Diagrammreihen
description: Erfahren Sie, wie Sie mithilfe von Aspose.Cells for .NET den Typ der
keywords: Aspose.Cells for .NET, charting, X values, Y values, data types, access, work with, chart series.
type: docs
weight: 150
url: /de/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
##  **Mögliche Nutzungsszenarien**
Manchmal möchten Sie die Art der X- und Y-Werte von Diagrammpunkten in einer Reihe wissen. Aspose.Cells stellt die Eigenschaften ChartPoint.XValueType und ChartPoint.YValueType bereit, die für diesen Zweck verwendet werden können. Bitte beachten Sie, dass Sie die Methode Chart.Calculate() aufrufen müssen, bevor Sie diese Eigenschaften effektiv nutzen können.
##  **Finden Sie die Art der X- und Y-Werte von Punkten in Diagrammreihen**
 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](64716905.xlsx) und greift auf das erste Diagramm im ersten Arbeitsblatt zu. Anschließend ruft es die Methode Chart.Calculate() auf, ermittelt den Typ der X- und Y-Werte des ersten Diagrammpunkts und gibt sie auf der Konsole aus. Als Referenz sehen Sie sich bitte die unten gezeigte Konsolenausgabe an.
##  **Beispielcode**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
##  **Konsolenausgabe**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
