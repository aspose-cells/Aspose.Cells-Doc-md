---
title: Achsenbeschriftungen nach Berechnen des Diagramms lesen
description: Erfahren Sie, wie Sie Achsenbeschriftungen in Aspose.Cells für Python via .NET nach der Diagrammberechnung lesen. Unser Leitfaden zeigt, wie Sie auf Achsenbeschriftungen zugreifen und sie abrufen, einschließlich ihrer Formatierung und Positionierung.
keywords: Aspose.Cells für Python via .NET, Diagramm, Achsenbeschriftungen, Berechnung, Lesen, Zugriff, Abrufen, Formatierung, Positionierung.
type: docs
weight: 90
url: /de/python-net/read-axis-labels-after-calculating-the-chart/
---

## **Mögliche Verwendungsszenarien**

Sie können die Achsenbeschriftungen Ihres Diagramms nach Berechnen seiner Werte mit der Methode [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/) lesen. Verwenden Sie für diesen Zweck die Methode [**Axis.get_axis_texts()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/axis/get_axis_texts), die die Liste der Achsenbeschriftungen zurückgibt.

## **Lesen Sie die Achsenbeschriftungen nach der Berechnung des Diagramms**

Siehe bitte den folgenden Beispielcode, der die [Beispieldatei für Excel](ReadAxisLabels.xlsx) lädt und die Kategorienachsenbeschriftungen des Diagramms im ersten Arbeitsblatt liest. Anschließend werden die Werte der Achsenbeschriftungen in der Konsole ausgegeben. Bitte sehen Sie sich die Konsolenausgabe des untenstehenden Beispielcodes als Referenz an.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ReadAxisLabelsAfterCalculatingTheChart.py" >}}

## **Konsolenausgabe**

{{< highlight csharp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
