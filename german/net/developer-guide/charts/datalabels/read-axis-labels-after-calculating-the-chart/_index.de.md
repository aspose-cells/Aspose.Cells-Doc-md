---
title: Achsenbeschriftungen nach Berechnen des Diagramms lesen
description: Erfahren Sie, wie Sie nach Berechnen des Diagramms die Achsenbeschriftungen in Aspose.Cells for .NET lesen. Unsere Anleitung zeigt Ihnen, wie Sie auf Achsenbeschriftungen zugreifen und diese abrufen können, einschließlich ihrer Formatierung und Positionierung.
keywords: Aspose.Cells for .NET, Diagramm, Achsenbeschriftungen, Berechnung, Lesen, Zugriff, Abrufen, Formatierung, Positionierung.
type: docs
weight: 90
url: /de/net/read-axis-labels-after-calculating-the-chart/
---

## **Mögliche Verwendungsszenarien**

Sie können die Achsenbeschriftungen Ihres Diagramms nach Berechnen seiner Werte mit der Methode [**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/calculate/) lesen. Verwenden Sie für diesen Zweck die Methode [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/getaxistexts/), die die Liste der Achsenbeschriftungen zurückgibt.

## **Lesen Sie die Achsenbeschriftungen nach der Berechnung des Diagramms**

Siehe bitte den folgenden Beispielcode, der die [Beispieldatei für Excel](ReadAxisLabels.xlsx) lädt und die Kategorienachsenbeschriftungen des Diagramms im ersten Arbeitsblatt liest. Anschließend werden die Werte der Achsenbeschriftungen in der Konsole ausgegeben. Bitte sehen Sie sich die Konsolenausgabe des untenstehenden Beispielcodes als Referenz an.

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
