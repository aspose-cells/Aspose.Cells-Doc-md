---
title: Bestimmen Sie den Typ der X und Y Werte von Punkten in der Diagrammserie mit Golang über C++
linktitle: Suchen Sie nach dem Typ von X und Y Werten der Punkte in der Diagrammserie
description: Erfahren Sie, wie Sie den Typ der X und Y Werte in Diagrammserienpunkten mit Aspose.Cells for C++ bestimmen. Unser Leitfaden erklärt die verschiedenen Datentypen und zeigt, wie Sie auf diese zugreifen und sie in Ihren Diagrammen verwenden.
keywords: Aspose.Cells for C++, Diagrammerstellung, X Werte, Y Werte, Datentypen, Zugriff, Arbeiten mit, Diagrammserien.
type: docs
weight: 150
url: /de/go-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie den Typ der X- und Y-Werte eines Diagrammpunkts in einer Serie wissen. Aspose.Cells bietet die Methoden `ChartPoint::get_XValueType` und `ChartPoint::get_YValueType` an, die hierfür verwendet werden können. Bitte beachten Sie, dass Sie die Methode `Chart::Calculate()` aufrufen müssen, bevor Sie diese Eigenschaften effektiv nutzen können.

## **Typen von X- und Y-Werten von Punkten in Diagrammserien herausfinden**
Der folgende Beispielcode lädt die [Beispieldatei](64716905.xlsx) und greift auf das erste Diagramm im ersten Arbeitsblatt zu. Dann ruft er die `Chart::Calculate()`-Methode auf und ermittelt den Typ der X- und Y-Werte des ersten Diagrammpunkts und gibt sie in der Konsole aus. Siehe unten die Konsolenausgabe zur Referenz.

## **Beispielcode**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindTypeOfXAndYValuesOfPointsInChartSeries.go" >}}
## **Konsolenausgabe**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
