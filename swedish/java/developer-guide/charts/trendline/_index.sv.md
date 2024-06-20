---
title: Hämta ekvations text av diagramtrendlinje
linktitle: Trendlinje
type: docs
weight: 90
url: /sv/java/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Du kan hämta ekvations text av diagramtrendlinje med Aspose.Cells. Aspose.Cells tillhandahåller egenskapen [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) som returnerar ekvations texten av diagramtrendlinjen. För att använda denna egenskap måste du först anropa metoden [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--).

{{% /alert %}}

## **Exempel**

Följande skärmbild visar diagrammet med en trendlinje och dess ekvations text visas i rött. Vi kommer att hämta denna text med hjälp av egenskapen [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) i följande provkod.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

### Java-kod för att få ekvationstext av diagramtrendlinjen

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### Utmatning genererad av provkoden

Detta är konsoloutputen för ovanstående exempelkod.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
