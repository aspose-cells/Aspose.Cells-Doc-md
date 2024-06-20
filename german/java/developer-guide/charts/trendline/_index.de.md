---
title: Gleichungstext der Diagrammtrendlinie abrufen
linktitle: Trendlinie
type: docs
weight: 90
url: /de/java/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Sie können den Gleichungstext der Diagramm-Trendlinie mithilfe von Aspose.Cells abrufen. Aspose.Cells bietet eine [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)-Eigenschaft, die den Gleichungstext der Diagrammtrendlinie zurückgibt. Um diese Eigenschaft zu nutzen, müssen Sie zunächst die Methode [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) aufrufen.

{{% /alert %}}

## **Beispiel**

Der folgende Screenshot zeigt das Diagramm mit einer Trendlinie und ihr Gleichungstext wird in roter Farbe angezeigt. Wir werden diesen Text mithilfe der [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)-Eigenschaft im folgenden Beispielcode abrufen.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

### Java-Code zum Abrufen des Gleichungstextes der Diagrammtrendlinie

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### Ausgabe, generiert durch den Beispielcode

Dies ist die Konsolenausgabe des obigen Beispiels.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
