---
title: Einen Gleichungstext der Trendlinie eines Diagramms mit Golang über C++ abrufen
linktitle: Trendlinien
description: Lernen Sie, wie Sie Aspose.Cells for C++ verwenden, um den Gleichungstext einer Trendlinie in einem in Microsoft Excel erstellten Diagramm abzurufen. Unser Leitfaden zeigt, wie Sie die Gleichung einer Trendlinie für weitere Analysen oder zur Anzeige zugreifen und extrahieren.
keywords: Aspose.Cells for C++, Diagramm Trendlinie, Gleichungstext, Microsoft Excel, Datenanalyse, Anzeige.
type: docs
weight: 110
url: /de/go-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Sie können den Gleichungstext der Diagramm-Trendlinie mithilfe von Aspose.Cells abrufen. Aspose.Cells bietet eine [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/)-Eigenschaft, die den Gleichungstext der Diagrammtrendlinie zurückgibt. Um diese Eigenschaft zu nutzen, müssen Sie zunächst die Methode [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/) aufrufen.

{{% /alert %}}

Das folgende Bildschirmfoto zeigt das Diagramm mit einer Trendlinie, deren Gleichungstext in roter Farbe angezeigt wird. Wir werden diesen Text mit der [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/)-Eigenschaft im folgenden Beispielcode abrufen.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## C++-Code zum Abrufen des Gleichungstextes der Chart-Trendlinie

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Trendlines.go" >}}
## Ausgabe, die vom Beispielcode generiert wurde

Dies ist die Konsolenausgabe des obigen Beispiels.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
