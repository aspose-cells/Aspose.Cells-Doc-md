---
title: Få ekvationstext för diagramtrendlinje
linktitle: Trendlinje
type: docs
weight: 90
url: /sv/java/get-equation-text-of-chart-trendline/
---
{{% alert color="primary" %}}

 Du kan hämta ekvationstexten för diagramtrendlinjen med Aspose.Cells. Aspose.Cells tillhandahåller[**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) egenskap som returnerar ekvationstexten för diagramstrendlinjen. För att använda denna fastighet måste du först ringa[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()) metod.

{{% /alert %}}

## **Exempel**

 Följande skärmbild visar diagrammet med en trendlinje och dess ekvationstext visas i röd färg. Vi kommer att hämta denna text med hjälp av[**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)egenskap i följande exempelkod.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

### Java kod för att få ekvationstexten för diagramtrendlinjen

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### Utdata genererad av exempelkoden

Detta är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
