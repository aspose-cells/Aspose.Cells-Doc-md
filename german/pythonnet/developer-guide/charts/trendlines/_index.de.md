---
title: Gleichungstext der Diagrammtrendlinie abrufen
description: Erfahren Sie, wie Sie Aspose.Cells für Python via .NET verwenden, um die Gleichung eines Trendlinien in einem in Microsoft Excel erstellten Diagramm abzurufen. Unser Leitfaden zeigt, wie man auf die Gleichung zugreift und sie für weitere Analysen oder Anzeige extrahiert.
keywords: Aspose.Cells für Python via .NET, Diagramm Trendlinie, Gleichungstext, Microsoft Excel, Datenanalyse, Anzeige.
linktitle: Trendlinien
type: docs
weight: 110
url: /de/python-net/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Sie können den Gleichungstext der Trendlinie des Diagramms mit Aspose.Cells für Python via .NET abrufen. Aspose.Cells für Python via .NET bietet eine Eigenschaft, die den Gleichungstext der Trendlinie des Diagramms zurückgibt. Um diese Eigenschaft zu nutzen, müssen Sie zuerst die [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate)-Methode aufrufen.

{{% /alert %}}

Der folgende Screenshot zeigt das Diagramm mit einer Trendlinie und ihr Gleichungstext wird in roter Farbe angezeigt. Wir werden diesen Text mithilfe der [**Trendline.data_labels.text**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/datalabels/text)-Eigenschaft im folgenden Beispielcode abrufen.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## C#-Code, um den Gleichungstext der Diagrammtrendlinie zu erhalten

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetEquationTextOfChartTrendLine-1.py" >}}

## Ausgabe, die vom Beispielcode generiert wurde

Dies ist die Konsolenausgabe des obigen Beispiels.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
