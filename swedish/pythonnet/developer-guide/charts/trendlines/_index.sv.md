---
title: Hämta ekvations text av diagramtrendlinje
description: Lär dig hur du använder Aspose.Cells för Python via .NET för att hämta lutningslinjens ekvationstext i ett diagram skapat i Microsoft Excel. Vår guide visar hur man får åtkomst till och extraherar ekvationen för lutningslinjen för vidare analys eller visning.
keywords: Aspose.Cells för Python via .NET, Diagramlutningslinje, Ekvationstext, Microsoft Excel, Dataanalys, Visning.
linktitle: Trendlinjer
type: docs
weight: 110
url: /sv/python-net/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Du kan hämta ekvationstexten för lutningslinjen i ett diagram med Aspose.Cells för Python via .NET. Aspose.Cells för Python via .NET tillhandahåller en egenskap som returnerar ekvationen för lutningslinjen i diagrammet. För att använda denna egenskap måste du först anropa [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate) metoden.

{{% /alert %}}

Följande skärmbild visar diagrammet med en trendlinje och dess ekvations text visas i rött. Vi kommer att hämta denna text med hjälp av egenskapen [**Trendline.data_labels.text**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/datalabels/text) i följande provkod.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## C#-kod för att få ekvationstexten för diagramtrendlinje

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetEquationTextOfChartTrendLine-1.py" >}}

## Utdata genererad av provkoden

Detta är konsoloutputen för ovanstående exempelkod.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
