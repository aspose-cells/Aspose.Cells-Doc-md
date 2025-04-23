---
title: Obtenir le texte d équation de la tendance du graphique
description: Apprenez à utiliser Aspose.Cells for .NET pour récupérer le texte d équation d une tendance dans un graphique créé dans Microsoft Excel. Notre guide démontrera comment accéder et extraire l équation d une tendance pour une analyse ultérieure ou son affichage.
keywords: Aspose.Cells for .NET, Tendance de graphique, Texte d équation, Microsoft Excel, Analyse de données, Affichage.
linktitle: Trendlines
type: docs
weight: 110
url: /fr/net/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Vous pouvez récupérer le texte d'équation de la tendance du graphique en utilisant Aspose.Cells. Aspose.Cells fournit la propriété [**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text) qui retourne le texte d'équation de la tendance du graphique. Pour utiliser cette propriété, vous devrez d'abord appeler la méthode [**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/calculate).

{{% /alert %}}

La capture d'écran suivante montre le graphique avec une tendance et son texte d'équation est affiché en rouge. Nous récupérerons ce texte en utilisant la propriété [**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text) dans le code d'exemple suivant.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Code C# pour obtenir le texte d'équation de la tendance du graphique

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetEquationTextOfChartTrendLine-1.cs" >}}

## Sortie générée par le code d'exemple

Il s'agit de la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
