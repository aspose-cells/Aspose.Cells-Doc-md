---
title: Suchen Sie nach dem Typ von X und Y Werten der Punkte in der Diagrammserie
description: Erfahren Sie, wie man den Typ der X und Y Werte in Diagrammseries Punkten mit Aspose.Cells für Python via .NET bestimmt. Unser Leitfaden erklärt die verschiedenen Arten von Datenwerten und zeigt, wie Sie darauf zugreifen und sie in Ihren Diagrammen verwenden.
keywords: Aspose.Cells für Python via .NET, Diagrammerstellung, X Werte, Y Werte, Datentypen, Zugriff, Arbeit mit, Diagrammseries.
type: docs
weight: 150
url: /de/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie den Typ der X- und Y-Werte von Diagrammpunkten in einer Serie kennen. Aspose.Cells für Python via .NET bietet die Eigenschaften [**ChartPoint.x_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/x_value_type/) und [**ChartPoint.y_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/y_value_type/), die dafür verwendet werden können. Bitte beachten Sie, dass Sie die [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#)-Methode aufrufen müssen, bevor Sie diese Eigenschaften effektiv nutzen können.

## **Typen von X- und Y-Werten von Punkten in Diagrammserien herausfinden**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716905.xlsx) und greift auf das erste Diagramm im ersten Arbeitsblatt zu. Anschließend ruft er die [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#)-Methode auf, um den Typ der X- und Y-Werte des ersten Diagrammpunkts zu ermitteln, und gibt sie in der Konsole aus. Bitte siehe die Konsolenausgabe unten zur Referenz.

## **Beispielcode**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.py" >}}

## **Konsolenausgabe**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
