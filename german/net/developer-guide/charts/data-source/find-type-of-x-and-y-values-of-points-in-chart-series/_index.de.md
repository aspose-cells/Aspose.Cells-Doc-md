---
title: Suchen Sie nach dem Typ von X und Y Werten der Punkte in der Diagrammserie
description: Erfahren Sie, wie Sie die Art der X und Y Werte in Diagrammpunkten anhand von Aspose.Cells for .NET ermitteln können. Unser Leitfaden erläutert die verschiedenen Arten von Datenwerten und zeigt Ihnen, wie Sie auf sie zugreifen und damit in Ihren Diagrammen arbeiten können.
keywords: Aspose.Cells for .NET, Diagrammerstellung, X Werte, Y Werte, Datentypen, Zugriff, Arbeit mit Diagrammserien.
type: docs
weight: 150
url: /de/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie den Typ der X- und Y-Werte von Diagrammpunkten in einer Serie kennen. Aspose.Cells bietet die Eigenschaften ChartPoint.XValueType und ChartPoint.YValueType, die zu diesem Zweck verwendet werden können. Bitte beachten Sie, dass Sie die Methode Chart.Calculate() aufrufen müssen, bevor Sie diese Eigenschaften effektiv verwenden können.
## **Typen von X- und Y-Werten von Punkten in Diagrammserien herausfinden**
Der folgende Beispielcode lädt die [Beispieldatei Excel](64716905.xlsx) und greift auf das erste Diagramm im ersten Arbeitsblatt zu. Anschließend wird die Methode Chart.Calculate() aufgerufen und der Typ der X- und Y-Werte des ersten Diagrammpunkts ermittelt und auf der Konsole ausgegeben. Bitte beachten Sie die unten gezeigte Konsolenausgabe als Referenz.

## **Beispielcode**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}

## **Konsolenausgabe**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
