---
title: Hämta ekvations text av diagramtrendlinje
description: Lär dig hur man använder Aspose.Cells for .NET för att hämta ekvationstexten för en trendlinje i ett diagram skapat i Microsoft Excel. Vår guide kommer att visa hur man får åtkomst till och extraherar ekvationen för en trendlinje för ytterligare analys eller visning.
keywords: Aspose.Cells for .NET, Diagram Trendlinje, Ekvationstext, Microsoft Excel, Dataanalys, Visning.
linktitle: Trendlinjer
type: docs
weight: 110
url: /sv/net/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Du kan hämta ekvations text av diagramtrendlinje med Aspose.Cells. Aspose.Cells tillhandahåller egenskapen [**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text) som returnerar ekvations texten av diagramtrendlinjen. För att använda denna egenskap måste du först anropa metoden [**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/calculate).

{{% /alert %}}

Följande skärmbild visar diagrammet med en trendlinje och dess ekvations text visas i rött. Vi kommer att hämta denna text med hjälp av egenskapen [**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text) i följande provkod.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## C#-kod för att få ekvationstexten för diagramtrendlinje

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetEquationTextOfChartTrendLine-1.cs" >}}

## Utdata genererad av provkoden

Detta är konsoloutputen för ovanstående exempelkod.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
