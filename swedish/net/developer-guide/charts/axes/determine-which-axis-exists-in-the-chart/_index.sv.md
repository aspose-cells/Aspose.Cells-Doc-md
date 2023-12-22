---
title: Bestäm vilken axel som finns i diagrammet
description: Lär dig hur du avgör vilken axel som finns i ett diagram skapat med Aspose.Cells for .NET. Vår guide hjälper dig att förstå hur du identifierar och kommer åt de olika axlarna i ett diagram, inklusive kategori, värde och sekundära axlar.
keywords: Aspose.Cells for .NET, chart, axis, existence, category, value, secondary.
type: docs
weight: 140
url: /sv/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

Ibland behöver användaren veta om en viss axel finns i diagrammet. Till exempel vill han veta om en sekundär värdeaxel finns i diagrammet eller inte. Vissa diagram som Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, etc. har ingen axel.

 Aspose.Cells tillhandahåller[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) metod för att avgöra om diagrammet har en viss axel eller inte.

{{% /alert %}}

 Följande exempelkod visar användningen av[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)för att avgöra om provdiagrammet har primär och sekundär kategori och värdeaxel.

##  C# kod för att avgöra vilken axel som finns i diagrammet

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Konsolutdata genererad av exempelkoden

Konsolutmatningen av koden har visats nedan som visar sant för primär kategori och värdeaxel och falskt för sekundär kategori och värdeaxel.

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
